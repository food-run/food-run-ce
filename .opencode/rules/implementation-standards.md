# Implementation Standards

## TL;DR

Implement narrowly, reuse before inventing, keep boundaries stable, and leave work easy to explain, review, and roll back. Apply `.opencode/rules/dryness-review.md` before implementation starts and before completion.

## Core Principles

- keep diffs small and coherent
- prefer reuse over invention
- choose clear ownership over convenience
- optimize for explainability, not cleverness
- preserve active-vs-legacy boundaries

## Path And Ownership Rules

- new implementation belongs only in active rebuild paths, never in `legacy-v0/`
- keep one home per concept
- avoid junk-drawer roots and vague shared buckets
- stop and escalate if ownership is ambiguous

## Code And Structure Rules

- follow the current planning packet before adding structure
- keep abstractions earned and current-use-case driven
- do not hide business rules in transport, middleware, or UI layers
- do not suppress errors to make checks pass
- keep comments sparse and only where they help with non-obvious logic

## Verification Rules

- pair meaningful implementation with the right level of verification
- leave review hotspots and rollback notes when risk is non-trivial
- keep docs and ADR context aligned when shared understanding changes
- reject work that is not meaningfully unique under `.opencode/rules/dryness-review.md`

## Commit And Coordination Rules

- stop at stable rollback points and recommend a checkpoint commit
- choose Conventional Commit scopes using the first qualifying parent surface; prefer `coordination`, `templates`, or `opencode` when they cleanly fit the change, and fall back to `repo` only when no narrower context covers the diff
- if a checkpoint would need an overly broad `repo` scope, split it into smaller coherent slices before committing
- write commit subjects in clear English using 12-22 words, and avoid raw identifier names in the message
- do not batch unrelated work after a coherent checkpoint is ready
- keep `docs/coordination/` current as work progresses
- include reused, created, refactored, and deferred consolidation notes at closeout

## Escalate Instead Of Guessing

- protected-path edits
- planning conflicts
- unclear concept ownership
- scope that cannot remain narrow
