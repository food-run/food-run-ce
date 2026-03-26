# Repo Layout

## TL;DR

The repository has one active rebuild surface and one archived prototype surface. Contributors and agents must add new work only to the active rebuild paths, treat `legacy-v0/` as read-most reference material, and preserve a shallow, ownership-driven root layout.

## Repo Intent

This repo preserves validated prototype evidence while the team rebuilds Food Run into a production-grade, documented system. The root should make that split obvious: active rebuild control surfaces stay active, and prototype implementation surfaces stay archived.

## Active Versus Archived Paths

Active rebuild surfaces:

- `apps/`
- `shared/`
- `tools/`
- `platform/`
- `docs/`
- `.opencode/`
- `.github/`
- `AGENTS.md`
- `opencode.json`
- repo-governance files kept at the root

Archived prototype surface:

- `legacy-v0/`

Current posture for active rebuild homes:

- `apps/` and `shared/` are already seeded and should be extended in place
- `tools/` is already seeded for shared repo automation and verification work
- `platform/` remains the later Sprint 0 runtime-parity layer and should be added only when the current planning packet calls for it

## Root Directory Rules

- keep only repo-level control, governance, and navigation files at the root
- keep planning and coordination under `docs/`
- do not restore prototype app paths such as `client/` or `server/` to the root
- do not treat archived runtime files in `legacy-v0/` as the active build entrypoint

## Path Ownership

- `legacy-v0/` preserves the validated prototype as a coherent snapshot
- `apps/` holds deployable runtime homes for active rebuild work
- `apps/web/` owns its app-local Bun package surface, including frontend build, lint, and browser-smoke dependencies
- `shared/` holds seam-level shared contracts, schemas, adapters, and test support
- `tools/` holds shared automation, verification, and operator-facing scripts for the rebuild
- `docs/` holds planning, coordination, and durable technical documentation
- `.opencode/` holds agent lane docs, commands, rules, and reusable skills
- `.opencode/` may keep its own local package surface when plugin dependencies are specific to OpenCode rather than the active app runtime
- `.github/` holds repository automation and review workflow files
- future application and shared-code ownership belongs in the active rebuild tree, not in archived prototype paths

## Planning Drift Rule

- when the committed repo has already evolved beyond an older planning packet, treat the current committed permanent structure as canonical by default
- refine the planning packet to name the current permanent files instead of recreating stale packet-era filenames
- stub a missing durable doc only when the exact permanent home is absent and its expected content is not already sufficiently covered elsewhere
- do not create duplicate repo-control or docs-spine files just to satisfy stale planning wording

## Prohibited Drift Patterns

- adding new implementation directly under `legacy-v0/`
- recreating archived prototype paths at the root by convenience
- mixing prototype build artifacts into active planning or technical-doc paths
- describing future Sprint 0 scaffolding as if it already exists in the repo
- recreating stale packet-era repo-control files after the committed repo has already converged on a better permanent home

## Naming and Depth Rules

- prefer ownership-driven root names over generic buckets
- keep the root shallow and reviewable
- preserve original prototype names inside `legacy-v0/` when practical so the archive stays inspectable
- add new rebuild paths only when the relevant planning packet explicitly calls for them
