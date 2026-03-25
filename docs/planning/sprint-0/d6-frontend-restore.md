# S0-D6 — 🌐 Reviewer-Visible Frontend Restore + Static Deploy Path

## TL;DR

S0-D6 restores a truthful, reviewer-visible frontend deployment path from the active rebuild tree so the repo once again presents a live surface that matches current work instead of pointing at deprecated legacy build output.

It closes Sprint 0 by reconnecting the seeded `apps/web` boundary to a real static deployment workflow, updating operator docs, and making the GitHub Pages path honest again for reviewers, demos, and repo credibility.

## Table of Contents

- [Why this deliverable exists](#why-this-deliverable-exists)
- [👤 Ownership](#-ownership)
- [🌿 Branch](#-branch)
- [🏷️ Deliverable PR title](#️-deliverable-pr-title)
- [🎯 Purpose](#-purpose)
- [⛓️ Depends on](#️-depends-on)
- [🚫 Blocks](#-blocks)
- [📁 Files touched](#-files-touched)
- [🏷️ Recommended names](#️-recommended-names)
- [🧾 Exact TL;DR sections per new or refactored file](#-exact-tldr-sections-per-new-or-refactored-file)
- [⚠️ Hotspot files](#️-hotspot-files)
- [🎟️ Task tickets](#️-task-tickets)
- [🧪 Verification tickets](#-verification-tickets)
- [✅ Deliverable verification](#-deliverable-verification)
- [🛑 Bad agent output patterns to watch for](#-bad-agent-output-patterns-to-watch-for)
- [🧠 Rationale in one sentence](#-rationale-in-one-sentence)

---

## Why this deliverable exists

Sprint 0 already establishes the active rebuild tree, the governed docs spine, the quality gates, and the first runtime parity layer.

What Sprint 0 still does **not** guarantee is that external reviewers can see a truthful frontend surface generated from the active rebuild path.

Right now, that creates three avoidable problems:

- the repo can look more complete than the actual reviewer-facing deployment path
- GitHub Pages can continue pointing at deprecated or inactive build assumptions
- future reviewers, mentors, or funders may judge the project through a broken or stale public surface instead of the current governed rebuild tree

S0-D6 fixes that by making the `apps/web` boundary the source of truth for the public static frontend path and wiring one honest deployment workflow around it.

---

## 👤 Ownership

**Owner:** 🎨 FE/Data  
**Reviewer:** 🛠️ Platform/QA  
**Required consult:** 🧩 BE/API, 👤🎯 Team Lead

---

## 🌿 Branch

` s0/d6-frontend-restore `

---

## 🏷️ Deliverable PR title

`deploy(web): restore reviewer-visible frontend path from active web app and publish one honest static GitHub Pages build`

---

## 🎯 Purpose

Restore a live reviewer-facing frontend from the active rebuild tree by:

- making `apps/web` the only public frontend source of truth
- adding one honest static deployment workflow for GitHub Pages
- removing stale or misleading references to deprecated deployment paths
- updating repo and operations docs so the public demo story matches current code reality
- optionally leaving a documented placeholder for a later static Render mirror without pretending it already exists

---

## ⛓️ Depends on

- S0-D1 — Repo Reset + Legacy Freeze
- S0-D2 — Active Tree + Shared Seams
- S0-D3 — Agent Steering + Docs Spine
- S0-D4 — CI/CD + 🧪 Quality Gates
- S0-D5 — Docker + ☸️ k3s + Observability Baseline

---

## 🚫 Blocks

- honest Sprint 0 reviewer demos
- a trustworthy GitHub Pages deployment path
- repo credibility for external reviewers and mentors
- later frontend implementation work that assumes the active web boundary can already build and publish
- optional later static mirror deployment on Render

---

## 📁 Files touched

### New workflow files

- `.github/workflows/web-pages.yml`

### Meaningfully refactored frontend files

- `apps/web/package.json`
- `apps/web/angular.json`
- `apps/web/src/`
- `apps/web/public/` or equivalent static asset home if needed
- `apps/web/README.md` if later needed as the permanent runtime-local guide

### Meaningfully refactored repo and operator docs

- `README.md`
- `docs/operations.md`
- `docs/architecture.md`
- `docs/adr.md`

### Optional config or helper files if required by the chosen static path

- `.github/workflows/cd.yml`
- `tools/scripts/release.py`
- `tools/scripts/verify.py`

Only update these optional files if the final deployment flow truly requires alignment there.

---

## 🏷️ Recommended names

### Deployment workflow names

- `web pages deploy`
- `reviewer frontend publish`

### Public deployment vocabulary

- `reviewer-visible frontend`
- `static frontend`
- `GitHub Pages deployment`
- `active web build`
- `public demo path`

### Build and publish environment names

- `production`
- `preview`
- `pages`

---

## 🧾 Exact TL;DR sections per new or refactored file

S0-D6 should apply exact TL;DR sections to:

- `.github/workflows/web-pages.yml`

S0-D6 should update existing TL;DR sections or add missing ones to:

- `apps/web/package.json`
- `apps/web/angular.json`
- `README.md`
- `docs/operations.md`
- `docs/architecture.md`
- `docs/adr.md`

If web source files are created or meaningfully refactored, keep their comments and top-of-file guidance aligned with the same Sprint 0 truth:

- the public frontend now comes from the active rebuild path
- GitHub Pages is a static reviewer surface, not proof of full production maturity
- the deployment is intentionally honest about current scope

---

## ⚠️ Hotspot files

These files define whether the public reviewer story stays truthful:

- `.github/workflows/web-pages.yml`
- `apps/web/package.json`
- `apps/web/angular.json`
- `README.md`
- `docs/operations.md`
- `docs/adr.md`

---

## 🎟️ Task tickets

### 🎟️ S0-D6-T1 — Make the active web boundary build into one honest static reviewer surface

**Commit title:** `feat(frontend): add the first reviewer-visible web shell so active rebuild work can publish from one honest path`

### 🎟️ S0-D6-T2 — Add a dedicated GitHub Pages deployment workflow for the active web build

**Commit title:** `deploy(web): add a GitHub Pages publish workflow for the active frontend static build path`

### 🎟️ S0-D6-T3 — Remove stale deployment assumptions from root and operator docs

**Commit title:** `docs(operations): align root guidance and operator docs with the active frontend deployment story`

### 🎟️ S0-D6-T4 — Record the deployment truth in the ADR and architecture docs

**Commit title:** `docs(adr): record active frontend deployment boundaries and reviewer-surface limitations for sprint zero closeout`

---

## 🧪 Verification tickets

### S0-D6-T1-V — Verify the active web boundary can build from a clean environment

**Commit title:** `test(web): verify the active frontend builds cleanly from the seeded rebuild boundary`

### S0-D6-T2-V — Verify the public Pages deployment matches the active web source of truth

**Commit title:** `test(deploy): verify GitHub Pages publishes the active frontend rather than deprecated legacy output`

### S0-D6-T3-V — Verify docs and public links tell the same deployment story

**Commit title:** `test(docs): verify repo guidance live demo links and operator docs describe one truthful frontend path`

---

## ✅ Deliverable verification

S0-D6 is done only when:

- `apps/web` is the only reviewer-visible frontend source of truth
- GitHub Pages can build and publish from the active frontend boundary
- the public demo link no longer depends on deprecated `docs/` build assumptions
- root guidance and operator docs describe the same deployment path
- the repo does not pretend the public static site is the full production system
- Sprint 0 closes with one honest public frontend surface that reviewers can see

---

## 🛑 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- republish the deprecated docs-based frontend path instead of the active web boundary
- build a fake frontend solely to make the URL green without matching current rebuild intent
- treat GitHub Pages as proof that the full platform is production-ready
- introduce a second competing public frontend path without explicit need
- mix legacy output and active output in the same deployment workflow
- add provider-specific Render deployment complexity before the GitHub Pages truth path works
- update README demo links without updating matching operations or ADR docs

---

## 🧠 Rationale in one sentence

S0-D6 is successful when reviewers can open one live frontend URL that truthfully reflects the active rebuild path rather than a stale or deprecated deployment artifact.
