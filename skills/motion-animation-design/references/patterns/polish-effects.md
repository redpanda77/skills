---
name: pattern-polish-effects
description: Blur, clip-path, shimmer, line drawing, and other polish effects for masking imperfections.
---

# Polish Effects

Use effects sparingly to mask imperfections or add visual interest.

## Blur

Add `filter: blur(2px)` during transitions to blend states together.

```css
.state-transition {
  transition: filter 0.2s ease, opacity 0.2s ease;
}

.state-transition.is-transitioning {
  filter: blur(2px);
}
```

Blur works because it bridges the visual gap between the old and new states. Without it, you see two distinct objects, which feels less natural. It tricks the eye into seeing a smooth transition by blending the two states together.

## Shimmer / Skeleton

A placeholder with a moving sheen shown while content loads.

```css
.shimmer {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## Line Drawing

An SVG path that draws itself in.

```css
.line-draw {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: draw 2s ease-out forwards;
}

@keyframes draw {
  to { stroke-dashoffset: 0; }
}
```

## See Also

- `Examples/10-polish-and-effects.html` for polish demos
- `references/principles/hard-rules.md` for the blur rule
