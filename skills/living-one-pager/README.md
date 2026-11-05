# Living One-pager

Skill **0.3.0** · Product template **1.0.0**. Keep a product understandable and its content materials current as it develops, launches, and evolves.

围绕同一个产品、能力或功能，把“是什么、给谁、价值、场景、怎么体验、有什么依据”讲清楚，并持续积累和更新内容材料。新目标、新版本、开发轮次不会自动另开一份 pager。个人可以同时提供和使用这些材料。

## Install and start

```sh
npx skills@latest add shczhen/skills --skill living-one-pager
```

Use it in your current work conversation: “用 $living-one-pager，把这个产品和已有材料整理清楚，后面继续维护。” Give the current conversation, an existing product page, a document, or an accessible agent session. Start at the actual state of the work; there is no need to retell its history or complete a form.

The agent reads the material, drafts a usable product explanation, and identifies the next useful input. Existing product pages and storage choices are reused. When there is no storage agreement, it shows these defaults together once:

| Choice | Default |
|---|---|
| Where | Local current project; reuse the record directory, otherwise `./work-items/<product-id>/one-pager.md`. |
| What | Related facts, progress, materials, discussion, decisions, feedback, data, and available original conversations and attachments, with sources. |
| How much | As complete as possible; keep context and history without automatic cleanup. |

Accept or adjust them together. Collection can continue while saving awaits your choice. Other local locations, Gist, documents/wiki, or combined destinations work with your choice and available tools. Secret Gists are unlisted, not access-controlled private storage.

For direct reading without installing, ask the agent to read `SKILL.md` from this package. Loading instructions does not choose storage.

## What stays together

The [template](assets/one-pager.md) helps explain the product, users/value, capabilities and scenarios, how to experience it, availability, evidence, and content materials. Adapt sections as needed. A main page can link detailed sources, history, demos, blogs, videos, decks, and handouts instead of containing every detail.

An internal product entry and a concise public one-sheet may use the same page or different views. No PDF, campaign, team, launch, business metric, or complete set of content formats is required. Product development continues through your existing tools; this skill gathers and maintains the facts and material for explanation and content.

When something changes, say it naturally: “新增能力和试用反馈在这里，更新原来的介绍，看看哪些材料也要改。” The agent updates the same product entry, retains important decisions/sources, and shows which existing claims or assets need attention.

## Versions and upgrades

Skill version, applied template version, and a page's own revision are separate. A generated Markdown page contains small version metadata; a wiki can show the same values in a version line. Actual saved changes get a short changelog entry; unchanged replays do not bump the revision.

Read [CHANGELOG.md](CHANGELOG.md) for skill and template changes. To update the installed skill, rerun the installation command and reload its instructions using your host's supported method. This does not automatically restructure existing documents.

To upgrade a page, say: “用当前模板升级这份已有 one-pager，保留内容、历史和我们改过的栏目。” The [upgrade guide](references/versions.md) covers unversioned/old work-round pages, current pages, and unknown/newer template versions. Keep the existing entry and customizations, retain its earlier account, and record the applied template and revision change. Unknown template versions are not silently downgraded.

## Examples

All examples are fictional:

- [Product and content materials](examples/product/one-pager.md), with [inputs and update](examples/product/source.md): a local API-contract toolkit receives a new capability and measured result, while its product page and affected content stay connected.
- [Solo product](examples/solo/one-pager.md), with [source](examples/solo/source.md): one person's local tool has a product explanation and useful documentation inputs.
- [Upgraded existing page](examples/existing-session/one-pager.md), with [prior account and source](examples/existing-session/source.md): preserve completed work, local choices and custom sections, and add explicit versions.

## Feedback and scope

Tell the agent what worked or felt wrong in ordinary language. Keep complete private notes in your chosen location. Personal preferences can change your local template; reusable problems can improve the skill. Public feedback can use the [shared multi-select Issue forms](https://github.com/shczhen/skills/issues/new/choose); select living-one-pager and other relevant skills. A public draft contains only shareable material, and submission happens when requested. See the [contribution guide](https://github.com/shczhen/skills/blob/main/CONTRIBUTING.md).

This remains an early tool to try in real work. Source-backed explanations, updates and upgrades need factual review; a plausible draft is not proof of product effectiveness. This package contains neutral fictional examples and no private development records. [MIT license](LICENSE).
