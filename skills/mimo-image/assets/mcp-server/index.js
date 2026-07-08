#!/usr/bin/env node

/**
 * mimo-image — MCP server that forwards images to a Mimo vision model
 *
 * Problem: some agent runtimes cannot pass images to the active model.
 * Solution: Accept image paths/base64 via MCP tools, send them to
 *           a Mimo vision endpoint with proper image support,
 *           and return the text response.
 *
 * Configuration via environment variables:
 *   MIMO_API_BASE_URL  — Mimo vision API endpoint (required)
 *   MIMO_API_KEY       — API key (required)
 *   MIMO_MODEL         — model name (default: mimo-v2.5)
 *   MIMO_API_FORMAT    — anthropic or openai (default: anthropic)
 */

import { readFileSync, existsSync, statSync } from "node:fs";
import { resolve, extname } from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ── Config ───────────────────────────────────────────────────────────────────

const API_BASE_URL = (process.env.MIMO_API_BASE_URL || "").replace(/\/+$/, "");
const API_KEY = process.env.MIMO_API_KEY || "";
const MODEL = process.env.MIMO_MODEL || "mimo-v2.5";
const API_FORMAT = (process.env.MIMO_API_FORMAT || "anthropic").toLowerCase();

if (!API_BASE_URL) {
  console.error("[mimo-image] MIMO_API_BASE_URL is required.");
  process.exit(1);
}

if (!API_KEY) {
  console.error("[mimo-image] MIMO_API_KEY is required.");
  process.exit(1);
}

if (!["anthropic", "openai"].includes(API_FORMAT)) {
  console.error("[mimo-image] MIMO_API_FORMAT must be 'anthropic' or 'openai'.");
  process.exit(1);
}

// ── Helpers ──────────────────────────────────────────────────────────────────

const MIME_MAP = {
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".gif": "image/gif",
  ".webp": "image/webp",
  ".bmp": "image/bmp",
  ".tiff": "image/tiff",
  ".tif": "image/tiff",
  ".svg": "image/svg+xml",
};

/**
 * Resolve image to { mediaType, base64Data } for Anthropic API.
 */
function resolveImage(input) {
  // Data URI
  const dataUriMatch = input.match(/^data:(image\/\w+);base64,(.+)$/);
  if (dataUriMatch) {
    return { mediaType: dataUriMatch[1], base64Data: dataUriMatch[2] };
  }

  // Raw base64
  if (/^[A-Za-z0-9+/=\n\r]{100,}$/.test(input.replace(/\s/g, ""))) {
    return { mediaType: "image/png", base64Data: input.replace(/\s/g, "") };
  }

  // File path
  const filePath = resolve(input);
  if (!existsSync(filePath) || !statSync(filePath).isFile()) {
    throw new Error(`File not found: ${filePath}`);
  }
  const ext = extname(filePath).toLowerCase();
  const mediaType = MIME_MAP[ext] || "application/octet-stream";
  const buf = readFileSync(filePath);
  return { mediaType, base64Data: buf.toString("base64") };
}

async function callMimo(image, prompt) {
  const { mediaType, base64Data } = resolveImage(image);

  if (API_FORMAT === "openai") {
    return callOpenAICompatibleMimo({ mediaType, base64Data, prompt });
  }

  return callAnthropicCompatibleMimo({ mediaType, base64Data, prompt });
}

async function callAnthropicCompatibleMimo({ mediaType, base64Data, prompt }) {
  const body = {
    model: MODEL,
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "image",
            source: { type: "base64", media_type: mediaType, data: base64Data },
          },
          { type: "text", text: prompt },
        ],
      },
    ],
  };

  const res = await fetch(`${API_BASE_URL}/v1/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": API_KEY,
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const errText = await res.text().catch(() => "");
    throw new Error(`mimo API ${res.status}: ${errText}`);
  }

  const data = await res.json();
  return data.content?.[0]?.text || "(no response)";
}

async function callOpenAICompatibleMimo({ mediaType, base64Data, prompt }) {
  const body = {
    model: MODEL,
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          {
            type: "image_url",
            image_url: { url: `data:${mediaType};base64,${base64Data}` },
          },
        ],
      },
    ],
  };

  const res = await fetch(`${API_BASE_URL}/v1/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const errText = await res.text().catch(() => "");
    throw new Error(`mimo API ${res.status}: ${errText}`);
  }

  const data = await res.json();
  return data.choices?.[0]?.message?.content || "(no response)";
}

// ── MCP Server ───────────────────────────────────────────────────────────────

const server = new McpServer({ name: "mimo-image", version: "1.0.0" });

server.tool(
  "recognize_image",
  "Send an image to mimo-v2.5 for recognition. Returns a text description. Use when you need to see an image but cannot process it directly.",
  {
    image: z.string().describe("File path or base64-encoded image"),
    prompt: z.string().default("Describe this image in detail.").describe("What to ask about the image"),
  },
  async ({ image, prompt }) => {
    try {
      const result = await callMimo(image, prompt);
      return { content: [{ type: "text", text: result }] };
    } catch (err) {
      return { isError: true, content: [{ type: "text", text: `Error: ${err.message}` }] };
    }
  }
);

server.tool(
  "read_text_from_image",
  "Extract all text from an image via mimo-v2.5 OCR.",
  {
    image: z.string().describe("File path or base64-encoded image"),
  },
  async ({ image }) => {
    try {
      const result = await callMimo(image, "Extract and transcribe ALL visible text from this image exactly as written. Preserve formatting. If no text, say '(no text found)'.");
      return { content: [{ type: "text", text: result }] };
    } catch (err) {
      return { isError: true, content: [{ type: "text", text: `Error: ${err.message}` }] };
    }
  }
);

server.tool(
  "explain_screenshot",
  "Explain a screenshot (code, error, UI) via mimo-v2.5.",
  {
    image: z.string().describe("File path or base64-encoded image"),
    context: z.string().default("").describe("Optional context about the screenshot"),
  },
  async ({ image, context }) => {
    try {
      const prompt = context
        ? `Context: ${context}\n\nExplain this screenshot in detail. If it contains code, transcribe and explain it. If it shows an error, explain and suggest fixes. If it shows a UI, describe the layout.`
        : "Explain this screenshot in detail. If it contains code, transcribe and explain it. If it shows an error, explain and suggest fixes. If it shows a UI, describe the layout.";
      const result = await callMimo(image, prompt);
      return { content: [{ type: "text", text: result }] };
    } catch (err) {
      return { isError: true, content: [{ type: "text", text: `Error: ${err.message}` }] };
    }
  }
);

// ── Start ────────────────────────────────────────────────────────────────────

const transport = new StdioServerTransport();
await server.connect(transport);
