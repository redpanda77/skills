---
name: pattern-page-transition
description: Crossfade page transitions with mode=wait for React route changes.
---

# Page Transition

Crossfade between states using duplicate layers.

## Approach: React / Framer Motion

```jsx
<AnimatePresence mode="wait">
  <motion.div
    key={route}
    initial={{ opacity: 0, x: 20 }}
    animate={{ opacity: 1, x: 0 }}
    exit={{ opacity: 0, x: -20 }}
    transition={{ duration: 0.3, ease: "easeOut" }}
  >
    {children}
  </motion.div>
</AnimatePresence>
```

## Key Points

- `mode="wait"` ensures the outgoing view fully disappears before the new one appears
- For vanilla JS, use duplicate layers at different scales and crossfade between them
- Direction-aware: horizontal navigation uses horizontal transitions, vertical uses vertical

## See Also

- `Examples/04-transitions-between-states.html` for page transition demos
- `references/principles/directional-consistency.md`
