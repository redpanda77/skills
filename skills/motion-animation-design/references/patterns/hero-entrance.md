---
name: pattern-hero-entrance
description: CSS-only staggered fade-up hero entrance with delays and easing.
---

# Hero Entrance

The hero section is the best place to begin adding motion. Even a simple staggered entrance produces a noticeable lift.

## Approach

CSS-only staggered fade-up.

## CSS

```css
.hero-headline,
.hero-subtext,
.hero-cta {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeUp 0.6s ease-out forwards;
}

.hero-subtext { animation-delay: 0.15s; }
.hero-cta { animation-delay: 0.3s; }

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## Key Points

- Start at `opacity: 0` and `translateY(20px)`
- Animate to `opacity: 1` and `translateY(0)` over `0.6s` with `ease-out`
- Stagger headline, subtext, and CTA with delays: `0s`, `0.15s`, `0.3s`
- This is the foundation of any animated landing page

## See Also

- `Examples/01-entrances-and-exits.html` for entrance demos
- `references/guidelines/hero-entrance.md`
