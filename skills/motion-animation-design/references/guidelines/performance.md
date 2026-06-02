---
name: guidelines-performance
description: Performance rules for smooth 60fps animations. Only animate transform and opacity.
---

# Performance Rules

- Only animate `transform` and `opacity` — they are GPU-composited and avoid layout recalculation
- Avoid animating `width`, `height`, `margin`, or `padding` since they force costly reflows
- Use `will-change` sparingly, applying it only to elements about to move and removing it after
- Test on real devices — workstations misrepresent actual speed
- Add `will-change: "transform"` to frequently animated nodes
- Skip `filter` effects on mobile

## Compositing

Letting the GPU move or fade an element on its own layer without redoing layout or paint is the key to smooth animation.

## Layout Thrashing

Animating properties like `width`, `height`, `top`, or `left` forces the browser to recalculate layout every frame, causing jank.

## See Also

- `Examples/11-performance.html` for performance demos
- `references/implementation/css.md` for CSS-specific performance tips
