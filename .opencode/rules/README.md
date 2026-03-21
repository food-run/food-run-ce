# Rules

## TL;DR

This folder holds shared execution rules that multiple agents and commands must follow. Keep cross-cutting behavior here so lane docs can stay short and consistent.

## Rule Set

- `coordination-standards.md` - stable coordination naming plus live reporting cadence and packet rules
- `master-packet-alignment.md` - how repo-control surfaces stay aligned with the master planning packet
- `implementation-standards.md` - shared coding standards, commenting rules, and implementation guidelines for active rebuild work

## Template Guidance

- Shared coordination template structure lives in `docs/templates/coordination/artifact-template.md`.
- Specialized templates should only add fields that are unique to that artifact type.

## Usage

- Treat these files as canonical when a lane or command references them.
- Keep agent and command docs DRY by linking here instead of re-explaining shared rules.
- Update these rules first when a cross-cutting workflow changes.
