---
description: Prepare a Conventional Commit from the current checkpoint without pushing
agent: developer
---
# Checkpoint Commit Command

## TL;DR

This command evaluates the current diff for checkpoint readiness. It should be routed whenever a stable rollback point is reached, propose a Conventional Commit, summarize the checkpoint, and stop before pushing.

## Inputs

- None required

## Execution

Current diff:

!`git diff -- .`

Create:

- A recommended Conventional Commit subject
- An optional commit body
- A short checkpoint summary for `docs/coordination/checkpoints/`
- A refresh to `docs/coordination/active.md` so the checkpoint is visible in the dashboard
- A yes-or-no decision on whether the current diff should be committed now
- If the diff is coherent, ask for approval to run `git add` and `git commit` instead of batching more unrelated work first

## Failure Conditions

- The diff is not coherent enough for a useful rollback point.
- The checkpoint mixes unrelated changes.
- Coordination notes are not current enough to support the commit.

## Escalation Rules

Escalate when the right answer is to split the diff before committing.
