from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import publish_screenshot  # noqa: E402


class ConfigTests(unittest.TestCase):
    def test_updating_gist_id_preserves_retention_policy(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "gist_id": "old-gist",
                        "retention": {
                            "enabled": True,
                            "keep_days": 7,
                            "timezone": "Asia/Shanghai",
                            "description_pattern": "evidence",
                        },
                    }
                )
            )

            publish_screenshot.write_saved_gist_id(config_path, "new-gist")

            config = publish_screenshot.read_config(config_path)
            self.assertEqual(config["gist_id"], "new-gist")
            self.assertEqual(config["retention"]["keep_days"], 7)

    def test_seven_day_cutoff_uses_midnight_in_configured_timezone(self) -> None:
        policy = publish_screenshot.retention_policy(
            {
                "retention": {
                    "enabled": True,
                    "keep_days": 7,
                    "timezone": "Asia/Shanghai",
                    "description_pattern": "evidence",
                }
            }
        )

        cutoff = publish_screenshot.retention_cutoff(
            policy,
            now=datetime(2026, 8, 30, 18, 30, tzinfo=ZoneInfo("Asia/Shanghai")),
        )

        self.assertEqual(cutoff.isoformat(), "2026-08-23T00:00:00+08:00")


class RotationTests(unittest.TestCase):
    def test_gist_created_before_cutoff_is_replaced(self) -> None:
        gist = {"id": "old", "created_at": "2026-08-22T15:59:59Z"}
        replacement = {"id": "new", "created_at": "2026-08-30T00:00:00Z"}
        cutoff = datetime(2026, 8, 23, tzinfo=ZoneInfo("Asia/Shanghai"))

        with patch.object(publish_screenshot, "replace_gist", return_value=replacement) as replace_gist:
            result, rotated = publish_screenshot.rotate_expired_gist(gist, Path("config.json"), cutoff)

        self.assertEqual(result, replacement)
        self.assertTrue(rotated)
        replace_gist.assert_called_once()

    def test_gist_created_at_cutoff_is_kept(self) -> None:
        gist = {"id": "current", "created_at": "2026-08-22T16:00:00Z"}
        cutoff = datetime(2026, 8, 23, tzinfo=ZoneInfo("Asia/Shanghai"))

        with patch.object(publish_screenshot, "replace_gist") as replace_gist:
            result, rotated = publish_screenshot.rotate_expired_gist(gist, Path("config.json"), cutoff)

        self.assertEqual(result, gist)
        self.assertFalse(rotated)
        replace_gist.assert_not_called()


class PruneHookTests(unittest.TestCase):
    def test_prune_hook_invokes_account_cleanup_with_cutoff_and_scope(self) -> None:
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"deleted_count": 2}', "stderr": ""})()
        cutoff = datetime(2026, 8, 23, tzinfo=ZoneInfo("Asia/Shanghai"))

        with patch.object(publish_screenshot.subprocess, "run", return_value=completed) as run:
            result = publish_screenshot.prune_account_for_retention(
                Path("/tmp/config.json"),
                cutoff,
                "evidence",
            )

        self.assertEqual(result["deleted_count"], 2)
        command = run.call_args.args[0]
        self.assertIn("prune-account", command)
        self.assertIn("2026-08-23T00:00:00+08:00", command)
        self.assertIn("evidence", command)
        self.assertIn("--apply", command)


if __name__ == "__main__":
    unittest.main()
