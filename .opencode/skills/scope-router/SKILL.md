---
name: scope-router
description: Parse scope IDs and route work deterministically by sprint, deliverable, or task
license: Proprietary
compatibility: opencode
metadata:
  audience: maintainers
  workflow: orchestration
---
# Scope Router

## TL;DR

This skill parses a scope ID and determines the correct planning level, parent-child relationships, coordination file target, and next routing behavior.

## What I Do

- Parse `Sx`, `Sx-Dy`, `Sx-Dy-Tz`, `X-slug`, and `X-slug-Tn`
- Determine whether the scope is sprint, deliverable, or task
- Identify parent scope and likely child scopes
- Select the correct stable coordination file
- Prevent accidental broadening beyond the requested scope

## Stable Coordination Naming

Always prefer stable scope files:

- sprint: `docs/coordination/tasks/Sx.md`
- deliverable: `docs/coordination/tasks/Sx-Dy.md`
- task: `docs/coordination/tasks/Sx-Dy-Tz.md`
- ad hoc workstream: `docs/coordination/tasks/X-slug.md`
- ad hoc child task: `docs/coordination/tasks/X-slug-Tn.md`

Examples:

- `S0` -> `docs/coordination/tasks/S0.md`
- `S0-D1` -> `docs/coordination/tasks/S0-D1.md`
- `S0-D1-T2` -> `docs/coordination/tasks/S0-D1-T2.md`
- `X-repo-control` -> `docs/coordination/tasks/X-repo-control.md`
- `X-repo-control-T1` -> `docs/coordination/tasks/X-repo-control-T1.md`

## Routing Rules

### Sprint scope

- child scopes are deliverables
- route in dependency order
- do not execute sprint scope blindly if deliverable packets are missing

### Deliverable scope

- child scopes are tasks
- route in task order
- do not skip unfinished earlier tasks unless the packet explicitly allows it

### Task scope

- child scope is the implementation or review lane
- keep the task bounded
- do not automatically broaden into sibling tasks unless the parent run policy explicitly says `complete`

## When to Use Me

Use this skill at the start of every orchestration run and whenever a scope string is ambiguous.
