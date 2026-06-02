---
name: creation-gotchas
description: Common failure modes when Claude writes motion code. Self-check against these before presenting generated code.
---

# Creation Gotchas

Common failure modes when writing motion code. Self-check against every item before presenting generated code.

---

## 1. Forgetting `prefers-reduced-motion`

**The mistake**: Writing animation code without any reduced-motion handling.

**The fix**: Every animation must include `prefers-reduced-motion` handling in the same code block. No exceptions, no follow-up.

```css
@media (prefers-reduced-motion: no-preference) {
  .animated { /* your animation */ }
}
```

```jsx
import { useReducedMotion } from "framer-motion";
const shouldReduceMotion = useReducedMotion();
```

---

## 2. Animating Layout Properties

**The mistake**: Using `width`, `height`, `top`, `left`, `margin`, or `padding` in animations.

**The fix**: Only animate `transform`, `opacity`, and `filter`. These are GPU-composited and avoid layout recalculation.

```jsx
// BAD
animate={{ width: 200, height: 100 }}

// GOOD
animate={{ scale: 1.2 }}
```

---

## 3. Using Default CSS Easing

**The mistake**: Using `ease`, `ease-in-out`, or `ease-in` without custom curves.

**The fix**: Always use custom Bezier curves. Built-in easing lacks strength for professional results.

```css
/* BAD */
transition: transform 0.2s ease;

/* GOOD */
transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
```

---

## 4. Animating from `scale(0)`

**The mistake**: Using `initial={{ scale: 0 }}` or `transform: scale(0)`.

**The fix**: Start from `scale(0.9)` or higher with opacity. `scale(0)` makes elements appear from nowhere.

```jsx
// BAD
initial={{ scale: 0 }}

// GOOD
initial={{ scale: 0.9, opacity: 0 }}
animate={{ scale: 1, opacity: 1 }}
```

---

## 5. Equal Enter and Exit Animations

**The mistake**: Making exit animations as prominent as enter animations.

**The fix**: Exits should be subtler than enters. The user's focus is moving to what comes next.

```jsx
// BAD
initial={{ opacity: 0, y: 20 }}
exit={{ opacity: 0, y: 20 }}

// GOOD
initial={{ opacity: 0, y: 20 }}
exit={{ opacity: 0, y: -8 }}
```

---

## 6. Missing `animation-fill-mode`

**The mistake**: Not setting `animation-fill-mode` for delayed sequences.

**The fix**: Use `animation-fill-mode: backwards` or `both` so elements don't flash at full opacity before their delayed animation starts.

```css
.element {
  animation: fadeUp 0.6s ease-out 0.3s backwards;
}
```

---

## 7. Wrong Transform Origin

**The mistake**: Dropdowns and popovers expanding from `center` instead of their trigger.

**The fix**: Set `transform-origin` to the trigger point.

```css
.dropdown {
  transform-origin: top center;
}
```

---

## 8. Using Keyframes for Interruptible Animations

**The mistake**: CSS `@keyframes` for animations that need to retarget mid-flight.

**The fix**: Use CSS transitions with state-driven classes. Keyframes can't be interrupted.

```css
/* BAD */
@keyframes slideIn {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}

/* GOOD */
.toast {
  transform: translateY(100%);
  transition: transform 400ms ease;
}
.toast.mounted {
  transform: translateY(0);
}
```

---

## 9. CSS Variables for Frequent Updates

**The mistake**: Using CSS custom properties for values that update frequently (drag, mouse follow).

**The fix**: Update styles directly on the element to avoid expensive cascade recalculation.

```javascript
// BAD
element.style.setProperty('--drag-y', `${y}px`);

// GOOD
element.style.transform = `translateY(${y}px)`;
```

---

## 10. `will-change` Everywhere

**The mistake**: Applying `will-change` globally or to too many elements.

**The fix**: Apply `will-change` sparingly and only to elements about to animate. Remove it after.

```css
/* BAD */
* { will-change: transform; }

/* GOOD */
.animated-button { will-change: transform, opacity; }
```

---

## 11. Forgetting Exit Animations

**The mistake**: Wrapping conditionals in `AnimatePresence` but not providing `exit` props.

**The fix**: Every element that enters should also have an exit. Elements that just disappear feel broken.

```jsx
<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -8 }}  // ← Don't forget this
    />
  )}
</AnimatePresence>
```

---

## 12. Uniform Animation Across All Elements

**The mistake**: Applying the same enter animation to every element on the page.

**The fix**: Context should drive timing and easing. Hero elements can be more expressive; utility elements should be subtle or instant.

---

## 13. Bounce on Utility Actions

**The mistake**: Using `bounce: > 0` on dropdowns, toggles, menus, or modals.

**The fix**: Reserve bounce for playful moments. Utility actions should use `bounce: 0` for professional deceleration.

```jsx
// BAD for utility
transition={{ type: "spring", bounce: 0.2 }}

// GOOD for utility
transition={{ type: "spring", bounce: 0 }}
```

---

## 14. Missing `key` on AnimatePresence Children

**The mistake**: Children of `AnimatePresence` without unique `key` props.

**The fix**: Direct children must carry a `key` so the tracker can follow them.

```jsx
<AnimatePresence mode="wait">
  {isVisible && (
    <motion.div key="modal" /* ... */ />  // ← key is required
  )}
</AnimatePresence>
```

---

## 15. `layoutId` Inside `AnimatePresence`

**The mistake**: Putting elements with `layoutId` inside `AnimatePresence`.

**The fix**: Keep morphing nodes outside `AnimatePresence` to prevent broken cross-fades.

```jsx
// BAD
<AnimatePresence>
  {isExpanded && <motion.div layoutId="card" />}
</AnimatePresence>

// GOOD
{isExpanded && <motion.div layoutId="card" />}
```

---

## 16. Motion on Text-Only Elements

**The mistake**: Entrance animations on headings, paragraphs, and navigation that should appear instantly.

**The fix**: Static content should be static. Motion should serve orientation, feedback, or continuity — not just announce itself.

---

## 17. Forgetting Hover on Touch Devices

**The mistake**: Hover effects that trigger on touch devices.

**The fix**: Disable hover effects on touch devices.

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover { /* hover styles */ }
}
```

---

## 18. Distance Thresholds Instead of Velocity

**The mistake**: Using distance thresholds for swipe dismissal.

**The fix**: Use velocity (distance / time). Fast, short gestures should work.

```javascript
// BAD
if (dragDistance > 100) dismiss();

// GOOD
const velocity = dragDistance / elapsedTime;
if (velocity > 0.11) dismiss();
```

---

## 19. Forgetting `mode="wait"` for Page Transitions

**The mistake**: `AnimatePresence` without `mode="wait"` for page/route transitions.

**The fix**: `mode="wait"` ensures the outgoing view fully disappears before the new one appears.

```jsx
<AnimatePresence mode="wait">
  <motion.div key={route} /* ... */ />
</AnimatePresence>
```

---

## 20. No `transition` Property on Dynamic Inline Styles

**The mistake**: Dynamic inline styles that change values without a `transition` property.

**The fix**: If `style={{ prop: dynamicValue }}` is used, ensure the element has a `transition` rule for that property.

```css
.expandable {
  transition: height 0.3s ease-out;
}
```
