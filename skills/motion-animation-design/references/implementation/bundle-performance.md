---
name: implementation-bundle-performance
description: Bundle size and performance considerations when choosing between CSS, Framer Motion, and GSAP.
---

# Bundle & Performance Considerations

## Bundle Size

- CSS animations have **zero bundle cost** and are always the first choice
- Framer Motion adds **significant bundle size**. Use it only when declarative React animation is needed
- GSAP is **powerful but heavy**. Use it only for complex timelines that CSS cannot express
- If bundle size is critical, prefer native CSS

## Performance Rules

- Only animate `transform` and `opacity` — they are GPU-composited
- Avoid animating `width`, `height`, `margin`, `padding` — they force layout recalculation
- Use `will-change` sparingly, applying it only to elements about to move and removing it after
- Test on real devices — workstations misrepresent actual animation speed and performance

## When to Skip the Library

- Simple hover effects are lighter in plain CSS
- Scroll-progress animations often suit CSS `scroll-timeline` or GSAP
- Complex choreographed timelines are easier in GSAP
- If bundle size is critical, prefer native CSS
