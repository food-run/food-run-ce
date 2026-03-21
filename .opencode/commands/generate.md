---
description: Generate a new implementation file or scaffold that matches repository standards from the first line
agent: architect
---

# Generate Command

## TL;DR

This command generates new implementation files or scaffolding without creating cleanup debt. It belongs to `architect` so implementation-bearing generation starts from an explicit TDD shape, invariants, and boundary plan before `developer` or `designer` extends it.

## Inputs

- a short description of what to generate
- optional target paths
- optional planning files

## Execution

Before writing anything:

- open the relevant planning packet
- if the packet drifted from committed repo reality, refine the packet target to the current permanent structure before generating files
- confirm the intended ownership boundary
- check for reuse and consolidation under `.opencode/rules/implementation-standards.md`
- identify whether the file is:
  - a script-like entry file
  - an automation runner
  - a non-script code file
  - a documentation file

When generating code:

- write the file in its real permanent home
- use exact semantic naming
- prefer 1–2 words where possible and 4 words maximum
- keep the first checkpoint bounded and explainable
- if the file allows comments and is not Markdown:
  - start with the canonical all-caps `TL;DR` multi-line header wrapped with `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
  - use only single-line comments outside the TL;DR: should be 1 line per intent
  - add section-group comments using the shared style for the language
  - mark partial or deferred work with `TODO:`
- if the exact permanent file cannot be named yet:
  - do not generate a placeholder file
  - stop and escalate instead

When generating documentation:

- put deep technical documents under `docs/**`
- do not create generic placeholder documents
- stub only the first exact permanent file that will actually be needed first
- if the expected durable home already exists or its content is already sufficiently covered elsewhere, extend that home instead of creating another doc
- if that file cannot be named yet, omit it

Before returning:

- state what was reused
- state what was created
- state what was refactored
- state what should be consolidated elsewhere but is outside the current scope
- say whether a checkpoint commit is due
- say whether the next lane should be `developer`, `designer`, or `librarian`

## Failure Conditions

- the generated file duplicates an existing concept
- the chosen path is ambiguous
- the file is not in its real permanent home
- a comment-capable code file is generated without the canonical TL;DR header when required
- multi-line comments are used outside the TL;DR
- generic placeholder files are created instead of exact permanent files
- the generated structure is not meaningfully unique for the current boundary

## Escalation Rules

Escalate when:

- generation would require a protected-path change
- the ownership boundary is unclear
- the exact permanent file cannot be named yet
- the planning packet does not support the requested structure
- reuse or consolidation would require a broader scope decision
