---
name: pattern-expandable-card
description: Layout animation on the outer node with AnimatePresence for conditional inner content.
---

# Expandable Card

Layout animation on the outer node, plus conditional inner content.

## Approach

`layout` on the outer node, `AnimatePresence` for inner content.

## React / Framer Motion

```jsx
<motion.div layout>
  <motion.div layout="position">
    {/* Always-visible header */}
  </motion.div>
  <AnimatePresence>
    {isExpanded && (
      <motion.div
        initial={{ opacity: 0, height: 0 }}
        animate={{ opacity: 1, height: "auto" }}
        exit={{ opacity: 0, height: 0 }}
      >
        {/* Expanded content */}
      </motion.div>
    )}
  </AnimatePresence>
</motion.div>
```

## Key Points

- `layout` on the outer node automatically animates when geometry changes
- `AnimatePresence` handles the enter/exit of the inner content
- `layout="position"` on the header prevents it from resizing during the layout animation

## See Also

- `Examples/04-transitions-between-states.html` for accordion demos
- `references/guidelines/layout-shared.md`
