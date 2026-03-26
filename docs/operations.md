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

- CI still owns merge-blocking repo verification and PR-gate workflows, while `python3 tools/scripts/coordination.py watch` stays a local operator control loop for minute-level reminder checks
- the watch loop only delegates to the shared reminder runtime in `tools/scripts/coordination.py`, so the repo does not grow a second coordination engine just to support local scheduling
- operators who prefer `launchd` or `cron` should schedule `python3 tools/scripts/coordination.py remind --warn-before-minutes 1 --write-stub` instead of creating a second coordination script

## Protected-Path Escalation

- the new `reporter` lane normalizes packets, but PM still owns orchestration decisions, branch hygiene, and `docs/coordination/active.md` refresh policy
- coordination reminders may surface overdue scopes every minute, but they do not change scope order or override protected-path approval gates

## Release Marker Discipline

- `python3 tools/scripts/release.py prepare` emits release-readiness metadata only; it does not publish, deploy, or claim runtime parity that does not exist yet
- `.github/workflows/cd.yml` is manual-only so the repo can exercise release controls without pretending an always-on deployment path exists

## Rollback-Aware Delivery

- the D4 release scaffold is easy to roll back because it only changes release-preparation messaging and manual workflow control surfaces
- any real deploy or publish behavior remains deferred to D5, where runtime parity and rollback mechanics will have durable homes

## Frontend Deployment

- `apps/web` is now the only reviewer-visible frontend source of truth
- `.github/workflows/web-pages.yml` builds the Angular app with `bun run build:pages` and deploys to GitHub Pages on push to main
- GitHub Pages serves static output from `apps/web/dist/browser`
- the Pages build targets the `/food-run-ce/` project path and copies `index.html` to `404.html` so SPA refreshes stay on the active web shell
- This deployment path is intentionally honest: it is a static reviewer surface, not proof of full production maturity
- The workflow triggers on changes to `apps/web/**` or the workflow file itself
- Later work that adds real backend services will need separate deployment workflows
