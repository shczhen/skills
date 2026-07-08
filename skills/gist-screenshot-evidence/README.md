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
