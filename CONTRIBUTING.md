# Trying skills and contributing

## Try a skill

Start with that skill's instructions or README and a real task. Keep track of its installation source or commit when available, so you can tell which version you tried. Unknown is fine.

You can keep notes in your own files or conversation. No extra skill, account, or feedback tool is required for local use. Follow each skill's actual storage and publishing behavior; this repository does not collect your conversations automatically.

## Share feedback

You can tell your agent what helped or felt wrong in ordinary language. Ask it to prepare a public Issue draft if you want help reporting the experience. Review the draft before submitting it yourself or explicitly asking the agent to submit it.

- [Usage feedback or problem](https://github.com/shczhen/skills/issues/new?template=usage-feedback.yml): what you tried, what happened, and what you would have preferred. Successful experiences are useful too.
- [Improvement or new skill](https://github.com/shczhen/skills/issues/new?template=improvement.yml): the situation and unmet need. A proposed implementation is optional.

Both forms allow multiple related skills and an Other / Unsure choice. Keep one independently actionable problem or suggestion per Issue; a single problem may involve several skills. You can also open a blank Issue.

If you find an existing Issue about the same problem, add your details there. Otherwise, start with what you know. Environment details, versions, small examples, and screenshots help when relevant, but you do not need a full diagnostic report to give feedback. Free-text responses can be in any language.

Keep complete private materials in your own chosen location. Public Issues should contain only relevant shareable details, with credentials and private information removed; a fictional example is welcome when it explains the problem.

## Make a change

Explain the problem and resulting behavior in your PR, and link a related Issue when there is one. Update the affected instructions, templates, examples, or scripts together. Keep personal preferences local unless the change is useful as a shared default.

For behavior changes, retry the reported situation and relevant existing examples or tests. State what you checked and any remaining limits. Ordinary wording or layout changes do not need a new test suite. Root tooling commands are in the [README](README.md#development).

When adding, renaming, or removing a skill, update the skill choices in both `.github/ISSUE_TEMPLATE/usage-feedback.yml` and `improvement.yml` in the same PR. These lists are maintained in the files, not generated automatically. Include published skills; use Other / Unsure for anything not listed.

## Follow up after a change

Link the fix or explanation in the original Issue. Say which available version or commit contains it and how to get the update using the skill's installation method. A merged PR and a user's installed version can differ.

Try the original situation again after updating, and reply in the same Issue if it is still confusing or broken. Describe unverified results as unverified. Preserve existing user records and local settings when changing templates or storage conventions; document migration steps if needed.
