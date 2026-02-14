# Contributing to Food Run (Community Edition)

Thanks for contributing to Food Run Community Edition (CE). This repo is licensed under GPLv3. By contributing, you agree to follow the workflow below and sign the CLA.

## Quick rules

- be respectful and collaborative
- keep changes focused and reviewable
- prefer small PRs over large bundles
- do not include secrets, keys, or personal data in commits

## Where to start

- check existing issues first
- if you want to propose a feature, open an issue describing:
  - the user problem
  - proposed behavior
  - acceptance criteria
  - any expected API or schema changes

## Development workflow (high level)

1) fork the repo
2) create a feature branch from `main`
3) make changes with tests
4) open a PR to `main`
5) address review feedback
6) merge after checks pass and approvals are complete

## Branch naming

Use one of these prefixes:

- `feat/` new feature
- `fix/` bug fix
- `chore/` tooling, refactors, maintenance
- `docs/` documentation updates
- `test/` test-only changes

Example:

- `feat/recipe-import-fallback`
- `fix/pantry-subtraction-rounding`

## Commit messages

Use clear, descriptive commits. Prefer imperative mood.
Examples:

- `add import draft approval endpoint`
- `fix household scope enforcement for pantry items`
- `add playwright smoke test for login`

## Pull request requirements

Your PR must include:

- a clear summary of the change
- why the change is needed (issue link if applicable)
- how to test it locally
- updated docs if behavior changes
- tests that cover new logic (or an explanation for why tests are not feasible)

### PR size guideline

If a PR is very large, maintainers may request it be split into smaller PRs.

## CLA requirement (mandatory)

All contributors must sign the Contributor License Agreement (CLA) before a PR can be merged.

- the CLA text is in `CLA.md`
- the PR will be blocked until the CLA requirement is satisfied

## Code quality expectations

- follow the project style and naming rules
- keep file structure minimal (no nesting deeper than 3 levels from repo root without maintainer approval)
- keep REST endpoints resource-oriented and consistent
- avoid breaking changes to the public API without discussion

## Security and privacy

- do not commit secrets, tokens, or credentials
- avoid adding new third-party dependencies without justification
- report security issues privately (see SECURITY section below)

## Reporting security issues

Please do not open public issues for security vulnerabilities.
Instead, contact the maintainers using the method described in `GOVERNANCE.md`.

## License note

By contributing, you agree that your contributions are licensed under the same license as this repo (GPLv3), and you also agree to the CLA terms in `CLA.md`.
