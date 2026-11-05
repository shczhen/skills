---
name: living-one-pager
description: "Guide contributors to supply the facts and materials needed for content, and collect, clarify, sync, and update them in a living one-pager throughout the work. Use existing conversations, agent sessions, documents, or new ideas to prepare and maintain content inputs; this skill does not implement the underlying product."
metadata:
  version: "0.2.0-draft.4"
---

# Living One-pager

Help the person doing the work supply what content production needs. Provide a lightweight guide and template, extract available facts and materials, ask for useful missing inputs, and keep the one-pager current as the work changes. Match the user's language and existing tools. One person can be both the contributor and the eventual content author.

The skill's work is collecting, clarifying, and maintaining content inputs. Engineering planning and implementation belong to the underlying work and are not taken over by this skill. Finished articles, tutorials, or announcements are optional outputs when requested; useful source material is the core deliverable.

## Pick up the work where it is

- First use can happen at any point. Read the existing record and relevant sources identified by the user before summarizing or updating. Resolve supplied paths from the current project or their stated base; if a source is inaccessible, describe that specific gap and work from what is available. Preserve supplied originals and use their actual contents as evidence. Reuse the information already available rather than asking the user to repeat it.
- For an existing conversation or agent session, follow [source intake guidance](references/workflow.md#existing-work-and-sessions). Read the relevant available history, distinguish adopted decisions from suggestions, and capture the actual current state. Creating a record now does not mean the work is just starting.
- One record follows one round with a clear goal, including phased delivery. Reuse its location and identifier; link a new record when a later round has an independent goal.
- Describe progress by quoting or paraphrasing what the sources establish has happened. When only a goal is known, leave actual progress unverified and request existing material. Carry this same account into the saved page and final reply: saving a record changes the record, not the product. Establish availability, ownership, project identity, and dates from facts or an existing agreement; leave unsupported details unknown or omit them. Account and directory names identify the environment, not business ownership.
- Start with what is known and add detail as work happens. Solo use needs no invented team, reviewer, launch plan, or metric. Bring collaborators into important shared work early when useful; keep lightweight changes lightweight.

When the subject or intended output is unclear, clarify what is being documented or collected before assuming a writing assignment. A mention of building a tool or writing a skill is not a request for this skill to perform that development. When no subject or source is available, a short invitation to share the work or existing material is enough.

## Agree storage once

Before creating records, use the project's existing explicit storage choice. If none is available, read [initialization](references/workflow.md#initialization) and present the three defaults together with the resolved destination: **local project storage; relevant materials and available originals; as complete as possible, with history retained**. Give a useful synthesis while awaiting acceptance or adjustment; continue collecting material in conversation.

Loading a project-local skill selects instructions, not storage. Once defaults have been presented, an explicit request to create or save the one-pager can accept them; reuse that choice without another confirmation. Ask again only when the arrangement changes.

Follow existing record directories; otherwise use `work-items/<stable-id>/one-pager.md` in the current project. Record the accepted location, content, and detail level at the chosen entry point. External destinations depend on the user's selection and available tools.

## Gather what content needs

Use [the content-input guide](references/workflow.md#content-inputs) to find the relevant facts, examples, and evidence already available. Make the one-pager useful to someone preparing an explanation, tutorial, demo, update, or other content: what changed, for whom, why it matters, what is actually available, how to experience it, and what supports those claims.

Lead with the available material, what it can support, and the next useful source or clarification. Distinguish the product's users from the intended readers or use of the content when that helps. Ask for an existing example, document, dashboard, or explanation before expanding into a broad questionnaire. Keep ideas and planned value separate from delivered behavior and measured results.

## Leave useful work behind

Adapt the [template](assets/one-pager.md) rather than requiring every field. Keep the main page readable and link detailed materials:

- The intended audience or user, their problem, and this round's change or value.
- Actual progress, scope, availability, limits, and the next content input needed.
- Content inputs: explanations, examples, demos, screenshots, usage steps, documents, code references, and evidence, as available.
- Discussions, decisions, and their reasons.
- Actual results, feedback, and follow-up when available.

Preserve available original conversations, documents, attachments, and sources within the agreed scope; a concise main page is not a reason to discard them. Link originals already stored appropriately or copy them when needed. For conversations, retain relevant user **and assistant** contributions, including explanations, suggestions, and decisions, with their roles clear. As work continues, add the new material and substantive discussion to the linked source/history as well as updating the main page. State the coverage of an excerpt or summary honestly; note unavailable material.

## Update and learn

Read [update guidance](references/updates.md) for existing records. Preserve valid earlier decisions and important history; briefly explain changes and their basis. Treat suggestions as suggestions until adopted. Repeated input should update an existing entry rather than duplicate it.

Accept feedback in ordinary language, including what worked well. Distinguish its target:

- New information about the work belongs in the current record.
- A personal format or workflow choice belongs in the local template or agreement.
- Reusable skill behavior, unclear guidance, or missing capabilities can become a skill improvement; record the observed situation before guessing its cause.

Use the existing record or feedback notes to retain the situation, expected/actual result, and follow-up. Do not require a questionnaire or a GitHub account. When asked to prepare a public Issue, make a separate shareable draft with relevant skills, a concrete example, and known host/model/version details; unknowns can stay unknown. Keep private originals in their agreed location. Submit only when requested.

Change the relevant guide, template, or implementation when authorized, retaining local customizations. For behavior changes, try the original situation and relevant existing examples; ordinary wording or layout edits need no new test process. State what changed and how to try the updated version; a proposed fix is not a verified result.

## Reuse materials for communication

When there is an actual audience or request, build a tutorial, demo, explanation, or [brief](assets/communication-brief.md) from accumulated materials. Describe what exists, what is planned, and what remains unknown accurately. Drafting does not imply sending or publishing. For a public copy, use [export guidance](references/public-export.md).

Lead with the collected content inputs, meaningful changes, and the next material needed; link the one-pager and sources so they are easy to open. An updated record should help the content author see what can be used and what still needs clarification. Keep setup narration short. Do not add approval chains, stage gates, or scheduled checklists.
