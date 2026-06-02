---
name: implementation-platform-specific
description: Platform-specific notes for iOS native feel, reduced motion, touch devices, and real device testing.
---

# Platform-Specific Notes

## iOS Native Feel

Use spring-based curves inspired by native iOS motion. Framer Motion springs can mimic this.

```jsx
<motion.div
  transition={{ type: "spring", stiffness: 400, damping: 30 }}
/>
```

## prefers-reduced-motion

Always respect this setting.

### CSS

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Framer Motion

```jsx
import { useReducedMotion } from "framer-motion";
const shouldReduceMotion = useReducedMotion();
```

## Touch Devices

Disable hover animations on touch.

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover { /* hover styles */ }
}
```

- Tailwind v4 handles this automatically
- For Tailwind v3, enable `hoverOnlyWhenSupported` in config

## Test on Real Devices

Workstations misrepresent actual animation speed and performance. Always test on the target devices.

## See Also

- `references/principles/reduced-motion.md`
- `references/transitions/best-practices.md`
