---
name: pattern-shared-element
description: Shared element transitions using matching layoutId values for morphing.
---

# Shared Element

An element travels and transforms from one position into another.

## Approach

Matching `layoutId` values.

## React / Framer Motion

```jsx
{!isExpanded ? (
  <motion.img layoutId="image" src={src} className="thumbnail" />
) : (
  <motion.img layoutId="image" src={src} className="fullsize" />
)}
```

## Key Points

- Keep morphing nodes outside `AnimatePresence` to prevent broken cross-fades
- Use cases: sliding tab indicators, thumbnail-to-detail expansions
- The engine bridges position and size as one replaces the other

## See Also

- `Examples/04-transitions-between-states.html` for shared element demos
- `references/guidelines/layout-shared.md`
