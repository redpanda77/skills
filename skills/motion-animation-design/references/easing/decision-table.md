---
name: easing-decision-table
description: Quick decision table for choosing the right easing based on the animation situation.
---

# Easing Decision Table

| Situation | Easing | Example |
|-----------|--------|---------|
| Enter/exit screen | Strong ease-out | Modal, dropdown, toast |
| On-screen morph/move | ease-in-out | Timeline, dynamic island |
| Hover color/opacity | ease | Button hover, card hover |
| Constant loop | linear | Marquee, spinner |
| Hold-to-delete | linear | Time visualization |
| UI enter/exit | **Never ease-in** | — |

## Perception of Speed

Easing affects perceived performance more than actual duration. A dropdown with `ease-out` at 300ms feels faster than the same dropdown with `ease-in` at 300ms.

**Choose easing before shortening duration.**

A faster-spinning spinner makes the app seem to load faster even when load times are identical.

## When Nothing Else Works

If you tried a few different easings and durations and something still feels off, try adding a bit of `filter: blur()` to mask imperfections.

Blur bridges the visual gap between the old and new states. Without it, you see two distinct objects, which feels less natural. It tricks the eye into seeing a smooth transition by blending the two states together.
