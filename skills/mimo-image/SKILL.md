---
name: mimo-image
description: Use mimo-v2.5 for image recognition, OCR, and screenshot explanation through a bundled MCP server. Use when Codex needs to inspect an image file, read text from an image, explain a code/error/UI screenshot, or work around an environment where the active model cannot receive images directly.
---

# Mimo Image

Use this skill when the task requires visual inspection through Mimo instead of native model vision.

## Capabilities

- Describe image contents with `recognize_image`.
- Extract visible text with `read_text_from_image`.
- Explain code, error, or UI screenshots with `explain_screenshot`.

## MCP Server

The bundled MCP server lives in `assets/mcp-server/`.

Install dependencies before registering it:

```bash
cd <path-to-this-skill>/assets/mcp-server
npm install
```

Configure it with:

```bash
claude mcp add mimo-image \
  -e MIMO_API_BASE_URL=<your-mimo-api-base-url> \
  -e MIMO_API_KEY=<your-key> \
  -- node <path-to-this-skill>/assets/mcp-server/index.js
```

Environment variables:

- `MIMO_API_BASE_URL`: required Anthropic-compatible API endpoint
- `MIMO_API_KEY`: required API key
- `MIMO_MODEL`: defaults to `mimo-v2.5`

## Workflow

1. Confirm the local MCP server is configured when the tools are unavailable.
2. Use `recognize_image` for general visual questions.
3. Use `read_text_from_image` for OCR-like extraction.
4. Use `explain_screenshot` for screenshots where code, UI state, or errors matter.
5. Pass local file paths whenever possible; use base64 or data URIs only when no file path is available.
