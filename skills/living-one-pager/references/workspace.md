# Workspace layout

A workspace has a **catalog** that lists product pages, and usually a guide and a template page for people.

## Wiki

- A product page is a child of the catalog page. Its subpages are its children.
- Use the wiki's native headings, tables, and links. Link the subpages at the bottom of the product page.
- When the catalog is an automatic child-page list, creating the child page lists it. Otherwise add a link.
- Reach the wiki with whatever the host provides (a CLI, an MCP server, a wiki skill). When it is out of reach, write the page as local files, and name the missing access in the report.

## Local folder

```text
<workspace>/README.md              catalog: one link per product
<workspace>/<product>/product-page.md
<workspace>/<product>/decisions.md
<workspace>/<product>/plan.md
<workspace>/<product>/sources.md
<workspace>/<product>/drafts/      content prepared from the page
```

## A page owned by someone else

Edit pages the user maintains or names for editing in the request. A page that belongs to someone else, or that arrives as source material, stays as it is: write the new page in the workspace, list the original in its Sources table, and say in the report that the original still exists and who owns it when that is known. The user decides with the owner which one stays.

## Supplied files

Link files and pages where they already live. Material that exists only in the conversation is saved in the product's folder, or as a child page in a wiki, so the Sources table has something to link to. A local product folder takes a short lowercase name from the product's most official name.

## A page in an older format

On its next update, move it into the skeleton: each fact goes to its one home, wording that still holds is kept, and material with no home on the product page goes to a subpage. Say in the report that the page was restructured.

## Keep current

A page goes stale when product changes never reach it. Close the gap at the source by adding one line to the agent instructions of the product's repository (`AGENTS.md`, `CLAUDE.md`, or equivalent), filled in with the page's address:

```text
After a change to what users can do, how they get in, or a limit they will hit, use living-one-pager to update the product page: <page link>
```
