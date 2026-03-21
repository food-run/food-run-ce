# Master Packet Alignment Rule

## TL;DR

`docs/planning/master-packet.md` is the canonical planning source for product posture, architecture posture, governance posture, operating model, non-negotiables, and emoji semantics. Repo-control docs should reference and operationalize it without duplicating it carelessly.

## What Must Stay Aligned

- the prototype-preserving rebuild stance
- the active-vs-legacy boundary
- the five-plane architecture posture
- governed multi-agent delivery
- docs and ADR discipline
- protected human-only zones
- quality and review gates
- failure-posture honesty and operability
- the non-negotiables in section 23

## Repo-Control Reflection Rule

- keep canonical cross-cutting behavior in `.opencode/rules/`
- keep `AGENTS.md` as the always-on human and agent contract
- keep agents, commands, and skills short by referencing rules instead of restating them
- expand skills only where unique behavior is needed to help meet the master packet standards
- when current committed repo reality has already evolved beyond an older planning packet, treat the committed permanent structure as canonical by default
- refine planning docs to name the current permanent files instead of recreating stale packet-era homes
- stub a missing durable doc only when the exact permanent home is absent and its expected content is not already sufficiently covered elsewhere

## Emoji Rule

- when repo-control docs use the master packet emoji vocabulary, preserve the meanings defined in section 25
- do not introduce conflicting emoji semantics for existing lanes, markers, or events
- prefer plain text over improvised emoji when no approved master-packet emoji fits cleanly

## Drift Triggers

Escalate if any repo-control change:

- describes future-state architecture as if already implemented
- weakens a non-negotiable from the master packet
- conflicts with active-vs-legacy boundaries
- changes lane semantics or review rigor without updating the matching rule
