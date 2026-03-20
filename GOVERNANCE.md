# Food Run Community Edition (CE) Governance

This document describes how Food Run Community Edition (CE) is maintained, how decisions are made, and how project authority is exercised.

Food Run CE is maintained as an open source Community Edition. Governance over roadmap direction, releases, trademarks, contribution review, and project quality remains with the Project Owner and any maintainers the Project Owner appoints.

## 1) Project scope

Food Run Community Edition (CE) is the public, open source codebase for the community edition of Food Run.

This governance document applies to:
- this repository
- related issue trackers and discussion spaces for this repository
- contribution review and release decisions for CE

This governance document does **not** grant any rights to:
- the Food Run name, logos, icons, or other brand assets
- any separately licensed commercial, enterprise, hosted, or partner offerings maintained by the Project Owner

See `TRADEMARKS.md`, `LICENSE`, and `CLA.md` for those boundaries.

## 2) Project roles

### 2.1 Project Owner

The Project Owner has ultimate authority over Food Run CE.

The Project Owner may:
- appoint or remove maintainers
- approve or reject roadmap direction
- decide release strategy and support boundaries
- approve exceptions to repo policies
- enforce trademark, CLA, contribution, and security policies
- offer separate commercial, hosted, enterprise, or partner arrangements outside CE

### 2.2 Maintainers

Maintainers are individuals authorized by the Project Owner to help operate the repository.

Maintainers have final authority over day-to-day repository operations, including:
- triaging issues and pull requests
- requesting changes to contributions
- merging or closing pull requests
- approving releases and release notes
- enforcing contribution standards
- protecting project stability, security, maintainability, and scope control

Maintainers act on behalf of the project, but the Project Owner retains final authority if there is disagreement or escalation.

### 2.3 Contributors

Contributors are anyone who submits issues, discussions, documentation, designs, code, tests, or other material to the repository.

Contributors may:
- report bugs
- propose features
- improve docs
- submit pull requests
- participate in discussions

Contributors do not automatically gain maintainer rights or roadmap authority by contributing.

## 3) Decision-making

### 3.1 Day-to-day decisions

Routine technical decisions are made through normal maintainer review in issues and pull requests.

Examples include:
- bug fixes
- documentation improvements
- non-breaking refactors
- tests and tooling improvements
- implementation details that do not alter public behavior or repo boundaries

### 3.2 Major changes

Major changes should be discussed in an issue, proposal, or planning document before implementation work begins.

Examples of major changes include:
- breaking API or schema changes
- large auth or data model redesigns
- major architecture changes
- adding or removing core infrastructure
- changing public extension boundaries
- changing licensing, contribution, or trademark policy
- introducing large dependencies with long-term maintenance cost

Maintainers may ask that major changes be:
- narrowed in scope
- split into phases
- documented more clearly before review
- deferred until they align with roadmap priorities

### 3.3 Final authority

The project is not governed by a voting or consensus-only model.

Maintainers will usually seek alignment where practical, but if consensus is not reached, the Project Owner or maintainers decide based on:
- user impact
- correctness
- security
- maintainability
- sustainability
- roadmap alignment
- legal and brand protection constraints

## 4) Pull request and merge authority

A pull request may be merged when maintainers determine that it is ready.

Readiness may include:
- required checks passing
- tests or other validation being adequate for the change
- documentation being updated where behavior changes
- repo-boundary rules being followed
- CLA requirements being satisfied
- the change aligning with current roadmap and architectural direction

Maintainers may reject or close a pull request if it:
- creates undue maintenance burden
- conflicts with current architecture or repo boundaries
- introduces legal, security, or privacy concerns
- is too large to review responsibly
- conflicts with project direction or sustainability goals
- attempts to bypass trademark, CLA, or license boundaries

Acceptance of a contribution is always discretionary.

## 5) Releases

Releases are created by maintainers or the Project Owner.

Maintainers may decide:
- when a release is cut
- what changes are included
- whether a change is deferred
- whether a release is major, minor, patch, preview, or otherwise specially marked

Release notes should summarize:
- user-facing changes
- breaking changes, if any
- migration or upgrade notes, if relevant
- major documentation or policy changes, if relevant

The project may use semantic versioning or another documented versioning approach.

## 6) Roadmap and scope control

Maintainers and the Project Owner maintain the public roadmap in the repository or associated planning documents.

Roadmap priorities may be adjusted at any time to protect:
- product coherence
- security
- quality
- maintainability
- resource constraints
- commercial sustainability
- legal and brand boundaries

Public discussion of a feature does not guarantee acceptance, scheduling, or implementation.

## 7) Licensing and commercial boundary

Food Run CE is maintained under the license stated in `LICENSE`.

Contributions to CE are reviewed under the contribution rules in `CONTRIBUTING.md` and the Contributor License Agreement in `CLA.md`.

The Project Owner may maintain:
- CE under an open source license
- separate proprietary or differently licensed offerings
- hosted or managed services
- premium integrations, support, or operational services

Nothing in this governance document limits the Project Owner from maintaining separate commercial or enterprise offerings, provided the applicable licenses and agreements are respected.

## 8) Security

Do **not** report security vulnerabilities in public issues, discussions, or pull requests.

Security reports should be sent privately to the maintainers using the dedicated security contact listed in:
- the repository security policy
- the repository profile or contact section
- another private contact method explicitly published by the Project Owner

A useful report should include, where possible:
- a clear description of the issue
- affected components or paths
- impact
- reproduction steps
- proof-of-concept details if safe to share
- any proposed mitigation

Maintainers may:
- acknowledge receipt
- request clarification
- coordinate a fix window
- delay public disclosure until a fix is available
- decline to publish additional exploit detail if doing so would materially increase risk

## 9) Code of conduct

If a `CODE_OF_CONDUCT.md` file exists, it applies to all project spaces governed by this repository.

If no code of conduct file exists yet, maintainers still reserve the right to moderate project spaces and remove abusive, harassing, malicious, deceptive, or disruptive participation.

## 10) Trademark and branding boundary

The Food Run name, logos, icons, and related source-identifying brand assets are not governed by this document alone and are not granted by the open source software license.

Use of those marks is governed separately by `TRADEMARKS.md`.

Forks, modified versions, and hosted services must respect the trademark policy even when use of the underlying code is permitted by the software license.

## 11) Policy changes

The Project Owner may update this document as the project evolves.

Policy changes take effect when merged into the default branch unless otherwise stated.

## 12) Contact

Project contact methods may be published in:
- the repository profile
- `SECURITY.md`
- the repository security page
- the project website or official org profile

If no dedicated public address has been published yet, do not disclose security issues publicly while waiting for one.

---

Last updated: 2026-03-20