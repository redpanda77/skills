---
name: material-design-peer-transitions
description: Material Design peer transitions — sibling transitions between screens sharing a parent, and top-level transitions between primary destinations.
---

# Peer Transitions

Peer transitions occur between screens at the same level of hierarchy. These are not parent-child relationships — the screens are siblings or independent top-level destinations.

## Sibling Transitions

Screens that share the same parent (such as photos in an album, sections of a profile, or steps in a flow) move in unison to reinforce their relationship to one another. The peer screen slides in from one side, while its sibling moves off screen in the opposite direction.

### Core Behavior

- Both the outgoing and incoming elements move horizontally in opposite directions
- The outgoing element slides out to the left while the incoming element slides in from the right
- The movement is symmetric — both elements travel at the same speed and distance
- Tabs or indicators sit at the same elevation and move together to show they are related

### Timing

- **Duration**: 300ms
- **Incoming**: `translateX(100%)` to `translateX(0)`, `cubic-bezier(0.4, 0, 0.2, 1)`
- **Outgoing**: `translateX(0)` to `translateX(-100%)`, `cubic-bezier(0.4, 0, 0.2, 1)`

### Bidirectional Movement

- Moving forward (left to right in the tab order): incoming slides from right, outgoing slides to left
- Moving backward (right to left in the tab order): incoming slides from left, outgoing slides to right
- The direction should match the spatial order of the tabs or pages

### Implementation Notes

- Keep the content of the outgoing element visible during the early part of the transition so it does not feel like it disappears
- Use `overflow: hidden` on the parent container to clip the outgoing and incoming elements at the edges
- For tab bars, the active indicator should also animate laterally to the new tab position

## Top-Level Transitions

At the top level of an app, destinations are often grouped into major tasks that may not relate to one another. These screens transition in place using a **fade through** pattern.

### Core Behavior

- The outgoing screen fades out completely before the incoming screen fades in
- No directional movement — the screens are independent contexts
- The transition is symmetrical regardless of which destination is selected

### Timing

- **Duration**: 250-300ms
- **Outgoing**: Fades out, `opacity 1` to `opacity 0`, 150ms
- **Incoming**: Fades in, `opacity 0` to `opacity 1`, 150ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)`

### Implementation Notes

- The outgoing and incoming screens should share the same layout structure (e.g., both have a top app bar) so the persistent elements do not animate
- The transition should feel instant and responsive — the user is switching tasks, not navigating a flow
- Do not use directional sliding for top-level transitions — it implies a hierarchy or sequence that does not exist

## What to Avoid

- Do not use lateral transitions for parent-to-child navigation — that is a hierarchical transition
- Do not animate the outgoing element fading out instead of sliding for sibling transitions — it breaks the lateral spatial model
- Do not change the direction logic unexpectedly for siblings (e.g., always sliding right regardless of which tab was tapped)
- Do not make top-level transitions too long; the user is switching contexts frequently and needs speed
- Do not animate persistent UI elements (top bars, bottom bars) during any peer transition
