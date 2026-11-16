---
name: living-one-pager
description: "Keep one product page that the people who build a product and the people who explain it both work from: what it is, what works today, which claims are safe to make, and what materials exist. Use to build a product page from existing material, to update it after a product change, decision, or new evidence, or to prepare a blog, intro, or demo script from it."
metadata:
  version: "0.4.0"
---

# Living One-pager

A product page lets someone who was not in the room answer four questions: what is this product, what works today, what can I say about it, and what materials already exist. Product, engineering, content, and ecosystem people all read and change the same page, so it has to stay true as the product moves.

Every request is one of three jobs: **build** a page from existing material, **update** it after something changed, or **prepare** content from it. Each starts by finding the page.

## Find the page

The **workspace** is where the team keeps its product pages: a wiki space, a docs folder, or a directory in a repository. Take it from the request or from project instructions. When neither names one, ask once, offering `./product-pages/` in the current project as the default. [Workspace layout](references/workspace.md) covers wikis, local folders, supplied files, pages owned by someone else, and pages in an older format.

One product has one page. Search the workspace's product catalog for this product first: a new version, a new round of development, and a new conversation all belong on the existing page. Read the page and its subpages in full before changing them.

Write in the language the workspace already uses. Product names, commands, and quoted claims keep their original wording.

## The page

The skeleton is fixed, so readers know where to look and every fact has **one home**. Use the workspace's own template page when it has one, otherwise [the bundled skeleton](assets/product-page.md).

| Fact | Its one home |
|-|-|
| What the product is, who uses it, what it gives them | Product description |
| A goal or target the team is working toward | Product description, under a heading marked internal |
| Whether a capability works today | Capabilities and status table |
| What content may say where a material makes a number, comparison, or promise; its basis; how far it may travel | Claims table |
| Something made to show the product's audience, its state, and the claims it uses | Materials table |
| A change in the product | Recent changes |
| A decision and its reason | Decisions subpage, append-only |
| A date or milestone | Plan subpage |
| Where the facts come from, full evidence, discussion, original conversations | Sources subpage |

Everywhere else, link to a fact's home. Create a subpage from [the subpage skeletons](assets/subpages.md) once it has content. The page and these three subpages hold everything recorded about the product; drafts prepared from it sit beside them.

The page is a one-pager: a colleague from another team reads it in five minutes. A table cell holds a sentence or two that state what is known and where it shows. The reasoning and the full evidence behind a cell live on the Sources subpage.

## What counts as a fact

- **The product outranks its descriptions.** The running product, its repository, and its public docs are sources for what exists and how it works. Pages, decks, drafts, and the promotional lines inside those sources are claims to check.
- **What users can reach decides a status.** "Available" means a user can get to it today; whether anyone has seen it work goes in the basis. Work that exists only in a repository or a local build is in development, and its basis says how far it has come.
- **Every status and claim carries its basis:** where it comes from and the conditions under which it holds, such as date, environment, sample size, and what was measured. Say whether you ran the thing or read about it, once above the table when the answer is the same for every row. A figure the company publishes on its own site is basis for repeating it as published.
- **The page holds what is true now.** A basis cell, a source row, and each section of the Sources subpage state the current finding; a new read replaces the old text. The account of what a check did and did not cover goes in your report.
- **Unknown stays visible.** Write "to be confirmed" and what would settle it.
- **Disagreement stays visible.** When two materials say different things, record each with where it appears: in the claim's row when the subject is a claim, otherwise in the disagreement table on the Sources subpage. The maintainer chooses between them.
- **You suggest, people confirm.** A claim's scope starts as your suggestion with its reason: "suggest public" or "suggest internal only". Once the maintainer or the user confirms it, the cell reads "public" or "internal only" with their name and the date.

## Build a page

1. **Read everything offered,** then follow it to the direct sources a status or claim will rest on: the live product, the repository, the public docs. Fetch the source itself; a search result or a cached copy is a lead. Run the product when you can and a run would settle a conflict; otherwise name that run in the report. Done when each source is read, or listed as unread with the reason.
2. **Write the product description** in the team's own words where they exist. It holds what stays true for months, as plain statements; the team's comparatives and superlatives go to the claims table. When materials disagree on the product's name, title the page with the public docs' name in the workspace's language, or the name the request uses when the docs have none, and record the others as a disagreement.
3. **Fill the capabilities table,** one row per thing a user comes to the product to do or per component, each status checked against a direct source. A set of examples is one row.
4. **Pull the claims.** A claim is a line the materials use to win their reader, whose truth rests on evidence or conditions: a number, a comparison or superlative, a promise about time, effort, or outcome such as "no setup needed". Go through every material and collect them. A promotional line in a direct source counts when a material repeats it. Plain description that agrees with the product description and the capabilities table stays there, and setup requirements, test records, and other working detail stay with their sources.
   - **One row per subject,** such as time to first result or the number of examples. Every wording of that subject, from every material, lands in its row.
   - **Say this** is one sentence a writer can paste into a post unchanged, in the voice and at the length of a line in the team's materials: the widest wording that the evidence and the statuses from step 3 support. When it would mislead without a condition, it carries that one condition in a few words, such as "in our test"; every other condition stays in the basis cell. A test result someone will want to quote belongs here. When the evidence supports no sentence yet, write a dash.
   - **Not yet** lists each wording in circulation that goes further than the basis: the few words that overreach, quoted once, then the materials that use them, then what would release it.
   - **Scope** covers the Say-this sentence: public or internal only, with the reason. A row with no sentence to use is on hold.
   - Order the rows hold, internal only, public. Once the page is saved a claim keeps its number, and later claims take the next one.

   Done when every number, comparison, and promise the materials use to win their reader appears in a row, as the sentence to use or under Not yet.
5. **Fill materials, recent changes, and the status line.** A material is something made to show the product's audience: an intro, a post, a deck, a video, a demo, public docs. Plans, test notes, and review records are sources, and so are the product's own pages and guides until users can open them. Under materials, list what content will need that does not exist yet. Recent changes starts with the few most recent dated changes to capabilities found in the sources.
6. **Create the Sources subpage,** source table first, and any other subpage that has content.
7. **Save** the page under the workspace's catalog and confirm the catalog lists it. A link supplied as source material is read-only. When the user maintains the product's repository, offer the [keep-current line](references/workspace.md#keep-current).
8. **Report** in this order: where the page is, the conflicts between materials that matter most (the full list lives on the Sources subpage), the wordings content has to stop using and why, what you did not read or run, what a person needs to confirm or supply.

## Update a page

[One worked update](examples/lantern/update.md) shows the steps on a small page.

1. **State the change in one sentence** after reading the page, its subpages, and what the user supplied. When the request is to check the page and names no change, re-read each source in the Sources table, compare it with the page, and set its "last read" date. A source you cannot reach keeps its old date.
2. **Edit the fact's one home.**
3. **Follow the ripple** in this order:
   - the capabilities row;
   - claims whose basis or wording depends on it, plus the claims that any new or changed material makes, pulled as in Build step 4. A Not-yet wording whose release condition is now met moves into Say this;
   - materials that use those claims;
   - plan: write the outcome beside the target, and add target dates the sources newly show;
   - decisions: append what a person stated or a source records, citing it, and mark what it supersedes. A decision you only inferred goes under open questions;
   - status line.

   Done when every claims row and every materials row has been checked against the change. In every table, a row the change does not touch stays word for word.
4. **Add one dated line to Recent changes** for each change to the capabilities table, dated when the product changed, or when you found the change if no source dates it. Changes that arrived together share a line. Set "last checked" to today.
5. **Report:** what changed on the page, claims added or changed in scope or wording, materials that no longer match the product with the exact passage in each, what this check did not cover, what a person needs to confirm. Edit a material itself when the request includes it. When the page had drifted from the product, check that the repository carries the [keep-current line](references/workspace.md#keep-current) with this page's address.

## Prepare content

1. **Re-check before writing.** Read the page, then compare each capability and claim the piece will rely on with its direct source, and set "last read" on the sources you re-read. Reading the source again counts; a past measurement is checked against its record. When a source contradicts a status or a claim's basis, or now supports a Not-yet wording, fix the page first as in Update steps 2 to 4. A re-check that finds nothing different changes only the "last read" dates. Anything else you notice goes in the report. Done when each one is re-checked today or named in the report as not re-checked.
2. **Write from the page:** the product description, capabilities whose status is available, and the Say-this sentence of each claim whose scope covers this audience. A scope that is still a suggestion may go into a draft. Fit a sentence to the piece's voice and keep its numbers and conditions; the basis cell stays on the page. On a subject the claims table covers, the claim outranks the other sections. A capability that is not yet available appears with its status.
3. **Save the draft** where the request says, otherwise beside the product page (a child page in a wiki, `drafts/` in a local folder). The file holds the piece; its state and the claim numbers it uses go in the materials table.
4. **Report** alongside the draft: what the re-check found and the page edits it caused, what was not re-checked, claims used, which of them need confirmation before publishing, what you left out and why.
