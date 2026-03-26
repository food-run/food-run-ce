---
description: Prepare a Conventional Commit from the current checkpoint without pushing
agent: developer
---
# Checkpoint Commit Command

## TL;DR

This command evaluates the current diff for checkpoint readiness. It should be routed whenever a stable rollback point is reached, propose multiple Conventional Commits (micro slices), summarize the checkpoint, and stop before pushing.

## Inputs

- None required

## Execution

Current diff:

!`git diff -- .`

Create:

- Recommended Conventional Commit subjects (type, scope, and description) written in clear English with 12-22 words and no raw identifier names
- Optional commit bodies
- A short checkpoint summary for `docs/coordination/checkpoints/`
- A confirmation that `docs/coordination/` reflects the checkpoint before the commits are created
- A confirmation that any required ADR entries are complete before the commit is considered merge-ready, including 2-5 bullets per ADR question and a 5-10 bullet `Current Status` sprint recap in `docs/adr.md`
- A refresh to `docs/coordination/active.md` so the checkpoint is visible in the dashboard
- A yes-or-no decision on whether the current diff should be committed now
- A scope choice that uses the first qualifying parent surface, such as `coordination`, `templates`, or `opencode`, and falls back to `repo` only when no narrower context cleanly covers the diff
- A split recommendation when the current diff is too broad and would force `repo` unnecessarily
- If the diff is coherent, ask for approval to run `git add` and `git commit` instead of batching more unrelated work first

## Failure Conditions

- The diff is not coherent enough for a useful rollback point.
- The checkpoint mixes unrelated changes.
- Coordination notes are not current enough to support the commit.
- A meaningful change is missing its completed ADR entry.

## Escalation Rules

Escalate when the right answer is to split the diff before committing.
