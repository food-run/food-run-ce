
# Food Run Agent Operating Contract

## TL;DR

Food Run is a prototype-preserving rebuild. `legacy-v0/` is preserved reference material. All new implementation work must target the active rebuild paths. `AGENTS.md` is the always-on repo contract. Planning packets under `docs/planning/` must be opened explicitly for the current sprint, deliverable, or task.

## Table of Contents

- [Repo State](#repo-state)
- [Planning Source of Truth](#planning-source-of-truth)
- [Active vs Archived Paths](#active-vs-archived-paths)
- [Path Ownership Rules](#path-ownership-rules)
- [Hotspot Files](#hotspot-files)
- [Protected Paths](#protected-paths)
- [Lane Model](#lane-model)
- [Planning and Execution Protocol](#planning-and-execution-protocol)
- [TDD and Quality Standard](#tdd-and-quality-standard)
- [Review Questions](#review-questions)
- [Commit Rhythm](#commit-rhythm)
- [Documentation Rule](#documentation-rule)
- [Done Means](#done-means)

## Repo State

- The current public repo is validated prototype evidence.
- The rebuild is intentionally overbuilt, governed, and documentation-heavy.
- Do not silently extend legacy prototype paths for v1 work.
- Do not describe future-state architecture as if it already exists in the repo.

## Planning Source of Truth

Always loaded:

- `AGENTS.md`

Open explicitly when relevant:

- `docs/planning/master-packet.md`
- `docs/planning/sprint-0/overview.md`
- `docs/planning/sprint-0/d1-repo-reset.md`
- The current sprint and deliverable files only

Rules:

- Do not pin the full master packet into project instructions.
- Load only the smallest planning set needed for the current work unit.
- For UI or UX implementation work, also open `docs/design-system/MASTER.md`, the relevant page file in `docs/design-system/pages/`, and any directly relevant supporting design-system file before planning or implementation begins.
- Use the UI/UX skills when the runtime has them loaded; this means `frontend-first-principles` for planning or implementation and `ui-ux-review` for review. If the local skill inventory has not refreshed yet, open the same design-system files directly and continue without blocking on the missing-skill error.
- If planning files conflict, escalate the conflict before editing code or docs.
- If current committed repo reality has already evolved beyond an older packet, refine the packet to the committed permanent structure by default instead of recreating stale file names.
- Stub a missing durable doc only when the exact permanent home is absent and its expected content is not already sufficiently covered elsewhere.
- Follow `.opencode/rules/master-packet-alignment.md` when translating master-packet intent into repo-control behavior.

## Active vs Archived Paths

Archived reference only:

- `legacy-v0/**`

Active rebuild surfaces:

- `apps/**`
- `shared/**`
- `platform/**`
- `tools/**`
- `docs/**`
- `.github/**`
- `.opencode/**`
- `AGENTS.md`
- `opencode.json`

Boundary rules:

- `legacy-v0/` is for reference, inspection, and deliberate extraction only.
- New implementation work must not extend archived prototype paths directly.
- If a reusable idea originates in `legacy-v0/`, port it deliberately into an active path.

## Path Ownership Rules

- One home per concept.
- Prefer deployable-unit boundaries first.
- Prefer shared seams over app-local duplication.
- Do not create junk-drawer roots like `utils/`, `types/`, `interfaces/`, `misc/`, or `helpers/` unless the repo has already standardized them.
- If a concept could reasonably live in two places, stop and escalate before editing.
- Keep naming semantic, stable, and easy to review.
- Keep folder depth shallow unless a framework or tool requires otherwise.

## Hotspot Files

These files and path groups deserve slower, more deliberate review because mistakes here multiply across later work:

- `AGENTS.md`
- `opencode.json`
- `.opencode/agents/**`
- `.opencode/commands/**`
- `.opencode/skills/**`
- `docs/planning/**`
- `docs/repo.md`
- `docs/adr.md`
- `.github/workflows/**`
- Any file that defines repo-wide rules, path ownership, or merge policy

Rules for hotspot files:

- Prefer small diffs.
- Explain why each change is needed.
- Keep terminology consistent across all repo-control docs.
- Do not make speculative edits “for future flexibility.”
- Treat wording changes as behavior changes when they affect humans or agents.

## Protected Paths

Treat these as protected and escalate by default:

- Auth or session policy
- Migrations and schema-destructive changes
- Repo-control workflows
- Tenancy and role enforcement
- Secrets handling
- Release workflows
- Queue replay controls
- Failover controls
- `AGENTS.md`
- `opencode.json`
- `.opencode/**`

Protected-path rules:

- Ambiguous work defaults to deny-or-escalate.
- Destructive work defaults to deny-or-escalate.
- Do not “probably safe” your way through protected paths.
- If a protected-path change is approved, keep the diff narrow and well documented.

## Lane Model

### PM

- Owns orchestration, status, task routing, handoffs, course correction, and human-in-the-loop checkpoints

### Reporter

- Owns structured coordination packet emission and normalization for PM and subagents
- Does not own scope selection, planning, implementation, or review decisions

### Scout

- Owns discovery, grounding, reuse search, hotspot mapping, and packet inconsistency detection

### Planner

- Owns decomposition, task breakdowns, async-safe work splits, file impact, and verification checklists

### Architect

- Owns edge cases, scaffolding, TDD shaping, invariants, and implementation structure
- Must shape implementation-bearing task work before `developer` or `designer` starts so the implementation lane inherits an explicit strategy, test shape, and boilerplate boundary

### Developer

- Owns bounded implementation with a staff-level mindset

### Designer

- Owns UX, UI, accessibility-minded implementation, and visual consistency
- Must implement all UI and UX changes from the design-system planning set, using `docs/design-system/**` as the governing source before editing product surfaces
- Must be the default implementation lane for any product-surface UI or UX change unless the work is docs-only or the human explicitly overrides the lane choice

### Reviewer

- Owns drift detection, boundary checks, explainability burden, and reject-or-approve recommendations
- Must use the `ui-ux-review` skill and the relevant `docs/design-system/**` files when reviewing UI or UX diffs

### Integrator

- Owns QA, smoke-path reasoning, test expansion, rollback-risk reduction, and integration summaries

### Ops

- Owns DevSecOps and FinOps review, blast-radius awareness, and cost-critical change review

### Librarian

- Owns docs, standards, diagrams, durable summaries, and narrative alignment

## Planning and Execution Protocol

At the start of each work unit:

1. Open the current planning file set.
2. Restate the exact scope and boundaries.
3. Identify active paths, protected paths, and hotspot files.
4. Create or update a live task note in `docs/coordination/tasks/`.
5. Follow `.opencode/rules/coordination-standards.md` for every coordination artifact.
6. Create or switch to the scoped working branch before implementation begins.

During work:

- Leave a checkpoint note after each meaningful step.
- Follow `.opencode/rules/coordination-standards.md`.
- Follow the `DRYness Gates` section in `.opencode/rules/implementation-standards.md` before implementation starts and before calling work complete.
- For UI or UX implementation work, plan from the design-system documents first, load `frontend-first-principles` when available, and route the implementation lane to `designer` rather than `developer`.
- Route architect first on implementation-bearing tasks so invariants, failure modes, TDD shape, and scaffolding are defined before developer or designer execution.
- Route ops review after reviewer and integrator pass implementation-bearing work, and do that before librarian closeout or merge preparation.
- Keep tracked work recorded in small Conventional Commit slices that match the current checkpoint rhythm.
- Leave a handoff note before switching lanes.
- Keep task scope narrow.
- Prefer async-safe work splits with minimal merge-conflict risk.
- Do not broaden scope without stating it explicitly.
- Keep `docs/coordination/` visibly current by updating the stable task file and adding scope-named notes, checkpoints, or handoffs as work progresses.

Before asking for a commit or review:

- Summarize what changed.
- Summarize what did not change.
- Name blockers, risks, and follow-up work.
- Make the next action obvious for the next agent or human.

## TDD and Quality Standard

Default to:

- Red → Green → Refactor
- Reuse before invention
- Small diffs over sprawling rewrites
- Explainability over cleverness
- Stable boundaries over convenience hacks
- Follow `.opencode/rules/implementation-standards.md` for shared coding and implementation guidelines.

Do not:

- Suppress errors to make checks pass
- Hide business rules inside transport or middleware layers
- Introduce plausible-but-unowned code
- Add speculative abstractions without a current use case
- Leave coordination notes stale after meaningful changes

## Review Questions

No meaningful change is done until the answer to each is yes:

- Does it follow the current planning packet?
- Does it preserve active-vs-legacy boundaries?
- Does it reuse existing patterns where possible?
- Is it meaningfully unique where it did not reuse an existing pattern?
- Does it keep ownership boundaries intact?
- Can the human explain every changed line?
- Can the human modify it without reprompting?
- Did architect shape the implementation-bearing task before developer or designer execution?
- For UI or UX work, was the change planned against the design-system documents, shaped with `frontend-first-principles` when available, implemented by `designer`, and reviewed with the `ui-ux-review` skill when available in the runtime, or otherwise reviewed directly against the same design-system packet?
- Are live coordination notes current?
- Is the related docs or ADR delta prepared when needed?
- Did ops review the implementation-bearing change before librarian closeout or merge preparation?
- If protected paths or hotspot files changed, was the slower review standard followed?

## Commit Rhythm

- Commit in small, coherent steps.
- Default micro-commits to one file at a time.
- Only group files into one micro-commit when 4 or fewer touched files share the same immediate parent folder and the grouped change stays under 10 total changed lines.
- Use Conventional Commits.
- Choose the first meaningful parent surface that preserves enough context; use `repo` only when no narrower qualifying parent cleanly covers the whole change.
- If a diff would force an overly broad `repo` scope, split the checkpoint into smaller coherent slices first so each commit can use a narrower qualifying parent surface.
- Write commit subjects as clear English summaries in the 12-22 word range.
- Do not use variable names, function names, or raw identifier spellings as commit-message wording; translate them into ordinary English.
- Good: `docs(coordination): ...` for `docs/coordination/**`, `fix(templates): ...` for shared template work, `chore(opencode): ...` for cross-cutting `.opencode/**` changes, and `chore(repo): ...` when the diff spans root governance plus multiple surfaces.
- Avoid: scopes that are too broad for the actual review context, or too narrow because they are only the last nested folder without enough meaning.
- Avoid: `chore(rules): ...` or `chore(skills): ...` when those names are only the last nested folder and not the real review context.
- Do not wait until the full deliverable is complete to commit.
- Commit after each stable checkpoint that would be useful to roll back to.
- Prefer one meaningful checkpoint commit over one giant “finished everything” commit.
- Do not commit broken work unless the task is explicitly marked as a spike and the checkpoint note says so.

## Documentation Rule

- `AGENTS.md` is always-on.
- Planning files are opened explicitly for the current work.
- Durable docs live in committed repo paths.
- Live coordination belongs in `docs/coordination/` and is Git-ignored.
- If a change affects shared understanding, the relevant durable docs must be updated with it.
- ADR entries must be completed before PRs or merge commits for meaningful changes, using the master packet documentation questions in recency-first order.
- Do not create side-channel process docs in random folders.

## Done Means

A meaningful change is only complete when all of the following are true:

- The change is bounded and understandable.
- Repo-wide DRYness review has passed for the affected concept areas.
- Coordination notes are current.
- Review or integration output exists when relevant.
- Ops review output exists for implementation-bearing work before merge-ready status.
- Durable docs are updated when shared understanding changed.
- Protected-path handling was explicit where required.
- The next agent or human can continue without chat archaeology.
