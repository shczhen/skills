# Living One-pager

Skill **0.4.0**. One page per product that the people who build it and the people who explain it both work from.

给每个产品维护一页：产品是什么，现在什么能用，哪些话可以对外讲，有哪些素材。研发的变化及时进到页面，内容从页面出。

## Install

```sh
npx skills@latest add shczhen/skills --skill living-one-pager
```

## Three things to ask for

```text
Use $living-one-pager to build a product page for <product>.
Material: <links, files, a repository path, or "this conversation">
Workspace: <wiki space or folder where product pages live>
```

```text
Use $living-one-pager to update the product page <link>:
<what changed; paste links, test results, or chat logs>
```

```text
Use $living-one-pager to prepare a <blog post / intro / demo script> for <audience> from the product page <link>.
```

## What a page holds

| Section | Answers |
|-|-|
| One-line summary and status line | What this is, where it stands, who maintains it, when it was last checked |
| Product description | What it is, who uses it, what it gives them |
| Capabilities and status | What works today and what does not yet |
| Try it | Where to start and how to get through it once |
| Claims | The numbers, comparisons, and promises external content may make, on what basis, within what limits |
| Materials | What exists, what needs to change, what is missing |
| Recent changes | What changed in the product |

Subpages hold decisions (append-only), the plan, and sources with discussion. The skeletons are in [assets](assets/).

A page stays true when changes reach it. Add one line to the product repository's agent instructions and the coding agent updates the page as it changes the product; the line is in [workspace layout](references/workspace.md#keep-current).

Claims are the part content people rely on. Each row gives one sentence content can use as written, the wordings to stay away from for now, and how far the sentence may travel. The agent suggests the scope and gives its reason. A person confirms it.

## Workspace

Pages live wherever the team already works: a wiki space, a docs folder, a repository directory. Name it in the request or in project instructions. Without one, the agent offers `./product-pages/` in the current project.

## Example

[Lantern](examples/lantern/product-page.md) is a fictional product: [what its maker supplied](examples/lantern/inputs.md), [the sources page](examples/lantern/sources.md), and [one update](examples/lantern/update.md).

## Feedback

Say what worked and what did not in the conversation, or open an issue with the [shared forms](https://github.com/shczhen/skills/issues/new/choose). See [CHANGELOG.md](CHANGELOG.md) for what changed between versions. [MIT license](LICENSE).
