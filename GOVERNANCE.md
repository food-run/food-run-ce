# Food Run Community Edition (CE) Governance

This document describes how Food Run CE is maintained and how decisions are made.

## 1) Project roles

### 1.1 Project Owner / Maintainers

The Project Owner appoints maintainers. Maintainers have final authority over:

- merging pull requests
- releases and versioning
- roadmap prioritization
- security response process
- enforcement of contribution, CLA, and trademark policies

### 1.2 Contributors

Contributors are anyone who submits issues, discussions, documentation, or code through pull requests.

## 2) Decision-making

- day-to-day technical decisions are made by maintainers through PR review
- major changes require an issue or proposal before implementation
- if consensus is not reached, maintainers decide based on project goals and constraints

Examples of "major changes":

- breaking API changes
- database schema redesigns that require migrations affecting core flows
- switching core infrastructure or auth strategy
- adding or removing key dependencies

## 3) Pull request merging rules

A PR may be merged when:

- required checks pass (CI)
- the change matches the roadmap and constraints
- the PR includes the required CLA confirmation
- maintainers approve the PR

Maintainers may request:

- changes to reduce scope
- additional tests
- documentation updates
- splitting a PR into smaller PRs

## 4) Releases

- releases are created by maintainers
- release notes should summarize user-facing changes and migration needs
- maintainers may use semantic versioning or another versioning scheme, documented in release notes

## 5) Roadmap

- maintainers maintain the public roadmap in issues or a roadmap document
- roadmap items are prioritized by:
  - user impact
  - correctness and security
  - maintainability and cost controls
  - alignment with the project vision

Roadmap changes may be made at any time to protect project quality and sustainability.

## 6) Security

Do not report vulnerabilities in public issues.

To report a security issue:

- contact maintainers privately using the method published in the repository "Security" section (or the email listed in the repo description once added)
- include a clear description, impact, and reproduction steps if possible

Maintainers will:

- acknowledge receipt
- assess impact
- coordinate a fix and disclosure plan

## 7) Code of conduct

If a code of conduct file exists, it applies to all project spaces.

## 8) Contact

Maintainer contact method will be published in the repository once the project owner sets a dedicated address.

---

Last updated: 2026-02-08
