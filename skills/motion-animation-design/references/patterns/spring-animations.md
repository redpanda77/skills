---
name: pattern-spring-animations
description: Physics-based spring animations with stiffness, damping, and bounce.
---

# Spring-Based Animation

Springs generally outperform fixed-duration curves for interface work.

## Approach

Physics-based animation.

## Framer Motion

```jsx
<motion.div
  initial={{ y: 0 }}
  animate={{ y: 100 }}
  transition={{ type: "spring", stiffness: 400, damping: 30 }}
/>
```

## Key Points

- A default snappy spring: `stiffness: 400, damping: 30`
- For layout shifts: `duration: 0.55, bounce: 0.1`
- Physics-based curves feel natural because they factor in velocity
- Springs beat fixed-duration curves for gesture feedback because they run on the compositor and respond to velocity

## See Also

- `Examples/08-spring-animations.html` for spring demos
- `references/vocabulary.md` for spring terminology
