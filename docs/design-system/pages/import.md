# Import

## Page Role

The Import page is the front door into the workflow.

It should make starting feel easy and trustworthy.

## Dominant Job

Import a recipe URL and understand what the system will do next.

## Primary Action

Import recipe.

This action should be unmistakably primary.

## Required Information Before Action

The user should understand:
- What input is expected
- What the action will do
- Any important limitations, if relevant

The user should not need to read a long explanation before acting.

## Visual Priorities

1. Page purpose
2. URL input
3. Import action
4. Concise helper guidance
5. Any honest status or limitation language

## Layout Guidance

- Lead quickly into the input
- Keep the main interaction region compact and clear
- Avoid crowding the form with excessive supporting text
- Use whitespace and typography to make the flow feel easy

## Surface Guidance

The current reviewer shell uses a bordered `.import-form` container.

That may remain temporarily if it improves focus, but Sprint 1 should evaluate whether the same clarity could come from:
- Better spacing
- Stronger heading rhythm
- Cleaner input-and-button grouping
- Less reliance on a visible panel shell

Do not let the form become a “card because forms are cards” pattern.

For the current Sprint 1 shell, prefer a direct field-and-action grouping before adding another visible container.

## Tone Guidance

The page should feel:
- Welcoming
- Low-friction
- Honest
- Calm

Avoid hype or fake smartness.

## Trust Notes

Do not imply:
- Recipe-parsing accuracy beyond what exists
- Hidden background-processing sophistication
- Strong automation confidence if not implemented

If review or confirmation comes later, hint at it clearly and honestly.

## Empty and Initial State Guidance

The initial state should feel complete, not empty.

It should immediately communicate:
- What to do
- Why it is useful
- That the action is approachable

## Mobile Behavior

On mobile:
- Keep the primary action close to the input
- Avoid helper-text sprawl
- Ensure the field and button remain comfortably tappable
- Maintain a short, obvious path from title to action

## Banned Clutter

Do not add:
- Extra cards that split the form unnecessarily
- Long introductory copy
- Multiple competing call-to-action options
- Speculative metadata panels
- Fake preview confidence

## Review Questions

1. Would a first-time user know what to paste and where?
2. Is the import action the most obvious thing on the page?
3. Does the page feel easier than manual planning, not more complex?
4. Does the page remain honest about current product maturity?
5. Is the bordered form container still earning its place?
