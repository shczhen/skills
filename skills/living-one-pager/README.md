# Living One-pager

Trial version: **0.2.0-draft.4**. A lightweight guide and workflow for contributors to supply what content production needs: collect facts and materials, clarify useful gaps, and keep a one-pager updated from idea to outcome. Works for one person or collaborators.

围绕一轮目标，提供规范、模板和流程，引导使用者交出内容需要的信息与素材，汇集到 one-pager 并持续同步更新。个人也可以给未来的自己准备这些材料。

The core output is usable content input: who the work is for, what changes and why it matters, actual progress and availability, usage examples and assets, and evidence when available. Use the [collection guide](references/workflow.md#content-inputs) to extract existing information and ask for the next useful missing material. Underlying development stays with the contributor's existing workflow. Finished content can be prepared separately when requested.

**可以随时开始用。** 工作已经做了一半、已经上线，或只存在聊天记录里，都可以先整理出当前档案，再接着维护。

## Install and use / 安装与使用

Install this skill with the skills.sh CLI:

```sh
npx skills@latest add shczhen/skills --skill living-one-pager
```

Use it in a new or existing conversation, for example:

```text
用 $living-one-pager，把我们刚才讨论的这件事整理起来，后面有进展继续更新。
```

Your existing conversation or materials are enough to start. Installation does not choose where your work is stored; the skill follows the project agreement or presents the local defaults below once.

## Try without installing / 直接试用

Open a project folder in an agent with file access. Ask it to read the skill directly; this does not require adding it to a global skill directory:

```text
读取 <此技能目录>/SKILL.md，并按它处理。
把当前聊天里这件事整理成一份可持续更新的档案，沿用已有决定和进展。
```

也可以直接给已有材料或 session：“根据这份文档／这个 agent session 整理当前工作”；如果还没有任何材料，给一段新想法即可。工具能直接读取就先读，不能读取时再提供导出或内容。无需先开一个从零开始的项目，也不需要重新讲一遍已有历史。

The agent extracts available content inputs, shows the important material gaps, and asks once about storage if this project has no agreement. Collection and clarification can continue while saving awaits confirmation. Defaults are:

| Choice | Default |
|---|---|
| Where / 存在哪儿 | Local current project; reuse its record directory, otherwise `./work-items/`. |
| What / 存什么 | This work's background, progress, materials, discussions, decisions, feedback, data, and available original conversations and attachments, with sources. |
| How much / 存多少 | As complete as possible; retain context and history, with no automatic truncation or cleanup. |

Accept or change these together. Existing explicit choices are reused. You may choose another local path, Git repository, Gist, document/wiki, or a combination; external storage requires suitable tools and access. Secret Gists are unlisted, not access-controlled private storage.

A concise main page links to detailed materials; it does not replace them. The [guide](references/workflow.md) and [template](assets/one-pager.md) can also be used manually. No connector, database, or script is required for local Markdown use.

## Keep content inputs current / 更新内容材料

```text
这些是新的进展或素材：<已有内容>。更新原来的 one-pager，告诉我内容现在能用什么，还缺什么。
```

```text
根据这份档案和已有材料，准备一份给 <读者> 的 <说明/教程/演示/brief>。
```

One record follows one goal through development, delivery, feedback, and iteration as relevant. As facts and materials arrive, synchronize the relevant parts to the agreed destinations and show unresolved content gaps. A later independent goal gets a linked record. Adapt the sections and requested materials to the actual stage; solo use requires no team, approval chain, launch, or business metric. Reviews happen when useful.

## Feedback and changes / 反馈与修改

You can say “这里太长”“漏掉了之前的决定”“这个格式很好用” directly. Keep the situation, relevant input/output, and follow-up in the agreed local record. Good results matter as well as failures.

- New information about the work updates that work's record.
- Personal preferences change the local template or agreement.
- Reusable skill problems or ideas can become improvements to the guide, template, or implementation.

For public discussion, use the [shared feedback forms](https://github.com/shczhen/skills/issues/new/choose), or ask the agent to prepare a separate shareable Issue draft. Select `living-one-pager` and any other related skills. The [contribution guide](https://github.com/shczhen/skills/blob/main/CONTRIBUTING.md) explains reporting and follow-up. Include what you tried, what happened, what you wanted, and any relevant skills. Host/model/version and a small example help when known; unknowns are acceptable. Keep complete private originals local. Review the draft before submitting it or asking the agent to submit it. No GitHub account is required for local use and feedback notes.

After a change, retry the original situation and relevant existing examples. Record what changed, the result, and which version to try. Updating a skill should preserve your records and local customizations. For a direct-read setup, ask the agent to read the updated skill source; you can continue in the same conversation. For an installed copy, use the host's supported installation/update method.

## Example / 示例

The [solo example](examples/solo/one-pager.md) and [input](examples/solo/source.md) are entirely fictional. They illustrate a local record, a progress update, and a personal workflow choice.

The [existing-session example](examples/existing-session/one-pager.md) and its [input](examples/existing-session/source.md) show first using the skill after work has already been completed, preserving decisions without restarting the project. All details are fictional.

## Scope and public copies / 使用范围与公开副本

Follow the user's language, tools, and chosen storage. Use [export guidance](references/public-export.md) when preparing a public copy; keep private sources separate. Preparing content does not send, sync, or publish it.

## Trial status / 试用状态

This is an early trial, `0.2.0-draft.4`. Limited runs covered new goals, intake from existing work, and updates. Some outputs still turned missing information into unsupported progress or result claims, or drifted into planning the underlying development. Review the facts and proposed next actions before reusing the material. These trials do not establish long-term content or GTM effectiveness.

The [MIT license](LICENSE) applies to this skill and its fictional examples.
