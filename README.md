# skills

Personal Codex skills and bundled agent tools.

## Layout

```text
skills/
└── mimo-image/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── assets/
        └── mcp-server/
```

Each folder under `skills/` is a standalone skill. Keep reusable runtime code,
scripts, templates, and MCP servers inside that skill's `assets/`, `scripts/`, or
`references/` folders.

## Skills

| Skill | Description |
|---|---|
| `mimo-image` | Uses a bundled MCP server to send images, OCR tasks, and screenshots to `mimo-v2.5`. |

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
