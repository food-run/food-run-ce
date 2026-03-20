---
description: Kick off a sprint, deliverable, or task from the relevant planning files
agent: pm
---
# Kickoff Command

## TL;DR

This command starts a bounded work unit from the current planning files. It should ground the task, restate boundaries, identify risks, and create the first coordination state before implementation begins.

## Inputs

- One or more relevant planning files

## Execution

Use these planning sources as the current source of truth:

!`cat $ARGUMENTS`

Do all of the following:

1. Summarize the goal, boundaries, dependencies, and success criteria.
2. Identify active paths, protected paths, and ⚠️ hotspot files.
3. Name the best initial routing order.
4. Create or update a task note in `docs/coordination/tasks/`.
5. Seed `docs/coordination/active.md` with the in-flight scope and next expected heartbeat.
6. Create or switch to the scoped working branch before implementation begins.
7. Stop before implementation unless the user explicitly asked to implement now.

## Failure Conditions

- The planning files conflict materially.
- The scope is too broad to route safely.
- The requested work implies protected-path edits without explicit approval.

## Escalation Rules

Escalate when planning ambiguity would lead to drift or when protected paths are unexpectedly involved.
