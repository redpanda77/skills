---
name: implementation-css
description: CSS-only animation implementation, transition syntax, animation syntax, and best practices.
---

# CSS Implementation

CSS is the default choice. It has zero bundle cost and handles most UI animations well.

## When to Use CSS

- Simple hover effects
- Scroll reveals (with IntersectionObserver)
- Hero entrances with staggered `animation-delay`
- Button press feedback with `:active`
- Toast positioning with `transition` (for interruptibility)
- Any animation where the end state does not change mid-flight

## CSS Transition Syntax

```css
/* Good — explicit properties */
.button {
  transition: transform 0.2s ease, opacity 0.2s ease;
}

/* Good — shorthand with explicit property list */
.button {
  transition: 0.2s ease;
  transition-property: transform, opacity;
}

/* Bad — transition: all forces browser to watch every property */
.button {
  transition: all 0.2s ease;
}
```

## CSS Animation Syntax

```css
/* Staggered entrance */
.hero-item {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeUp 0.6s ease-out forwards;
}

.hero-item:nth-child(2) { animation-delay: 0.15s; }
.hero-item:nth-child(3) { animation-delay: 0.3s; }

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## Key CSS Rules

- Only animate `transform` and `opacity` for GPU-composited motion
- Never animate `width`, `height`, `margin`, `padding`, or `top`/`left` — they force layout recalculation
- Use `will-change: transform` sparingly, only on elements about to move, and remove after
- Disable hover effects on touch devices with `@media (hover: hover) and (pointer: fine)`

## `@starting-style` At-Rule

For enter animations without JavaScript state:

```css
.toast {
  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
  opacity: 1;
  transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
}
```

## See Also

- `references/transitions/fundamentals.md`
- `references/transitions/best-practices.md`
- `references/transitions/interruptibility.md`
