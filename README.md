# skills

Personal agent skills for writing and development, installable with [skills.sh](https://www.skills.sh/shczhen/skills).

## Install

Install skills with the skills.sh CLI:

```bash
npx skills@latest add shczhen/skills
```

Or with Bun:

```bash
bunx skills@latest add shczhen/skills
```

Install a specific skill:

```bash
npx skills@latest add shczhen/skills --skill anti-defensive-writing
```

## Layout

```text
skills/
├── anti-defensive-writing/
├── gist-screenshot-evidence/
└── living-one-pager/
```

Each folder contains its skill instructions and any supporting resources.

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
| [`anti-defensive-writing`](skills/anti-defensive-writing/SKILL.md) | Writing guidance for direct, precise GPT-6.x replies and documents. |
| [`gist-screenshot-evidence`](skills/gist-screenshot-evidence/README.md) | Publish screenshot evidence to a reusable secret GitHub Gist for PR or issue comments. |
| [`living-one-pager`](skills/living-one-pager/README.md) | Maintain a product explanation, evidence, and content materials, with versioned draft templates and document changelogs. |

## Feedback and contributions

[Share usage feedback, report a problem, or suggest an improvement or new skill](https://github.com/shczhen/skills/issues/new/choose).
The forms support multiple related skills and an Other / Unsure choice. Start
with what you tried and what happened; a full diagnostic report is optional.
See [CONTRIBUTING.md](CONTRIBUTING.md) for trying skills, preparing shareable
feedback, and following up after a change.

## Try Living One-pager

```bash
npx skills@latest add shczhen/skills --skill living-one-pager
```

Use it with your existing conversation or materials to explain a product and keep
its one-pager and content materials current through releases and iteration. Skill
0.3.0 includes draft template 0.1.0, page revisions, and changelogs. Future template
changes will describe their differences when defined. It supports solo use and local storage defaults.
See the [guide and fictional examples](skills/living-one-pager/README.md) for use,
updates, and trial limits.
