---
name: material-design-enter-exit
description: Material Design enter and exit patterns — how elements appear and disappear in place without changing position or hierarchy.
---

# Enter and Exit Patterns

Enter and exit patterns describe how individual elements appear or disappear within a screen without changing the user's position in the hierarchy or navigation flow.

## Fade In (Enter)

The simplest and most common enter pattern. An element fades from transparent to opaque.

- **Duration**: 150-200ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)`
- **Use for**: Toasts, snackbars, banners, simple reveals

## Fade Out (Exit)

The reverse of fade in. An element fades from opaque to transparent.

- **Duration**: 150-200ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)`
- **Use for**: Dismissing temporary elements, hiding modals

## Scale In (Enter)

An element scales up from a smaller size while fading in. Often used for popovers, menus, and dialogs.

- **Initial**: `scale(0.8)` to `scale(1)` with `opacity 0` to `opacity 1`
- **Duration**: 200-250ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` for scale, `linear` for opacity
- **Transform origin**: Must match the trigger point (origin-aware)

## Scale Out (Exit)

The reverse of scale in. An element scales down and fades out.

- **Initial**: `scale(1)` to `scale(0.8)` with `opacity 1` to `opacity 0`
- **Duration**: 200-250ms
- **Easing**: `cubic-bezier(0.4, 0, 1, 1)` for the exit scale (ease-in feel)

## Slide In (Enter)

An element slides into its final position from a nearby edge.

- **Direction**: Slide from the edge the element is attached to (e.g., a bottom sheet slides up from the bottom)
- **Duration**: 250-300ms
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)`
- **Use for**: Bottom sheets, side panels, dropdowns, full-screen dialogs

## Slide Out (Exit)

The reverse of slide in. An element slides out toward the edge it came from.

- **Duration**: 250-300ms
- **Easing**: `cubic-bezier(0.4, 0, 1, 1)` for exit (ease-in)

## Staggered Enter

When multiple elements enter simultaneously, stagger them slightly to create hierarchy and avoid visual clutter.

- **Stagger gap**: 20-50ms between elements
- **Direction**: Stagger in the direction of reading (top to bottom, left to right)
- **Use for**: List items, grid items, form fields, chips

## Implementation Notes

- Always animate from a non-zero scale — `scale(0.8)` or higher, never `scale(0)`
- For slide patterns, the element should be fully visible and clipped by the container edge, not sitting off-screen in a way that affects layout
- For enter animations, use `ease-out` or `cubic-bezier(0.4, 0, 0.2, 1)` to feel responsive
- For exit animations, use `ease-in` or `cubic-bezier(0.4, 0, 1, 1)` to feel like the element is accelerating away

## What to Avoid

- Do not mix inconsistent enter patterns on the same screen (e.g., some items fade in while others slide in arbitrarily)
- Do not animate layout properties (width, height, margin) for enter/exit — use transform and opacity only
- Do not let elements enter and exit at the same time without a clear relationship between them
