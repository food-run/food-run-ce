# Contributing to Food Run Community Edition (CE)

Thanks for contributing to Food Run Community Edition (CE).

Food Run CE is licensed under the GNU Affero General Public License, version 3 or any later version (AGPLv3-or-later). By contributing, you agree to follow this workflow and the Contributor License Agreement in `CLA.md`.

## 1) Before you start

Please:
- be respectful and collaborative
- keep changes focused and reviewable
- prefer smaller PRs over large bundles
- avoid unrelated cleanup in feature PRs
- do not include secrets, tokens, credentials, or personal data in commits

Before starting substantial work:
- check for an existing issue or discussion
- open an issue if the work changes behavior, architecture, repo boundaries, or public interfaces
- wait for maintainer guidance before investing in a large or speculative implementation

## 2) What kinds of contributions are welcome

Examples of welcome contributions:
- bug fixes
- tests
- documentation improvements
- scoped feature work that aligns with project priorities
- accessibility, UX, and reliability improvements
- performance improvements with clear reasoning
- refactors that reduce complexity without widening scope

Examples of changes that may need discussion first:
- major architecture changes
- new infrastructure dependencies
- broad file-tree reorganizations
- public API changes
- schema redesigns
- auth or data-boundary changes
- large dependency additions
- licensing, governance, or trademark policy changes

## 3) Development workflow

High-level flow:

1. Fork the repo.
2. Create a feature branch from `main`.
3. Make the smallest change that solves the problem well.
4. Add or update tests when appropriate.
5. Update docs if behavior, setup, or repo boundaries change.
6. Open a PR to `main`.
7. Address review feedback.
8. Wait for maintainer approval and merge.

## 4) Branch naming

Use one of these prefixes when possible:
- `feat/` for new feature work
- `fix/` for bug fixes
- `chore/` for tooling, maintenance, or non-user-facing cleanup
- `docs/` for documentation changes
- `test/` for test-only changes
- `refactor/` for scoped internal refactors

Examples:
- `feat/recipe-import-fallback`
- `fix/pantry-subtraction-rounding`
- `docs/license-boundary-clarification`

## 5) Commit messages

Use clear, descriptive commit messages in imperative mood.

Examples:
- `add recipe import retry fallback`
- `fix pantry subtraction rounding`
- `update trademark notice in readme`
- `add integration tests for shopping list aggregation`

## 6) Pull request requirements

Your PR should include:
- a clear summary of the change
- why the change is needed
- a linked issue if applicable
- local test or validation steps
- screenshots or recordings for meaningful UI changes, when relevant
- updated docs if behavior, setup, or policy changes
- tests for new logic, or a clear explanation for why tests are not feasible

Maintainers may ask that a PR be:
- reduced in scope
- split into smaller PRs
- rebased or cleaned up
- documented more clearly
- delayed until dependent roadmap work lands

## 7) Quality expectations

Please:
- follow the project’s style and naming conventions
- keep changes consistent with the documented repo layout
- avoid unnecessary nesting or file sprawl
- preserve maintainability and clarity
- keep interfaces explicit and reviewable
- avoid breaking changes without prior discussion

A technically clever change may still be declined if it increases long-term maintenance cost or conflicts with the current rebuild direction.

## 8) Security and dependency hygiene

Please do not:
- commit secrets, credentials, or production identifiers
- add third-party dependencies without clear justification
- open public issues containing exploit details for vulnerabilities
- introduce telemetry, tracking, or external calls without clear discussion and documentation

Report vulnerabilities privately using the method described in `GOVERNANCE.md` or `SECURITY.md`.

## 9) CLA requirement (mandatory)

All contributors must agree to the Contributor License Agreement in `CLA.md` before a PR can be merged.

By opening a contribution, you must confirm in the PR description:

`I agree to the CLA in CLA.md`

If CLA automation is enabled, your PR may be blocked until the required confirmation is present.

If the repository owner opens their own PR, the automation may skip that phrase check for the owner-authored PR. `CLA.md` remains the canonical source for that exception.

## 10) License note

By contributing to this repository, you agree that:
- your contribution may be distributed under the repository’s AGPLv3-or-later license as part of Food Run CE
- your contribution is also subject to the separate rights grant in `CLA.md`
- your contribution may be used by the Project Owner in CE and in separately licensed commercial, hosted, enterprise, or partner offerings, as described in `CLA.md`

## 11) Trademark note

Contributing code does **not** grant any right to use the Food Run name, logos, icons, or other brand assets beyond the permissions described in `TRADEMARKS.md`.

If you publish a fork, modified version, or hosted version, you must respect the trademark policy even if your use of the source code is permitted by the software license.

## 12) Maintainer discretion

Submitting a contribution does not create an obligation to review, merge, release, or support it.

Maintainers may close or decline a contribution for project, legal, quality, security, sustainability, or roadmap reasons.

---

Last updated: 2026-03-21
