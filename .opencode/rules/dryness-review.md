# DRYness Review Rule

## TL;DR

Reuse and consolidation are mandatory review gates, not optional cleanup. Check DRYness before implementation starts and again before a scope can be called complete.

## Before Implementation

- run a reuse scan for the relevant concept across the repo
- identify what can be reused directly
- identify what should be extended or refactored instead of duplicated
- justify any newly created structure as meaningfully unique for the current boundary

## Meaningfully Unique Means

New code or structure must differ in at least one real way that matters to the repo, such as:

- different deployable boundary or ownership
- different runtime or execution model
- different data contract or invariants
- different user-facing responsibility
- different protected-path or operational requirements

If the change is not meaningfully unique, refactor or reuse instead of adding another copy.

## Before Completion

- PM must orchestrate a repo-wide DRYness review before declaring a goal complete
- reviewer must check for duplicate logic, duplicate concepts, and duplicate homes across the repo
- if the result is not meaningfully unique, the scope is not complete and must refactor or retry first

## Required Completion Summary

Every completion or closeout summary must include:

- what was reused
- what was created
- what was refactored
- what should be consolidated elsewhere but is outside the current scope

## Non-Goals

- do not invent abstraction just to sound DRY
- do not broaden scope just to chase every possible consolidation
- do not approve near-duplicates without an explicit uniqueness reason
