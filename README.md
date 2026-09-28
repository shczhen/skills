# skills

Personal agent skill for publishing screenshot evidence to GitHub Gist, installable with [skills.sh](https://www.skills.sh/shczhen/skills).

## Install

Install the skill with the skills.sh CLI:

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
└── gist-screenshot-evidence/
```

The `gist-screenshot-evidence` folder contains the skill instructions, scripts,
and tests.

## Development

Install the root tooling and format every Biome-supported file:

```bash
npm ci
npm run format
```

Use `npm run format:check` for a non-writing check. Biome currently covers the repository's JSON; Python, Markdown, and YAML remain outside its formatter scope.

## Skills

| Skill | Description |
|---|---|
| [`gist-screenshot-evidence`](skills/gist-screenshot-evidence/README.md) | Publish screenshot evidence to a reusable secret GitHub Gist for PR or issue comments. |
