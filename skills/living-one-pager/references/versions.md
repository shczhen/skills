# Versions, changelog, and upgrades

## Three independent versions

| Version | Meaning | Current value |
|---|---|---|
| Skill | Instructions used by the agent; recorded in SKILL.md and CHANGELOG.md. | `living-one-pager@0.3.0` |
| Template | Structure actually applied to a document. Each template has an identifier and its own version. | `living-one-pager` / `1.0.0`; optional `living-one-pager/communication-brief` / `1.0.0` |
| Document revision | This particular page's saved changes. It does not name a product release. | Positive integer, starting at `1` for a new page. |

The Markdown templates contain `template`, `template_version`, `revision`, `updated_with`, and `updated_at`. Fill the actual document change date, not a guessed product event date. A wiki or another format can use a visible line with the same values. Keep the user's existing format and metadata where possible.

On an actual page change, advance the existing revision by one and append a brief changelog entry with what changed and its source/reason. Reuse an existing history section or link rather than creating a separate history system. Re-reading, replaying already incorporated information, or changing only the current clock does not change the page, its revision, or changelog. Preserve an established revision history; never restart its count as part of an upgrade.

An ordinary content update keeps the page's applied template version. Record the current skill as `updated_with` when it actually changes the document. If an older/unversioned page only needs a content change, retain its layout and identify its template as unversioned where useful; do not claim the current template was applied.

## Upgrading a one-pager on request

1. Read the existing page, metadata, customization, linked history, and the current template and changelog. Identify the applied template; missing metadata means **unversioned**, not a guessed old version.
2. Determine the supported path below. Use existing Git/document history to retain the old account. Without such history, a verbatim pre-upgrade copy beside the page keeps relative links working; link it from the history. An existing archive layout is also suitable when its source base and links remain usable. Keep the current entry's path, identifier, existing links, business decisions, sources, and custom sections.
3. Reorganize the existing facts into a useful product explanation. Incorporate existing progress; unknown information stays unknown. Link long discussions and preserve their contents. Do not require the user to refill fields or implement a missing capability.
4. Write the version actually applied, advance the known document revision once (start at `1` only if none was recorded), and record the upgrade and retained customization in the page's existing changelog/history. Link the pre-upgrade account when needed.
5. Report the old and new template versions, document revision, useful structure changes, and any unresolved facts. A second identical upgrade is a no-op.

## Supported paths in this release

- **Unversioned / 0.2.0-draft.4-era pages → main template 1.0.0:** keep the existing product entry; replace work-round framing with product definition, users/value, capabilities/use cases, experience, current availability, evidence and materials as relevant. Retain local-only choices, original source/history, and custom sections. Prior rounds become history within the same product, not new one-pagers. The skill version written in an old page does not by itself establish a template version.
- **Main template 1.0.0 → 1.0.0:** already current. Apply requested content changes if any, otherwise leave the files unchanged.
- **Unknown or newer template versions:** preserve them, explain the compatibility gap, and use the matching template/skill or request a scoped adaptation. Do not downgrade or falsely label the current template as an upgrade. Follow the same rule for unknown future formats.

Updating the installed skill does not rewrite documents automatically. Read the [skill and template changelog](../CHANGELOG.md) for differences, then request an upgrade for the existing page when wanted. The supported path is specific to this release, not a promise about future formats.

## Maintaining future releases

Keep skill and template versions independent. Describe skill behavior changes and each affected template version in CHANGELOG.md. Use template patch versions for compatible clarification, minor versions for compatible optional additions, and major versions for incompatible structural/meaning changes. Document the upgrade path when the template changes. Existing pages retain their applied version until actually migrated; new skill releases can keep the same template version.
