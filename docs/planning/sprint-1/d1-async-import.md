# 🌟 S1-D1 — 🍽️ Async Import Pipeline + 6 Domains + 🌐 Fallback + ✅ Review / Edit / Approval Loop

**Subtitle:** Establish the first real product-truth ingress path for the live MVP by turning recipe import into a durable, asynchronous, parser-backed, reviewable workflow that produces approved recipe truth for downstream planning, shopping, and recommendation flows.

## 1. 🧭 TL;DR

This deliverable is the first real product-runtime activation point in **📅 Sprint 1**.

At the end of **📅 Sprint 0**, the repo already has:

- a governed **🐝 agentic harness**
- a strong **📚 docs / 🧾 ADR / coordination** baseline
- real **🐙 repo verification / protected-path / frontend quality** controls
- a live **🖼️ frontend shell**
- seeded **🐍 API / 🧩 domain / 📦 worker / 🤖 agent** seams

What it does **not** yet have is durable recipe truth entering the active runtime.

This deliverable creates that truth path and fixes the first major product-runtime gap.

It defines and implements:

- the durable import state model
- the async import execution model
- the parser contract and normalization target
- the six guaranteed domain parsers
- the **🌐** fallback path
- the review / edit / approval loop
- durable approved recipe handoff semantics
- parser regression fixtures
- error classification and operator-visible failure states
- test-first implementation expectations for every code-bearing change

This deliverable is complete only when:

- a recipe URL can be submitted to the live runtime
- the import executes asynchronously
- one of the guaranteed domain parsers or the fallback path handles the source
- the result reaches a durable reviewable state
- low-confidence imports can be edited and approved
- approval produces stable recipe truth
- that recipe truth is ready for downstream **✏️ planning**, **🧃 shopping**, and **🤖 recommendations**
- all new behavior is covered by tests
- verification tooling makes regressions obvious instead of surprising

## 2. 📚 Table of Contents

- [1. 🧭 TL;DR](#1--tldr)
- [2. 📚 Table of Contents](#2--table-of-contents)
- [3. 📌 Deliverable Intent](#3--deliverable-intent)
  - [3.1. 🎯 Why this deliverable exists](#31--why-this-deliverable-exists)
  - [3.2. 🎯 Purpose](#32--purpose)
  - [3.3. 🧩 Deliverable success definition](#33--deliverable-success-definition)
  - [3.4. 🧠 Architectural role inside Sprint 1](#34--architectural-role-inside-sprint-1)
- [4. 👥 Ownership and Delivery Controls](#4--ownership-and-delivery-controls)
  - [4.1. 👥 Ownership](#41--ownership)
  - [4.2. 🌿 Branch](#42--branch)
  - [4.3. 🏷️ Deliverable PR title](#43-️-deliverable-pr-title)
  - [4.4. ⛓️ Depends on](#44-️-depends-on)
  - [4.5. 🚧 Blocks](#45--blocks)
  - [4.6. ⏱️ Time estimate](#46-️-time-estimate)
  - [4.7. 🧪 TDD rule for this deliverable](#47--tdd-rule-for-this-deliverable)
- [5. 🗂️ Scope and File Surfaces](#5-️-scope-and-file-surfaces)
  - [5.1. 📂 Files touched](#51--files-touched)
  - [5.2. 🧠 Fixed implementation decisions](#52--fixed-implementation-decisions)
  - [5.3. ⚠️ Hotspot files](#53-️-hotspot-files)
  - [5.4. 🧪 Required test surfaces](#54--required-test-surfaces)
- [6. 🌲 Safe Parallelism Plan](#6--safe-parallelism-plan)
  - [6.1. 🔗 Serial truth that must stabilize first](#61--serial-truth-that-must-stabilize-first)
  - [6.2. 🔀 Safe parallel workstreams](#62--safe-parallel-workstreams)
  - [6.3. 🐝 Dedicated boilerplate / test-setup lane](#63--dedicated-boilerplate--test-setup-lane)
  - [6.4. 🚫 Parallelism that is not safe](#64--parallelism-that-is-not-safe)
- [7. 🧾 Exact TL;DR Sections Per New or Refactored File](#7--exact-tldr-sections-per-new-or-refactored-file)
- [8. 🎟️ Task Tickets](#8-️-task-tickets)
  - [8.1. 🎟️ S1-D1-T0 — 🧪 Test harness and boilerplate setup for import work](#81-️-s1-d1-t0--test-harness-and-boilerplate-setup-for-import-work)
  - [8.2. 🎟️ S1-D1-T1 — 🧩 Durable import truth model + shared schemas](#82-️-s1-d1-t1--durable-import-truth-model--shared-schemas)
  - [8.3. 🎟️ S1-D1-T2 — 🐍 Import API activation + request flow](#83-️-s1-d1-t2--import-api-activation--request-flow)
  - [8.4. 🎟️ S1-D1-T3 — 📦 Worker runtime activation + queue + retry + status transitions](#84-️-s1-d1-t3--worker-runtime-activation--queue--retry--status-transitions)
  - [8.5. 🎟️ S1-D1-T4 — 🍽️ Guaranteed-domain parsers + 🌐 fallback implementation](#85-️-s1-d1-t4--guaranteed-domain-parsers---fallback-implementation)
  - [8.6. 🎟️ S1-D1-T5 — ✅ Review / edit / approval loop and approved recipe handoff](#86-️-s1-d1-t5--review--edit--approval-loop-and-approved-recipe-handoff)
  - [8.7. 🎟️ S1-D1-T6 — 🧪 Regression fixtures + 🔍 failure classification + import-check tooling](#87-️-s1-d1-t6--regression-fixtures---failure-classification--import-check-tooling)
- [9. 👾 Verification Tickets](#9--verification-tickets)
  - [9.1. 👾 S1-D1-T0-V — verify test harness and boilerplate setup](#91--s1-d1-t0-v--verify-test-harness-and-boilerplate-setup)
  - [9.2. 👾 S1-D1-T1-V — verify durable import truth model + shared schemas](#92--s1-d1-t1-v--verify-durable-import-truth-model--shared-schemas)
  - [9.3. 👾 S1-D1-T2-V — verify import API activation + request flow](#93--s1-d1-t2-v--verify-import-api-activation--request-flow)
  - [9.4. 👾 S1-D1-T3-V — verify worker runtime activation + queue + retry + status transitions](#94--s1-d1-t3-v--verify-worker-runtime-activation--queue--retry--status-transitions)
  - [9.5. 👾 S1-D1-T4-V — verify guaranteed-domain parsers + 🌐 fallback](#95--s1-d1-t4-v--verify-guaranteed-domain-parsers---fallback)
  - [9.6. 👾 S1-D1-T5-V — verify review / edit / approval loop and approved recipe handoff](#96--s1-d1-t5-v--verify-review--edit--approval-loop-and-approved-recipe-handoff)
  - [9.7. 👾 S1-D1-T6-V — verify regression fixtures + failure classification + import-check tooling](#97--s1-d1-t6-v--verify-regression-fixtures--failure-classification--import-check-tooling)
- [10. ✅ Deliverable Verification](#10--deliverable-verification)
  - [10.1. 👾 S1-D1-V — full deliverable verification](#101--s1-d1-v--full-deliverable-verification)
- [11. 🚨 Bad Agent Output Patterns To Watch For](#11--bad-agent-output-patterns-to-watch-for)
- [12. 🧩 Rationale in One Sentence](#12--rationale-in-one-sentence)

## 3. 📌 Deliverable Intent

### 3.1. 🎯 Why this deliverable exists

The live MVP cannot produce:

- **✏️ diet-aware plans**
- **🧃 pantry-aware lists**
- **🤖 recipe recommendations**
- **🏠 shared recipe usage**

until the active runtime has trustworthy recipe truth.

Right now, that truth does not exist in the active runtime.

This deliverable exists to create one stable ingest truth path that later Sprint 1 work can consume without redefining what a recipe import means.

#### 3.1.1. Who this deliverable serves

This deliverable serves:

- **users**
  - because they need recipe imports to become usable product objects
- **frontend developers**
  - because they need one stable import/status/review contract
- **backend developers**
  - because they need one domain-owned state machine
- **AI/runtime developers**
  - because import assist and later recommendations need durable recipe truth
- **operators/reviewers**
  - because they need failures to be classifiable and reproducible

#### 3.1.2. What problem it solves

Without this deliverable, the system has:

- no durable async ingest path
- no parser-backed MVP runtime
- no reviewable draft truth
- no approved recipe handoff model
- no supportable parser regression harness

That means every later MVP capability would either:
- be fake
- rely on hardcoded placeholder data
- or invent its own incompatible recipe vocabulary

### 3.2. 🎯 Purpose

Create a durable, async, reviewable import pipeline that converts recipe URLs into approved recipe truth.

### 3.3. 🧩 Deliverable success definition

This deliverable is successful when:

- import submission is live
- import execution is async
- parser coverage exists for all 6 required domains
- fallback exists and is honest about confidence
- low-confidence outputs are reviewable/editable
- approval produces durable recipe truth
- parser regressions are testable
- failures are classifiable and triageable
- every new implementation path is covered by tests
- verification tooling can be run by another engineer without asking follow-up questions

### 3.4. 🧠 Architectural role inside Sprint 1

This deliverable establishes the first durable product-truth boundary in the active runtime.

That means it has to do more than “make parsing work.” It must also lock:

- the import state machine
- the approval prerequisites
- the approved recipe handoff shape
- the parser ordering rules
- the failure-class vocabulary
- the distinction between:
  - domain-owned truth
  - worker-owned async progression
  - API-owned transport
  - parser-owned extraction
  - test-owned reproducibility

If this deliverable is vague, later Sprint 1 work becomes ambiguous.  
If it is precise, later Sprint 1 work becomes implementation-focused.

## 4. 👥 Ownership and Delivery Controls

### 4.1. 👥 Ownership

- **Owner:** 👤🧰 BE/API
- **Primary Reviewer:** 👤🎯 Team Lead
- **Support / Pairing:** 👤🛡️ Platform/QA
- **Required Consult:** 👤👻 AI/Cloud, 👤🎨 FE/Data

#### 4.1.1. Who owns what inside this deliverable

- **👤🧰 BE/API**
  - owns the durable import truth model
  - owns the route/domain separation
  - owns approval semantics
- **👤🛡️ Platform/QA**
  - owns the worker/runtime reliability posture
  - owns repeatable verification support
  - owns the test and smoke discipline around async behavior
- **👤👻 AI/Cloud**
  - supports parser/fallback quality strategy and later import-assist integration points
- **👤🎨 FE/Data**
  - reviews contract usability for later UI wiring
- **👤🎯 Team Lead**
  - reviews architectural coherence and guards against schema/state churn

### 4.2. 🌿 Branch

` s1/d1-async-import `

### 4.3. 🏷️ Deliverable PR title

`feat(import): activate async recipe ingestion with durable review states guaranteed parsers and approved recipe handoff`

### 4.4. ⛓️ Depends on

- **✅ 📅 Sprint 0 baseline**
- specifically:
  - **📚 docs / 🧾 ADR / planning**
  - **🐙 repo verification**
  - **🖼️ deployed frontend shell**
  - seeded **🐍 / 🧩 / 📦 / 🤖** seams
  - **🔍** request-id / health / release-marker vocabulary

### 4.5. 🚧 Blocks

- **🌟 S1-D2** because the frontend and import-assist AI need real import states
- **🌟 S1-D4** because plans and lists need approved recipe truth
- any meaningful MVP recommendation path
- MVP smoke coverage for the full user loop

### 4.6. ⏱️ Time estimate

- Total: **22–30 implementation person-hours**
- **🎟️ S1-D1-T0 — 🧪 Test harness and boilerplate setup for import work:** **2–3h**
- **🎟️ S1-D1-T1 — 🧩 Durable import truth model + shared schemas:** **4–5h**
- **🎟️ S1-D1-T2 — 🐍 Import API activation + request flow:** **3–4h**
- **🎟️ S1-D1-T3 — 📦 Worker runtime activation + queue + retry + status transitions:** **4–5h**
- **🎟️ S1-D1-T4 — 🍽️ Guaranteed-domain parsers + 🌐 fallback:** **5–7h**
- **🎟️ S1-D1-T5 — ✅ Review / edit / approval loop and approved recipe handoff:** **2–3h**
- **🎟️ S1-D1-T6 — 🧪 Regression fixtures + 🔍 failure classification + import-check tooling:** **3–4h**
- **✅ Deliverable verification + reviewer pass:** **2h**

### 4.7. 🧪 TDD rule for this deliverable

This deliverable is explicitly **TDD-first**.

#### 4.7.1. Core rule

No implementation ticket is considered complete until:

- a failing or incomplete test surface existed first
- the code was written to satisfy that test surface
- the tests were expanded to cover the final intended behavior
- docs were updated to match the actual implemented behavior

#### 4.7.2. Dedicated boilerplate/test-setup agent rule

A dedicated **🐝 boilerplate / initial-test-setup** lane must exist for this deliverable.

Its job is to reduce setup drag by handling:

- test file scaffolding
- fixture skeletons
- test helper boilerplate
- baseline test-case structure
- non-controversial repetitive setup

It must **not** decide:
- import truth semantics
- approval semantics
- parser ordering
- retry classes
- durable status meanings

Those decisions are fixed here in the packet.

#### 4.7.3. Test expansion rule

As code expands, tests must expand with it.

That means:

- adding a parser without a deterministic fixture is incomplete
- adding a status or transition without a verification path is incomplete
- adding approval behavior without approved-recipe assertions is incomplete
- adding fallback behavior without confidence/review assertions is incomplete

## 5. 🗂️ Scope and File Surfaces

### 5.1. 📂 Files touched

#### 5.1.1. ⚠️ Hotspot

- `apps/domain/models.py`
- `apps/domain/services.py`
- `apps/domain/imports.py`
- `shared/schema/imports.py`
- `apps/worker/jobs.py`
- `apps/worker/retry.py`

#### 5.1.2. New or meaningfully refactored

- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/schemas.py`
- `apps/api/imports.py`
- `apps/api/health.py`
- `apps/domain/models.py`
- `apps/domain/services.py`
- `apps/domain/imports.py`
- `apps/worker/main.py`
- `apps/worker/jobs.py`
- `apps/worker/queue.py`
- `apps/worker/retry.py`
- `apps/worker/imports.py`
- `apps/worker/normalize.py`
- `apps/worker/status.py`
- `shared/schema/common.py`
- `shared/schema/events.py`
- `shared/schema/imports.py`
- `shared/adapter/queue.py`
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `shared/testkit/workflows.py`
- `tools/scripts/import_check.py`
- `docs/imports.md`
- `docs/adr.md`
- `docs/testing.md`
- `docs/operations.md`

#### 5.1.3. New or meaningfully refactored tests

- `shared/testkit/workflows.py`
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- any runtime-specific test files created under the repo’s active backend/frontend test conventions
- import verification script output expectations in `tools/scripts/import_check.py`

### 5.2. 🧠 Fixed implementation decisions

These choices are fixed by the packet and should not be re-decided during implementation.

#### 5.2.1. Import state model

Durable states are exactly:

- `queued`
- `fetching`
- `parsing`
- `normalizing`
- `review_required`
- `approved`
- `failed`

No additional durable states should be introduced in D1.

#### 5.2.2. Confidence model

Confidence is a normalized three-level enum:

- `high`
- `medium`
- `low`

Mapping rule:
- guaranteed-domain parser with all required fields and no major warnings → `high`
- guaranteed-domain parser with missing optional fields or normalization warnings → `medium`
- fallback result or materially incomplete parse → `low`

#### 5.2.3. Review-required rule

`review_required = true` exactly when any of the following are true:

- confidence is `low`
- one or more required approval fields are missing
- fallback path was used and warnings were emitted
- normalization emitted warnings on required recipe structures

#### 5.2.4. Required recipe fields for approval

The following fields must exist before approval can produce approved recipe truth:

- `source_url`
- `source_domain`
- `title`
- `ingredients_raw`
- `instructions_raw`

Optional at approval time:

- `description`
- `image_url`
- `prep_time_minutes`
- `cook_time_minutes`
- `servings`

#### 5.2.5. Approved recipe handoff behavior

Approval always produces:

- durable approved recipe record
- retained source attribution
- retained pointer back to the import record
- normalized ingredient and instruction arrays
- raw source text preserved for auditability

Approval never:

- deletes the import record
- strips attribution
- silently overwrites source metadata
- auto-canonicalizes ingredients beyond D1 normalization intent

#### 5.2.6. Parser order

Parser selection order is fixed:

1. exact guaranteed-domain parser by normalized host match
2. structured fallback extraction
3. heuristic fallback extraction
4. failure classification if neither yields minimally usable output

#### 5.2.7. Queue model

For D1, the worker queue model is fixed as:

- one enqueue call from the API
- one root import job
- stage transitions managed by the worker path
- bounded retry behavior only for fetch/network classes
- parser/content-shape failures are **not** retryable by default

#### 5.2.8. Failure classes

Failure classes are fixed as:

- `fetch_error`
- `parse_error`
- `normalize_error`
- `validation_error`
- `unsupported_source`

No generic user-facing `unknown_error` class should be introduced in D1.

#### 5.2.9. Editable draft fields

Only the following fields are editable in review:

- `title`
- `description`
- `ingredients_raw`
- `instructions_raw`
- `image_url`

Everything else is immutable in D1 review mode.

#### 5.2.10. Retry rules

Retry behavior is fixed:

- retry `fetch_error` exactly 2 additional times
- do not retry `parse_error`
- do not retry `normalize_error`
- do not retry `validation_error`
- do not retry `unsupported_source`

### 5.3. ⚠️ Hotspot files

#### 5.3.1. `apps/domain/models.py`

Defines durable import truth and approved recipe handoff shape.

#### 5.3.2. `shared/schema/imports.py`

Defines the single import vocabulary shared across API, domain, worker, and frontend.

#### 5.3.3. `apps/worker/jobs.py`

Defines whether async import is real and stage-driven.

#### 5.3.4. `apps/domain/imports.py`

Defines the actual state machine and approval semantics.

### 5.4. 🧪 Required test surfaces

The following test surface categories are mandatory for this deliverable:

#### 5.4.1. Truth-model tests

Must prove:
- the state model is coherent
- invalid transitions are rejected
- approval prerequisites are enforced

#### 5.4.2. Route/contract tests

Must prove:
- submission route works
- status route works
- patch/review/approval route works
- public transport shapes remain stable

#### 5.4.3. Worker/runtime tests

Must prove:
- async execution is real
- retries behave as fixed in the packet
- state transitions are durable and ordered

#### 5.4.4. Parser/fixture tests

Must prove:
- each guaranteed domain produces deterministic output
- fallback produces deterministic review/failure behavior
- attribution and warnings survive parsing

#### 5.4.5. Approval tests

Must prove:
- editable fields are exactly the allowed set
- approval produces approved recipe truth
- immutable fields are protected

## 6. 🌲 Safe Parallelism Plan

### 6.1. 🔗 Serial truth that must stabilize first

These must be frozen before wide parallel work begins.

#### 6.1.1. Durable status set

Exactly:

- `queued`
- `fetching`
- `parsing`
- `normalizing`
- `review_required`
- `approved`
- `failed`

#### 6.1.2. Approval prerequisites

Exactly the required fields listed in section **5.2.4**.

#### 6.1.3. Failure-class vocabulary

Exactly the classes listed in **5.2.8**.

#### 6.1.4. Editable-field policy

Exactly the editable fields listed in **5.2.9**.

### 6.2. 🔀 Safe parallel workstreams

Once the serial truth above is frozen, these streams are safe.

#### 6.2.1. Stream A — 🧪 Boilerplate and initial test setup

Safe files:

- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `shared/testkit/workflows.py`
- test file scaffolding for domain/api/worker/import checks

#### 6.2.2. Stream B — 🧩 Domain truth + shared schemas

Safe files:

- `apps/domain/models.py`
- `apps/domain/imports.py`
- `shared/schema/common.py`
- `shared/schema/events.py`
- `shared/schema/imports.py`

#### 6.2.3. Stream C — 🐍 API route activation

Safe files:

- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/schemas.py`
- `apps/api/imports.py`
- `apps/api/health.py`

#### 6.2.4. Stream D — 📦 Worker activation

Safe files:

- `apps/worker/main.py`
- `apps/worker/jobs.py`
- `apps/worker/queue.py`
- `apps/worker/retry.py`
- `apps/worker/status.py`

#### 6.2.5. Stream E — 🍽️ Parser implementation

Safe split:

- sub-agent/dev 1:
  - `joshuaweissman.com`
  - `simplyrecipes.com`
  - `allrecipes.com`
- sub-agent/dev 2:
  - `delish.com`
  - `epicurious.com`
  - `livingchirpy.com`
- sub-agent/dev 3:
  - structured fallback
  - heuristic fallback
  - normalization helper support

#### 6.2.6. Stream F — 📚 Docs + verification tooling

Safe files:

- `docs/imports.md`
- `docs/adr.md`
- `docs/testing.md`
- `docs/operations.md`
- `tools/scripts/import_check.py`

### 6.3. 🐝 Dedicated boilerplate / test-setup lane

This lane exists specifically to reduce friction and make TDD realistic instead of aspirational.

#### 6.3.1. What it should do

- create test file skeletons
- create fixture loaders/builders
- create helper factories for import records and parser outputs
- create reusable workflow helpers for async import progression tests
- prepare import-check script skeleton structure

#### 6.3.2. What it must not do

- decide durable status semantics
- decide approval prerequisites
- decide failure classes
- decide parser ordering
- decide retry rules

Those are already fixed in this packet.

### 6.4. 🚫 Parallelism that is not safe

Do **not** do these in parallel without direct sync.

#### 6.4.1. State model and approval logic in separate unsynced streams

This causes contradictions about:
- draft meaning
- approval meaning
- approved recipe handoff shape

#### 6.4.2. Shared schema and API contract in separate unsynced streams

This creates duplicate import vocabularies.

#### 6.4.3. Retry policy before failure-class vocabulary is frozen

This creates mismatched retry and triage behavior.

#### 6.4.4. Parser implementation before normalized output target is frozen

This causes each parser to invent its own output semantics.

## 7. 🧾 Exact TL;DR Sections Per New or Refactored File

Use the exact TL;DR snippets in the separate block after this document.

## 8. 🎟️ Task Tickets

## 8.1. 🎟️ S1-D1-T0 — 🧪 Test harness and boilerplate setup for import work

**Owner:** 👤🛡️ Platform/QA  
**Support/Pairing:** 👤🧰 BE/API  
**Goal:** Create the boilerplate and baseline test scaffolding so every later D1 task can follow TDD without setup drift.  
**Depends On:** none inside D1  
**Blocks:** no ticket logically, but unblocks faster TDD execution for all later tickets  
**Parallelization Notes:** may begin immediately and should stay constrained to setup, helpers, and scaffolding

**Files touched:**
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `shared/testkit/workflows.py`
- new test skeleton files for domain / api / worker / parser flows
- `tools/scripts/import_check.py` skeleton
- `docs/testing.md`

### 8.1.1. Purpose

This ticket exists because “TDD-first” fails in practice when nobody creates the harness work up front.

The purpose is to front-load:

- repetitive test scaffolding
- fixture factories
- workflow helpers
- import-check entry structure

so later implementation tickets can focus on behavior instead of setup churn.

### 8.1.2. Step-by-step implementation plan

- [ ] **Create shared import fixture builders**
  - [ ] **Base raw-input fixtures**
    - [ ] add a factory for raw recipe URL inputs
    - [ ] add a factory for raw parser HTML/content fixture containers
    - [ ] add a factory for import-record seed objects in each durable status
  - [ ] **Parsed-output fixtures**
    - [ ] add a factory for successful guaranteed-domain parser output
    - [ ] add a factory for low-confidence fallback output
    - [ ] add a factory for classified failure output
  - [ ] **Approved-output fixtures**
    - [ ] add a factory for approved recipe handoff result
    - [ ] add a factory for partially complete reviewable draft
    - [ ] add a factory for invalid approval attempt input
- [ ] **Create workflow test helpers**
  - [ ] **Import progression helpers**
    - [ ] add helper for queued → fetching → parsing progression assertions
    - [ ] add helper for parsing → normalizing → review_required progression assertions
    - [ ] add helper for failure progression assertions
  - [ ] **Approval helpers**
    - [ ] add helper for editable-draft update assertions
    - [ ] add helper for approval success assertions
    - [ ] add helper for approval rejection/failure assertions
  - [ ] **Parser fixture helpers**
    - [ ] add helper for loading a domain fixture by host
    - [ ] add helper for loading fallback fixtures
    - [ ] add helper for comparing normalized parser outputs against expectations
- [ ] **Create skeleton test files**
  - [ ] **Domain tests**
    - [ ] create skeleton file for import state-machine tests
    - [ ] create skeleton file for approval-rule tests
    - [ ] create skeleton file for failure-class tests
  - [ ] **API tests**
    - [ ] create skeleton file for submit/status/patch route tests
    - [ ] create skeleton file for envelope and error-shape assertions
    - [ ] create skeleton file for request-id / context-related route behavior if applicable
  - [ ] **Worker/parser tests**
    - [ ] create skeleton file for worker async progression tests
    - [ ] create skeleton file for retry tests
    - [ ] create skeleton file for parser and fallback regression tests
- [ ] **Create import-check tooling skeleton**
  - [ ] **CLI structure**
    - [ ] define one entrypoint function
    - [ ] define one single-domain check path
    - [ ] define one all-domains check path
  - [ ] **Output structure**
    - [ ] define readable pass/fail output structure
    - [ ] define failure classification output shape
    - [ ] define summary output shape
  - [ ] **Docs update**
    - [ ] add a TDD/testing note in `docs/testing.md`
    - [ ] explain that later D1 tickets must extend these tests instead of inventing new ad hoc harnesses
    - [ ] document where the boilerplate/test-setup lane stops and behavior tickets begin

### 8.1.3. Required micro-slice conventional commits

- `test(import): add shared import fixture builders and workflow helper scaffolding`
- `test(import): add skeleton test files for domain api worker and parser paths`
- `tools(import): scaffold import-check runner and document test-first workflow`

## 8.2. 🎟️ S1-D1-T1 — 🧩 Durable import truth model + shared schemas

**Owner:** 👤🧰 BE/API  
**Support/Pairing:** 👤🎯 Team Lead  
**Goal:** Freeze and implement the import truth model, shared transport shapes, and approval handoff semantics so later D1 tasks can build on one vocabulary.  
**Depends On:** T0 helpful, but not required  
**Blocks:** T2, T3, T4, T5, T6  
**Parallelization Notes:** first behavior-defining ticket; all other D1 behavior tickets depend on its vocabulary

**Files touched:**
- `apps/domain/models.py`
- `apps/domain/imports.py`
- `shared/schema/common.py`
- `shared/schema/events.py`
- `shared/schema/imports.py`
- `docs/imports.md`

### 8.2.1. Purpose

This ticket freezes the core semantics of what an import is.

Without this ticket, every other stream would be guessing about:
- states
- confidence
- approval behavior
- failure semantics
- output shape

### 8.2.2. Step-by-step implementation plan

- [ ] **Implement the durable import record model**
  - [ ] **Create identity and origin fields**
    - [ ] add `id`
    - [ ] add `actor_id`
    - [ ] add `tenant_id`
    - [ ] add `source_url`
    - [ ] add `source_domain`
    - [ ] add `imported_at`
  - [ ] **Create state and classification fields**
    - [ ] add `status` using exactly the 7 durable states
    - [ ] add `confidence` using exactly `high | medium | low`
    - [ ] add `review_required` as a boolean
    - [ ] add `failure_class` using exactly the 5 fixed classes
    - [ ] add `warnings` as durable structured warning storage
  - [ ] **Create recipe draft content fields**
    - [ ] add `title`
    - [ ] add `description`
    - [ ] add `image_url`
    - [ ] add `ingredients_raw`
    - [ ] add `instructions_raw`
    - [ ] add normalized companion fields for ingredients and instructions
- [ ] **Implement the approved recipe handoff model**
  - [ ] **Create durable approved recipe target**
    - [ ] add approved record identity
    - [ ] add back-reference `import_id`
    - [ ] add `tenant_id`
    - [ ] add approved recipe content fields
  - [ ] **Preserve attribution**
    - [ ] copy `source_url`
    - [ ] copy `source_domain`
    - [ ] preserve import linkage for auditability
  - [ ] **Preserve raw + normalized content**
    - [ ] keep `ingredients_raw`
    - [ ] keep `ingredients_normalized`
    - [ ] keep `instructions_raw`
    - [ ] keep `instructions_normalized`
- [ ] **Implement shared transport schemas**
  - [ ] **Submission/status shapes**
    - [ ] define submission result shape
    - [ ] define import status/result shape
    - [ ] expose state, confidence, review_required, failure_class, warnings
  - [ ] **Edit/approval shapes**
    - [ ] define request shape for editable fields only
    - [ ] define approval response with approved recipe linkage
    - [ ] define rejection/error response shape for invalid review/approval attempts
  - [ ] **Common/event support**
    - [ ] add common ID/timestamp shapes where needed
    - [ ] add event-ish import progress shape if used by worker tests
    - [ ] keep names aligned with domain meaning
- [ ] **Write tests before finalizing implementation**
  - [ ] **Truth-model tests**
    - [ ] write failing test for valid durable state set
    - [ ] write failing test for invalid transition rejection
    - [ ] write failing test for approval prerequisite enforcement
  - [ ] **Schema tests**
    - [ ] write failing test for shared import result shape coverage
    - [ ] write failing test for editable-field request shape restriction
    - [ ] write failing test for approval response shape
  - [ ] **Docs parity tests / checks**
    - [ ] verify docs terminology matches state vocabulary
    - [ ] verify no second synonym appears in docs
    - [ ] verify all fixed decisions are reflected in `docs/imports.md`

### 8.2.3. Required micro-slice conventional commits

- `test(import): add failing tests for durable import states and approval prerequisites`
- `feat(import): add durable import record and approved recipe handoff model`
- `feat(schema): add shared import transport shapes and review state vocabulary`
- `docs(imports): define import state machine approval rules and failure classes`

## 8.3. 🎟️ S1-D1-T2 — 🐍 Import API activation + request flow

**Owner:** 👤🧰 BE/API  
**Support/Pairing:** 👤🎨 FE/Data  
**Goal:** Turn import submission, status retrieval, and review/approval actions into live route surfaces over the frozen import vocabulary.  
**Depends On:** T1  
**Blocks:** D2 frontend wiring, T5 approval loop integration  
**Parallelization Notes:** can run in parallel with T3 and T4 after T1 is frozen

**Files touched:**
- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/schemas.py`
- `apps/api/imports.py`
- `apps/api/health.py`
- `shared/contract/http.py`
- `shared/contract/errors.py`

### 8.3.1. Purpose

This ticket turns the import model into a real network entrypoint.

### 8.3.2. Step-by-step implementation plan

- [ ] **Write route tests first**
  - [ ] **Submission tests**
    - [ ] add failing test for valid URL submission
    - [ ] add failing test for malformed URL rejection
    - [ ] add failing test that submission returns durable import reference immediately
  - [ ] **Status tests**
    - [ ] add failing test that import status can be retrieved by id
    - [ ] add failing test that status exposes warnings/confidence/failure_class
    - [ ] add failing test that in-progress versus review versus approved states are distinguishable
  - [ ] **Patch/review tests**
    - [ ] add failing test for valid editable-field patch
    - [ ] add failing test rejecting immutable field patch
    - [ ] add failing test for approval action response shape
- [ ] **Implement route registration**
  - [ ] **Mount import routes**
    - [ ] register `POST /imports`
    - [ ] register `GET /imports/{id}`
    - [ ] register `PATCH /imports/{id}`
  - [ ] **Preserve route grouping clarity**
    - [ ] keep import routes isolated in `apps/api/imports.py`
    - [ ] keep route registration explicit in `apps/api/routes.py`
    - [ ] avoid mixing import routes into unrelated MVP route modules
  - [ ] **Preserve visibility hooks**
    - [ ] keep middleware path for request IDs intact
    - [ ] keep release marker / runtime identity attachable
    - [ ] keep public envelope and error handling consistent
- [ ] **Implement submit-import behavior**
  - [ ] **Request validation**
    - [ ] require request body field `source_url`
    - [ ] strip surrounding whitespace
    - [ ] normalize host/domain casing
  - [ ] **Durable creation**
    - [ ] create durable import record in `queued`
    - [ ] populate actor/tenant context placeholders or actual values as available
    - [ ] return the created import reference immediately
  - [ ] **Async handoff**
    - [ ] enqueue one root import job
    - [ ] do not parse inline in route
    - [ ] ensure enqueue failure maps to public error shape
- [ ] **Implement get-import behavior**
  - [ ] **Durable lookup**
    - [ ] load import record by id
    - [ ] return stable shared import result shape
    - [ ] include normalized draft content if available
  - [ ] **State rendering**
    - [ ] expose `queued`, `fetching`, `parsing`, `normalizing`
    - [ ] expose `review_required` with review metadata
    - [ ] expose `approved` with approved recipe linkage
  - [ ] **Error rendering**
    - [ ] return classified failure states
    - [ ] avoid vague generic failure responses
    - [ ] preserve warnings/failure_class visibility
- [ ] **Implement patch-import behavior**
  - [ ] **Editable-draft path**
    - [ ] accept only the fixed editable fields
    - [ ] reject immutable field updates
    - [ ] require current state `review_required`
  - [ ] **Approval path**
    - [ ] accept explicit `approve` action
    - [ ] route approval through domain helper
    - [ ] return approved recipe linkage
  - [ ] **Failure handling**
    - [ ] reject approval from non-review states
    - [ ] reject approval with missing required fields
    - [ ] map invalid actions to stable public error responses

### 8.3.3. Required micro-slice conventional commits

- `test(api): add failing tests for live import submission status and patch flows`
- `feat(api): register import routes and return durable queued import references`
- `feat(api): add import status and review patch handling over shared contracts`
- `refactor(api): keep import route layer thin and aligned with domain-owned transitions`

## 8.4. 🎟️ S1-D1-T3 — 📦 Worker runtime activation + queue + retry + status transitions

**Owner:** 👤🛡️ Platform/QA  
**Support/Pairing:** 👤🧰 BE/API  
**Goal:** Make import execution actually asynchronous and ensure durable status transitions are real, bounded, and explainable.  
**Depends On:** T1  
**Blocks:** T4 parser execution, T6 failure classification proofs  
**Parallelization Notes:** can run in parallel with T2 and T4 once T1 is frozen

**Files touched:**
- `apps/worker/main.py`
- `apps/worker/jobs.py`
- `apps/worker/queue.py`
- `apps/worker/retry.py`
- `apps/worker/imports.py`
- `apps/worker/normalize.py`
- `apps/worker/status.py`
- `shared/adapter/queue.py`

### 8.4.1. Purpose

This ticket makes “async import” real rather than rhetorical.

### 8.4.2. Step-by-step implementation plan

- [ ] **Write worker/runtime tests first**
  - [ ] **Async progression tests**
    - [ ] add failing test for queued → fetching progression
    - [ ] add failing test for fetching → parsing → normalizing progression
    - [ ] add failing test for final `review_required` or `failed` state
  - [ ] **Retry tests**
    - [ ] add failing test for exactly 2 additional retries on `fetch_error`
    - [ ] add failing test for no retry on `parse_error`
    - [ ] add failing test for no retry on `unsupported_source`
  - [ ] **Visibility tests**
    - [ ] add failing test that failure_class persists durably
    - [ ] add failing test that warnings remain visible after worker processing
    - [ ] add failing test that worker never sets `approved`
- [ ] **Activate worker runtime**
  - [ ] **Startup**
    - [ ] create explicit worker startup entry
    - [ ] register one root job `run_import`
    - [ ] keep startup behavior readable and explainable
  - [ ] **Queue seam**
    - [ ] implement enqueue helper behind shared adapter
    - [ ] implement consume/dispatch path in worker
    - [ ] ensure queue payload matches API enqueue payload
  - [ ] **Identity and observability**
    - [ ] preserve runtime identity structure
    - [ ] keep clear log/telemetry hook points
    - [ ] avoid hidden queue behavior outside explicit files
- [ ] **Implement stage-driven execution**
  - [ ] **Fetch stage**
    - [ ] set durable status to `fetching`
    - [ ] perform fetch
    - [ ] on network-like failure classify as `fetch_error`
  - [ ] **Parse stage**
    - [ ] set durable status to `parsing`
    - [ ] choose parser using fixed parser-order rule
    - [ ] on parser mismatch classify as `parse_error` or `unsupported_source`
  - [ ] **Normalize stage**
    - [ ] set durable status to `normalizing`
    - [ ] normalize parsed output into fixed draft target shape
    - [ ] on normalization failure classify as `normalize_error`
- [ ] **Implement finalization behavior**
  - [ ] **Review-required path**
    - [ ] if any review-required rule matches, set `review_required = true`
    - [ ] set durable status to `review_required`
    - [ ] preserve warnings and confidence
  - [ ] **Failure path**
    - [ ] if no minimally usable output exists, set `failed`
    - [ ] preserve failure_class
    - [ ] preserve warnings/error detail
  - [ ] **Never-approve rule**
    - [ ] worker must never set `approved`
    - [ ] worker must never create approved recipe truth
    - [ ] approval must remain domain-owned
- [ ] **Implement retry policy**
  - [ ] **Retryable**
    - [ ] retry `fetch_error` once
    - [ ] retry `fetch_error` a second time
    - [ ] after that, finalize `failed`
  - [ ] **Non-retryable**
    - [ ] do not retry `parse_error`
    - [ ] do not retry `normalize_error`
    - [ ] do not retry `validation_error`
    - [ ] do not retry `unsupported_source`
  - [ ] **Attempt accounting**
    - [ ] preserve attempt count in worker-visible metadata if feasible
    - [ ] make final failure explainable to operators
    - [ ] keep retry logic simple enough to explain line by line

### 8.4.3. Required micro-slice conventional commits

- `test(worker): add failing tests for async import progression retry and durable status rules`
- `feat(worker): activate import worker startup and queue-driven execution path`
- `feat(worker): add stage-driven status transitions across fetch parse and normalize`
- `feat(worker): add fixed bounded retry behavior and durable failure classification`

## 8.5. 🎟️ S1-D1-T4 — 🍽️ Guaranteed-domain parsers + 🌐 fallback implementation

**Owner:** 👤🧰 BE/API  
**Support/Pairing:** 👤👻 AI/Cloud  
**Goal:** Implement the six guaranteed parser paths and one fallback path using the fixed parser-order and confidence rules.  
**Depends On:** T1, T3  
**Blocks:** T6 regression proofs, D2 import-assist AI wiring  
**Parallelization Notes:** domain parsers can be safely split across sub-agents after parser output shape is frozen

**Files touched:**
- `apps/worker/imports.py`
- `apps/worker/normalize.py`
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `tools/scripts/import_check.py`
- `docs/imports.md`

### 8.5.1. Purpose

This ticket makes the import path actually useful by meeting the required domain support guarantee.

### 8.5.2. Step-by-step implementation plan

- [ ] **Write parser regression tests first**
  - [ ] **Guaranteed-domain parser tests**
    - [ ] write failing test for `joshuaweissman.com`
    - [ ] write failing test for `simplyrecipes.com`
    - [ ] write failing test for `allrecipes.com`
    - [ ] write failing test for `delish.com`
    - [ ] write failing test for `epicurious.com`
    - [ ] write failing test for `livingchirpy.com`
  - [ ] **Fallback tests**
    - [ ] write failing test for structured fallback success
    - [ ] write failing test for heuristic fallback review-required success
    - [ ] write failing test for unsupported-source failure
  - [ ] **Normalization tests**
    - [ ] write failing test for raw + normalized ingredient preservation
    - [ ] write failing test for raw + normalized instruction preservation
    - [ ] write failing test for attribution preservation
- [ ] **Implement guaranteed parser set A**
  - [ ] **Parser 1 — `joshuaweissman.com`**
    - [ ] detect normalized host match
    - [ ] extract title
    - [ ] extract raw ingredient lines
    - [ ] extract raw instruction lines
    - [ ] extract optional metadata when present
  - [ ] **Parser 2 — `simplyrecipes.com`**
    - [ ] detect normalized host match
    - [ ] extract the same required target fields
    - [ ] preserve warnings when optional fields are missing
    - [ ] preserve attribution fields exactly
  - [ ] **Parser 3 — `allrecipes.com`**
    - [ ] detect normalized host match
    - [ ] extract the same required target fields
    - [ ] preserve warnings when optional fields are missing
    - [ ] preserve attribution fields exactly
- [ ] **Implement guaranteed parser set B**
  - [ ] **Parser 4 — `delish.com`**
    - [ ] detect normalized host match
    - [ ] extract title, ingredient lines, instruction lines
    - [ ] preserve metadata and warnings
  - [ ] **Parser 5 — `epicurious.com`**
    - [ ] detect normalized host match
    - [ ] extract title, ingredient lines, instruction lines
    - [ ] preserve metadata and warnings
  - [ ] **Parser 6 — `livingchirpy.com`**
    - [ ] detect normalized host match
    - [ ] extract title, ingredient lines, instruction lines
    - [ ] preserve metadata and warnings
- [ ] **Implement fallback stage 1 — structured extraction**
  - [ ] **Structured success**
    - [ ] attempt generic structured extraction first
    - [ ] map output into the fixed draft target fields
    - [ ] set confidence according to completeness and warnings
  - [ ] **Structured limitations**
    - [ ] if required fields are missing, keep `review_required = true`
    - [ ] do not silently elevate incomplete output to `high`
    - [ ] preserve structured extraction warnings
  - [ ] **Structured failure handoff**
    - [ ] if no usable structured output exists, route to heuristic fallback
    - [ ] do not mark failed yet
    - [ ] preserve source metadata for later stages
- [ ] **Implement fallback stage 2 — heuristic extraction**
  - [ ] **Heuristic success**
    - [ ] attempt title extraction
    - [ ] attempt ingredient block extraction
    - [ ] attempt instruction block extraction
  - [ ] **Heuristic review policy**
    - [ ] if minimally usable, force `confidence = low`
    - [ ] force `review_required = true`
    - [ ] preserve warnings on every partial extraction
  - [ ] **Heuristic failure**
    - [ ] if minimally usable output still cannot be produced, classify as `unsupported_source` or `parse_error`
    - [ ] do not fabricate partial trusted recipes
    - [ ] return clear failure detail to downstream stages
- [ ] **Implement normalization**
  - [ ] **Ingredients**
    - [ ] preserve original lines exactly
    - [ ] create normalized ingredient list structure
    - [ ] attach warnings when line parsing is partial
  - [ ] **Instructions**
    - [ ] preserve original instruction content
    - [ ] create normalized step list structure
    - [ ] attach warnings when segmentation is partial
  - [ ] **Metadata**
    - [ ] keep title and description as extracted/edited
    - [ ] preserve `source_url` and `source_domain` exactly
    - [ ] preserve image/time/servings metadata only when actually extracted

### 8.5.3. Required micro-slice conventional commits

- `test(parser): add failing guaranteed-domain and fallback parser regression coverage`
- `feat(parser): add first three guaranteed domain parsers against the fixed import contract`
- `feat(parser): add remaining guaranteed domain parsers and metadata preservation`
- `feat(parser): add structured and heuristic fallback with fixed review-required rules`
- `refactor(import): normalize parser outputs into one durable draft target shape`

## 8.6. 🎟️ S1-D1-T5 — ✅ Review / edit / approval loop and approved recipe handoff

**Owner:** 👤🧰 BE/API  
**Support/Pairing:** 👤🎨 FE/Data  
**Goal:** Turn low-confidence import results into trusted recipe truth through a stable review/edit/approval loop.  
**Depends On:** T1, T2, T4  
**Blocks:** D4 planning/list work over approved recipe truth  
**Parallelization Notes:** can run in parallel with T6 after approval semantics are frozen

**Files touched:**
- `apps/domain/imports.py`
- `apps/domain/services.py`
- `apps/api/imports.py`
- `shared/schema/imports.py`
- `docs/imports.md`
- `docs/adr.md`

### 8.6.1. Purpose

This ticket ensures the system can take imperfect parse results and turn them into trusted product truth without ambiguity.

### 8.6.2. Step-by-step implementation plan

- [ ] **Write review/approval tests first**
  - [ ] **Edit tests**
    - [ ] write failing test for editing allowed fields in `review_required`
    - [ ] write failing test rejecting immutable source-field edits
    - [ ] write failing test rejecting edits outside `review_required`
  - [ ] **Approval tests**
    - [ ] write failing test approving a valid review-required draft
    - [ ] write failing test rejecting approval when required fields are missing
    - [ ] write failing test proving approval preserves attribution/import linkage
  - [ ] **Approved-output tests**
    - [ ] write failing test that approved recipe truth exists separately from import draft
    - [ ] write failing test that approved recipe truth preserves raw + normalized content
    - [ ] write failing test that import record survives approval
- [ ] **Implement editable draft policy**
  - [ ] **Allow only fixed fields**
    - [ ] allow `title`
    - [ ] allow `description`
    - [ ] allow `ingredients_raw`
    - [ ] allow `instructions_raw`
    - [ ] allow `image_url`
  - [ ] **Reject all other fields**
    - [ ] reject `source_url`
    - [ ] reject `source_domain`
    - [ ] reject actor/tenant linkage
    - [ ] reject timestamps and immutable historical fields
  - [ ] **State gate**
    - [ ] edits only when status is `review_required`
    - [ ] reject edits for `approved`
    - [ ] reject edits for `failed`
- [ ] **Implement approval behavior**
  - [ ] **Validate prerequisites**
    - [ ] require fixed required fields
    - [ ] require current state `review_required`
    - [ ] require valid actor/tenant context hooks for later D3 integration
  - [ ] **Create approved recipe truth**
    - [ ] create separate durable approved recipe record
    - [ ] carry over source attribution
    - [ ] carry over import linkage
  - [ ] **Finalize import**
    - [ ] set import status to `approved`
    - [ ] preserve warnings and confidence history
    - [ ] never collapse import and approved recipe into one record
- [ ] **Implement rejection/continued-review behavior**
  - [ ] **Explicit rejection**
    - [ ] allow explicit reject action from `review_required`
    - [ ] keep result durable and explainable
    - [ ] only use `failed` when the draft should no longer remain actionable
  - [ ] **Continued review**
    - [ ] preserve `review_required` after edit-only changes
    - [ ] return updated draft truth
    - [ ] never auto-approve on edit
  - [ ] **Document the decision**
    - [ ] update `docs/imports.md`
    - [ ] add ADR entry if approval separation or lifecycle semantics changed architecture meaningfully
    - [ ] keep docs language exactly aligned to implementation

### 8.6.3. Required micro-slice conventional commits

- `test(review): add failing tests for editable draft policy and approval prerequisites`
- `feat(review): add state-gated review edits over fixed editable fields`
- `feat(review): add approval transition that creates separate durable approved recipe truth`
- `docs(imports): document review edit and approval semantics for the live MVP`

## 8.7. 🎟️ S1-D1-T6 — 🧪 Regression fixtures + 🔍 failure classification + import-check tooling

**Owner:** 👤🛡️ Platform/QA  
**Support/Pairing:** 👤🧰 BE/API  
**Goal:** Make the import loop regression-resistant and operator-supportable under real usage.  
**Depends On:** T3, T4, T5  
**Blocks:** deliverable closeout, D6 readiness  
**Parallelization Notes:** begins once the parser/worker/approval paths are coherent enough to test repeatably

**Files touched:**
- `shared/testkit/fixtures.py`
- `shared/testkit/factory.py`
- `shared/testkit/workflows.py`
- `tools/scripts/import_check.py`
- `docs/testing.md`
- `docs/operations.md`

### 8.7.1. Purpose

This ticket ensures the import loop remains reliable as the codebase expands.

### 8.7.2. Step-by-step implementation plan

- [ ] **Add deterministic fixtures**
  - [ ] **Guaranteed domains**
    - [ ] add at least one deterministic fixture for `joshuaweissman.com`
    - [ ] add at least one deterministic fixture for `simplyrecipes.com`
    - [ ] add at least one deterministic fixture for `allrecipes.com`
    - [ ] add at least one deterministic fixture for `delish.com`
    - [ ] add at least one deterministic fixture for `epicurious.com`
    - [ ] add at least one deterministic fixture for `livingchirpy.com`
  - [ ] **Fallback and failure**
    - [ ] add one structured-fallback fixture
    - [ ] add one heuristic-fallback fixture
    - [ ] add one unsupported-source fixture
  - [ ] **Approval fixtures**
    - [ ] add one review-required draft fixture
    - [ ] add one editable corrected draft fixture
    - [ ] add one approval-success expected output fixture
- [ ] **Add regression assertions**
  - [ ] **Required content assertions**
    - [ ] assert title presence for successful parse outputs
    - [ ] assert ingredient presence for successful parse outputs
    - [ ] assert instruction presence for successful parse outputs
  - [ ] **Attribution and confidence assertions**
    - [ ] assert `source_url` preservation
    - [ ] assert `source_domain` preservation
    - [ ] assert low-confidence fallback never reports `high`
  - [ ] **State assertions**
    - [ ] assert low-confidence/fallback outputs can land in `review_required`
    - [ ] assert invalid outputs land in classified `failed`
    - [ ] assert approved output shape remains consistent after approval tests
- [ ] **Implement import-check tooling**
  - [ ] **CLI entry**
    - [ ] implement single-domain run mode
    - [ ] implement all-domains run mode
    - [ ] implement fallback-only run mode if useful
  - [ ] **Output design**
    - [ ] print domain/fallback identifier
    - [ ] print pass/fail
    - [ ] print failure_class when failing
  - [ ] **Docs**
    - [ ] update `docs/testing.md` with run instructions
    - [ ] update `docs/operations.md` with operator-facing meaning of the failure classes
    - [ ] document how to tell fixture drift from intended parser improvement

### 8.7.3. Required micro-slice conventional commits

- `test(import): add deterministic fixtures for guaranteed domains fallback and approval cases`
- `test(import): add regression assertions for attribution confidence and durable import states`
- `tools(import): add import-check modes for single-domain full-suite and failure output`
- `docs(operations): document import failure classes and parser verification workflow`

## 9. 👾 Verification Tickets

## 9.1. 👾 S1-D1-T0-V — verify test harness and boilerplate setup

**Verifier:** 👤🛡️ Platform/QA  
**Expected behavior:** the test harness exists, is reusable, and reduces later implementation ambiguity rather than adding it.

### 9.1.1. Verification checklist

- [ ] **Verify fixture helpers**
  - [ ] confirm raw input factories exist
  - [ ] confirm parsed output factories exist
  - [ ] confirm approved output fixtures exist
- [ ] **Verify workflow helpers**
  - [ ] confirm queued→processing helper exists
  - [ ] confirm review/approval helper exists
  - [ ] confirm failure-path helper exists
- [ ] **Verify skeleton tests**
  - [ ] confirm domain, API, worker, and parser test skeletons exist
  - [ ] confirm the skeletons align to the D1 ticket boundaries
  - [ ] confirm the skeletons do not invent extra semantics outside the packet
- [ ] **Verify tooling scaffold**
  - [ ] confirm `import_check.py` entry exists
  - [ ] confirm it has at least placeholder single-domain and all-domains modes
  - [ ] confirm docs explain how later tickets should extend it

## 9.2. 👾 S1-D1-T1-V — verify durable import truth model + shared schemas

**Verifier:** 👤🎯 Team Lead  
**Expected behavior:** exactly one durable import vocabulary exists and approval handoff semantics are stable enough for later MVP work.

### 9.2.1. Verification checklist

- [ ] **Verify durable state model**
  - [ ] confirm the only durable statuses are exactly:
    - [ ] `queued`
    - [ ] `fetching`
    - [ ] `parsing`
    - [ ] `normalizing`
    - [ ] `review_required`
    - [ ] `approved`
    - [ ] `failed`
  - [ ] confirm `review_required` remains a boolean flag and is not duplicated as a second state family
  - [ ] confirm no hidden synonyms for approved/draft/review exist in code or docs
- [ ] **Verify approval semantics**
  - [ ] confirm approval prerequisites are exactly the required fields fixed in section 5.2.4
  - [ ] confirm approval preserves attribution and import linkage
  - [ ] confirm approval does not delete or collapse the original import record
- [ ] **Verify shared schema coherence**
  - [ ] confirm shared schema names match domain names
  - [ ] confirm API transport shapes do not invent extra meanings
  - [ ] confirm `docs/imports.md` describes the same vocabulary as the code

## 9.3. 👾 S1-D1-T2-V — verify import API activation + request flow

**Verifier:** 👤🎨 FE/Data  
**Expected behavior:** live API routes exist, are thin, and expose stable import states and approval behavior.

### 9.3.1. Verification checklist

- [ ] **Verify submission route**
  - [ ] submit a valid URL and confirm a durable import id is returned
  - [ ] confirm the route returns quickly without synchronous parser execution
  - [ ] confirm the returned shape includes status and review metadata
- [ ] **Verify status route**
  - [ ] fetch the import record by id and confirm durable status is returned
  - [ ] confirm warnings/confidence/failure_class are exposed consistently
  - [ ] confirm in-progress states are distinguishable from review and approved states
- [ ] **Verify patch route**
  - [ ] confirm editable fields can be changed while in `review_required`
  - [ ] confirm immutable source fields are rejected
  - [ ] confirm approval action returns approved recipe linkage rather than vague success noise

## 9.4. 👾 S1-D1-T3-V — verify worker runtime activation + queue + retry + status transitions

**Verifier:** 👤🛡️ Platform/QA  
**Expected behavior:** import execution is truly async, durable status transitions are meaningful, and retry behavior is bounded.

### 9.4.1. Verification checklist

- [ ] **Verify async execution**
  - [ ] confirm route submission enqueues work rather than parsing inline
  - [ ] confirm worker startup registers import jobs
  - [ ] confirm worker progress updates durable statuses in order
- [ ] **Verify finalization rules**
  - [ ] confirm successful parses end in `review_required` or `failed`, never `approved`
  - [ ] confirm approval is never assigned by worker code
  - [ ] confirm unusable parses end in classified `failed`
- [ ] **Verify retry behavior**
  - [ ] confirm `fetch_error` retries exactly 2 additional times
  - [ ] confirm `parse_error` does not retry
  - [ ] confirm final durable state preserves failure_class after retries are exhausted

## 9.5. 👾 S1-D1-T4-V — verify guaranteed-domain parsers + 🌐 fallback

**Verifier:** 👤🧰 BE/API  
**Expected behavior:** all guaranteed domains and fallback paths produce stable, normalized outputs or classified failures.

### 9.5.1. Verification checklist

- [ ] **Verify guaranteed domains**
  - [ ] run parser checks for `joshuaweissman.com`
  - [ ] run parser checks for `simplyrecipes.com`
  - [ ] run parser checks for `allrecipes.com`
  - [ ] run parser checks for `delish.com`
  - [ ] run parser checks for `epicurious.com`
  - [ ] run parser checks for `livingchirpy.com`
- [ ] **Verify normalized outputs**
  - [ ] confirm title, ingredient lines, and instruction lines are present for successful parses
  - [ ] confirm attribution is preserved for every successful parse
  - [ ] confirm warnings/confidence are emitted when extraction is partial
- [ ] **Verify fallback**
  - [ ] confirm structured fallback can produce minimally usable results when structured markup exists
  - [ ] confirm heuristic fallback can produce low-confidence reviewable results when structured extraction fails
  - [ ] confirm unsupported content reaches `unsupported_source` or `parse_error` rather than fake success

## 9.6. 👾 S1-D1-T5-V — verify review / edit / approval loop and approved recipe handoff

**Verifier:** 👤🎯 Team Lead  
**Expected behavior:** low-confidence import results can be corrected and approved into durable approved recipe truth.

### 9.6.1. Verification checklist

- [ ] **Verify edit loop**
  - [ ] confirm editable fields are exactly the allowed set
  - [ ] confirm immutable source fields reject patch attempts
  - [ ] confirm editing does not silently approve the record
- [ ] **Verify approval loop**
  - [ ] confirm approval only works from `review_required`
  - [ ] confirm approval fails if required fields are missing
  - [ ] confirm approval creates durable approved recipe truth with attribution and import linkage
- [ ] **Verify future-MVP compatibility**
  - [ ] confirm approved recipe truth is shaped for later planning/list use
  - [ ] confirm later recommendation input can reference approved recipe truth without redesign
  - [ ] confirm docs and ADR language match actual approval behavior

## 9.7. 👾 S1-D1-T6-V — verify regression fixtures + failure classification + import-check tooling

**Verifier:** 👤🛡️ Platform/QA  
**Expected behavior:** parser regressions are catchable, failure classes are stable, and tooling is reusable.

### 9.7.1. Verification checklist

- [ ] **Verify fixture coverage**
  - [ ] confirm there is at least one deterministic fixture per guaranteed domain
  - [ ] confirm fallback structured + heuristic fixtures exist
  - [ ] confirm there is at least one hard-failure fixture
- [ ] **Verify classification coverage**
  - [ ] confirm tooling and tests can surface `fetch_error`
  - [ ] confirm tooling and tests can surface `parse_error`
  - [ ] confirm tooling and tests can surface `normalize_error`, `validation_error`, and `unsupported_source`
- [ ] **Verify tooling**
  - [ ] run `import_check.py` for one specific domain and confirm readable pass/fail output
  - [ ] run `import_check.py` across all domains and confirm aggregate visibility
  - [ ] confirm docs explain how to interpret failures without guesswork

## 10. ✅ Deliverable Verification

### 10.1. 👾 S1-D1-V — full deliverable verification

**Verifier:** 👤🎯 Team Lead  
**Support:** 👤🛡️ Platform/QA, 👤🎨 FE/Data  
**Expected behavior:** the full async import loop is real, supportable, and ready to unblock the rest of Sprint 1.

#### 10.1.1. Verification checklist

- [ ] **Verify end-to-end import truth**
  - [ ] submit one guaranteed-domain URL and confirm it reaches a reviewable draft state
  - [ ] submit one fallback URL and confirm it reaches either reviewable low-confidence state or classified failure
  - [ ] approve one reviewed import and confirm approved recipe truth is created
- [ ] **Verify supportability**
  - [ ] confirm request path returns durable import reference immediately
  - [ ] confirm job execution is async and observable
  - [ ] confirm parser/fallback failures are classified and visible
- [ ] **Verify downstream readiness**
  - [ ] confirm approved recipe truth is ready for D2 frontend wiring
  - [ ] confirm approved recipe truth is ready for D4 planning/list work
  - [ ] confirm import vocabulary and docs reduce guesswork for later Sprint 1 work instead of creating it
- [ ] **Verify completion discipline**
  - [ ] confirm `docs/imports.md`, `docs/testing.md`, `docs/operations.md`, and `docs/adr.md` are updated
  - [ ] confirm micro-slice commits tell the implementation story in narrow rollback-safe chunks
  - [ ] confirm no hidden architectural decision remains undocumented

## 11. 🚨 Bad Agent Output Patterns To Watch For

- inventing a second import state machine in the API layer
- treating `review_required` as both a durable state and an independent parallel state family
- performing parser execution synchronously inside the request path
- adding retry behavior to parser/content-shape failures despite the fixed failure-class rules
- auto-approving high-confidence imports in D1
- dropping source attribution during approval
- flattening import records and approved recipe records into one ambiguous structure
- using generic `failed` without durable `failure_class`
- adding parser implementations without deterministic fixtures
- writing giant mixed commits instead of micro-slice story commits
- updating code without updating `docs/imports.md`, `docs/testing.md`, `docs/operations.md`, and `docs/adr.md`

## 12. 🧩 Rationale in One Sentence

This deliverable establishes one durable, asynchronous, reviewable import truth path so the rest of the live MVP can build on approved recipes instead of placeholders, duplicate vocabularies, or unstable state transitions.