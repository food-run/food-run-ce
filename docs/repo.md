# Repo Layout

## TL;DR

The repository has one active rebuild surface and one archived prototype surface. Contributors and agents must add new work only to the active rebuild paths, treat `legacy-v0/` as read-most reference material, and preserve a shallow, ownership-driven root layout.

## Repo Intent

This repo preserves validated prototype evidence while the team rebuilds Food Run into a production-grade, documented system. The root should make that split obvious: active rebuild control surfaces stay active, and prototype implementation surfaces stay archived.

## Active Versus Archived Paths

Active rebuild surfaces:

- `docs/`
- `.opencode/`
- `.github/`
- `AGENTS.md`
- `opencode.json`
- repo-governance files kept at the root

Archived prototype surface:

- `legacy-v0/`

Planned active rebuild homes that later Sprint 0 deliverables will seed:

- `apps/`
- `shared/`
- `platform/`
- `tools/`

## Root Directory Rules

- keep only repo-level control, governance, and navigation files at the root
- keep planning and coordination under `docs/`
- do not restore prototype app paths such as `client/` or `server/` to the root
- do not treat archived runtime files in `legacy-v0/` as the active build entrypoint

## Path Ownership

- `legacy-v0/` preserves the validated prototype as a coherent snapshot
- `docs/` holds planning, coordination, and durable technical documentation
- `.opencode/` holds agent operating rules and reusable skills
- `.github/` holds repository automation and review workflow files
- future application and shared-code ownership belongs in the active rebuild tree, not in archived prototype paths

## Prohibited Drift Patterns

- adding new implementation directly under `legacy-v0/`
- recreating archived prototype paths at the root by convenience
- mixing prototype build artifacts into active planning or technical-doc paths
- describing future Sprint 0 scaffolding as if it already exists in the repo

## Naming and Depth Rules

- prefer ownership-driven root names over generic buckets
- keep the root shallow and reviewable
- preserve original prototype names inside `legacy-v0/` when practical so the archive stays inspectable
- add new rebuild paths only when the relevant planning packet explicitly calls for them
