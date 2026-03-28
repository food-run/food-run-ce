# Spacing and Layout

## Purpose

Minimalist interfaces succeed or fail on spacing and layout discipline.

Food Run should rely heavily on spacing and composition to create hierarchy. This is especially important because the brand personality is already expressive. Layout must provide the calm counterbalance.

## Layout Goals

The layout system should feel:
- Clean
- Stable
- Breathable
- Efficient
- Deliberate
- Easy to scan
- Easy to revisit weekly

## Core Rule

Use whitespace and grouping before adding more surfaces.

If a region only feels separated once a border or filled box is added, check whether spacing and alignment are doing enough work first.

## Spacing Model

Use semantic spacing tokens consistently.

Spacing should communicate:
- Grouping
- Separation
- Importance
- Flow
- Rhythm

Spacing should not feel accidental or uniformly equal everywhere.

## Grouping Rules

Elements that belong together should feel visually close.

Elements that do not belong together should be separated with enough space that the relationship is obvious without relying on extra labels.

Prefer:
- Gap-based grouping
- Clear vertical rhythm
- Sectional spacing that scales with importance

Avoid:
- Equal spacing between everything
- Micro-gaps that feel cramped
- Giant blank zones with no structural meaning

## Section Rhythm

Pages should have a predictable vertical rhythm.

Recommended pattern:
- Shell padding establishes the page frame
- The page title region introduces the task
- The primary content region begins quickly
- Supporting regions stay clearly secondary
- Bottom-of-page space feels intentional, not abrupt

## Shell Behavior

The shell should:
- Provide stable route framing
- Reduce the need for each page to solve global layout from scratch
- Make transitions between routes feel coherent

Shell spacing should not be redefined casually per page.

## Surface Discipline

The current reviewer-facing frontend still uses multiple bordered surfaces inherited from earlier prototype habits.

Sprint 1 should reduce that pattern.

### Keep a Surface When It Clearly Improves
- Scope
- Separation
- Repeated-item clarity
- Local action framing
- Trust

### Remove or Soften a Surface When
- Spacing can do the job
- The border does not communicate anything new
- It duplicates an outer surface
- It turns a simple page into a stack of cards
- It makes the hierarchy feel flatter instead of clearer

## Card Discipline

Cards are allowed, but they are not the default language.

Use a card only when it truly helps:
- Isolate an item
- Establish local action scope
- Protect a piece of data from surrounding noise

Do not:
- Nest cards inside cards
- Use cards just to create style
- Split simple information into too many boxed panels
- Keep old card shells merely because the prototype used them

## Alignment Rules

Pay attention to optical alignment, not only numeric alignment.

Check:
- Left edges
- Input and button baselines
- Title and subtitle spacing
- Icon and text spacing
- Button-row distribution
- Empty-state centering logic

Clean alignment is a major part of perceived polish.

## Page-Density Rules

Food Run should feel neither sparse nor crowded.

Good density feels:
- Breathable
- Intentional
- Quick to scan
- Compact enough for workflow efficiency

Bad density feels:
- Packed and stressful
- Empty and underdesigned
- Inconsistent from region to region

## Primary-Action Placement

The primary action should be placed where the flow naturally leads.

Prefer:
- Close to the relevant input or decision
- Easy to find without searching
- Visually distinct but not oversized to compensate for weak layout

## Responsive Layout Guidance

Design mobile first, then expand outward.

On smaller screens:
- Reduce side-by-side complexity
- Preserve primary flow
- Avoid cramming secondary tools above core actions
- Maintain generous tap targets
- Keep headings and helper text from wrapping awkwardly

## Layout Review Checklist

Before approval, check:
- Can the page be understood by scanning?
- Are section boundaries obvious?
- Is there a stable rhythm from top to bottom?
- Are there any unnecessary boxes?
- Is the primary region clearly dominant?
- Does the layout remain clear on narrow screens?
- Does the page feel polished without relying on decoration?
- Did we reduce any leftover prototype card weight where possible?