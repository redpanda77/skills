---
name: guidelines-micro-interactions
description: Hover states, press feedback, and icon swaps that go beyond a simple color change.
---

# Micro-Interactions

Hover states should go beyond a simple color swap.

## Buttons

Transition `transform` and `box-shadow` across `0.15s ease`, shifting `translateY(-2px)` on hover and resetting on active.

```css
.button {
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.button:active {
  transform: scale(0.97);
}
```

## Cards

Lift `translateY(-4px)` and shift `border-color`.

## Icon Swaps

When users copy text, briefly swap the icon to a checkmark to close the feedback loop.

## Principle

Keep feedback loops subdued — gentle scale or border shifts work best. The interface should feel as if it is listening to the user.

## See Also

- `Examples/06-feedback-and-interaction.html` for interaction demos
- `references/patterns/micro-interactions.md` for full implementation
