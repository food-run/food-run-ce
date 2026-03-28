---
description: Orchestrate a sprint, deliverable, or task deterministically from scope, action, and run policy
agent: pm
---
# Orchestrate Command

## TL;DR

This is the main workflow entrypoint for planning, resuming, executing, and reviewing scoped work. Reuse stable coordination state whenever possible, invoke only the minimum necessary subagents, parallelize only when it is clearly safe, continue until the requested scope is complete or a real stop condition is reached, and enforce `.opencode/rules/coordination-standards.md`.

## Inputs

- `$1` = scope ID
- `$2` = action
- `$3` = run policy
- `$ARGUMENTS` = optional extra planning or context files

## Accepted Scope Formats

- `S<number>` = sprint scope
- `S<number>-D<number>` = deliverable scope
- `S<number>-D<number>-T<number>` = task scope

Examples:

- `S0`
- `S0-D1`
- `S0-D1-T2`

## Accepted Actions

- `plan`
- `resume`
- `execute`
- `review`

If `$2` is omitted, default to `resume`.

## Accepted Run Policies

- `single` = do one bounded child unit and stop
- `complete` = keep advancing through remaining child units until the requested scope is complete or a stop condition is reached

If `$3` is omitted:

- default to `single` for task scope
- default to `complete` for deliverable and sprint scope

## Scope

- Scope ID: `$1`
- Action: `$2`
- Run Policy: `$3`
- Extra context: `$ARGUMENTS`

## Required Skills

Load these skills at the right times:

- `scope-router`
- `coordination-state`
- `parallel-lane-policy`

Also load when helpful:

- `planning-reader`
- `protected-paths`
- `drift-check`
- `review-rubric`
- `frontend-first-principles` for UI or UX implementation planning and execution
- `ui-ux-review` for UI or UX review passes

## Planning-File Policy

Always use:

- `AGENTS.md`

Then open only the smallest planning set needed.

### Sprint scope

Open:

- `docs/planning/master-packet.md`
- `docs/planning/sprint-<n>/overview.md`

### Deliverable scope

Open:

- `docs/planning/sprint-<n>/overview.md`
- the single matching deliverable file for that scope

### Task scope

Open:

- the parent deliverable file only

### Extra context

Also open any explicitly passed extra files in `$ARGUMENTS`, but only if they are directly relevant.

Do not open the full master packet for deliverable or task scope unless:

- the user explicitly passes it
- a planning conflict requires escalation

## Stable Coordination-State Policy

Before routing, use `coordination-state` to look for existing state in this order:

1. `docs/coordination/tasks/$1.md`
2. `docs/coordination/tasks/<parent-scope>.md`
3. the newest matching scoped coordination artifact for the same scope
4. if none exist, create `docs/coordination/tasks/$1.md`

When scoped coordination artifacts exist but a stable scope file does not:

- create the stable scope file
- carry forward the latest valid state
- use the stable scope file from then on
- seed or refresh `docs/coordination/active.md` so humans can see live progress without opening chat history

All coordination filenames must follow `.opencode/rules/coordination-standards.md`.

## Reuse-First Rule

If stable coordination state already exists and still matches repo reality:

- `resume` must continue from that state
- `execute` must use that state as input
- `review` must use that state plus the current diff

Do **not** rerun Scout or Planner unless one of these is true:

- no stable packet exists for the scope
- the packet is incomplete
- the planning files changed materially
- the repo state invalidates the packet
- the human explicitly requests fresh discovery or replanning

When the planning packet and the committed repo differ:

- treat the current committed permanent structure as canonical by default
- refine the packet to match repo reality instead of recreating stale packet-era file names
- stub a missing durable doc only when the exact permanent home is absent and the expected content is not already sufficiently covered elsewhere
- escalate only if the committed repo and planning packet differ in a way that materially changes ownership, safety, or scope

## Branch Rule

Before implementation begins for a deliverable or task scope:

- create or switch to the scoped working branch if it is not already active
- verify `git branch --show-current` matches the intended work unit branch
- keep tracked implementation changes and checkpoint commits on that branch until the scope closes

## Routing Matrix

### Sprint Scope

#### `plan`

1. scout
2. planner
3. stop with:
   - sprint summary
   - deliverable order
   - blockers
   - first recommended deliverable

#### `resume`

1. load sprint packet
2. if missing or stale, run sprint `plan`
3. identify next incomplete deliverable
4. if run policy is `single`, stop with the next recommended deliverable
5. if run policy is `complete`, continue into that deliverable using deliverable rules

#### `execute`

1. load sprint packet
2. identify next incomplete deliverable
3. for each deliverable in dependency order:
   - plan it only if needed
   - execute it
   - review it
   - update sprint state
   - update user in the chat
4. continue until:
   - sprint complete
   - blocker
   - approval gate
   - planning conflict
   - stop condition

#### `review`

1. reviewer
2. integrator
3. ops for implementation-bearing work
4. librarian if durable sprint docs changed
5. final sprint status

### Deliverable Scope

#### `plan`

1. scout
2. planner
3. use `parallel-lane-policy`
4. split into async-safe lanes only if clearly safe
5. stop with:
   - deliverable packet
   - task order
   - async-safe split
   - blockers
   - next recommended task

#### `resume`

1. load deliverable packet
2. if missing or stale, run deliverable `plan`
3. identify next incomplete task
4. if run policy is `single`, stop with the next recommended task
5. if run policy is `complete`, continue into that task using task rules

#### `execute`

1. load deliverable packet
2. identify next incomplete task
3. execute one task at a time unless `parallel-lane-policy` explicitly approves safe fan-out
4. after each task:
    - reviewer
    - integrator
    - ops before librarian whenever implementation-bearing work passed review and integration
    - apply `.opencode/rules/coordination-standards.md`
    - run repo-wide DRYness review before treating the task as done
    - evaluate checkpoint readiness against the commit rhythm rule
    - route `checkpoint-commit` before continuing when the diff is a stable rollback point
   - librarian if durable docs changed
   - update deliverable state
   - update the user in the chat
5. continue until:
   - deliverable complete
   - blocker
   - approval gate
   - planning conflict
   - stop condition

#### `review`

1. reviewer
2. integrator
3. ops for implementation-bearing work
4. librarian if durable docs changed
5. final deliverable status

### Task Scope

#### `plan`

1. load task packet
2. scout only if grounding is missing
3. planner only if decomposition is missing
4. if the task includes UI or UX implementation, open the relevant `docs/design-system/**` files before shaping the packet
5. architect only if implementation-bearing strategy, TDD shape, or scaffolding guidance is missing
6. stop with a bounded execution packet

#### `resume`

1. load task packet
2. if missing or stale, run task `plan`
3. continue from the next unfinished lane

#### `execute`

1. restate:
   - exact objective
   - exact boundaries
   - non-goals
   - active paths
   - protected paths
   - ⚠️ Hotspot Files
2. if the task includes UI or UX implementation, confirm the relevant `docs/design-system/**` files are part of the active planning set
3. if the task is implementation-bearing, route `architect` first to define invariants, failure modes, TDD shape, and scaffolding
4. choose exactly one implementation lane from the architect handoff:
   - `designer` for any UI or UX implementation work
   - `developer` for non-UI code, structure, relocations, tests
   - `librarian` for docs-only work when no implementation lane is needed
5. reviewer, using `ui-ux-review` when the diff includes UI or UX surfaces
6. integrator
7. ops for implementation-bearing work before any librarian closeout
8. apply `.opencode/rules/coordination-standards.md`
9. run repo-wide DRYness review before marking the task complete
10. if the task produced a stable checkpoint, route `checkpoint-commit` before advancing or closing the task
11. librarian only if durable docs changed
12. final task status

#### `review`

1. reviewer
2. integrator
3. ops for implementation-bearing work
4. librarian if docs changed
5. final task status

## Parallelism Policy

Before any async fan-out, use `parallel-lane-policy`.

Parallelize only when all of these are true:

- scope is sprint or deliverable level
- path overlap is low
- protected paths are not involved
- ⚠️ Hotspot File overlap is low
- the split is already defined as safe

If any of those are false, sequence the work.

## Always Do These

At the end of the run:

- update the stable coordination file
- refresh `docs/coordination/active.md`
- state whether a checkpoint commit is due, completed, or intentionally deferred
- state whether `.opencode/rules/coordination-standards.md` was satisfied
- state what was reused, created, refactored, and deferred for later consolidation
- state whether branch hygiene and checkpoint rhythm were satisfied
- mention planning files opened
- mention active paths
- mention protected paths
- mention ⚠️ Hotspot Files
- mention blockers
- mention next recommended agent
- mention next recommended command

## Stop Conditions

Stop immediately if any of these are true:

- the requested scope is complete
- a protected path needs explicit approval
- the planning packet and repo state conflict materially
- the coordination packet is invalid and cannot be safely repaired
- the next child scope would broaden beyond the requested scope
- a human decision is required
- review rejected the current diff and rework is required first

## Output Contract

Every run must end with:

- Scope
- Action
- Run Policy
- Planning files opened
- Coordination packet used or created
- What changed
- What is next
- Current blockers
- Human decisions needed
- Recommended next agent
- Recommended next command
