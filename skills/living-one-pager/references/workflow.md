# Living record guide

## Content inputs

The guide and template help contributors supply material that someone can turn into useful content. Extract what already exists before asking for more. One person may supply and use the material themselves; no content team or public launch is required.

Use these prompts where they fit the work and its current stage:

| Content need | Useful facts or materials to collect |
|---|---|
| Explain why it matters | Intended users and situations, their problem, the change from the current experience, expected value. |
| Describe what exists | This round's scope, actual progress, availability, access conditions, known limits, and changes to earlier plans or descriptions. |
| Show or teach it | A concrete example, usage steps, demo, screenshots, recording, code or documentation references, as available. |
| Support the claims | Results, observations, user feedback, data with its source and conditions; distinguish expected benefits from demonstrated outcomes. |
| Prepare the next content work | Which material is ready to use, the important gaps, and who or what can supply the missing input when known. |

These prompts are a collection aid, not required fields or approval gates. At idea stage, a problem and intended benefit may be all that exists; during development, gather examples and evolving scope; around delivery, clarify actual access and usage; after use, add results and feedback. Follow the actual work instead of demanding every stage's materials at once.

Show the useful synthesis first and ask for the next material gap that affects understanding or content preparation. For example, a tutorial may need the actual usage steps; a release update may need confirmation of who can use it. Ask for those inputs, rather than designing or implementing the underlying feature to fill the gap. Record missing or unavailable material honestly.

## Existing work and sessions

The input can be a new idea, an ongoing conversation, an existing agent session, documents/code/results, or an existing living record. Infer the useful entry point from what the user has already given; this is not a required mode-selection questionnaire.

- **Current conversation:** use visible earlier messages and supplied artifacts directly. Retain relevant exchanges with speaker roles, including assistant explanations and proposals; their presence in the source does not make them adopted decisions. Do not ask the user to restate information already present.
- **Specified session:** use the host's available conversation-reading tools for the supplied link or identifier, following pagination for the relevant history. If the host cannot read it, accept an export or pasted conversation. Ask for a locator or accessible material only when missing; do not scan unrelated sessions or rely on a guessed local session-storage path.
- **Existing documents or output:** resolve the supplied location and read it before extracting facts. For example, `fixtures/observations.md` refers to that existing project file; use its contents, retaining any test-data label and limits. If unavailable, ask for access or an accessible copy. A request to summarize it includes this read-only inspection without another approval question. Reading sources does not authorize unrelated edits or publication.
- **Existing record:** reuse it for the same goal. If no record exists, create the first record from the work already done; do not reset status to idea or invent earlier lifecycle steps.

Recover the problem and goal, what actually happened, the current state, decisions with their reasons, and materials that can support content. Identify the next useful contribution or factual clarification without turning every unknown into a question. Suggestions from an assistant or another source stay suggestions unless adopted.

Keep source references and available original content under the storage agreement. Distinguish the record's creation date from event dates and any actual project start date. Describe which messages/pages/files were read; an incomplete transcript or retrieval summary is not a complete session export. Later evidence can extend the same record.

## Initialization

On first use in a project, show these defaults together for acceptance or adjustment. Display the resolved destination, not just a relative placeholder. An existing explicit arrangement takes precedence and needs no repeated confirmation.

| Choice | Default | Alternatives |
|---|---|---|
| Where | Local current project. Reuse its record directory; otherwise `./work-items/`. No automatic external sync. | A specified local path, Git repository, Gist, document/wiki, or a combination; identify the destination and audience. |
| What | This work item's background, progress, materials, discussions, decisions, feedback, data, and available original conversations and attachments, retaining sources. | Adjust the scope; keep originals, links, or different kinds of material in different places. |
| How much | As complete as possible, with context and history. No automatic truncation or cleanup. | Summaries, key events, or different detail/retention choices for different materials. |

Example: “I'll keep this locally at `<actual project path>/work-items/`, preserving this work's materials, discussions, decisions, feedback, and available originals as completely as possible. Use these defaults, or change anything?”

Save the agreement in the selected project entry point or record; reuse it for subsequent work items. A brief acceptance or an already explicit user choice is enough. An explicit request to create or save the one-pager after these defaults were displayed can accept that arrangement. Do not turn this into separate questions for every field. Confirm changes to location, scope, or detail level before applying them.

Present the default arrangement alongside an initial synthesis when source material is already available. If the user continues discussing the work without answering the storage question, continue collecting and clarifying content inputs in conversation and leave saving pending; do not reissue the same setup question. An explicit request to save after that can be paired with the unresolved storage confirmation. Never treat silence or continued discussion as acceptance.

The main page summarizes the current situation. Detailed sources and history remain accessible through links or supporting files. Preserve supplied originals when available; record links or availability limits for material you cannot retrieve. This scope covers the current work, not unrelated conversations or files.

Different materials can use different locations. Follow the user's actual tools and access; if a destination cannot be written, explain the limitation and prepare the content in the conversation without silently changing storage. A secret Gist is unlisted, not access-controlled private storage.

## Use one entry point through the work

One record follows a round with a clear goal and can link to a long-lived product or capability. Keep it through idea, development, delivery, observation, and iteration as relevant. A later independent goal can get a linked record. These are descriptions of work, not required stages.

Begin with a few useful sentences; adapt the template and add material as work happens. An individual maintains their own record. In shared work, one maintainer keeps the current account while contributors supply facts they know. Involve people who will need the output early for important work; lighter changes can be reviewed when useful.

Keep progress, content inputs, discussions, decisions, results, and the next missing material together. Describe plans as plans, suggestions as suggestions, and observations with their actual scope. Do not require a launch, business metric, content campaign, or an empty section where none serves the work.

When new information arrives, update the agreed one-pager and its material links. If multiple destinations were selected, synchronize the relevant parts according to that agreement and report any destination that could not be updated. An update request does not imply continuous background monitoring or sending notifications.

## Maintain the guide and template

When information is missing, duplicated, or awkward to use, adjust the relevant local guide or template. Keep a short reason in the discussion or commit. A personal preference need not become a universal default; recurring friction can justify a reusable change.

Reviews happen when they help answer a real question. There is no required reporting schedule, approval chain, or fixed checklist.
