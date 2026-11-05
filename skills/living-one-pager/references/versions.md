# Versions and changelog

Keep three versions separate:

| Version | Meaning | Current draft |
|---|---|---|
| Skill | Instructions used by the agent; recorded in SKILL.md and CHANGELOG.md. | `living-one-pager@0.3.0` |
| Template | Structure actually applied to a document, identified independently for each template. | `living-one-pager` / `0.1.0`; optional `living-one-pager/communication-brief` / `0.1.0` |
| Document revision | This particular page's saved changes, independent of product releases. | Positive integer, starting at `1` for a new page. |

New Markdown pages record `template`, `template_version`, `revision`, `updated_with`, and `updated_at`. A wiki can show the same information in a small version line. Use the actual document change date, not a guessed product event date. These draft versions identify the material; they do not promise a stable schema.

On a real saved change, advance the existing document revision once, record the skill used, and add a short entry to its existing changelog/history explaining what changed and its source/reason. Re-reading, replaying incorporated information, or changing only the clock leaves the page and revision unchanged. Preserve an existing revision count and local customizations.

An ordinary content update retains the page's applied template version. Updating the installed skill does not automatically relabel or restructure documents. Existing work can be incorporated without refilling a form; do not claim a new template was applied merely because a newer skill wrote the update.

Read [CHANGELOG.md](../CHANGELOG.md) to see skill and template changes. Future template releases should describe the differences and any needed adaptation when that change is defined. A requested future adaptation should preserve product facts, custom sections, sources and history. This draft does not provide or guarantee migration paths for earlier drafts or unknown formats.
