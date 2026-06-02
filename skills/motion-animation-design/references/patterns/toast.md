---
name: pattern-toast
description: CSS transition-based toast with interruptible positioning and enter animation.
---

# Toast

Use CSS transitions (not keyframe animations) for toast enter animations. This ensures that if a new toast is added while others are animating, existing toasts smoothly shift to their new positions without jumping.

## Approach

CSS transition with strong ease-out.

## CSS

```css
.toast {
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
```

## Key Points

- CSS transitions are interruptible; CSS animations are not
- This is why Sonner uses transitions for toast positioning
- Choose `ease-out` or a strong custom ease-out for enter animations so the toast feels responsive
- Use `data-mounted` attribute or `@starting-style` for enter animation

## See Also

- `Examples/01-entrances-and-exits.html` for enter/exit demos
- `exercises/toast-component.md` for full implementation
- `references/transitions/interruptibility.md`
