---
name: guidelines-gestures
description: Gesture-driven interactions with subdued feedback loops for hover, tap, focus, and drag.
---

# Gestures

Interaction should be declarative and subdued.

## Framer Motion Gestures

`whileHover`, `whileTap`, `whileFocus`, and `drag` provide declarative gesture feedback.

```jsx
<motion.button
  whileHover={{ y: -2, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}
  whileTap={{ scale: 0.97 }}
  whileFocus={{ outline: "2px solid blue" }}
/>
```

## Behavior

- The tap gesture aborts if the pointer drifts too far, avoiding collision with drag
- Focus effects behave like `:focus-visible`, activating only during keyboard navigation
- Keep those feedback loops subtle — gentle scale or border shifts work best

## See Also

- `Examples/06-feedback-and-interaction.html` for gesture demos
- `references/patterns/micro-interactions.md` for implementation
