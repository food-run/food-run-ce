# Rules

## TL;DR

This folder holds shared execution rules that multiple agents and commands must follow. Keep cross-cutting behavior here so lane docs can stay short and consistent.

## Rule Set

- `coordination-naming.md` - stable naming for coordination files across planned and ad hoc work
- `dryness-review.md` - preflight and closeout DRY/reuse gates for implementation and review
- `master-packet-alignment.md` - how repo-control surfaces stay aligned with the master planning packet
- `progress-reporting.md` - how active work reports status in `docs/coordination/` and in chat
- `implementation-standards.md` - shared coding standards and implementation guidelines for active rebuild work

## Template Guidance

- Shared coordination template structure lives in `docs/templates/coordination/artifact-template.md`.
- Specialized templates should only add fields that are unique to that artifact type.

## Usage

- Treat these files as canonical when a lane or command references them.
- Keep agent and command docs DRY by linking here instead of re-explaining shared rules.
- Update these rules first when a cross-cutting workflow changes.
