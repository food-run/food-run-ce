# 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze

## TL;DR

S0-D1 creates the hard repo boundary that every later Sprint 0 deliverable depends on. The validated prototype is preserved under `legacy-v0/`, the repo root stops implying that the old layout is still active, and the README/docs rewrite the project story so humans and agents follow the rebuild path rather than extending prototype paths directly.

## Index

- [Why this deliverable is scoped narrowly](#why-this-deliverable-is-scoped-narrowly)
- [👥 Ownership](#ownership)
- [🌿 Branch](#branch)
- [🏷️ Deliverable PR title](#deliverable-pr-title)
- [🎯 Purpose](#purpose)
- [⛓️ Depends on](#depends-on)
- [🚧 Blocks](#blocks)
- [📂 Files touched](#files-touched)
- [🧠 Recommended names](#recommended-names)
- [🧾 Exact section maps and TL;DR text](#exact-section-maps-and-tldr-text)
- [⚠️ Hotspot files](#hotspot-files)
- [🎟️ Task tickets](#task-tickets)
- [👾 Verification tickets](#verification-tickets)
- [✅ Deliverable verification](#deliverable-verification)
- [🚨 Bad agent output patterns to watch for](#bad-agent-output-patterns-to-watch-for)
- [🧩 Rationale in one sentence](#rationale-in-one-sentence)

---

<a id="why-this-deliverable-is-scoped-narrowly"></a>
## Why this deliverable is scoped narrowly

S0-D1 should do **one job extremely well**:

- freeze the prototype as historical proof
- make the active rebuild path unambiguous
- rewrite the repo narrative so humans and agents stop treating the prototype layout as the base to harden

It should **not** also try to finish:

- agent lane rules
- CI/CD enforcement
- Docker/k3s parity
- app skeleton implementation
- observability wiring

Those belong to later Sprint 0 deliverables. If D1 tries to do all of them, the boundary between “archived proof” and “active rebuild” gets muddied immediately.

---

<a id="ownership"></a>
## 👥 Ownership

**Owner:** 👤🎯 Team Lead  
**Reviewer:** 👤🛡️ Platform/QA  
**Required consult:** 👤🧰 BE/API, 👤🎨 FE/Data

---

<a id="branch"></a>
## 🌿 Branch

` s0/d1-repo-reset `

---

<a id="deliverable-pr-title"></a>
## 🏷️ Deliverable PR title

`chore(repo): freeze the prototype as legacy and establish a single authoritative starting point for the rebuild`

---

<a id="purpose"></a>
## 🎯 Purpose

Create the hard repo boundary that all later Sprint 0 work depends on:

- the prototype becomes preserved reference material
- the rebuild becomes the only active path
- the root README and docs tell the truth about that split
- no contributor or agent has to guess where new work belongs

---

<a id="depends-on"></a>
## ⛓️ Depends on

None.

---

<a id="blocks"></a>
## 🚧 Blocks

- 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams
- 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine
- 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates
- 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline
- all later sprints, because none of them should build on an ambiguous repo root

---

<a id="files-touched"></a>
## 📂 Files touched

### Path moves

- `client/**` → `legacy-v0/client/**`
- `server/**` → `legacy-v0/server/**`
- current prototype-oriented docs/assets that describe or support the old layout → `legacy-v0/docs/**`

### New files

- `legacy-v0/README.md`
- `docs/legacy-v0.md`
- `docs/repo.md`

### Meaningfully refactored files

- `README.md`

### Conditional touch only if needed

- root links/badges/navigation that still point contributors at archived paths
- any repo-level references that still describe the prototype as the active architecture

---

<a id="recommended-names"></a>
## 🧠 Recommended names

### File names

- `legacy-v0/README.md`
- `docs/legacy-v0.md`
- `docs/repo.md`

### Preferred repo terms

- `validated prototype`
- `legacy-v0`
- `active tree`
- `authoritative rebuild path`
- `archived surface`
- `rebuild baseline`

### Section names to reuse consistently

- `TL;DR`
- `Current Status`
- `Why Archived`
- `What Still Works`
- `What Is Frozen`
- `Path Ownership`
- `What Not To Build On`
- `Rebuild Rule`

### Function / variable names

Not applicable in this deliverable. S0-D1 is structure + docs only.

---

<a id="exact-section-maps-and-tldr-text"></a>
## 🧾 Exact section maps and TL;DR text

### `README.md`

#### Required section order

- `# Food Run`
- `## TL;DR`
- `## Quick Navigation`
- `## Where Technical Docs Live`
- `## Current Status`
- `## What This Repo Contains Now`
- `## Active Rebuild Path`
- `## Legacy Prototype`
- `## Architecture Direction`
- `## Contribution Boundary`

#### Exact TL;DR text

```md
## TL;DR

Food Run is being rebuilt from a validated prototype into a production-grade, technically documented system. The old prototype is preserved under `legacy-v0/` as reference material, while all new work targets the active rebuild paths and the technical docs in `/docs`.
```

#### What belongs under each section

- `Current Status`
  - explain that the repo is in rebuild mode
  - state that `legacy-v0/` is preserved, not active
- `What This Repo Contains Now`
  - list active root areas at a high level
  - clarify that active work is moving into the new rebuild tree
- `Active Rebuild Path`
  - explicitly say where new work must go
  - state that later Sprint 0 deliverables will seed the full active tree
- `Legacy Prototype`
  - explain what the prototype validated
  - link to `legacy-v0/README.md` and `docs/legacy-v0.md`
- `Architecture Direction`
  - one short summary of the multi-plane rebuild direction
- `Where Technical Docs Live`
  - point to `/docs`
  - explain that deep technical reasoning belongs there, not in ad hoc root notes
- `Contribution Boundary`
  - tell contributors not to extend `legacy-v0/`
  - state that prototype paths are preserved for reference only
- `Quick Navigation`
  - repo link targets
  - docs link targets
  - legacy link targets

### `legacy-v0/README.md`

#### Required section order

- `# Food Run Legacy v0`
- `## TL;DR`
- `## What the Prototype Validated`
- `## Why It Was Archived`
- `## What Is Frozen`
- `## What Still Works as Reference`
- `## What Not to Build On`
- `## How to Reuse It Safely`

#### Exact TL;DR text

```md
## TL;DR

This folder preserves the validated Food Run prototype exactly so the team can reference what was already proven. It is not the active base for the rebuild, and new implementation work must not extend these paths directly.
```

### `docs/legacy-v0.md`

#### Required section order

- `# Legacy v0`
- `## TL;DR`
- `## Snapshot of the Prototype`
- `## Validated User Flows`
- `## Prototype Architecture Snapshot`
- `## Known Constraints`
- `## Preservation Rules`
- `## Safe Reuse Candidates`

#### Exact TL;DR text

```md
## TL;DR

Legacy v0 is preserved because it already proved the core Food Run product loop, but it should be treated as historical evidence rather than as the active technical base. This document records what v0 validated, what technical shortcuts it contained, and which concepts are safe to carry into the rebuild.
```

### `docs/repo.md`

#### Required section order

- `# Repo Layout`
- `## TL;DR`
- `## Repo Intent`
- `## Active Versus Archived Paths`
- `## Root Directory Rules`
- `## Path Ownership`
- `## Prohibited Drift Patterns`
- `## Naming and Depth Rules`

#### Exact TL;DR text

```md
## TL;DR

The repository has one active rebuild surface and one archived prototype surface. Contributors and agents must add new work only to the active rebuild paths, treat `legacy-v0/` as read-most reference material, and preserve a shallow, ownership-driven root layout.
```

---

<a id="hotspot-files"></a>
## ⚠️ Hotspot files

These files carry the narrative boundary for the entire rebuild:

- `README.md`
- `legacy-v0/README.md`
- `docs/legacy-v0.md`
- `docs/repo.md`

If any of them are vague, contributors and agents will still plausibly build in the wrong place.

---

<a id="task-tickets"></a>
## 🎟️ Task tickets

### 🎟️ S0-D1-T1 — 🧭 Inventory the prototype surface and lock the archive map

**Commit title:**  
`chore(repo): inventory the prototype surface and map every legacy path before establishing the rebuild boundary`

#### Purpose

Create the exact relocation map before any files move so the archive is deliberate, reviewable, and reversible.

#### Checklist

- **Survey the current root**
  - identify what is truly prototype-era
  - identify what must remain root-owned
- **Draft the archive decision map**
  - map every moved path to a legacy destination
  - map every narrative/doc destination
- **Create the review packet for the move**
  - present move-vs-keep decisions path by path
  - prevent accidental active-path duplication

#### Review heuristics — reject the task if

- the archive map mixes active rebuild docs with prototype docs
- a root path is both “kept active” and “archived” without an explicit reason
- the move plan assumes later Sprint 0 files already exist
- reviewers cannot tell, path by path, what is being frozen versus kept

### 🎟️ S0-D1-T2 — 📦 Relocate the prototype and create the legacy boundary

**Commit title:**  
`chore(repo): relocate the validated prototype into an archive path and remove active-path ambiguity at the root`

#### Purpose

Perform the structural move that turns the prototype into preserved reference material and clears the repo root for the rebuild.

#### Checklist

- **Execute the path relocation**
  - move the current frontend prototype paths into `legacy-v0/client/`
  - move the current backend prototype paths into `legacy-v0/server/`
  - move prototype-oriented docs and artifacts into `legacy-v0/docs/`
- **Create the archive-facing surface**
  - add `legacy-v0/README.md`
  - create `docs/legacy-v0.md`
  - create `docs/repo.md`
- **Clean the root boundary**
  - ensure no top-level prototype app folders remain active by implication
  - preserve only true repo-level files at the root

#### Review heuristics — reject the task if

- the move breaks the ability to inspect the prototype as a coherent snapshot
- the root still visually suggests that the prototype layout is active
- legacy files are copied instead of moved, creating two competing sources of truth
- archive files are renamed in a way that obscures what they originally were

### 🎟️ S0-D1-T3 — 🧾 Rewrite the repo narrative so humans and agents follow the rebuild path

**Commit title:**  
`docs(repo): rewrite the repository narrative so contributors follow the rebuild path and treat the prototype as archived`

#### Purpose

Replace the old “this repo is the prototype app” story with the new “this repo contains both preserved proof and an active rebuild baseline” story.

#### Checklist

- **Refactor root guidance**
  - rewrite the root README
  - add navigation that prevents wrong-path work
- **Write the two repo-boundary docs**
  - write `docs/repo.md`
  - write `docs/legacy-v0.md`
- **Normalize terminology**
  - keep `legacy-v0`, `active tree`, and `validated prototype` consistent
  - ensure the docs say new work belongs only on active rebuild paths

#### Review heuristics — reject the task if

- the README still reads like the prototype is the current architecture
- `README.md`, `docs/repo.md`, and `docs/legacy-v0.md` disagree about what is active
- the docs describe the archive emotionally or vaguely instead of operationally
- a new contributor could still plausibly open the wrong folder and start building there

---

<a id="verification-tickets"></a>
## 👾 Verification tickets

### 👾 S0-D1-T1-V — 🔍 Verify the structural boundary is real

**Commit title:**  
`test(repo): verify legacy assets stay preserved while active instructions no longer point at archived paths`

#### Purpose

Prove the move created one clear archived surface and removed the false appearance that the prototype is still the active tree.

#### Verification pass condition

A reviewer can clone the repo, look only at the root, and correctly infer in under a minute:

- what is archived
- what is active
- where future work belongs

### 👾 S0-D1-T2-V — 🧠 Verify the narrative boundary is consistent

**Commit title:**  
`docs(repo): align repository and archive documents so path ownership, purpose, and contributor guidance match exactly`

#### Purpose

Prove the repo story is internally consistent across the root README and the new boundary docs.

#### Verification pass condition

A new human reviewer and a planning agent would both derive the same answer to:

- what is the archived prototype?
- what is the active rebuild surface?
- where should new work start?

---

<a id="deliverable-verification"></a>
## ✅ Deliverable verification

S0-D1 is done only when all of the following are true:

- **The repo boundary is physically correct**
  - prototype app paths live under `legacy-v0/`
  - the root no longer presents the old runtime layout as active
  - there is no duplicate active/archive copy of the same prototype paths
- **The repo boundary is narratively correct**
  - `README.md` says the rebuild is active and the prototype is archived
  - `legacy-v0/README.md` says the prototype is preserved, not extended
  - `docs/repo.md` and `docs/legacy-v0.md` agree on path ownership and reuse rules
- **The repo boundary is review-safe**
  - a reviewer can explain what was moved, what stayed, and why
  - a planner agent would have no reason to assign new implementation work into `legacy-v0/`
  - later Sprint 0 deliverables can now seed the active tree without path ambiguity

---

<a id="bad-agent-output-patterns-to-watch-for"></a>
## 🚨 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- keep `client/` or `server/` at the root “for convenience”
- archive only some prototype paths but leave others active-looking
- copy old paths instead of moving them
- write vague docs like “the old app is still here if needed” without strict boundary language
- create new active app skeletons inside D1 just because it “seems efficient”
- rename legacy paths so aggressively that the preserved prototype becomes hard to inspect
- describe the rebuild as if it were already fully scaffolded when that happens in D2+

---

<a id="rationale-in-one-sentence"></a>
## 🧩 Rationale in one sentence

S0-D1 is successful when the repo stops being “a prototype plus intentions” and becomes “a preserved prototype plus one unmistakable rebuild starting point.”
