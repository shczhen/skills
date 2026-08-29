# skills

Personal agent skills and bundled tools, installable with [skills.sh](https://www.skills.sh/shczhen/skills).

## Install

Install this collection with the skills.sh CLI:

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

## Development

Install the root tooling and format every Biome-supported file:

```bash
npm ci
npm run format
```

Use `npm run format:check` for a non-writing check. Biome currently covers the repository's JavaScript and JSON; Python, Markdown, and YAML remain outside its formatter scope.

## Skills

| Skill | Description |
|---|---|
| [`gist-screenshot-evidence`](skills/gist-screenshot-evidence/README.md) | Publish screenshot evidence to a reusable secret GitHub Gist for PR or issue comments. |
| [`mimo-image`](skills/mimo-image/README.md) | Inspect images, OCR text, and explain screenshots through a bundled Mimo MCP server. |
