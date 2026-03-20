---
name: coordination-state
description: Reuse and repair stable coordination packets so resume and execute modes stay deterministic
license: Proprietary
compatibility: opencode
metadata:
  audience: maintainers
  workflow: orchestration
---
# Coordination State

## TL;DR

This skill makes `resume`, `execute`, and `review` deterministic by preferring stable coordination files over ad hoc loose notes and reusing valid state before replanning.

## What I Do

- Prefer stable scope files
- Fall back to the newest matching scoped coordination artifact only when necessary
- Carry forward valid current state into stable scope files
- Detect stale, conflicting, or incomplete coordination state
- Reduce unnecessary reruns of Scout and Planner

## Stable Coordination Lookup Order

For a requested scope, search in this order:

1. exact stable scope file
2. parent stable scope file
3. newest matching scoped coordination artifact
4. create the stable scope file if none exist

## Repair Rules

If scoped artifacts exist but a stable scope file does not:

- create the stable scope file
- carry forward the latest valid state
- mark the stable file as the canonical resume target

If the stable file exists but is stale:

- repair only the minimum missing state
- rerun Scout or Planner only if repair is not possible from current evidence

## Valid State Means

A coordination packet is valid when it clearly includes:

- scope
- current status
- current blockers
- current next step
- relevant planning file references
- enough detail to continue without chat archaeology

## When to Use Me

Use this skill in `resume`, `execute`, `review`, and `close-scope`.
