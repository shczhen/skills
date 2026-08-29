# gist-screenshot-evidence

Publish screenshot evidence to a reusable secret GitHub Gist and return
Markdown image links for GitHub PR or issue comments.

## Requirements

- `gh` CLI authenticated with gist access.
- `git` available on PATH.
- A screenshot file to publish.

## First Use

Create and remember the reusable secret gist once:

```bash
python3 skills/gist-screenshot-evidence/scripts/publish_screenshot.py ./screenshot.png --create
```

The gist id is stored locally in:

```text
skills/gist-screenshot-evidence/.local/config.json
```

That file is ignored by git and should stay local.

## Reuse

Later publishes reuse the remembered gist automatically:

```bash
python3 skills/gist-screenshot-evidence/scripts/publish_screenshot.py ./screenshot.png
```

Use a stable filename and alt text when posting PR or issue evidence:

```bash
python3 skills/gist-screenshot-evidence/scripts/publish_screenshot.py ./screenshot.png \
  --filename issue-123-after.png \
  --alt "Issue 123 after fix"
```

Uploaded filenames are prefixed with UTC date and time, for example:

```text
20260708-071523-issue-123-after.png
```

The script prints JSON containing `raw_url` and `markdown`. Paste `markdown`
directly into the GitHub PR or issue comment.

## Cleanup

List the configured gist, preview a batch deletion, or preview clearing all screenshots:

```bash
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py list
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py delete <gist-filename> [<gist-filename> ...]
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py clear
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py reset
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py prune-account \
  --before 2026-08-29T00:00:00+08:00
```

Deletion is a preview unless `--apply` is present. `clear --apply` keeps `README.md` but removes every other file. `reset --apply` creates and configures a replacement gist, then deletes the old gist and its history. Both invalidate existing screenshot links.

`prune-account` selects account gists by `updated_at` and defaults to descriptions matching `evidence`, leaving unrelated gists untouched. Add `--apply` after reviewing the preview.

Enable automatic retention for publishes that use the local gist configuration:

```bash
python3 skills/gist-screenshot-evidence/scripts/cleanup_gist.py configure-retention \
  --keep-days 7 \
  --timezone Asia/Shanghai
```

This provides a one-week buffer, rolls an older configured gist into a replacement before uploading, and prunes other expired evidence gists after a successful upload. Explicit `--gist-id` and `SCREENSHOT_GIST_ID` overrides bypass the policy.
