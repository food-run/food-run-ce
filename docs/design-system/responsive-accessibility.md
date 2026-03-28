# Responsive Accessibility

## Purpose

Food Run will be used by real people in real contexts. Responsive and accessible behavior is part of product quality, not optional polish.

This file defines the minimum expectations for Sprint 1.

## Responsive Principles

### 1) Design Mobile First

The narrow layout should preserve:
- The dominant job
- The primary action
- Readable type
- Stable spacing
- Clear section order

Desktop should expand the layout, not completely redefine the experience.

### 2) Content Decides Breakpoints

Breakpoints should respond to layout pressure, not arbitrary device mythology.

Watch for:
- Awkward wrapping
- Compressed controls
- Unreadable line lengths
- Broken button groups
- Unstable section hierarchy

### 3) Priority Must Survive Compression

On smaller screens:
- Keep the primary task visible
- Push secondary content down
- Simplify multi-column layouts
- Avoid placing too much context above action

## Mobile Guidance

On mobile:
- Keep the flow vertical where possible
- Avoid wide control groups that wrap poorly
- Preserve generous tap targets
- Use short labels
- Keep helper text concise
- Avoid dense side-by-side metadata unless critical

## Desktop Guidance

On desktop:
- Use additional width to improve scanability
- Constrain text measure
- Do not spread simple forms into awkward horizontal compositions
- Do not let whitespace become aimless emptiness

## Accessibility Principles

### 1) Clarity First

Accessible UI often overlaps with better UI:
- Clearer labels
- Stronger hierarchy
- More specific actions
- More visible states
- Less guessing

### 2) Semantic Meaning Matters

Where applicable, preserve semantic structure:
- Headings
- Lists
- Labels
- Buttons
- Links
- Status text

### 3) Focus-Visible Is Mandatory

Keyboard users must be able to understand where they are at all times.

Focus treatment should be:
- Visible
- Attractive
- Consistent
- High enough in contrast to trust

### 4) Text Must Stay Readable

Especially check:
- Helper text
- Status text
- Muted text
- Dark-mode text
- Disabled text
- Button labels

### 5) State Meaning Cannot Rely on Color Alone

Error, success, selection, or emphasis should be communicated by more than hue.

Use:
- Text
- Icons, where appropriate
- Structure
- Label changes
- Position or grouping when helpful

## Target and Control Guidance

Interactive targets should be comfortably usable on touch screens.

Do not compress:
- Buttons
- Checkboxes
- List rows
- Small icon buttons

## Motion and Accessibility

Use reduced and purposeful motion.

Avoid:
- Attention-seeking effects
- Large layout jumps
- Excessive animation chains

## Content Accessibility

Write:
- Direct labels
- Explicit button text
- Error messages with next steps
- Helper text that reduces ambiguity

Avoid:
- Vague verbs
- Jargon-heavy microcopy
- Unexplained abbreviations
- Placeholder-only instructions

## Sprint 1 Review Checklist

Before approval, check:
- Does the layout hold up on narrow screens?
- Does the hierarchy survive wrapping?
- Is focus-visible strong?
- Are tap targets usable?
- Is muted text still readable?
- Are errors understandable?
- Does the page remain calm instead of crowded on mobile?
- Did any boxed surface survive purely because it looked cleaner on desktop while harming mobile clarity?