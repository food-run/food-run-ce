# 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams

## TL;DR

S0-D2 seeds the first permanent active tree for the rebuild. It creates one stable home for each deployable unit and one stable home for each shared seam so later work extends real boundaries instead of inventing parallel structures.

## Index

- [Why this deliverable exists](#why-this-deliverable-exists)
- [👥 Ownership](#ownership)
- [🌿 Branch](#branch)
- [🏷️ Deliverable PR title](#deliverable-pr-title)
- [🎯 Purpose](#purpose)
- [⛓️ Depends on](#depends-on)
- [🚧 Blocks](#blocks)
- [📂 Files touched](#files-touched)
- [🧠 Recommended names](#recommended-names)
- [🧾 Exact TL;DR sections per new or refactored file](#exact-tldr-sections-per-new-or-refactored-file)
- [⚠️ Hotspot files](#hotspot-files)
- [🎟️ Task tickets](#task-tickets)
- [👾 Verification tickets](#verification-tickets)
- [✅ Deliverable verification](#deliverable-verification)
- [🚨 Bad agent output patterns to watch for](#bad-agent-output-patterns-to-watch-for)
- [🧩 Rationale in one sentence](#rationale-in-one-sentence)

---

<a id="why-this-deliverable-exists"></a>
## Why this deliverable exists

If the team jumps straight from archive cleanup into feature work, three bad things happen immediately:

- new work gets dropped into random folders because the active homes do not exist yet
- the same concepts get reintroduced in multiple places because shared seams were never defined
- agent lanes start competing over path ownership because the repo shape is still implicit

D2 must establish the structural spine for all later work:

- deployable-unit homes
- shared seam homes
- starter files with permanent names
- section maps and TL;DR blocks that later sprints can extend instead of replacing

---

<a id="ownership"></a>
## 👥 Ownership

**Owner:** 👤🧰 BE/API  
**Reviewer:** 👤🎯 Team Lead  
**Required consult:** 👤🎨 FE/Data, 👤👻 AI/Cloud, 👤🛡️ Platform/QA

---

<a id="branch"></a>
## 🌿 Branch

` s0/d2-active-tree `

---

<a id="deliverable-pr-title"></a>
## 🏷️ Deliverable PR title

`chore(structure): seed the active rebuild tree and shared boundary files so later work lands in one stable surface`

---

<a id="purpose"></a>
## 🎯 Purpose

Create the permanent starter structure for the active rebuild so that:

- every deployable unit has a defined home
- every cross-cutting concept has one shared home
- later sprints extend existing files instead of inventing parallel ones
- humans and agents can reason about ownership before logic exists

---

<a id="depends-on"></a>
## ⛓️ Depends on

- 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze

---

<a id="blocks"></a>
## 🚧 Blocks

- 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine
- 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates
- 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline
- all later feature sprints, because they need stable app homes and shared seams before implementation

---

<a id="files-touched"></a>
## 📂 Files touched

### New top-level active paths created

- `apps/`
- `shared/`

### New deployable-unit starter files

- `apps/web/angular.json`
- `apps/web/package.json`
- `apps/web/tsconfig.json`
- `apps/web/src/main.ts`
- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/middleware.py`
- `apps/api/schemas.py`
- `apps/domain/manage.py`
- `apps/domain/config.py`
- `apps/domain/models.py`
- `apps/domain/services.py`
- `apps/domain/auth.py`
- `apps/worker/main.py`
- `apps/worker/jobs.py`
- `apps/worker/queue.py`
- `apps/worker/retry.py`
- `apps/agent/main.py`
- `apps/agent/graph.py`
- `apps/agent/evals.py`
- `apps/agent/store.py`

### New shared seam starter files

- `shared/contract/http.py`
- `shared/contract/errors.py`
- `shared/contract/version.py`
- `shared/schema/common.py`
- `shared/schema/events.py`
- `shared/schema/auth.py`
- `shared/adapter/ports.py`
- `shared/adapter/factory.py`
- `shared/adapter/cache.py`
- `shared/adapter/queue.py`
- `shared/adapter/store.py`
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `shared/testkit/helpers.py`

### Meaningfully refactored file

- `README.md`

---

<a id="recommended-names"></a>
## 🧠 Recommended names

### Directory names

- `apps`
- `shared`
- `contract`
- `schema`
- `adapter`
- `testkit`

### App names

- `web`
- `api`
- `domain`
- `worker`
- `agent`

### File naming rules

- use 1–2 words where possible
- use ≤4 words max
- prefer concept-first names over framework-heavy names
- use one permanent starter file per concept instead of placeholder scraps

### Preferred concept mapping

#### In `apps/`

- `web` = user-facing SPA
- `api` = public contract boundary
- `domain` = business truth boundary
- `worker` = async execution boundary
- `agent` = governed agent workflow boundary

#### In `shared/`

- `contract` = HTTP/public contract primitives
- `schema` = reusable shape definitions
- `adapter` = swappable dependency seams
- `testkit` = fixtures, helpers, and deterministic support

---

<a id="exact-tldr-sections-per-new-or-refactored-file"></a>
## 🧾 Exact TL;DR sections per new or refactored file

D2 seeds permanent growth surfaces. Each starter file should receive:

- the exact TL;DR block defined in the Sprint 0 packet
- stable semantic section headers
- no business logic that belongs to later deliverables
- no vendor-specific assumptions in shared seams

Key file groups:

- `apps/web/src/main.ts` — bootstrap only
- `apps/api/*.py` — contract-facing runtime surface
- `apps/domain/*.py` — domain authority surface
- `apps/worker/*.py` — async execution surface
- `apps/agent/*.py` — governed agent runtime surface
- `shared/contract/*` — transport vocabulary
- `shared/schema/*` — reusable shape vocabulary
- `shared/adapter/*` — capability-based ports and factories
- `shared/testkit/*` — deterministic shared test support

Also update the root `README.md` to add:

- `## Active Rebuild Path`
- `## Repo Layout Direction`
- `## Next Structural Layers`

and this exact addition:

```md
The active rebuild tree is now seeded under `apps/` and `shared/`. Later Sprint 0 deliverables will add agent controls, platform parity, CI/CD gates, and deeper documentation on top of these permanent homes.
```

---

<a id="hotspot-files"></a>
## ⚠️ Hotspot files

These files will disproportionately shape later path ownership and drift resistance:

- `README.md`
- `apps/api/main.py`
- `apps/domain/services.py`
- `shared/adapter/ports.py`
- `shared/schema/events.py`

---

<a id="task-tickets"></a>
## 🎟️ Task tickets

### 🎟️ S0-D2-T1 — 🗺️ Define the active tree ownership map before creating files

**Commit title:**  
`chore(structure): define deployable-unit and shared-seam ownership before seeding the active rebuild tree`

#### Purpose

Decide what each active directory owns before any starter files are created, so the structure encodes architecture instead of merely looking organized.

#### Checklist

- define deployable-unit boundaries
- define shared seam boundaries
- review for ownership clarity and future duplication risk

### 🎟️ S0-D2-T2 — 🧱 Seed the deployable-unit starter files

**Commit title:**  
`chore(apps): seed permanent starter files for web, api, domain, worker, and agent runtimes`

#### Purpose

Create the first permanent files inside each deployable unit so later work extends the same files rather than fragmenting the runtime surfaces.

#### Checklist

- seed `apps/web`
- seed `apps/api`
- seed `apps/domain`
- seed `apps/worker` and `apps/agent`
- keep each runtime role intentionally narrow

### 🎟️ S0-D2-T3 — 🔌 Seed the shared seam files

**Commit title:**  
`chore(shared): create stable homes for contracts schemas adapters and deterministic test support`

#### Purpose

Create the shared boundary files now so later work reuses one seam vocabulary instead of inventing overlapping helper and utility surfaces.

#### Checklist

- seed `shared/contract` and `shared/schema`
- seed `shared/adapter`
- seed `shared/testkit`
- keep shared seams capability-based and low-drift

### 🎟️ S0-D2-T4 — 🧾 Write file narratives and section maps into every starter file

**Commit title:**  
`docs(structure): add tl dr blocks and section maps so starter files grow predictably instead of fragmenting`

#### Purpose

Make each starter file immediately useful as a future growth surface by giving it a stable story, stable section headers, and clear ownership boundaries.

#### Checklist

- insert the exact TL;DR blocks
- insert stable section maps
- refactor the root README without overstating repo maturity

---

<a id="verification-tickets"></a>
## 👾 Verification tickets

### 👾 S0-D2-T1-V — 🧠 Verify the active tree is ownership-complete

**Commit title:**  
`test(structure): verify every major rebuild concern has one clear home in the active tree`

#### Verification pass condition

A reviewer can name a future concern from each plane and point to one obvious first home without hesitation.

### 👾 S0-D2-T2-V — 📚 Verify starter files are growable, not disposable

**Commit title:**  
`docs(apps): verify starter files have durable narratives and section headers that future work can extend safely`

#### Verification pass condition

A contributor starting Sprint 1 could extend the seeded files directly without first refactoring the structure that D2 created.

---

<a id="deliverable-verification"></a>
## ✅ Deliverable verification

S0-D2 is done only when:

- `apps/` and `shared/` exist with permanent starter files
- each starter file has a durable purpose and section map
- `web`, `api`, `domain`, `worker`, and `agent` have distinct responsibilities
- `contract`, `schema`, `adapter`, and `testkit` have distinct responsibilities
- the README accurately names `apps/` and `shared/` as active rebuild paths without overclaiming maturity

---

<a id="bad-agent-output-patterns-to-watch-for"></a>
## 🚨 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- create generic roots like `utils/`, `types/`, `interfaces/`, or `core/`
- put shared seam code inside `apps/api` or `apps/domain` before `shared/` is considered
- seed vendor-named adapter files instead of capability-named files
- create multiple startup files for the same deployable unit
- use vague section headers like `misc`, `helpers`, or `other`
- treat starter files as temporary throwaways

---

<a id="rationale-in-one-sentence"></a>
## 🧩 Rationale in one sentence

S0-D2 is successful when the rebuild has one real active tree with one obvious home for every major concern, so later work extends boundaries instead of inventing them.
