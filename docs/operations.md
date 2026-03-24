# Operations

## TL;DR

This file is the durable operations guide for the rebuild. It should capture runtime visibility, release controls, rollback posture, and operational safety expectations as they become concrete.

## Scope

- observability and release posture
- rollback and recovery expectations
- operator-facing controls and routines
- how runtime changes become supportable

## Expected Growth Areas

- health and readiness surfaces
- release markers and deployment visibility
- failure handling and degraded modes
- operational runbooks and escalation paths

## Current Status

- Sprint 0 has not yet seeded the full runtime parity and observability stack
- later deliverables should extend this file instead of creating separate operations notes outside `/docs`

## CI as Operational Control

- CI still owns merge-blocking repo verification and PR-gate workflows, while `python3 tools/script/coordination_status.py watch` stays a local operator control loop for minute-level reminder checks
- the watch loop only delegates to the shared reminder runtime in `tools/script/coordination_status.py`, so the repo does not grow a second coordination engine just to support local scheduling
- operators who prefer `launchd` or `cron` should schedule `python3 tools/script/coordination_status.py remind --warn-before-minutes 1 --write-stub` instead of creating a second coordination script

## Protected-Path Escalation

- the new `reporter` lane normalizes packets, but PM still owns orchestration decisions, branch hygiene, and `docs/coordination/active.md` refresh policy
- coordination reminders may surface overdue scopes every minute, but they do not change scope order or override protected-path approval gates

## Release Marker Discipline

- `python3 tools/script/release.py prepare` emits release-readiness metadata only; it does not publish, deploy, or claim runtime parity that does not exist yet
- `.github/workflows/cd.yml` is manual-only so the repo can exercise release controls without pretending an always-on deployment path exists

## Rollback-Aware Delivery

- the D4 release scaffold is easy to roll back because it only changes release-preparation messaging and manual workflow control surfaces
- any real deploy or publish behavior remains deferred to D5, where runtime parity and rollback mechanics will have durable homes
