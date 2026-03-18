---
name: parallel-lane-policy
description: Decide when async or parallel subagent work is truly safe and when sequencing is the correct choice
license: Proprietary
compatibility: opencode
metadata:
  audience: maintainers
  workflow: orchestration
---
# Parallel Lane Policy

## TL;DR

This skill decides whether work may be split into async-safe parallel lanes or whether sequencing is the safer answer. It exists to prevent fake speed that actually creates merge conflict, path drift, or review debt.

## What I Do

- Check path overlap
- Check protected-path involvement
- Check ⚠️ Hotspot-File overlap
- Check whether the planning packet already defines a safe split
- Recommend safe parallel fan-out or explicit sequencing

## Safe Parallel Conditions

Parallel work is allowed only when all of these are true:

- the scope is sprint or deliverable level
- path overlap is low
- protected paths are not involved
- ⚠️ Hotspot-File overlap is low
- the split is already defined as safe or clearly low-risk

## Unsafe Parallel Conditions

Do **not** parallelize when any of these are true:

- root ownership is changing
- structural relocation is in progress
- `README.md` is being rewritten
- `docs/repo.md` or `docs/adr.md` is being changed
- protected paths are involved
- sequencing is an explicit dependency in the planning packet

## Output Format

Return:

- safe to parallelize: yes or no
- reasoning
- suggested lanes if yes
- exact reason to sequence if no

## When to Use Me

Use this skill before async or parallel subagent fan-out at deliverable or sprint scope.
