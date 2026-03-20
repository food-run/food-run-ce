# Implementation Standards

## TL;DR

Implement narrowly, reuse before inventing, keep boundaries stable, and leave work easy to explain, review, and roll back. The repository must be deeply technical, well documented, and structured around exact permanent files rather than placeholders. Script-like files and automation surfaces must follow the team’s canonical TL;DR header and comment style from the first line.

## Index

- [📌 Core Principles](#-core-principles)
- [🗂️ Documentation and File-Creation Rules](#️-documentation-and-file-creation-rules)
- [🏷️ Naming Rules](#️-naming-rules)
- [🧱 Path and Ownership Rules](#-path-and-ownership-rules)
- [💬 Commenting and Scripting Style](#-commenting-and-scripting-style)
- [📝 TODO Rules](#-todo-rules)
- [🧪 Verification Rules](#-verification-rules)
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
- comments should explain:
  - ownership
  - boundary
  - runtime flow
  - extension seams
  - non-obvious logic
- comments should not narrate trivial syntax line by line

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

### Internal Comment Rule

All non-TL;DR comments must be single-line comments only.

Allowed forms:

- a single-line comment above a mini-group
- a single-line comment appended to the relevant code line

Not allowed:

- multi-line block comments outside the TL;DR
- stacked repetitive comments that restate obvious code
- long prose paragraphs inside code files

### Section Header Rule

Use section-group headers to divide large areas of the file.

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

- comments should be heavy enough that a teammate can understand the file quickly
- comments should be sparse enough that they are not repeating every obvious line
- prefer one strong section comment over five weak local comments
- use inline comments only for:
  - non-obvious logic
  - edge-case handling
  - ordering constraints
  - TODOs
  - boundary reminders

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

    # ---------- <first section> ----------

    # TODO: <exact next cleanup or deferred implementation>

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

    // ---------- <first section> ----------

    // TODO: <exact next cleanup or deferred implementation>

### Review Rule for Comment Style

Treat any of the following as explainability debt:

- missing TL;DR header where this rule applies
- vague TL;DR content
- missing section-group headers in script-like files
- comment spam
- trivial syntax narration
- multi-line comments outside the TL;DR
- missing TODO markers for knowingly incomplete work

## 📝 TODO Rules

- use `TODO:` for cleanup, deferred work, or partial implementation
- keep TODOs specific and actionable
- place TODOs near the relevant section or line
- remove TODOs once the work is done
- do not use TODOs to hide ownership ambiguity or planning gaps that should be escalated now

## 🧪 Verification Rules

- pair meaningful implementation with the right level of verification
- leave review hotspots and rollback notes when risk is non-trivial
- keep documents and ADR context aligned when shared understanding changes
- reject work that is not meaningfully unique under `.opencode/rules/dryness-review.md`
- check comment-style compliance during implementation and again during review closeout

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
