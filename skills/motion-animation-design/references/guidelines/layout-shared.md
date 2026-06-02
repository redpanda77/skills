---
name: guidelines-layout-shared
description: Layout animations and shared element transitions using FLIP and layoutId.
---

# Layout & Shared Elements

Adding `layout={true}` enables automatic FLIP interpolation whenever geometry or coordinates change.

## Layout Animation

```jsx
<motion.div layout>
  {/* Automatically animates when geometry changes */}
</motion.div>
```

- This powers sorted lists, accordions, and expanding surfaces
- Apply `layout` sparingly; it measures geometry on every frame

## Shared Element Morphing

Assign matching `layoutId` values to two nodes; the engine bridges their position and size as one replaces the other.

```jsx
{!isExpanded ? (
  <motion.img layoutId="image" src={src} className="thumbnail" />
) : (
  <motion.img layoutId="image" src={src} className="fullsize" />
)}
```

- Keep morphing nodes outside `AnimatePresence` to prevent broken cross-fades
- Use cases: sliding tab indicators, thumbnail-to-detail expansions

## See Also

- `Examples/03-movement-and-transforms.html` for transform demos
- `Examples/04-transitions-between-states.html` for shared element demos
- `references/patterns/expandable-card.md`
- `references/patterns/shared-element.md`
