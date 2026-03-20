# Food Run

## TL;DR

Food Run is being rebuilt from a validated prototype into a production-grade, technically documented system. The old prototype is preserved under `legacy-v0/` as reference material, while all new work targets the active rebuild paths and the technical docs in `/docs`.

## Quick Navigation

- Repo operating contract: `AGENTS.md`
- Sprint 0 overview: `docs/planning/sprint-0/overview.md`
- Repo layout rules: `docs/repo.md`
- Legacy archive guide: `docs/legacy-v0.md`
- Preserved prototype snapshot: `legacy-v0/README.md`

## Where Technical Docs Live

Deep technical guidance for the rebuild lives in `docs/`. Planning packets stay under `docs/planning/`, live coordination stays under `docs/coordination/`, and durable repo-boundary guidance lives in files like `docs/repo.md` and `docs/legacy-v0.md`.

## Current Status

The repo is in rebuild mode. The validated prototype is preserved under `legacy-v0/`, and Sprint 0 is establishing the governed baseline that later deliverables will use to seed the active application tree.

## What This Repo Contains Now

- repo-governance files such as `AGENTS.md`, `opencode.json`, and `.opencode/`
- planning and coordination material under `docs/`
- contributor and governance documents at the root
- the archived prototype under `legacy-v0/`

## Active Rebuild Path

New implementation work belongs only on the active rebuild surfaces described in `AGENTS.md`: `apps/`, `shared/`, `platform/`, `tools/`, and `docs/`, with repo-control surfaces such as `.opencode/`, `.github/`, `AGENTS.md`, and `opencode.json` remaining active for governance and automation. Sprint 0 deliverables after S0-D1 will seed the permanent active tree in those rebuild locations.

## Legacy Prototype

The archived prototype shows the validated Food Run product loop that existed before the governed rebuild started. Use `legacy-v0/README.md` for the preserved snapshot guide and `docs/legacy-v0.md` for the record of what v0 validated, what constraints it carried, and what can be reused safely.

## Architecture Direction

Food Run is moving from a single prototype layout into a documented multi-surface rebuild with explicit ownership boundaries, preserved legacy evidence, and durable technical docs that guide later product, platform, and agent work.

## Contribution Boundary

Do not extend `legacy-v0/` with new implementation work. Treat the prototype paths as preserved reference material only, and start new rebuild work in the active surfaces documented in `AGENTS.md` and `docs/repo.md`.
