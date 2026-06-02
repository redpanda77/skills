---
name: guidelines-reduced-motion
description: Respecting the user's prefers-reduced-motion setting in CSS and Framer Motion.
---

# Reduced Motion

Always respect `prefers-reduced-motion`.

## CSS

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Framer Motion

```jsx
import { useReducedMotion } from "framer-motion";

const shouldReduceMotion = useReducedMotion();
```

## Principle

Remove or severely reduce motion for users who have opted out. Test animations with reduced motion enabled to ensure the interface is still usable.

## See Also

- `references/principles/reduced-motion.md`
