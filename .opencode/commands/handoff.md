---
description: Write a handoff summary for the next agent or the human
agent: pm
---
# Handoff Command

## TL;DR

This command creates a structured handoff so the next agent or human can continue without chat archaeology. It should summarize what changed, what remains, and what the next best action is.

## Inputs

- A task or workstream reference

## Execution

Create a structured handoff for:

$ARGUMENTS

Include:

- What changed
- What is still in progress
- Blockers
- Exact files involved
- ⚠️ Hotspot Files if relevant
- Recommended next agent
- Recommended next command

## Failure Conditions

- The summary hides blockers or uncertainty.
- The next step is still ambiguous.
- The handoff omits exact files or path groups.

## Escalation Rules

Escalate when the current state is not stable enough for handoff without more review.
