# Testing

## TL;DR

This file is the durable testing and verification guide for the rebuild. It should explain how unit, integration, contract, smoke, and agent-output checks work as the system grows.

## Scope

- verification posture across runtime surfaces
- required test layers and when they apply
- how review, smoke checks, and quality gates fit together

## Expected Test Layers

- unit tests
- integration tests
- contract tests
- smoke validation
- agent-output verification

## Current Status

- Sprint 0 has established shared test support in `shared/testkit/`
- repo verification already runs through `python3 tools/scripts/verify.py`
- `.github/workflows/repo-verify.yml` already enforces that verifier in CI
- `python3 tools/scripts/coordination.py watch` now provides the local-only minute-level reminder loop without expanding the CI verifier contract
- the active frontend package surface currently uses Bun in `apps/web/`, while `legacy-v0/` still keeps its frozen npm-era workflow as archived reference only
- the active frontend now advertises an app-local `bun run lint` command and a minimal `bun run e2e` Playwright smoke suite under `apps/web/`
- the active frontend still does not advertise an app-local unit-test runner because the current truthful test contract is lint plus browser smoke plus build and Pages-artifact verification
- later deliverables should extend this file with deeper runtime, contract, and smoke-specific commands as those layers become real

## Merge Gates

- `tools/scripts/verify.py` is the central repo verification entrypoint for local and CI-safe checks
- `.github/workflows/repo-verify.yml` should stay a thin wrapper that sets up Python, installs Bun, and calls `python3 tools/scripts/verify.py --ci`
- later D4 release scaffolding should stay beside these workflows instead of duplicating their checks in YAML

## Docs and ADR Verification

- `.github/workflows/docs-guard.yml` now treats `Summary`, `Why this change`, `Files and boundaries`, and `Verification` as merge-blocking PR narrative sections for every PR
- `.github/workflows/docs-guard.yml` also checks governed changes for a real `Docs and ADR delta` plus an updated `docs/adr.md`
- meaningful repo-control and shared-understanding changes should keep `docs/adr.md` current before merge-ready status

## Protected-Path Verification

- `.github/workflows/protected-paths.yml` now requires explicit PR acknowledgement when protected paths change, including any `.github/workflows/**` edit and the exact protected-path categories from `AGENTS.md`
- `.github/workflows/cla-check.yml` now skips the CLA phrase gate for repository-owner-authored PRs while keeping the exact phrase requirement for outside contributors
- `shared/testkit/coordination.py` covers coordination parser and reminder-loop behavior for the shared runtime in `tools/scripts/coordination.py`
- `shared/testkit/release.py`, `shared/testkit/verify.py`, and `shared/testkit/workflows.py` keep the governed workflow and script contracts bound to the central script seams without a `tools/testing/` shadow home

## Current Verifier Scope

- Python script syntax across active rebuild script surfaces
- governed TL;DR header and section-comment checks for script files
- shared repo-control suites loaded from explicit `shared.testkit.*` modules instead of `test_*.py` filename discovery
- repo-verification workflow contract checks so CI keeps delegating to the central verifier
- coordination cadence checks outside CI, with an explicit CI-safe skip for local-only coordination artifacts
- reviewer-frontend build verification in `tools/scripts/frontend.py` that checks the GitHub Pages base path and SPA fallback artifact contract
- app-local frontend lint and Playwright smoke commands that operators run from `apps/web/` until the browser suite is mature enough for central repo gating
- governed header checks in `tools/scripts/verify.py` now also cover `apps/web/playwright.config.ts` and `apps/web/e2e/**/*.ts` so the first browser-smoke files stay inside the explainability contract

## Frontend Tooling Status

- `apps/web/package.json` uses Bun as the active JavaScript package manager via `packageManager: bun@1.2.17`
- `apps/web/` owns its own Bun dependencies, lint tooling, and Playwright browser-smoke tooling because those concerns belong to the active web app boundary
- `.opencode/package.json` stays separate because it owns plugin-local tooling instead of the reviewer frontend runtime or test stack
- `legacy-v0/package.json` still uses npm scripts because that archive preserves the validated prototype exactly instead of inheriting active-tree tooling decisions
- Jasmine and Karma were Angular scaffold defaults for `ng test`, but they were removed from the active rebuild once that test target proved incomplete and unused
- Playwright now provides the first active frontend browser-smoke seam under `apps/web/e2e/` without broadening into a full CI gate yet
- if the team later chooses app-level frontend unit tests, it should pick that runner deliberately and document the replacement here instead of restoring dead scaffold files by accident
- the current TDD posture for the frontend is Red-Green-Refactor on app-local lint and smoke coverage first, then expand deeper tests only when new behavior justifies them

## Frontend Commands

- `cd apps/web && bun run lint` checks the owned frontend source, Playwright config, and browser-smoke files with Biome
- `cd apps/web && bun run e2e:install` installs the Chromium browser used by the current Playwright smoke slice
- `cd apps/web && bun run e2e` boots the Angular dev server and verifies the current shell redirect and planner navigation paths
- `cd apps/web && bun run build` remains the active build command
- `cd apps/web && bun run build:pages` remains the GitHub Pages artifact command

## Release Scaffolding

- `.github/workflows/cd.yml` is now a manual release-preparation workflow, not a deploy pipeline
- `tools/scripts/release.py` owns D4 release-readiness messaging and rejects deploy or publish claims until D5 lands

## Future CI Extensions

- keep release-readiness scaffolding separate from repo verification so rollout logic stays reviewable
