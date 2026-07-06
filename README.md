# mimo-image

MCP server that forwards images to **mimo-v2.5** via its Anthropic-compatible API.

Claude Code strips images before sending to the model — this MCP works around that.

## Install

```bash
claude mcp add mimo-image \
  -e MIMO_API_KEY=你的key \
  -- node /Users/czhen/Documents/GitHub/mimo-image/index.js
```

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `MIMO_API_BASE_URL` | `https://token-plan-cn.xiaomimimo.com/anthropic` | mimo API endpoint |
| `MIMO_API_KEY` | **(required)** | API key |
| `MIMO_MODEL` | `mimo-v2.5` | Model name |

## Tools

| Tool | Description |
|---|---|
| `recognize_image` | General image description |
| `read_text_from_image` | OCR — extract text from image |
| `explain_screenshot` | Explain code/error/UI screenshots |
