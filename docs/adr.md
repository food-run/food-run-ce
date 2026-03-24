# 🧾 Architecture Decision Record

## TL;DR

This file is the durable reasoning spine for major Food Run technical and process decisions. It is sorted recency first. Later changes should extend these entries or add a new higher entry instead of scattering rationale across pull requests, chat history, or side-channel docs.

### How To Use This File

- Add new decision entries as the rebuild evolves
- Capture why a choice was made, not just what changed
- Link related repo surfaces and docs when the decision changes shared understanding
- Keep entries sorted newest first
- Keep slices as small as current understanding allows without creating duplicate ADR noise
- Plan out-of-scope human edits separately unless the human explicitly includes them

### Decision Entry Template

- ***What was built?***
- ***Why was it chosen?***
- ***What boundaries does it own?***
- ***What breaks if it changes?***
- ***What known edge cases or failure modes matter here?***
- ***Why does this work matter?***
- ***What capability does it unlock?***
- ***Why is the chosen design safer or more scalable?***
- ***What trade-off did the team accept?***

### Current Status

- Sprint 0 deliverables now backfill durable reasoning in reverse chronological order
- 

---

## Entries

---

### S0-D4 - Make the PR narrative and every workflow edit subject to the documented merge gates

- ***What was built?***
  - `.github/workflows/docs-guard.yml` now blocks pull requests that leave `Summary`, `Why this change`, `Files and boundaries`, or `Verification` blank or placeholder-only, and `.github/workflows/protected-paths.yml` now treats any `.github/workflows/**` edit as a protected-path change.
- ***Why was it chosen?***
  - The earlier D4 slices documented PR-shape enforcement and workflow-path protection, but the actual automation still left those two gaps open, which meant reviewers could trust rules that were not fully enforced.
- ***What boundaries does it own?***
  - The minimum reviewer-facing PR narrative every change must provide, and the protected-path boundary for all workflow automation under `.github/workflows/**`.
- ***What breaks if it changes?***
  - Pull requests can slip through with vague review context, workflow changes can avoid the protected-path acknowledgement gate, and the repo's documented merge posture can drift away from reality again.
- ***What known edge cases or failure modes matter here?***
  - The docs gate must still keep `Docs and ADR delta` conditional on governed changes instead of requiring ADR churn for every PR, and the workflow matcher must stay broad enough to catch new workflow files without producing opaque failures.
- ***Why does this work matter?***
  - It closes the last D4 enforcement gap between the documented PR contract and the actual merge-blocking automation.
- ***What capability does it unlock?***
  - Reviewers can rely on every PR carrying a real summary and verification story, and workflow edits now consistently trigger the protected-path review path.
- ***Why is the chosen design safer or more scalable?***
  - Extending the existing D4 workflows keeps the logic in the same audited homes, preserves clear failure messages, and automatically covers future workflow files without another policy split.
- ***What trade-off did the team accept?***
  - More PRs will now fail fast on incomplete narrative or workflow-acknowledgement details, so contributors must keep the template sections and protected-path notes up to date before review.

---

### S0-D4 - Align the OpenCode bash allowlist with the CLI commands the repo actually needs

- ***What was built?***
  - `opencode.json` now explicitly allows `printf *` and the spaced `git log *` matcher that the current repo-control workflows already rely on.
- ***Why was it chosen?***
  - The shell allowlist had drifted from the real command shapes the governed repo-control flow uses, which could block valid local automation or force awkward command rewrites.
- ***What boundaries does it own?***
  - OpenCode bash-command permissions for low-risk local inspection helpers that PM and repo-control workflows need during governed execution.
- ***What breaks if it changes?***
  - Valid local command paths can be denied unexpectedly, and repo-control automation can drift toward less direct shell patterns just to satisfy stale permission rules.
- ***What known edge cases or failure modes matter here?***
  - The allowlist must stay narrow; adding broad shell permissions would weaken guardrails, while overly specific stale patterns would keep breaking legitimate commands.
- ***Why does this work matter?***
  - It keeps the tool policy aligned with the commands the repo actually expects during governed execution.
- ***What capability does it unlock?***
  - PM and related repo-control flows can keep using the expected `git log` and formatting paths without permission mismatches.
- ***Why is the chosen design safer or more scalable?***
  - Small, explicit allowlist repairs preserve the deny-by-default posture while reducing avoidable friction in everyday governed workflows.
- ***What trade-off did the team accept?***
  - The repo must keep reviewing shell-allowlist changes carefully because even tiny permission edits affect operator behavior across the tool surface.

---

### S0-D4 - Rename the root legal files to explicit markdown filenames and repair the repo references

- ***What was built?***
  - The root legal docs now live as `LICENSE.md` and `NOTICE.md`, and the matching repo references in `README.md`, `SECURITY.md`, `GOVERNANCE.md`, `CLA.md`, and planning docs were updated to the new explicit markdown filenames.
- ***Why was it chosen?***
  - The repo already treats these as markdown documents, so the filename change keeps the root legal surfaces explicit and prevents broken links after the human rename landed.
- ***What boundaries does it own?***
  - Root legal-document naming, the canonical repo references to those files, and the planning-tree examples that describe the committed repo shape.
- ***What breaks if it changes?***
  - Root docs and planning material can point at missing files, contributors can miss the canonical legal text, and the repo can drift between actual filenames and documented references.
- ***What known edge cases or failure modes matter here?***
  - The rename must keep every root-policy reference aligned at once; partial link updates would leave the repo in a broken but plausible state.
- ***Why does this work matter?***
  - It keeps the legal boundary readable and prevents contributor-facing docs from pointing at stale filenames after the rename.
- ***What capability does it unlock?***
  - Later legal or governance updates can treat the markdown files as the stable homes without carrying filename ambiguity forward.
- ***Why is the chosen design safer or more scalable?***
  - Explicit markdown filenames match the repo’s document surfaces, reduce broken-link risk, and make future doc tooling behavior easier to explain.
- ***What trade-off did the team accept?***
  - Existing references had to be updated together, so even a small rename carried cross-doc coordination cost.

---

### S0-D4 - Replace the misleading pages deploy stub with honest release-preparation scaffolding

- ***What was built?***
  - `.github/workflows/cd.yml` now runs `tools/script/release.py --ci prepare`, `tools/script/release.py` emits release-readiness metadata without deploying anything, and the old Pages deploy workflow was retired so D4 no longer implies D5-level delivery maturity.
- ***Why was it chosen?***
  - The repo needed a visible release-control seam in Sprint 0, but the existing Pages deploy workflow oversold deployment maturity and hid too much behavior in YAML.
- ***What boundaries does it own?***
  - Manual release-preparation control flow, honest release-readiness messaging, and the boundary that D4 prepares releases while D5 will own real rollout behavior.
- ***What breaks if it changes?***
  - Reviewers and operators can mistake release scaffolding for a real deployment pipeline, workflow names can promise runtime behavior the repo does not own yet, and future rollout work can lose one obvious place to start from.
- ***What known edge cases or failure modes matter here?***
  - The workflow must stay manual-only, the script must reject deploy requests clearly, and later D5 work must extend this seam instead of reintroducing a second release path.
- ***Why does this work matter?***
  - It gives the repo a truthful release-control checkpoint before runtime parity exists, which keeps CI/CD vocabulary aligned with actual repo maturity.
- ***What capability does it unlock?***
  - Later D5 rollout work can extend one named release seam instead of starting from a misleading Pages deployment stub.
- ***Why is the chosen design safer or more scalable?***
  - A thin workflow wrapper plus one script seam keeps release policy explainable, reviewable, and easy to roll back while the platform story is still forming.
- ***What trade-off did the team accept?***
  - The repo now has a release workflow that intentionally stops short of deployment, so operators must accept a more modest but honest control loop until D5 lands.

---

### S0-D4 - Add a dedicated reporter lane and a local coordination reminder loop

- ***What was built?***
  - `.opencode/agents/reporter.md` now defines a packet-only coordination lane, PM can route packet normalization to it, and `tools/script/coordination_status.py` now exposes a local `watch` runner that reuses the shared reminder runtime every minute instead of creating a second coordination engine.
- ***Why was it chosen?***
  - D4 needed stronger progress-report automation, but adding another script or machine-specific scheduler artifact would have split coordination logic and made local-only reporting harder to explain and review.
- ***What boundaries does it own?***
  - Reporter-owned packet normalization, the PM handoff boundary for coordination formatting, and the local reminder loop that surfaces overdue scopes while keeping all coordination policy inside `tools/script/coordination_status.py`.
- ***What breaks if it changes?***
  - PM and subagents can drift into competing packet formats, overdue scopes can stop surfacing consistently, and local operators can lose the one obvious entrypoint for recurring coordination checks.
- ***What known edge cases or failure modes matter here?***
  - The reporter lane must stay narrow enough that it never takes PM orchestration ownership, the watch loop must stay honest about being local-only, and overdue output must remain per-scope so one stale workstream does not hide another healthy one.
- ***Why does this work matter?***
  - It turns the coordination packet into a first-class repo-control contract and gives active work a repeatable local reminder loop before more agents or workstreams overlap.
- ***What capability does it unlock?***
  - Later scopes can reuse one normalized reporting lane and one minute-level reminder loop instead of rebuilding coordination format or scheduling behavior ad hoc.
- ***Why is the chosen design safer or more scalable?***
  - Reusing the shared coordination runtime keeps policy in one home, reduces drift across PM and subagents, and lets local schedulers call one stable command instead of proliferating wrappers.
- ***What trade-off did the team accept?***
  - Operators still need to choose how to launch the local reminder loop on their machines, so the repo documents safe entrypoints without pretending a committed machine-specific scheduler file would generalize cleanly.

---

### S0-D4 - Separate docs, protected-path, and CLA gates into explicit pull-request workflows

- ***What was built?***
  - `.github/workflows/docs-guard.yml`, `.github/workflows/protected-paths.yml`, and the updated `.github/workflows/cla-check.yml` now enforce docs and ADR coverage for governed changes, protected-path acknowledgement for high-blast-radius files, and the repository-owner CLA exception already documented in `CLA.md`.
- ***Why was it chosen?***
  - D4 needed merge-blocking automation for reviewer-visible PR obligations, but folding every rule into `repo-verify.yml` or `tools/script/verify.py` would have blurred ownership and made the workflow surface harder to explain.
- ***What boundaries does it own?***
  - Pull-request body contract enforcement for docs and ADR deltas, protected-path acknowledgement across repo-control workflows and the other protected-path categories named in `AGENTS.md`, and CLA phrase handling for outside contributors versus repository-owner-authored PRs.
- ***What breaks if it changes?***
  - Governed repo-control changes can land without durable reasoning, protected files can merge without explicit risk acknowledgement, or the CLA gate can block the wrong authors.
- ***What known edge cases or failure modes matter here?***
  - The workflows must use the repo's exact protected-path vocabulary, distinguish repo-control workflows from true release scaffolding, avoid treating `docs/coordination/**` as a merge target, and keep the owner exception narrow enough that outside contributors still need the exact phrase from `CLA.md`.
- ***Why does this work matter?***
  - It turns the PR template obligations into explicit merge gates instead of leaving docs, protected-path notes, and CLA nuance to reviewer memory.
- ***What capability does it unlock?***
  - Later sprint work can rely on clear PR-level guardrails for governed changes before release scaffolding and runtime parity work land.
- ***Why is the chosen design safer or more scalable?***
  - Separate workflows keep each gate explainable, reduce policy overlap with the central repo verifier, and make later changes easier to review and roll back.
- ***What trade-off did the team accept?***
  - The repo now carries more workflow files and PR-body contract logic, so later governance edits must keep the template, docs, and workflow checks aligned.

---

### S0-D4 - Keep repo verification policy in one central script seam

- ***What was built?***
  - `tools/script/verify.py`, `.github/workflows/repo-verify.yml`, and `docs/testing.md` were aligned so merge-blocking repo verification stays owned by one central Python entrypoint and the workflow remains a thin CI wrapper around it.
- ***Why was it chosen?***
  - D4 needs automation that blocks bad changes before merge, but pushing policy logic into YAML would duplicate rules, hide failure reasoning, and make later workflow slices harder to review.
- ***What boundaries does it own?***
  - The shared repo-verification seam for script explainability, central workflow delegation, and CI-safe local-versus-CI behavior.
- ***What breaks if it changes?***
  - The repo-verify workflow can drift into a second policy engine, contributors can get inconsistent failure output, and later D4 workflows can start re-implementing checks in parallel.
- ***What known edge cases or failure modes matter here?***
  - CI checkouts do not include local-only coordination artifacts, so the verifier must keep that case explicit, and the workflow must stay thin enough that docs-guard and protected-path slices can add separate enforcement without overlap.
- ***Why does this work matter?***
  - It keeps D4 automation explainable and preserves one obvious place to extend repo verification as the governed rebuild grows.
- ***What capability does it unlock?***
  - Later workflows can compose around a stable central verifier instead of guessing which checks belong in Python versus YAML.
- ***Why is the chosen design safer or more scalable?***
  - A single verifier seam reduces duplicate policy, keeps failure messaging consistent, and lowers the review burden when later quality gates land.
- ***What trade-off did the team accept?***
  - The repo verifier now owns a clearer contract with CI, so later changes to `.github/workflows/repo-verify.yml` must preserve that thin-wrapper boundary instead of treating the workflow as a general automation scratchpad.

---

### S0-D4 - Standardize the PR review contract and centralize the CLA owner exception

- ***What was built?***
  - The D4 planning packet, `.github/pull_request_template.md`, `.opencode/commands/pr-prepare.md`, `CLA.md`, and `CONTRIBUTING.md` were aligned around one reviewer-facing PR structure, one canonical CLA confirmation phrase, and one documented repository-owner exception for the CLA phrase check.
- ***Why was it chosen?***
  - The repo already had partial PR and CLA guidance, but the template, PR-prep command, and contributor docs could drift from each other and force workflow automation to guess which wording was canonical.
- ***What boundaries does it own?***
  - Reviewer-facing PR narrative structure, canonical CLA confirmation wording, and the documentation boundary between outside contributors and repository-owner-authored PRs.
- ***What breaks if it changes?***
  - PR preparation can produce the wrong sections, workflow automation can block the wrong authors, and reviewers can lose a stable contract for summary, verification, docs, and protected-path notes.
- ***What known edge cases or failure modes matter here?***
  - Owner-authored PRs need a narrow exception without weakening the CLA requirement for outside contributors, and the PR template plus PR-prep command must stay structurally identical enough to avoid future drift.
- ***Why does this work matter?***
  - It gives the later D4 workflow changes one durable policy source instead of scattering PR and CLA semantics across markdown files, chat, and YAML.
- ***What capability does it unlock?***
  - Later automation can enforce PR structure and CLA rules against a stable documented contract.
- ***Why is the chosen design safer or more scalable?***
  - Centralizing the policy details reduces duplicate rule text and makes later workflow or script changes easier to audit for drift.
- ***What trade-off did the team accept?***
  - The repository now carries a slightly more explicit PR and CLA narrative, which requires future repo-control edits to keep the shared structure in sync.

---

### S0-D3 - Reconcile planning drift to current repo reality

- ***What was built?*** 
  - A repo-control rule set that treats the committed permanent structure as canonical when older planning packets drift, including updates in `AGENTS.md`, `docs/repo.md`, `README.md`, `.opencode/commands/generate.md`, `.opencode/commands/orchestrate.md`, and `docs/planning/sprint-0/d3-agent-docs.md`.
- ***Why was it chosen?*** 
  - The repo had already converged on permanent control surfaces, so recreating packet-era names would have duplicated governance files and pushed agents toward stale targets.
- ***What boundaries does it own?*** 
  - Planning translation, durable-doc stubbing decisions, and repo-control path selection across the active rebuild surfaces.
- ***What breaks if it changes?*** 
  - Agents can start generating duplicate files, reviving stale packet-era homes, or describing the active tree inaccurately during planning and execution.
- ***What known edge cases or failure modes matter here?*** 
  - A planning packet can still differ materially from the repo in ways that affect ownership or safety; those cases must escalate instead of being silently normalized.
- ***Why does this work matter?*** 
  - It keeps the rebuild honest about what is already real in the repo and prevents governance drift from compounding with each later deliverable.
- ***What capability does it unlock?*** 
  - Safe refinement of planning docs and agent execution without throwing away already-committed permanent structure.
- ***Why is the chosen design safer or more scalable?*** 
  - Reusing the committed structure reduces duplicate homes, review ambiguity, and agent confusion as more lanes work in parallel.
- ***What trade-off did the team accept?*** 
  - Older planning language now needs periodic reconciliation instead of being treated as immutable even after the repo evolves.

---

### S0-D3 - Make the implementation workflow architect-first and ops-gated

- ***What was built?*** 
  - The governed lane order now requires `architect` before `developer` or `designer` on implementation-bearing task scopes, and `ops` after reviewer and integrator but before librarian closeout, PR prep, or merge-ready status.
- ***Why was it chosen?*** 
  - Implementation strategy and operational hygiene were too easy to skip when the workflow jumped straight from PM framing into coding or docs closeout.
- ***What boundaries does it own?*** 
  - Task-scope execution order, TDD and scaffolding handoff expectations, and the operational review gate for implementation-bearing diffs.
- ***What breaks if it changes?*** 
  - Boilerplate can be designed ad hoc inside developer patches, and review can miss reliability, blast-radius, or workflow-hygiene issues such as leaked local runtime artifacts.
- ***What known edge cases or failure modes matter here?*** 
  - Docs-only tasks can bypass architect and ops, but implementation-bearing tasks cannot; the workflow must keep that distinction explicit.
- ***Why does this work matter?*** 
  - It turns architecture and operations review from best-effort habits into deterministic gates the human can rely on.
- ***What capability does it unlock?*** 
  - TDD-shaped implementation handoffs, earlier failure-mode thinking, and consistent ops checks before work is treated as mergeable.
- ***Why is the chosen design safer or more scalable?*** 
  - As more lanes contribute in parallel, explicit sequencing reduces hidden assumptions and catches operational drift before humans clean it up manually.
- ***What trade-off did the team accept?*** 
  - The path to merge-ready status becomes slightly longer because implementation-bearing work must clear more explicit gates.

---

### S0-D3 - Consolidate the governed repo-control surface under root and `.opencode/`

- ***What was built?*** 
  - `AGENTS.md`, `opencode.json`, `.opencode/agents/**`, `.opencode/commands/**`, `.opencode/rules/**`, and `.opencode/skills/**` were established or aligned as the canonical control surface for lane behavior, permissions, routing, and review expectations.
- ***Why was it chosen?*** 
  - A governed multi-agent rebuild needs one durable operating contract instead of scattered instructions hidden in chat or one-off notes.
- ***What boundaries does it own?*** 
  - Repo-level agent permissions, lane responsibilities, orchestration commands, reusable rules, and reusable skills for active rebuild work.
- ***What breaks if it changes?*** 
  - Humans and agents lose a shared source of truth for safe paths, coordination cadence, review gates, and escalation behavior.
- ***What known edge cases or failure modes matter here?*** 
  - Hotspot-file wording changes act like behavior changes, so small text edits can materially alter how agents execute or escalate work.
- ***Why does this work matter?*** 
  - It makes the operating theory inspectable, reviewable, and reusable instead of depending on conversational memory.
- ***What capability does it unlock?*** 
  - Deterministic routing, reusable commands, and permission-aware lane behavior that later sprints can extend safely.
- ***Why is the chosen design safer or more scalable?*** 
  - Centralized repo-control docs reduce rule duplication and help parallel contributors inherit the same behavioral contract.
- ***What trade-off did the team accept?*** 
  - The repo now carries heavier governance documentation that must be kept current as behavior evolves.

---

### S0-D3 - Standardize live coordination cadence and stable scope artifacts

- ***What was built?*** 
  - The coordination system now uses stable scope-based files, a shared six-minute reporting packet, dashboard refresh rules, and reusable templates under `docs/templates/coordination/**` with matching guidance in `.opencode/rules/coordination-standards.md`.
- ***Why was it chosen?*** 
  - Parallel human and agent work becomes hard to resume safely when status lives only in chat or in ad hoc filenames.
- ***What boundaries does it own?*** 
  - Coordination artifact naming, heartbeat cadence, shared status packet fields, and the human-visible active dashboard rules.
- ***What breaks if it changes?*** 
  - Resume and handoff flows become non-deterministic, and later agents must reconstruct state from chat archaeology.
- ***What known edge cases or failure modes matter here?*** 
  - Coordination files are gitignored live artifacts, so they must stay stable enough to resume work even though they are not durable merge history.
- ***Why does this work matter?*** 
  - It keeps in-flight work visible and reduces the risk that a later agent or human misses blockers, active paths, or the next checkpoint.
- ***What capability does it unlock?*** 
  - Reliable resume, handoff, and checkpoint behavior across scoped tasks and deliverables.
- ***Why is the chosen design safer or more scalable?*** 
  - Stable naming and repeated packet fields make coordination machine-readable and human-scannable at the same time.
- ***What trade-off did the team accept?*** 
  - Agents must spend time updating coordination artifacts during work instead of treating status as optional overhead.

---

### S0-D3 - Seed the durable docs spine for architecture, agent workflow, testing, operations, and ADRs

- ***What was built?*** `docs/architecture.md`, `docs/agent.md`, `docs/testing.md`, `docs/operations.md`, and `docs/adr.md` were created as the permanent technical-doc surfaces that later changes must extend in place.
- ***Why was it chosen?*** 
  - Shared theory was going to fragment across PR text and chat unless the rebuild established exact durable homes early.
- ***What boundaries does it own?*** 
  - Cross-cutting technical explanation, workflow narrative, testing posture, operations posture, and the single consolidated ADR record.
- ***What breaks if it changes?*** 
  - Contributors start inventing side-channel docs, and reviewers lose a stable place to confirm the current architecture and operating theory.
- ***What known edge cases or failure modes matter here?*** 
  - Stub docs can become misleading if they overclaim current repo maturity, so they must stay thin until later deliverables add concrete runtime detail.
- ***Why does this work matter?*** 
  - It gives every later change a permanent home for shared understanding instead of making documentation optional cleanup.
- ***What capability does it unlock?*** 
  - ADR-coupled delivery and durable technical explanation that can keep pace with the rebuild.
- ***Why is the chosen design safer or more scalable?*** 
  - Extending one durable doc spine is easier to review and maintain than chasing many ad hoc notes across the repo.
- ***What trade-off did the team accept?*** 
  - Some docs are intentionally skeletal now and need disciplined later extension rather than one-shot completion.

---

### S0-D2 - Seed durable runtime starter files under `apps/`

- ***What was built?*** 
  - Permanent starter files were seeded for the active runtime homes under `apps/web`, `apps/api`, `apps/domain`, `apps/worker`, and `apps/agent`, with TL;DR headers and narrow boundary narratives.
- ***Why was it chosen?*** 
  - The rebuild needed one obvious home for each deployable surface before feature work could begin without path drift.
- ***What boundaries does it own?*** 
  - Deployable runtime ownership for the experience, contract, domain, worker, and agent surfaces of the active rebuild tree.
- ***What breaks if it changes?*** 
  - Later work can splinter across duplicate app roots or treat the prototype archive as the path of least resistance.
- ***What known edge cases or failure modes matter here?*** 
  - Stub files must stay TL;DR-only until real implementation lands, otherwise comments and fake boilerplate turn into explainability debt.
- ***Why does this work matter?*** 
  - It creates real extension points for later sprints instead of leaving ownership implied.
- ***What capability does it unlock?*** 
  - Safe Sprint 1+ implementation work that can extend existing runtime homes instead of inventing parallel structures.
- ***Why is the chosen design safer or more scalable?*** 
  - Stable starter files reduce future relocation churn and make ownership visible before business logic arrives.
- ***What trade-off did the team accept?*** 
  - The repo carries many thin stub files early so later work can grow in place without renaming or moving foundational paths.

---

### S0-D2 - Seed shared seam starter files under `shared/`

- ***What was built?*** 
  - Permanent starter files were created for shared contracts, schemas, adapters, and deterministic test support under `shared/contract`, `shared/schema`, `shared/adapter`, and `shared/testkit`.
- ***Why was it chosen?*** 
  - Cross-cutting concepts needed one shared home before app-local implementations started duplicating schema, adapter, or test vocabulary.
- ***What boundaries does it own?*** 
  - Shared transport primitives, reusable shape definitions, swappable capability ports, and deterministic support for future verification layers.
- ***What breaks if it changes?*** 
  - Contract and adapter concepts can leak into app-local folders, creating duplicate ownership and harder refactors.
- ***What known edge cases or failure modes matter here?*** 
  - Shared seams can become junk drawers if later work adds vague helpers instead of capability-based surfaces.
- ***Why does this work matter?*** 
  - It gives the rebuild one place to centralize concepts that genuinely cross runtime boundaries.
- ***What capability does it unlock?*** 
  - Reuse-first implementation across apps without forcing every runtime surface to define its own duplicate vocabulary.
- ***Why is the chosen design safer or more scalable?*** 
  - A single shared seam layer makes later contract, adapter, and testing evolution more reviewable and less repetitive.
- ***What trade-off did the team accept?*** 
  - Shared surfaces now need stricter review so they stay capability-based instead of becoming generic dumping grounds.

---

### S0-D1 - Freeze the validated prototype under `legacy-v0/`

- ***What was built?*** 
  - The old runtime tree was relocated under `legacy-v0/` and documented as preserved reference material rather than the active base for the rebuild.
- ***Why was it chosen?*** 
  - The prototype had already validated the product loop, but scaling it in place would have carried forward ambiguous ownership and prototype-era coupling.
- ***What boundaries does it own?***
  -  The archival boundary between historical proof and active rebuild work.
- ***What breaks if it changes?*** 
  - Contributors can mistake the prototype for the active architecture and keep adding new work to archived paths.
- ***What known edge cases or failure modes matter here?***
  -  Useful ideas still exist in the archive, but they must be ported deliberately instead of extended in place.
- ***Why does this work matter?*** 
  - It preserves the evidence of what already worked while clearing the root for a more intentional rebuild.
- ***What capability does it unlock?*** 
  - Later sprint work can reference the prototype without being trapped by its structure.
- ***Why is the chosen design safer or more scalable?*** 
  - A hard archive boundary prevents legacy coupling from quietly reentering active development.
- ***What trade-off did the team accept?*** 
  - Anyone reusing prototype ideas now has to do explicit extraction work instead of shortcutting through the old folders.

---

### S0-D1 - Rewrite the repo narrative around active versus archived paths

- ***What was built?*** 
  - `README.md`, `docs/repo.md`, `docs/legacy-v0.md`, and `legacy-v0/README.md` were rewritten so the root tells a single story about the active rebuild surfaces and the archived prototype.
- ***Why was it chosen?*** 
  - Moving files alone would not have been enough if the repo narrative still implied that the prototype layout was active.
- ***What boundaries does it own?*** 
  - Contributor guidance, root navigation, path-ownership language, and the shared terminology for archive versus rebuild surfaces.
- ***What breaks if it changes?*** 
  - New humans and agents can still infer the wrong build path even if the filesystem technically contains the right folders.
- ***What known edge cases or failure modes matter here?*** 
  - Narrative docs can drift from repo reality if later structural changes are not reflected in the same durable guidance files.
- ***Why does this work matter?*** 
  - It makes path ownership explicit enough that a contributor can choose the right surface without external explanation.
- ***What capability does it unlock?*** 
  - Safer onboarding and safer agent planning because the repo tells the truth about where new work belongs.
- ***Why is the chosen design safer or more scalable?*** 
  - Shared terminology across root docs reduces ambiguous guidance as more durable docs and active surfaces are added.
- ***What trade-off did the team accept?*** 
  - Repo narrative docs now require deliberate upkeep whenever governance or structure changes.
