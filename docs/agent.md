# Agent Workflow

## TL;DR

This file explains how Food Run uses governed agent workflows. It should stay aligned with `AGENTS.md`, `opencode.json`, and `.opencode/**` as lane behavior evolves.

## Scope

- lane responsibilities
- approval and escalation expectations
- artifact and review expectations
- how agent work stays aligned with human review

## Current Control Surfaces

- `AGENTS.md`
- `opencode.json`
- `.opencode/agents/`
- `.opencode/commands/`
- `.opencode/rules/`
- `.opencode/skills/`

## Current Status

- the control surfaces already exist in the repo
- later changes should update this file when the agent operating theory changes in a durable way

## Required Lane Order

- implementation-bearing task work starts with `architect`
- `architect` defines invariants, failure modes, TDD shape, and scaffolding before `developer` or `designer` begins
- `developer` or `designer` executes one bounded implementation lane at a time
- `reviewer` and `integrator` must pass before `ops` reviews the same diff
- `ops` must run on implementation-bearing work before `librarian` closeout, PR preparation, or merge-ready status
- `librarian` closes the durable docs delta after the implementation and operational review path is complete

## Why This Order Exists

- it keeps implementation strategy explicit instead of burying it inside the first code patch
- it makes TDD shape and boilerplate a designed input rather than an accidental side effect
- it gives reviewer and integrator a bounded diff before ops evaluates blast radius, workflow hygiene, and cost or reliability risk
- it helps catch leaks such as local runtime byproducts before a human reviewer has to do cleanup
