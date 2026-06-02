---
name: guidelines-enter-exit
description: Enter and exit animation patterns for React and CSS, including AnimatePresence and interruptibility.
---

# Enter/Exit Patterns

React unmounts elements instantly, so leave effects are impossible by default.

## React / Framer Motion

Wrap conditional mounts in an `AnimatePresence` boundary and supply an `exit` definition.

```jsx
<AnimatePresence mode="wait">
  {isVisible && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.3, ease: "easeOut" }}
    />
  )}
</AnimatePresence>
```

- Direct children must carry a `key` so the tracker can follow them
- `mode="wait"` ensures the outgoing view fully disappears before the new one appears

## CSS

CSS transitions are interruptible; CSS keyframe animations are not. Use transitions when the end state might change mid-flight (e.g., toast positioning).

## See Also

- `Examples/01-entrances-and-exits.html` for enter/exit demos
- `references/patterns/toast.md` for interruptible positioning
