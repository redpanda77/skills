---
name: pattern-micro-interactions
description: Hover lift, active press, and icon swap for button and card micro-interactions.
---

# Micro-Interaction

Go beyond a simple color swap. Give physical feedback.

## Approach

Hover lift + active press.

## CSS

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

## Key Points

- When users copy text, briefly swap the icon to a checkmark
- Cards can lift `translateY(-4px)` and shift `border-color`
- Keep feedback loops subdued — gentle scale or border shifts work best
- Disable hover on touch devices with `@media (hover: hover) and (pointer: fine)`

## See Also

- `Examples/06-feedback-and-interaction.html` for interaction demos
- `references/guidelines/micro-interactions.md`
- `exercises/card-hover.md`
- `exercises/simple-transform.md`
