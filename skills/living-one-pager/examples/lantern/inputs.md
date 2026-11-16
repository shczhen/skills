# Lantern: what the maker supplied

Lantern, its maker, its commands, and every number here are fictional.

## 2026-03-02, to build the page

**Maker:** Lantern is a local API-contract toolkit for developers who maintain HTTP APIs. It compares two OpenAPI definitions before a change ships. The CLI runs the comparison, a local HTML viewer explains the differences, and sample contracts let people try it. The CLI and the viewer work on my machine. JSON output is half done. The sample guide is a draft. I don't know how many other people use it.

**Maker:** A typical use is checking whether renaming a required field would break an existing client. Run `lantern compare before.yaml after.yaml`, then open the HTML report.

**Handout draft:** "Start checking in 30 seconds." "Catches every breaking change before it ships."

**Test note:** Six synthetic contract pairs, one prepared macOS environment. Median 46 seconds from install to first report.

## 2026-03-16, a change

**Maker:** JSON report output works now, merged today. There's a CI example in the repo too, still a draft.
