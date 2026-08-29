#!/usr/bin/env python3
"""List or remove screenshot evidence files from the configured GitHub Gist."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from publish_screenshot import (
    DEFAULT_DESCRIPTION,
    DEFAULT_CONFIG_PATH,
    clone_or_update,
    create_gist,
    current_branch,
    get_gist,
    gh_auth_token,
    gist_git,
    read_config,
    read_saved_gist_id,
    require_tool,
    run,
    write_config,
    write_saved_gist_id,
)


PROTECTED_FILENAMES = {"README.md"}


def gist_files(repo_dir: Path) -> list[Path]:
    filenames = run(["git", "ls-files", "-z"], cwd=repo_dir).split("\0")
    return [repo_dir / filename for filename in filenames if filename]


def select_files(repo_dir: Path, action: str, requested_filenames: list[str]) -> list[Path]:
    available = {path.name: path for path in gist_files(repo_dir)}

    if action == "clear":
        return [path for name, path in available.items() if name not in PROTECTED_FILENAMES]

    selected: list[Path] = []
    for filename in requested_filenames:
        if Path(filename).name != filename:
            raise SystemExit(f"Gist filenames cannot contain path components: {filename}")
        if filename in PROTECTED_FILENAMES:
            raise SystemExit(f"Protected gist file cannot be deleted: {filename}")
        if filename not in available:
            raise SystemExit(f"Gist file not found: {filename}")
        if available[filename] not in selected:
            selected.append(available[filename])
    return selected


def delete_files(repo_dir: Path, files: list[Path], *, token: str) -> str | None:
    if not files:
        return None

    filenames = [path.name for path in files]
    run(["git", "rm", "--", *filenames], cwd=repo_dir)
    run(["git", "commit", "-m", f"Remove {len(files)} screenshot evidence file(s)"], cwd=repo_dir)
    revision = run(["git", "rev-parse", "HEAD"], cwd=repo_dir).strip()
    gist_git(["push", "origin", current_branch(repo_dir)], cwd=repo_dir, token=token)
    return revision


def reset_gist(gist: dict, config_path: Path) -> dict:
    replacement = create_gist(gist.get("description") or DEFAULT_DESCRIPTION)
    write_saved_gist_id(config_path, replacement["id"])
    run(["gh", "api", f"gists/{gist['id']}", "--method", "DELETE"])
    return replacement


def configure_retention(config_path: Path, keep_days: int, timezone_name: str, description_pattern: str) -> dict:
    if keep_days < 0:
        raise SystemExit("--keep-days must be non-negative")
    try:
        ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise SystemExit(f"Unknown timezone: {timezone_name}") from exc
    if not description_pattern:
        raise SystemExit("--match-description cannot be empty")

    config = read_config(config_path)
    config["retention"] = {
        "enabled": True,
        "keep_days": keep_days,
        "timezone": timezone_name,
        "description_pattern": description_pattern,
    }
    write_config(config_path, config)
    return config["retention"]


def parse_cutoff(value: str) -> datetime:
    try:
        cutoff = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SystemExit(f"Invalid --before timestamp: {value}") from exc
    if cutoff.tzinfo is None:
        raise SystemExit("--before must include a timezone offset, for example 2026-08-29T00:00:00+08:00")
    return cutoff.astimezone(timezone.utc)


def account_gists() -> list[dict]:
    output = run(["gh", "gist", "list", "--limit", "1000"])
    gists = []
    for line in output.splitlines():
        gist_id, remaining = line.split("\t", 1)
        description, file_summary, visibility, updated_at = remaining.rsplit("\t", 3)
        gists.append(
            {
                "id": gist_id,
                "description": description,
                "file_summary": file_summary,
                "visibility": visibility,
                "updated_at": datetime.fromisoformat(updated_at.replace("Z", "+00:00")),
            }
        )
    return gists


def select_account_gists(gists: list[dict], cutoff: datetime, description_pattern: str) -> list[dict]:
    try:
        pattern = re.compile(description_pattern, re.IGNORECASE)
    except re.error as exc:
        raise SystemExit(f"Invalid --match-description pattern: {exc}") from exc
    return [gist for gist in gists if gist["updated_at"] < cutoff and pattern.search(gist["description"])]


def delete_account_gists(gists: list[dict]) -> list[dict]:
    failures = []
    for gist in gists:
        try:
            run(["gh", "api", f"gists/{gist['id']}", "--method", "DELETE"])
        except SystemExit as exc:
            failures.append({"description": gist["description"], "error": str(exc).splitlines()[-1]})
    return failures


def prune_account(args: argparse.Namespace) -> int:
    cutoff = parse_cutoff(args.before)
    gists = account_gists()
    selected = select_account_gists(gists, cutoff, args.match_description)
    failures = delete_account_gists(selected) if args.apply else []
    deleted_count = len(selected) - len(failures) if args.apply else 0
    description_counts = Counter(gist["description"] or "<empty>" for gist in selected)
    result = {
        "action": "prune-account",
        "before": cutoff.isoformat().replace("+00:00", "Z"),
        "match_description": args.match_description,
        "account_gist_count": len(gists),
        "selected_count": len(selected),
        "selected_descriptions": [
            {"description": description, "count": count}
            for description, count in sorted(description_counts.items())
        ],
        "applied": args.apply,
        "deleted_count": deleted_count,
        "failed_count": len(failures),
        "failures": failures,
    }
    print(json.dumps(result, indent=2))
    return 1 if failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "action",
        choices=("list", "delete", "clear", "reset", "prune-account", "configure-retention"),
    )
    parser.add_argument("filenames", nargs="*", help="Exact gist filenames for the delete action.")
    parser.add_argument("--gist-id", help="Existing gist id. Overrides SCREENSHOT_GIST_ID and local config.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Local config path containing the reusable gist id.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path.home() / ".cache" / "agent-screenshot-gists",
        help="Local cache directory for cloned gist repositories.",
    )
    parser.add_argument("--apply", action="store_true", help="Perform the planned mutation.")
    parser.add_argument(
        "--before",
        help="For prune-account, select gists last updated before this ISO 8601 timestamp.",
    )
    parser.add_argument(
        "--match-description",
        default="evidence",
        help="For prune-account, case-insensitive regex matched against gist descriptions.",
    )
    parser.add_argument("--keep-days", type=int, help="For configure-retention, days before today's midnight to keep.")
    parser.add_argument(
        "--timezone",
        default="UTC",
        help="For configure-retention, IANA timezone used to calculate midnight.",
    )
    args = parser.parse_args()

    if args.action == "delete" and not args.filenames:
        parser.error("delete requires at least one filename")
    if args.action != "delete" and args.filenames:
        parser.error(f"{args.action} does not accept filenames")
    if args.action == "list" and args.apply:
        parser.error("list does not accept --apply")
    if args.action == "prune-account" and not args.before:
        parser.error("prune-account requires --before with an explicit timezone offset")
    if args.action == "configure-retention" and args.keep_days is None:
        parser.error("configure-retention requires --keep-days")
    return args


def main() -> int:
    args = parse_args()
    config_path = args.config.expanduser().resolve()
    if args.action == "configure-retention":
        retention = configure_retention(config_path, args.keep_days, args.timezone, args.match_description)
        print(json.dumps({"action": "configure-retention", "retention": retention}, indent=2))
        return 0

    require_tool("gh")
    if args.action == "prune-account":
        return prune_account(args)

    gist_id = args.gist_id or os.environ.get("SCREENSHOT_GIST_ID") or read_saved_gist_id(config_path)
    if not gist_id:
        raise SystemExit("A reusable gist is required. Pass --gist-id, set SCREENSHOT_GIST_ID, or configure it locally.")

    require_tool("git")
    token = gh_auth_token()
    gist = get_gist(gist_id)
    repo_dir = clone_or_update(gist, args.cache_dir.expanduser(), token=token)
    all_files = gist_files(repo_dir)
    file_count = len(all_files)
    total_bytes = sum(path.stat().st_size for path in all_files)

    if args.action == "list":
        selected = []
    elif args.action == "reset":
        selected = all_files
    else:
        selected = select_files(repo_dir, args.action, args.filenames)
    selected_bytes = sum(path.stat().st_size for path in selected)
    revision = None
    replacement = None
    if args.apply and args.action == "reset":
        replacement = reset_gist(gist, config_path)
    elif args.apply:
        revision = delete_files(repo_dir, selected, token=token)

    result = {
        "action": args.action,
        "gist_id": gist_id,
        "html_url": gist["html_url"],
        "file_count": file_count,
        "total_bytes": total_bytes,
        "selected_count": len(selected),
        "selected_bytes": selected_bytes,
        "selected_files": [path.name for path in selected],
        "applied": bool(args.apply and selected),
    }
    if revision:
        result["revision"] = revision
    if replacement:
        result["replacement_gist_id"] = replacement["id"]
        result["replacement_html_url"] = replacement["html_url"]
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
