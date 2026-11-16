# Lantern

A local toolkit that compares two versions of an OpenAPI definition and shows which changes would break existing clients.

**Stage:** works on the maker's machine, not announced · **Maintainer:** the maker · **Last checked:** 2026-03-16 · **Next milestone:** to be confirmed (no dates supplied)

## Product description

Lantern is for developers who maintain HTTP APIs. Before a change ships, they compare the old and new OpenAPI definitions and see what an existing client would trip over.

A typical case: a required field is renamed. The developer runs one command, opens the report, and sees which requests and responses no longer match.

It runs locally. The CLI does the comparison, an HTML viewer explains each difference, and sample contracts let a newcomer try the flow without an API of their own.

## Capabilities and status

Status lives only in this table.

| Capability or component | Status | Conditions and basis |
|-|-|-|
| Compare two OpenAPI definitions from the CLI | available | Maker's account, macOS. Other platforms to be verified |
| HTML report viewer | available | Local only. Maker's account |
| JSON report output | available | Since 2026-03-16. Maker's account |
| Sample contracts and guide | partly available | Contracts are usable. The guide is a draft |
| CI example | in development | Draft in the repository |

## Try it

1. `lantern compare before.yaml after.yaml`
2. Open the HTML report it writes.

## Claims

One row per subject whose truth rests on evidence or conditions. Rows run hold, internal only, public.

| # | Say this | Basis and conditions | Not yet | Scope |
|-|-|-|-|-|
| 1 | — | No coverage test supplied. | "Catches every breaking change before it ships" (handout). Needs a coverage test. | Hold. Nothing on coverage is supported yet. |
| 2 | In our test, Lantern went from install to first report in a median of 46 seconds. | [Test note](sources.md#test-note): six synthetic contract pairs in one prepared macOS environment. | "Start checking in 30 seconds" (handout). Needs a measurement of what "start" means here. | Suggest public. |

## Materials

| Material | Used for | State | Claims used and open items |
|-|-|-|-|
| [Handout](inputs.md#2026-03-02-to-build-the-page) | Introduction sheet | draft | Uses the Not-yet wordings of 1 and 2. Does not mention JSON output |
| CI example | Getting-started sample | draft | Makes no claim yet. Any "works in CI" line waits for the final example |

Missing: screenshots of the viewer, a blog post (proposed, not written), any account of use by someone other than the maker.

## Recent changes

- **2026-03-16** JSON report output became available.

[Sources](sources.md)
