---
name: gist-screenshot-evidence
description: Publish screenshot evidence for GitHub PRs and issues by uploading image files to a user-owned GitHub Gist and returning Markdown-ready raw image URLs. Use when an agent needs to attach UI proof, regression screenshots, visual diffs, or browser evidence to GitHub PR or issue comments.
---

# Gist Screenshot Evidence

Use this skill when GitHub PR or issue work needs visual evidence.

## Workflow

1. Capture the screenshot with the task-appropriate browser or screenshot tool.
2. Save the screenshot as a local image file.
3. Publish the image with `scripts/publish_screenshot.py`, reusing the configured secret gist.
4. Paste the returned Markdown image link into the GitHub PR or issue comment.

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
