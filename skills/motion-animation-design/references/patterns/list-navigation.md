---
name: pattern-list-navigation
description: Direction-aware list navigation with horizontal or vertical transitions.
---

# List Navigation

Align scroll directions and view-switching gestures with the application's dominant directional logic.

## Approach

Direction-aware sliding.

## CSS

```css
.list-forward {
  transform: translateX(0);
  transition: transform 0.3s ease-out;
}

.list-backward {
  transform: translateX(-100%);
  transition: transform 0.3s ease-out;
}
```

## Key Points

- Horizontal navigation should use horizontal view transitions
- Vertical layouts should use vertical motion
- Content slides one way going forward and the opposite way going back

## See Also

- `Examples/04-transitions-between-states.html` for direction-aware demos
- `references/principles/directional-consistency.md`
