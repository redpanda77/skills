---
name: easing-custom-curves
description: How to create and use custom cubic-bezier curves for more energetic and impactful animation.
---

# Custom Easings

Built-in curves are often not strong enough. Use custom `cubic-bezier` values for more energetic motion.

## Creating Custom Curves

```css
.custom-ease-out {
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
```

A strong `ease-out` curve moves very fast at the beginning and decelerates gently. Compare the built-in `ease-out` against a custom `cubic-bezier(0.16, 1, 0.3, 1)` — the custom one feels more alive.

## Recommended Sources

- `easings.co` — curated collection of custom easing variations
- Browser DevTools cubic-bezier editor — fine-tune curves visually

## Platform-Specific Mimicry

For components that need a native feel, use a curve specifically tuned to match the platform.

Example: iOS sheet-style bottom drawers use a custom easing inspired by Ionic Framework to mimic the native spring feel.

## Common Custom Curves

| Name | Curve | Use Case |
|------|-------|----------|
| ease-out-expo | `cubic-bezier(0.19, 1, 0.22, 1)` | Elegant hover reveals, card descriptions |
| ease-in-out-circ | `cubic-bezier(0.785, 0.135, 0.15, 0.86)` | Snappy button interactions, download arrows |
| strong ease-out | `cubic-bezier(0.16, 1, 0.3, 1)` | Dropdowns, modals, toasts |
| smooth ease-in-out | `cubic-bezier(0.65, 0, 0.35, 1)` | Timelines, on-screen morphs |
