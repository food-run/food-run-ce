# Architecture

## TL;DR

This file is the durable architecture map for the active rebuild. It should explain the major runtime surfaces, boundaries, and cross-surface responsibilities as they become real in the repo.

## Scope

- active rebuild surfaces only
- cross-runtime structure and responsibility boundaries
- architecture posture that matches the repo and planning packet

## Expected Growth Areas

- experience, product, event, agent, and operations surfaces
- active tree boundaries under `apps/`, `shared/`, `platform/`, and `tools/`
- long-lived ownership decisions that later implementation should extend

## Current Status

- Sprint 0 has seeded the active tree under `apps/`, `shared/`, and `tools/`
- `platform/` remains a later Sprint 0 layer for runtime parity work
- later deliverables should extend this file instead of introducing separate architecture side notes

## Web Application (`apps/web`)

The web application is the reviewer-visible frontend surface for Food Run, built from the active rebuild tree under `apps/web`.

### Boundaries

- **Source of truth:** `apps/web` is the only public frontend source of truth
- **Deployment:** GitHub Pages serves static output from `apps/web/dist/browser`
- **Build:** Angular 21 with standalone components, built via `@angular-devkit/build-angular`
- **Output:** Static HTML/CSS/JS bundles via `bun run build`

### Deployment Path

- `.github/workflows/web-pages.yml` builds and deploys on push to main
- Triggers on changes to `apps/web/**` or the workflow file itself
- GitHub Pages is a static reviewer surface — it is not proof of full production maturity
- Later work that adds real backend services will need separate deployment workflows
