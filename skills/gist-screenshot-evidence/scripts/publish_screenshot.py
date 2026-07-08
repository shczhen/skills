#!/usr/bin/env python3
"""Publish a screenshot to a GitHub Gist git repo and print Markdown metadata."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".svg"}
DEFAULT_DESCRIPTION = "Agent screenshot evidence"
SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = SKILL_DIR / ".local" / "config.json"


def run(
    command: list[str],
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
    display_command: str | None = None,
) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        details = stderr or stdout or f"exit code {result.returncode}"
        command_text = display_command or " ".join(command)
        raise SystemExit(f"Command failed: {command_text}\n{details}")
    return result.stdout


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required tool not found: {name}")


def sanitize_filename(value: str) -> str:
    name = Path(value).name.strip()
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)
    name = name.strip(".-")
    if not name:
        raise SystemExit("Filename cannot be empty after sanitization.")
    return name


def timestamped_filename(image_path: Path, requested_filename: str | None) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    base_name = sanitize_filename(requested_filename) if requested_filename else sanitize_filename(image_path.name)
    return f"{timestamp}-{base_name}"


def validate_image_path(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"Image file not found: {path}")
    if not path.is_file():
        raise SystemExit(f"Image path is not a file: {path}")
    if path.suffix.lower() not in IMAGE_EXTENSIONS:
        allowed = ", ".join(sorted(IMAGE_EXTENSIONS))
        raise SystemExit(f"Unsupported image extension: {path.suffix}. Allowed: {allowed}")


def gh_json(command: list[str], *, input_data: dict | None = None) -> dict:
    input_text = json.dumps(input_data) if input_data is not None else None
    output = run(["gh", "api", *command], input_text=input_text)
    return json.loads(output)


def gh_auth_token() -> str:
    token = run(["gh", "auth", "token"], display_command="gh auth token").strip()
    if not token:
        raise SystemExit("gh auth token returned an empty token.")
    return token


def gist_git(command: list[str], *, token: str, cwd: Path | None = None) -> str:
    basic_token = base64.b64encode(f"x-access-token:{token}".encode()).decode()
    header = f"AUTHORIZATION: basic {basic_token}"
    return run(
        ["git", "-c", f"http.https://gist.github.com/.extraheader={header}", *command],
        cwd=cwd,
        display_command=f"git {' '.join(command)}",
    )


def create_gist(description: str) -> dict:
    body = {
        "description": description,
        "public": False,
        "files": {
            "README.md": {
                "content": "# Agent screenshot evidence\n\nThis gist stores screenshot files published by an agent.\n"
            }
        },
    }
    return gh_json(["gists", "--method", "POST", "--input", "-"], input_data=body)


def get_gist(gist_id: str) -> dict:
    return gh_json([f"gists/{gist_id}"])


def clone_or_update(gist: dict, cache_dir: Path, *, token: str) -> Path:
    gist_id = gist["id"]
    repo_dir = cache_dir / gist_id
    clone_url = gist.get("git_push_url") or gist["git_pull_url"]

    if repo_dir.exists():
        branch = current_branch(repo_dir)
        gist_git(["fetch", "--all", "--prune"], cwd=repo_dir, token=token)
        run(["git", "reset", "--hard", f"origin/{branch}"], cwd=repo_dir)
        return repo_dir

    cache_dir.mkdir(parents=True, exist_ok=True)
    gist_git(["clone", clone_url, str(repo_dir)], token=token)
    return repo_dir


def current_branch(repo_dir: Path) -> str:
    return run(["git", "branch", "--show-current"], cwd=repo_dir).strip()


def commit_and_push(repo_dir: Path, filename: str, *, token: str) -> None:
    run(["git", "add", filename], cwd=repo_dir)
    status = run(["git", "status", "--porcelain", "--", filename], cwd=repo_dir).strip()
    if not status:
        return
    run(["git", "commit", "-m", f"Add {filename}"], cwd=repo_dir)
    gist_git(["push", "origin", current_branch(repo_dir)], cwd=repo_dir, token=token)


def build_raw_url(owner: str, gist_id: str, filename: str) -> str:
    return f"https://gist.githubusercontent.com/{owner}/{gist_id}/raw/{quote(filename)}"


def read_saved_gist_id(config_path: Path) -> str | None:
    if not config_path.exists():
        return None
    try:
        data = json.loads(config_path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid config JSON: {config_path}\n{exc}") from exc
    gist_id = data.get("gist_id")
    if gist_id is not None and not isinstance(gist_id, str):
        raise SystemExit(f"Invalid gist_id in config: {config_path}")
    return gist_id


def write_saved_gist_id(config_path: Path, gist_id: str) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    data = {"gist_id": gist_id}
    config_path.write_text(json.dumps(data, indent=2) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to the local screenshot image.")
    parser.add_argument("--gist-id", help="Existing gist id to reuse. Overrides SCREENSHOT_GIST_ID and local config.")
    parser.add_argument("--create", action="store_true", help="Create a new secret gist when no gist id is configured.")
    parser.add_argument("--filename", help="Filename to use inside the gist.")
    parser.add_argument("--alt", default="Screenshot evidence", help="Markdown image alt text.")
    parser.add_argument("--description", default=DEFAULT_DESCRIPTION, help="Description for a newly created gist.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Local config path that stores the reusable gist id.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path.home() / ".cache" / "agent-screenshot-gists",
        help="Local cache directory for cloned gist repositories.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs and print planned metadata without gh/git calls.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_path = args.image.expanduser().resolve()
    validate_image_path(image_path)

    config_path = args.config.expanduser().resolve()
    saved_gist_id = read_saved_gist_id(config_path)
    configured_gist_id = args.gist_id or os.environ.get("SCREENSHOT_GIST_ID") or saved_gist_id

    if not configured_gist_id and not args.create:
        raise SystemExit("A reusable gist is required. Run once with --create, pass --gist-id, or set SCREENSHOT_GIST_ID.")

    filename = timestamped_filename(image_path, args.filename)

    if args.dry_run:
        gist_id = configured_gist_id or "dry-run-created-gist-id"
        owner = "dry-run-owner"
        raw_url = build_raw_url(owner, gist_id, filename)
        print(
            json.dumps(
                {
                    "gist_id": gist_id,
                    "created": bool(args.create and not configured_gist_id),
                    "raw_url": raw_url,
                    "markdown": f"![{args.alt}]({raw_url})",
                    "filename": filename,
                    "config_path": str(config_path),
                },
                indent=2,
            )
        )
        return 0

    require_tool("gh")
    require_tool("git")
    token = gh_auth_token()

    gist = get_gist(configured_gist_id) if configured_gist_id else create_gist(args.description)
    gist_id = gist["id"]
    if args.create and not configured_gist_id:
        write_saved_gist_id(config_path, gist_id)
    owner = gist["owner"]["login"]
    repo_dir = clone_or_update(gist, args.cache_dir.expanduser(), token=token)

    target_path = repo_dir / filename
    shutil.copyfile(image_path, target_path)
    commit_and_push(repo_dir, filename, token=token)

    raw_url = build_raw_url(owner, gist_id, filename)
    result = {
        "gist_id": gist_id,
        "html_url": gist["html_url"],
        "raw_url": raw_url,
        "markdown": f"![{args.alt}]({raw_url})",
        "filename": filename,
        "created": bool(args.create and not configured_gist_id),
        "config_path": str(config_path),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
