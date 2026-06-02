---
name: guidelines-scroll-triggers
description: Scroll-triggered animations using useInView or IntersectionObserver.
---

# Scroll Triggers

The `useInView` hook (or `IntersectionObserver` in vanilla JS) detects viewport intersection.

## Framer Motion

```jsx
import { useInView } from "framer-motion";

const ref = useRef(null);
const isInView = useInView(ref, { once: true, margin: "-100px" });
```

## Options

- `once: true` — trigger only the first time
- `margin: "-100px"` — trigger before the element is fully in view
- `amount: 0.5` — trigger when 50% of the element is visible

## Principle

Options like these let you trigger entrance effects at specific visibility thresholds, removing the need for extra scroll libraries in most cases.

## See Also

- `Examples/05-scroll.html` for scroll-driven demos
- `references/patterns/scroll-reveal.md`
