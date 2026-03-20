# Legacy v0

## TL;DR

Legacy v0 is preserved because it already proved the core Food Run product loop, but it should be treated as historical evidence rather than as the active technical base. This document records what v0 validated, what technical shortcuts it contained, and which concepts are safe to carry into the rebuild.

## Snapshot of the Prototype

`legacy-v0/` contains the original prototype client, server, runtime entry files, and generated static output that previously lived at the repo root. The archive is preserved as a coherent snapshot so reviewers can inspect what was actually built and proven.

## Validated User Flows

The prototype validated the core Food Run loop:

- collecting recipe URLs
- extracting recipe metadata and ingredients
- letting users confirm or adjust parsed ingredients
- combining selected recipes into a shopping list
- grounding the concept in a working end-to-end demo

## Prototype Architecture Snapshot

Legacy v0 used a single prototype-era layout with root-owned frontend and backend runtime files, a `client/` app, a `server/` app, and generated static artifacts. That layout was useful for validation speed, but it blurred the long-term ownership boundaries needed for the rebuild.

## Known Constraints

- prototype runtime and build files lived at the root, which made the archive look like the active app
- generated static output sat beside active planning docs under `docs/`
- app, infra, docs, and governance boundaries were not yet separated into permanent rebuild surfaces
- the prototype optimized for proof of value, not for long-term maintainability or governed parallel work

## Preservation Rules

- preserve `legacy-v0/` as historical evidence of the validated prototype
- keep original structure and naming legible so the snapshot stays reviewable
- do not add new implementation work inside `legacy-v0/`
- document reuse decisions in active rebuild paths instead of mutating the archive

## Safe Reuse Candidates

- proven product flows and user sequencing
- data-model ideas and parsing heuristics worth re-implementing deliberately
- UX lessons from the working prototype
- operational knowledge about what the prototype needed to run, as input for later active-tree design
