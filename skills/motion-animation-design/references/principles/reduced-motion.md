---
name: principles-reduced-motion
description: Always respect the user's prefers-reduced-motion setting. Remove or severely reduce motion for users who have opted out.
---

# Reduced Motion

Always respect the user's `prefers-reduced-motion` setting.

## CSS

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Framer Motion

```jsx
import { useReducedMotion } from "framer-motion";

const shouldReduceMotion = useReducedMotion();
```

## Accessibility Considerations

Some users are sensitive to motion and animation. Respect `prefers-reduced-motion` for users with:

- **Vestibular disorders** — motion can cause dizziness, nausea, or vertigo
- **Epilepsy or photosensitive seizure disorders** — flashing or rapid movement can trigger seizures
- **ADHD** — excessive motion can be distracting and reduce focus
- **Motion sickness** — parallax and scroll-jacking can induce physical discomfort

**What to reduce or remove:**
- Parallax scrolling effects
- Auto-playing animations or videos
- Scroll-triggered animations that cannot be disabled
- Rapid flashing or strobing effects (more than 3 flashes per second)
- Large-scale motion that covers the entire viewport

**What to keep:**
- Essential state changes (e.g., a toggle switch moving to indicate on/off)
- Subtle color transitions that communicate status
- Very small micro-interactions that provide necessary feedback

When in doubt, reduce the motion rather than removing it entirely. A static interface can still be usable, but the goal is to preserve the informational value of the animation without the physical motion.

## Testing

Test animations with reduced motion enabled to ensure the interface is still usable. Do not simply hide content — make it accessible without motion.
