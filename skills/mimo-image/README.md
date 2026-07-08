# mimo-image

Inspect images through a bundled MCP server that forwards image tasks to a Mimo
vision model.

## Capabilities

- `recognize_image`: describe an image.
- `read_text_from_image`: extract visible text.
- `explain_screenshot`: explain UI, code, or error screenshots.

## Setup

Install the MCP server dependencies once:

```bash
npm install --prefix skills/mimo-image/assets/mcp-server
```

Register the MCP server with your agent runtime:

```bash
MCP_SERVER_PATH="$(pwd)/skills/mimo-image/assets/mcp-server/index.js"

claude mcp add mimo-image \
  -e MIMO_API_BASE_URL=https://your-mimo-api.example.com \
  -e MIMO_API_KEY=your-key \
  -e MIMO_API_FORMAT=anthropic \
  -- node "$MCP_SERVER_PATH"
```

Use the equivalent MCP registration flow if your agent runtime is not Claude.
The skill itself is installed through skills.sh and is not tied to a single
agent runtime.

## Environment

| Variable | Default | Description |
|---|---|---|
| `MIMO_API_BASE_URL` | **required** | Mimo vision API endpoint |
| `MIMO_API_KEY` | **required** | Mimo API key |
| `MIMO_MODEL` | `mimo-v2.5` | Model name |
| `MIMO_API_FORMAT` | `anthropic` | API format: `anthropic` or `openai` |

The MCP server is meant for agents that cannot pass images directly to their
active model, including OpenAI-based and Anthropic-based agent workflows.

When `MIMO_API_FORMAT=openai`, the server calls `/v1/chat/completions` with an
OpenAI-compatible image message. The default `anthropic` format calls
`/v1/messages`.
