---
name: material-design-container-transform
description: Material Design container transform — morphing a persistent container element into another container to maintain continuity between related states.
---

# Container Transform

A container transform transitions an element that serves as a container into another container. The container acts as a persistent element that morphs between states, maintaining continuity and drawing attention to the relationship between the two states.

## When to Use

Use for transitions between UI elements that include a container. Examples:
- A card expanding to a detail view
- A list item expanding to show more information
- A chip or button expanding to a full-screen dialog
- A thumbnail expanding to a full-size image
- A FAB (floating action button) expanding to a menu or sheet

## Core Behavior

The container itself is the persistent element. It changes shape and size while its contents crossfade. The container should:
- Maintain the same background color or surface throughout the transition
- Grow or shrink smoothly from the origin container's bounds to the target container's bounds
- Fade out the origin contents and fade in the target contents in parallel

## Timing

- **Duration**: 300-400ms for mobile, 400-500ms for larger screens
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` for the container morph
- **Content fade**: Coordinated with peak velocity — typically 150-200ms

## Implementation Notes

- The container's corner radius should animate smoothly between the origin and target values
- Content inside the container should fade out/in rather than scale, to avoid visual distortion
- Elevation or shadow may change during the transition to reinforce the change in prominence
- The element group maintains its aspect ratio, scaling by width to fit and pin to top of the container
- For the return transition, reverse the same animation sequence

## What to Avoid

- Do not morph the container and its contents simultaneously with the same transform — it creates a distorted, uncanny effect
- Do not change the container's color during the morph unless it is a subtle tonal shift
- Do not let the container morph outside the viewport bounds without clipping
- Do not animate multiple elements independently within the container. The various moving parts shift abruptly and make it difficult to focus
