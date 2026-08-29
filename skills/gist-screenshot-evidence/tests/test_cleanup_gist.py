from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import cleanup_gist  # noqa: E402


class SelectFilesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_dir = Path(self.temp_dir.name)
        subprocess.run(["git", "init", "-q"], cwd=self.repo_dir, check=True)
        for filename in ("README.md", "20260801-before.png", "20260802-after.png"):
            (self.repo_dir / filename).write_text(filename)
        subprocess.run(["git", "add", "."], cwd=self.repo_dir, check=True)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_clear_selects_every_file_except_readme(self) -> None:
        selected = cleanup_gist.select_files(self.repo_dir, "clear", [])
        self.assertEqual([path.name for path in selected], ["20260801-before.png", "20260802-after.png"])

    def test_clear_ignores_untracked_cache_files(self) -> None:
        (self.repo_dir / "failed-upload.png").write_text("not on the remote gist")

        selected = cleanup_gist.select_files(self.repo_dir, "clear", [])

        self.assertNotIn("failed-upload.png", [path.name for path in selected])

    def test_delete_accepts_multiple_exact_filenames_and_deduplicates(self) -> None:
        selected = cleanup_gist.select_files(
            self.repo_dir,
            "delete",
            ["20260802-after.png", "20260801-before.png", "20260802-after.png"],
        )
        self.assertEqual([path.name for path in selected], ["20260802-after.png", "20260801-before.png"])

    def test_delete_protects_readme(self) -> None:
        with self.assertRaisesRegex(SystemExit, "Protected gist file"):
            cleanup_gist.select_files(self.repo_dir, "delete", ["README.md"])

    def test_delete_rejects_missing_file(self) -> None:
        with self.assertRaisesRegex(SystemExit, "Gist file not found"):
            cleanup_gist.select_files(self.repo_dir, "delete", ["missing.png"])


class DeleteFilesTests(unittest.TestCase):
    def test_delete_files_commits_all_removals_before_push(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_dir = Path(temp_dir)
            subprocess.run(["git", "init", "-q"], cwd=repo_dir, check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_dir, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_dir, check=True)
            screenshot_paths = []
            for filename in ("README.md", "one.png", "two.png"):
                path = repo_dir / filename
                path.write_text(filename)
                if filename.endswith(".png"):
                    screenshot_paths.append(path)
            subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "Initial"], cwd=repo_dir, check=True)

            with patch.object(cleanup_gist, "gist_git") as gist_git:
                revision = cleanup_gist.delete_files(repo_dir, screenshot_paths, token="test-token")

            self.assertTrue((repo_dir / "README.md").exists())
            self.assertFalse((repo_dir / "one.png").exists())
            self.assertFalse((repo_dir / "two.png").exists())
            self.assertEqual(len(revision or ""), 40)
            gist_git.assert_called_once()

    def test_apply_reports_the_pre_deletion_size_after_files_are_removed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_dir = Path(temp_dir)
            subprocess.run(["git", "init", "-q"], cwd=repo_dir, check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_dir, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_dir, check=True)
            (repo_dir / "README.md").write_text("readme")
            (repo_dir / "one.png").write_text("screenshot")
            subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "Initial"], cwd=repo_dir, check=True)
            args = SimpleNamespace(
                action="clear",
                filenames=[],
                gist_id="test-gist",
                config=repo_dir / "config.json",
                cache_dir=repo_dir / "cache",
                apply=True,
            )

            output = io.StringIO()
            with (
                patch.object(cleanup_gist, "parse_args", return_value=args),
                patch.object(cleanup_gist, "require_tool"),
                patch.object(cleanup_gist, "gh_auth_token", return_value="test-token"),
                patch.object(
                    cleanup_gist,
                    "get_gist",
                    return_value={"id": "test-gist", "html_url": "https://example.test/gist"},
                ),
                patch.object(cleanup_gist, "clone_or_update", return_value=repo_dir),
                patch.object(cleanup_gist, "gist_git"),
                redirect_stdout(output),
            ):
                self.assertEqual(cleanup_gist.main(), 0)

            result = json.loads(output.getvalue())
            self.assertEqual(result["total_bytes"], len("readme") + len("screenshot"))
            self.assertTrue(result["applied"])
            self.assertFalse((repo_dir / "one.png").exists())


class ResetGistTests(unittest.TestCase):
    def test_reset_creates_and_configures_replacement_before_deleting_old_gist(self) -> None:
        old_gist = {"id": "old-gist", "description": "Evidence"}
        replacement = {"id": "new-gist", "html_url": "https://example.test/new"}
        config_path = Path("/tmp/config.json")
        calls = []

        with (
            patch.object(
                cleanup_gist,
                "create_gist",
                side_effect=lambda description: calls.append(("create", description)) or replacement,
            ),
            patch.object(
                cleanup_gist,
                "write_saved_gist_id",
                side_effect=lambda path, gist_id: calls.append(("configure", path, gist_id)),
            ),
            patch.object(
                cleanup_gist,
                "run",
                side_effect=lambda command: calls.append(("delete", command)) or "",
            ),
        ):
            result = cleanup_gist.reset_gist(old_gist, config_path)

        self.assertEqual(result, replacement)
        self.assertEqual(
            calls,
            [
                ("create", "Evidence"),
                ("configure", config_path, "new-gist"),
                ("delete", ["gh", "api", "gists/old-gist", "--method", "DELETE"]),
            ],
        )


class PruneAccountTests(unittest.TestCase):
    def test_account_gists_parses_descriptions_without_exposing_table_structure(self) -> None:
        output = (
            "gist-one\tAgent screenshot evidence\t2 files\tsecret\t2026-08-27T04:15:03Z\n"
            "gist-two\tUI evidence\t1 file\tsecret\t2026-08-29T01:00:00Z\n"
        )

        with patch.object(cleanup_gist, "run", return_value=output):
            gists = cleanup_gist.account_gists()

        self.assertEqual([gist["id"] for gist in gists], ["gist-one", "gist-two"])
        self.assertEqual(gists[0]["description"], "Agent screenshot evidence")

    def test_select_account_gists_uses_updated_time_and_description_scope(self) -> None:
        gists = [
            {
                "id": "old-evidence",
                "description": "UI verification evidence",
                "updated_at": datetime(2026, 8, 27, tzinfo=timezone.utc),
            },
            {
                "id": "old-memo",
                "description": "Open Source MEMO",
                "updated_at": datetime(2024, 11, 13, tzinfo=timezone.utc),
            },
            {
                "id": "new-evidence",
                "description": "Agent screenshot evidence",
                "updated_at": datetime(2026, 8, 29, tzinfo=timezone.utc),
            },
        ]

        selected = cleanup_gist.select_account_gists(
            gists,
            datetime(2026, 8, 28, 16, tzinfo=timezone.utc),
            "evidence",
        )

        self.assertEqual([gist["id"] for gist in selected], ["old-evidence"])

    def test_delete_account_gists_continues_after_a_failure(self) -> None:
        gists = [
            {"id": "first", "description": "First evidence"},
            {"id": "second", "description": "Second evidence"},
        ]

        def delete(command: list[str]) -> str:
            if "first" in command[2]:
                raise SystemExit("failed first")
            return ""

        with patch.object(cleanup_gist, "run", side_effect=delete) as run:
            failures = cleanup_gist.delete_account_gists(gists)

        self.assertEqual(failures, [{"description": "First evidence", "error": "failed first"}])
        self.assertEqual(run.call_count, 2)


class ConfigureRetentionTests(unittest.TestCase):
    def test_configure_retention_preserves_gist_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.json"
            config_path.write_text('{"gist_id": "current-gist"}\n')

            retention = cleanup_gist.configure_retention(config_path, 7, "Asia/Shanghai", "evidence")

            config = json.loads(config_path.read_text())
            self.assertEqual(config["gist_id"], "current-gist")
            self.assertEqual(retention["keep_days"], 7)
            self.assertEqual(retention["timezone"], "Asia/Shanghai")


if __name__ == "__main__":
    unittest.main()
