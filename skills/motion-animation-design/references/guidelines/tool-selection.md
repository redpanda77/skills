---
name: guidelines-tool-selection
description: When to use CSS, Framer Motion, or GSAP based on animation complexity and bundle size.
---

# Tool Selection

## CSS-Only

Simple hover effects, scroll reveals, hero entrances. Zero bundle cost. **Always start here.**

## Framer Motion

Layout animations, shared elements, enter/exit, gestures, orchestration. Adds significant bundle size. Use when declarative React animation is needed.

## GSAP

Complex choreographed timelines, scroll-driven animations, advanced sequencing. Use when CSS or Framer Motion cannot express the animation.

## When to Skip the Library

- Simple hover effects are lighter in plain CSS
- Scroll-progress animations often suit CSS `scroll-timeline` or GSAP
- Complex choreographed timelines are easier in GSAP
- If bundle size is critical, prefer native CSS

## See Also

- `references/implementation/css.md`
- `references/implementation/framer-motion.md`
- `references/implementation/gsap.md`
