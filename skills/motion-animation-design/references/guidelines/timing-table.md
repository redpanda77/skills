---
name: guidelines-timing-table
description: Timing and duration guidelines for different animation types.
---

# Timing Guidelines

| Animation Type | Duration | Easing |
|----------------|----------|--------|
| Micro-interaction (press, hover) | 100-200ms | ease, ease-out |
| Button feedback | 150ms | ease-out |
| Dropdown / modal enter | 200-300ms | strong ease-out |
| Toast enter | 200-300ms | strong ease-out |
| List stagger gap | 60-100ms per item | ease-out |
| Scroll reveal | 400-500ms | ease-out |
| Hero entrance | 500-800ms | ease-out, staggered |
| Page transition | 300-600ms | ease-out, crossfade |
| Ambient loop | 3-8s | linear |

## Principle

A speed from 100ms to 500ms is ideal for most interface needs. In-page micro-interactions should resolve faster than full-page changes. Complex structural transitions require enough time to prevent disorientation, yet never enough to create sluggishness.

## See Also

- `references/principles/timing-and-speed.md`
- `references/easing/decision-table.md`
