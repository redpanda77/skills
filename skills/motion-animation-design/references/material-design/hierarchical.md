---
name: material-design-hierarchical
description: Material Design hierarchical transitions — parent-child navigation using container transform to express hierarchy and continuity.
---

# Hierarchical Transitions

Hierarchical transitions move users one level upwards or downwards through an app's hierarchy. Screens at adjacent levels have a parent and child relationship, where the parent is placed at a higher level of hierarchy than its child.

## Parent-Child Transitions

From a parent screen, an embedded child element lifts up on touch and expands in place, using a container transform transition pattern. The motion both draws focus to the child screen (the destination of the interaction), while reinforcing the relationship between parent and child screens.

### Core Behavior

- The child element (such as a card or list item) is the persistent container
- The container lifts up on touch, then expands to fill the screen
- The parent screen's contents fade out as the child expands
- The child screen's contents fade in after the container has expanded

### Timing

- **Duration**: 300-400ms for mobile
- **Container expansion**: `cubic-bezier(0.4, 0, 0.2, 1)`
- **Content fade**: Coordinated with peak velocity

### Container Transform

For transitions between UI elements that include a container. The container itself is the persistent element. It changes shape and size while its contents crossfade. The container should:
- Maintain the same background color or surface throughout the transition
- Grow or shrink smoothly from the origin container's bounds to the target container's bounds
- Fade out the origin contents and fade in the target contents in parallel

### Implementation Notes

- The container's corner radius should animate smoothly between the origin and target values
- Content inside the container should fade out/in rather than scale, to avoid visual distortion
- Elevation or shadow may change during the transition to reinforce the change in prominence
- For the return transition, reverse the same animation sequence

## What to Avoid

- Do not morph the container and its contents simultaneously with the same transform — it creates a distorted, uncanny effect
- Do not change the container's color during the morph unless it is a subtle tonal shift
- Do not let the container morph outside the viewport bounds without clipping
