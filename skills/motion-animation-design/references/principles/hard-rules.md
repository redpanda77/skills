---
name: principles-hard-rules
description: The 7 non-negotiable rules that prevent the most common animation mistakes.
---

# The 7 Hard Rules

Apply these rules before any other consideration.

1. **Never animate from `scale(0)`** — use `scale(0.93)` or higher. A higher initial scale feels natural, like a deflated balloon still having shape.

2. **Never use `ease-in` for enter/exit animations** — it starts slow and makes UI feel sluggish. Use `ease-out` for user-initiated interactions.

3. **Never exceed 300ms for UI animations** — keep transitions fast. Remove animations entirely for elements seen tens of times daily.

4. **Always make popovers origin-aware** — set `transform-origin` to the trigger point, not `center`. Use component library variables like `var(--transform-origin)`.

5. **Scale buttons on press** — add `transform: scale(0.97)` on `:active` with a 150ms transition.

6. **Skip tooltip delays after first show** — once a tooltip is open, subsequent tooltips in the same group should appear instantly with `transition-duration: 0ms` via a `data-instant` attribute.

7. **Use `blur()` as a last resort** — if an animation still feels off after adjusting easing and duration, add `filter: blur(2px)` during the transition to blend states together.
