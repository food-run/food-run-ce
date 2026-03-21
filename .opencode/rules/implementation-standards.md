# Implementation Standards

## TL;DR

Implement narrowly, reuse before inventing, keep boundaries stable, and leave work easy to explain, review, and roll back. The repository must be deeply technical, well documented, and structured around exact permanent files rather than placeholders. Script-like files and automation surfaces must follow the team’s canonical TL;DR header and comment style from the first line. DRYness is a mandatory preflight and closeout gate, not optional cleanup.

## Index

- [📌 Core Principles](#-core-principles)
- [🗂️ Documentation and File-Creation Rules](#️-documentation-and-file-creation-rules)
- [🏷️ Naming Rules](#️-naming-rules)
- [🧱 Path and Ownership Rules](#-path-and-ownership-rules)
- [💬 Commenting and Scripting Style](#-commenting-and-scripting-style)
- [♻️ DRYness Gates](#️-dryness-gates)
- [📝 TODO Rules](#-todo-rules)
- [🧪 Verification Rules](#-verification-rules)
- [✅ Completion Checklist](#-completion-checklist)
- [🧾 Commit and Coordination Rules](#-commit-and-coordination-rules)
- [🚨 Escalate Instead of Guessing](#-escalate-instead-of-guessing)

## 📌 Core Principles

- keep diffs small and coherent
- prefer reuse over invention
- choose clear ownership over convenience
- optimize for explainability, not cleverness
- preserve active-vs-legacy boundaries
- make the first version of a file look like the permanent version of that file, not a throwaway scaffold
- keep comments DRY and useful instead of noisy or repetitive
- treat reuse and consolidation as review gates, not as optional cleanup

## 🗂️ Documentation and File-Creation Rules

- the entire repository must be well documented
- deep technical documentation belongs in `docs/**`
- do not create generic placeholder files such as throwaway `.md`, `.txt`, or “notes” files just to reserve a folder
- always stub the first exact permanent file that the folder will need first
- if the exact permanent file cannot be named yet, omit the folder entirely until it can
- documentation exceptions are allowed only for repository-control and agentic-IDE surfaces such as:
  - `AGENTS.md`
  - `.opencode/**`
  - other repository-control files explicitly used by OpenCode or the repository workflow

### File-Stubbing Rule

Correct:

- create `docs/repo.md` if that is the real first permanent document for the folder
- create `apps/api/main.py` if that is the real startup surface
- create `tools/script/verify.py` if that is the real first automation surface

Incorrect:

- `placeholder.md`
- `notes.txt`
- `temp.md`
- generic “overview” files where a more exact permanent file should exist instead

## 🏷️ Naming Rules

### General Naming Standard

- use exact semantic names
- prefer 1–2 words
- use 4 words maximum
- prefer concept-first names over framework-heavy names
- avoid vague names like:
  - `helpers`
  - `misc`
  - `stuff`
  - `temp`
  - `manager` unless it is the true domain term
  - `util` or `utils` unless already standardized and truly necessary

### Applies To

Use this naming standard for:

- files
- folders
- functions
- variables
- constants
- commands
- skills
- coordination artifacts
- generated surfaces

### Function and Variable Rules

- function names should describe one real responsibility
- variable names should describe the real data or state they hold
- avoid abbreviations unless they are already standard in the repository or domain
- avoid raw implementation-detail names when a domain or boundary name is clearer

## 🧱 Path and Ownership Rules

- new implementation belongs only in active rebuild paths, never in `legacy-v0/`
- keep one home per concept
- avoid junk-drawer roots and vague shared buckets
- stop and escalate if ownership is ambiguous
- present additions within the file groups they belong to
- use section groups to make extension seams explicit from the first implementation

## 💬 Commenting and Scripting Style

This section applies to any file that allows comments, excluding Markdown files.

### High-Level Standard

- every comment-capable file must be meaningfully documented
- comments must stay DRY
- comments should explain ownership, boundary, runtime flow, extension seams, non-obvious logic, and strategic intent
- comments should make skimming possible without forcing humans to infer hidden reasoning
- implemented files should feel heavily commented without collapsing into repetitive noise

### Canonical TL;DR Header Rule

Only the TL;DR section may use a multi-line comment syntax.

The TL;DR block must:

- use `TL;DR` in all caps
- be wrapped with `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
- appear at the top of the file
- be the only multi-line comment block in the file
- include these sections in this order:
  - `TL;DR  -->`
  - `- Later Extension Points:`
  - `- Role:`
  - `- Exports:`
  - `- Consumed By:`

### Stub File Rule

A stub-only file with no actual implementation may stop after the TL;DR block.

Use this lighter stub shape when all of these are true:

- the file has no real runtime or business logic yet
- the file only reserves the permanent home for future work
- any remaining body line is only a minimal syntax keeper such as `export {}`

For stub-only files:

- do not add section headers below the TL;DR
- do not add body comments below the TL;DR
- do not add placeholder code just to justify comments
- keep the future seam described in the TL;DR instead

### Implemented File Rule

Once a file has actual implementation, it must use the heavy comment style.

Implemented files must:

- use section-group headers to divide major areas
- use one-line comments for sections, mini-groups, and non-obvious lines
- keep each comment line between 4 and 18 words when practical
- prefer one one-line comment above a mini-group when the intent is shared
- avoid repeating the same sentence on every line when a mini-group comment already explains the block
- keep inline end-of-line comments rare and only for tight local clarification

### Internal Comment Rule

All non-TL;DR comments must be single-line comments only.

Allowed forms:

- a single-line section header
- a single-line comment above a mini-group
- a single-line comment above an individual non-obvious line
- a short appended comment on the relevant code line when proximity matters

Not allowed:

- multi-line block comments outside the TL;DR
- stacked repetitive comments that restate obvious code
- long prose paragraphs inside code files

### Section Header Rule

Use section-group headers to divide large areas of implemented files.

Examples:

#### Python

    # ---------- runtime identity ----------
    # ---------- imports and dependencies ----------
    # ---------- parsing helpers ----------
    # ---------- verification checks ----------
    # ---------- entrypoint ----------

#### TypeScript / JavaScript

    // ---------- bootstrap ----------
    // ---------- shared constants ----------
    // ---------- request parsing ----------
    // ---------- runtime flow ----------
    // ---------- entrypoint ----------

### Comment Density Rule

- comment every major section
- comment every mini-group whose shared purpose is not obvious at a glance
- comment individual lines when the reasoning or strategy would otherwise stay implicit
- prefer comments above the relevant lines over trailing explanation chains
- keep comments short, concrete, and skimmable
- if several adjacent lines share one intent, use one mini-group comment instead of repeating the same note

### TODO Rule Inside Code

- unfinished, partial, cleanup, or deferred work must be marked with `TODO:`
- each TODO should say what is missing or why it is deferred
- do not leave vague TODOs like:
  - `TODO`
  - `TODO fix`
  - `TODO later`

Prefer:

- `# TODO: replace local stub with adapter-selected provider wiring once D3 lands`
- `// TODO: move this temporary parsing guard into shared schema validation when the contract freezes`

### Canonical Python Template

    """  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    TL;DR  -->  <plain-English file purpose>

    - Later Extension Points:
        --> <next seam>

    - Role:
        --> <why this file exists>
        --> <what boundary it owns>
        --> <what it must stay thin, explicit, or governed about>

    - Exports:
        --> <stable outward surface>

    - Consumed By:
        --> <direct current callers or operators>
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

    # ---------- <first implemented section> ----------

    # <one-line section or mini-group comment>

### Canonical TypeScript / JavaScript Template

    /*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    TL;DR  -->  <plain-English file purpose>

    - Later Extension Points:
      --> <next seam>

    - Role:
      --> <why this file exists>
      --> <what boundary it owns>
      --> <what it must stay thin, explicit, or governed about>

    - Exports:
      --> <stable outward surface>

    - Consumed By:
      --> <direct current callers or operators>
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

    // ---------- <first implemented section> ----------

    // <one-line section or mini-group comment>

### Review Rule for Comment Style

Treat any of the following as explainability debt:

- missing TL;DR header where this rule applies
- vague TL;DR content
- missing section-group headers in implemented script-like files
- missing body comments in implemented files whose logic is no longer self-explanatory
- comment spam
- trivial syntax narration
- multi-line comments outside the TL;DR
- body comments in stub-only files with no actual implementation
- missing TODO markers for knowingly incomplete work

## ♻️ DRYness Gates

DRYness is a mandatory review gate before implementation begins and again before a scope can be called complete.

### Preflight Gate

Before implementation starts:

- run a reuse scan for the relevant concept across the repository
- identify what can be reused directly
- identify what should be extended or refactored instead of duplicated
- justify any newly created structure as meaningfully unique for the current boundary

### Meaningfully Unique Means

New code or structure must differ in at least one real way that matters to the repository, such as:

- different deployable boundary or ownership
- different runtime or execution model
- different data contract or invariants
- different user-facing responsibility
- different protected-path or operational requirements

If the change is not meaningfully unique, refactor or reuse instead of adding another copy.

### Closeout Gate

Before a scope is called complete:

- PM must orchestrate a repository-wide DRYness review
- reviewer must check for duplicate logic, duplicate concepts, and duplicate homes across the repository
- if the result is not meaningfully unique, the scope is not complete and must refactor or retry first

### DRYness Non-Goals

- do not invent abstraction just to sound DRY
- do not broaden scope just to chase every possible consolidation
- do not approve near-duplicates without an explicit uniqueness reason

## 📝 TODO Rules

- use `TODO:` for cleanup, deferred work, or partial implementation
- keep TODOs specific and actionable
- place TODOs near the relevant section or line
- remove TODOs once the work is done
- do not use TODOs to hide ownership ambiguity or planning gaps that should be escalated now

## 🧪 Verification Rules

- pair meaningful implementation with the right level of verification
- leave review hotspots and rollback notes when risk is non-trivial
- keep docs and ADR context aligned when shared understanding changes
- check comment-style compliance during implementation and again during review closeout
- run the DRYness preflight gate before implementation
- run the DRYness closeout gate before declaring the scope complete

## ✅ Completion Checklist

Every completion or closeout summary must include:

- what was reused
- what was created
- what was refactored
- what should be consolidated elsewhere but is outside the current scope

A scope is not complete until all of these are true:

- ownership is clear
- new structure is meaningfully unique where added
- no avoidable duplicate homes were created
- comment-capable files follow the repo comment standard
- TODOs are explicit where work is partial or deferred
- verification is complete at the right level for the change
- durable docs or ADR context were updated when shared understanding changed

## 🧾 Commit and Coordination Rules

- stop at stable rollback points and recommend a checkpoint commit
- choose Conventional Commit scopes using the first qualifying parent surface
- prefer `coordination`, `templates`, or `opencode` when they cleanly fit the change
- fall back to `repo` only when no narrower context covers the diff
- if a checkpoint would need an overly broad `repo` scope, split it into smaller coherent slices before committing
- write commit subjects in clear English using 12–22 words
- avoid raw identifier names in the message
- do not batch unrelated work after a coherent checkpoint is ready
- keep `docs/coordination/` current as work progresses
- include reused, created, refactored, and deferred consolidation notes at closeout

## 🚨 Escalate Instead of Guessing

Escalate instead of guessing when you hit:

- protected-path edits
- planning conflicts
- unclear concept ownership
- scope that cannot remain narrow
- a file that does not yet have an exact permanent name
- comment-style uncertainty that would affect repository-wide consistency
- a DRYness conflict that would require broadening scope without approval
