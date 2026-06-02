---
name: transitions-interruptibility
description: CSS transitions are interruptible — keyframe animations are not. This is critical for dynamic state changes.
---

# Interruptibility

CSS transitions are interruptible. If you hover and unhover before the transition finishes, it smoothly transitions back to the original state.

This is important to keep in mind as we compare it to CSS keyframe animations which are **not** interruptible.

## Why This Matters

When an animation can change its end state mid-way, CSS transitions are the right choice. CSS animations run to completion regardless of state changes, which can cause jumps.

## Toast Example

When adding a toast while others are still animating, existing toasts smoothly shift to their new positions with CSS transitions. This does not happen with CSS animations.

This is why Sonner uses CSS transitions for toast positioning.

## Enter Animations with Transitions

While less common, CSS transitions can also be used for enter animations. Use a `data-mounted` attribute or `@starting-style` to define the initial state.

```css
.toast {
  opacity: 0;
  transform: translateY(100%);
  transition: opacity 400ms ease, transform 400ms ease;
}

.toast[data-mounted="true"] {
  transform: translateY(calc(var(--index) * (100% + var(--gap)) * -1));
  opacity: 1;
}
```

## `@starting-style` At-Rule

This can also be solved without state or JavaScript by using the `@starting-style` CSS at-rule:

```css
.toast {
  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
  opacity: 1;
  transform: translateY(calc(var(--index) * (100% + var(--gap)) * -1));
  transition: opacity 400ms ease, transform 400ms ease;
}
```

This is supported in all major modern browsers.
