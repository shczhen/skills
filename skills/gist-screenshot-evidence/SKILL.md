---
name: gist-screenshot-evidence
description: Publish and clean up screenshot evidence in a user-owned GitHub Gist. Use when an agent needs Markdown-ready image URLs for GitHub PRs or issues, or needs to list, batch-delete, or clear previously uploaded evidence.
---

# Gist Screenshot Evidence

Use this skill when GitHub PR or issue work needs visual evidence.

## Workflow

1. Capture the screenshot with the task-appropriate browser or screenshot tool.
2. Save the screenshot as a local image file.
3. Publish the image with `scripts/publish_screenshot.py`, reusing the configured secret gist.
4. Paste the returned Markdown image link into the GitHub PR or issue comment.

Use `scripts/cleanup_gist.py` when the reusable gist needs inspection or cleanup. Deletion invalidates links to the removed screenshots.

## Requirements

- `gh` CLI must be installed and authenticated.
- The authenticated GitHub account must be able to create or update gists.
- `git` must be installed and able to push to GitHub.
- Reuse one secret gist. The script remembers the created gist in `.local/config.json`.

## Publish A Screenshot

Create and remember the reusable secret gist once:

```bash
python3 <path-to-this-skill>/scripts/publish_screenshot.py ./screenshot.png --create
```

Reuse the remembered gist for every later screenshot:

```bash
python3 <path-to-this-skill>/scripts/publish_screenshot.py ./screenshot.png
```

To override the remembered gist, pass `--gist-id <gist-id>` or set
`SCREENSHOT_GIST_ID`.

Set a stable filename and alt text:

```bash
python3 <path-to-this-skill>/scripts/publish_screenshot.py ./screenshot.png \
  --filename issue-123-after.png \
  --alt "Issue 123 after fix"
```

Uploaded filenames are always prefixed with the UTC date and time, for example
`20260708-071523-issue-123-after.png`. This avoids collisions and makes old
evidence easy to find or delete.

The script prints JSON containing:

- `gist_id`: reuse this for later screenshots.
- `raw_url`: direct image URL.
- `markdown`: GitHub-ready image Markdown.
- `html_url`: gist page URL.
- `config_path`: local ignored config path that stores the remembered gist id.

## Commenting

After publishing, include the `markdown` value in the PR or issue comment:

```markdown
Verification screenshot:

![Issue 123 after fix](https://gist.githubusercontent.com/example/abc123/raw/issue-123-after.png)
```

Prefer one gist per long-running repo or issue batch. Keep `.local/config.json`
uncommitted.

## Clean Up Screenshots

Inspect the configured gist without changing it:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py list
```

Preview a batch deletion by exact gist filename:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py delete \
  20260708-071523-issue-123-before.png \
  20260708-071700-issue-123-after.png
```

Preview removing every file except the gist's `README.md`:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py clear
```

Preview replacing the configured gist and deleting the old gist, including its history:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py reset
```

Deletion commands are plans by default. Repeat the reviewed command with `--apply` to perform the mutation. `clear --apply` keeps the gist and its Git history; use `reset --apply` when the gist is over its size quota or its history must be removed. Both invalidate existing screenshot links.

To preview deleting old evidence gists across the authenticated account, use an explicit timezone-aware cutoff:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py prune-account \
  --before 2026-08-29T00:00:00+08:00
```

`prune-account` selects by `updated_at` and defaults to descriptions matching `evidence`, keeping unrelated gists outside the skill's scope. Review the description summary, then repeat with `--apply` to delete every selected gist and its history.

## Automatic Retention

Enable opportunistic retention for publishes that use the locally configured gist:

```bash
python3 <path-to-this-skill>/scripts/cleanup_gist.py configure-retention \
  --keep-days 7 \
  --timezone Asia/Shanghai
```

On each successful publish, the script starts a replacement gist when the configured gist was created before the retention cutoff, then deletes older account gists whose descriptions match `evidence`. The cutoff is midnight in the configured timezone; `keep_days: 7` provides a one-week buffer. Calls that override the gist with `--gist-id` or `SCREENSHOT_GIST_ID` bypass automatic retention.
