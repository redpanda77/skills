---
name: implementation-framer-motion
description: Framer Motion implementation for React — core concepts, variants, AnimatePresence, layout, and gestures.
---

# Framer Motion Implementation

Framer Motion is the standard React animation library. Use it when you need declarative animations, layout interpolation, enter/exit effects, or gesture handling.

## When to Use Framer Motion

- Layout animations (sorted lists, accordions, expanding cards)
- Shared element transitions (thumbnail to detail)
- Enter/exit animations with `AnimatePresence`
- Gesture-driven interactions (drag, hover, tap)
- Complex orchestration with variants and `staggerChildren`

## Core Concepts

Three props control the story: `initial`, `animate`, `transition`.

```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6, ease: "easeOut" }}
/>
```

## Variants & Orchestration

```jsx
const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.08 }
  }
};

const item = {
  hidden: { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0 }
};

<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map(i => (
    <motion.li key={i} variants={item} />
  ))}
</motion.ul>
```

## Enter / Exit

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

- Direct children must carry a `key`
- `mode="wait"` ensures the outgoing view fully disappears before the new one appears

## Layout Animations

```jsx
<motion.div layout>
  {/* Automatically animates when geometry changes */}
</motion.div>
```

- For shared-element morphing, assign matching `layoutId` values to two nodes
- Keep morphing nodes outside `AnimatePresence`
- Apply `layout` sparingly; it measures geometry on every frame

## Scroll Triggers

```jsx
import { useInView } from "framer-motion";

const ref = useRef(null);
const isInView = useInView(ref, { once: true, margin: "-100px" });
```

## Gestures

```jsx
<motion.button
  whileHover={{ y: -2, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}
  whileTap={{ scale: 0.97 }}
  whileFocus={{ outline: "2px solid blue" }}
/>
```

## Performance

- Animate compositor-friendly properties (`x`, `y`, `scale`, `rotate`) rather than layout metrics (`width`, `height`, `top`, `left`)
- Add `willChange: "transform"` to frequently animated nodes
- Skip `filter` effects on mobile
- Use `lazy` to code-split the engine when animations are not immediately required

## Reduced Motion

```jsx
import { useReducedMotion } from "framer-motion";

const shouldReduceMotion = useReducedMotion();
```
