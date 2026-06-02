---
name: guidelines-hero-entrance
description: Staggered hero entrance animations with timing, delays, and easing recommendations.
---

# Hero & Entrance Animations

The hero section is the first thing visitors see. Use a staggered entrance to create rhythm and guide attention.

## Implementation

- Start at `opacity: 0` and `translateY(20px)`
- Animate to `opacity: 1` and `translateY(0)` over `0.6s` with `ease-out`
- Stagger headline, subtext, and CTA with delays: `0s`, `0.15s`, `0.3s`

## CSS Example

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

## Principle

Even a simple staggered entrance produces a noticeable lift. Start with the hero entrance; even alone, it improves the perceived quality of the page.

## See Also

- `Examples/01-entrances-and-exits.html` for entrance demos
- `references/patterns/hero-entrance.md` for full implementation
