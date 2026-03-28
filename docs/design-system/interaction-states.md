# Interaction States

## Purpose

Food Run should feel polished in motion and interaction without becoming flashy.

For Sprint 1, subtle details matter:
- Hover quality
- Focus visibility
- Active feedback
- Disabled clarity
- Loading honesty
- Error recovery

These details often separate a prototype-feeling UI from a production-feeling UI.

## State Principles

### 1) Every Interactive Element Needs an Intentional State Model

At minimum, relevant controls should have:
- Default
- Hover
- Focus-visible
- Active
- Disabled

Where applicable, also:
- Loading
- Error
- Success
- Selected

### 2) State Changes Should Communicate Meaning

State styling should answer:
- Can I interact with this?
- Am I currently interacting with this?
- Did something happen?
- Is this unavailable?
- Does this need attention?

### 3) Subtle Is Good, Vague Is Not

Because Food Run aims for refined minimalism:
- Avoid dramatic motion
- Avoid noisy glow or bounce
- Avoid arbitrary transitions

But subtle does not mean invisible. Users must still perceive feedback.

## Button Behavior

Buttons should:
- Look clickable
- Feel responsive
- Communicate priority
- Remain legible in all states

Check:
- Hover clarity
- Pressed feel
- Focus ring
- Disabled readability
- Loading treatment, if applicable

## Input Behavior

Inputs should:
- Be easy to identify
- Provide clear focus feedback
- Feel stable during editing
- Communicate invalid state clearly
- Support helper and error text without clutter

Avoid:
- Placeholder-only labeling
- Hyper-subtle focus treatment
- Error states that rely only on color

## Surface Interaction

Interactive list items, cards, or selectors should:
- Signal hover or selection clearly
- Preserve clean layout while still showing state
- Not rely on hidden affordances

Do not use interaction styling to justify keeping an unnecessary card shell.

## Motion Rules

Motion should be used for:
- Confirming a state change
- Smoothing a layout change
- Orienting the user
- Reducing jank

Do not use motion for:
- Decoration only
- Unrelated delight moments
- Over-animated emphasis
- Attention hijacking

## Transition Guidance

Transitions should feel:
- Short
- Smooth
- Non-distracting
- Consistent

Long or ornate animation sequences are not appropriate for core workflow UI.

## Loading Guidance

Loading states must be honest.

Do not imply:
- Deeper processing than exists
- Certainty about duration
- False completion

Prefer:
- Clear temporary feedback
- Stable layout during loading
- Direct language when needed

## Error and Recovery Guidance

Errors should:
- Be specific
- Stay near the relevant control when possible
- Explain the next step
- Preserve trust

Users should not feel punished for normal correction.

## Accessibility Guidance

State communication should not rely on color alone.

Ensure:
- Focus-visible is strong
- Disabled is understandable
- Error is legible
- Selection is obvious
- Hover-only cues are not required for core understanding

## Review Checklist

Before approval, check:
- Do controls feel alive but calm?
- Can keyboard users see where they are?
- Do state changes feel believable?
- Are disabled and error states still readable?
- Is motion supporting comprehension rather than noise?
- Does the page feel more polished because of states, not busier?