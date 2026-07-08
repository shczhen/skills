# skills

Personal Codex skills and bundled agent tools.

## Install

Install this skill collection with the skills.sh CLI:

```bash
npx skills@latest add shczhen/skills
```

Or with Bun:

```bash
bunx skills@latest add shczhen/skills
```

## Layout

```text
skills/
├── gist-screenshot-evidence/
└── mimo-image/
```

Each folder under `skills/` is a standalone skill. Keep reusable runtime code,
scripts, templates, and MCP servers inside that skill's `assets/`, `scripts/`, or
`references/` folders.

## Skills

| Skill | Description |
|---|---|
| `gist-screenshot-evidence` | Publishes screenshots to a GitHub Gist and returns Markdown image links for PR or issue comments. |
| `mimo-image` | Uses a bundled MCP server to send images, OCR tasks, and screenshots to `mimo-v2.5`. |

## Gist Screenshot Evidence

The first real publish creates and remembers a secret gist:

```bash
python3 skills/gist-screenshot-evidence/scripts/publish_screenshot.py ./screenshot.png --create
```

Later publishes reuse the remembered gist automatically:

```bash
python3 skills/gist-screenshot-evidence/scripts/publish_screenshot.py ./screenshot.png
```

The local gist id is stored in `skills/gist-screenshot-evidence/.local/config.json`.
That file is intentionally ignored by git.

## Mimo Image MCP

Install the server dependencies once:

```bash
npm install --prefix skills/mimo-image/assets/mcp-server
```

Then register the MCP server:

```bash
MCP_SERVER_PATH="$(pwd)/skills/mimo-image/assets/mcp-server/index.js"

claude mcp add mimo-image \
  -e MIMO_API_BASE_URL=https://your-mimo-api.example.com/anthropic \
  -e MIMO_API_KEY=your-key \
  -- node "$MCP_SERVER_PATH"
```

Environment variables:

| Variable | Default | Description |
|---|---|---|
| `MIMO_API_BASE_URL` | **(required)** | Mimo Anthropic-compatible API endpoint |
| `MIMO_API_KEY` | **(required)** | Mimo API key |
| `MIMO_MODEL` | `mimo-v2.5` | Model name |
