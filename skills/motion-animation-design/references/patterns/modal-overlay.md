---
name: pattern-modal-overlay
description: Scale underlying screen to 90% and dim background for modal presentations.
---

# Modal / Overlay

Scale the underlying screen slightly to reveal layered hierarchy.

## Approach

Scale background + dim overlay.

## CSS

```css
.overlay-open .page {
  transform: scale(0.9);
  opacity: 0.5;
  transition: transform 0.3s ease-out, opacity 0.3s ease-out;
}

.modal {
  transform: scale(0.95);
  opacity: 0;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              opacity 0.3s ease-out;
}

.modal.is-open {
  transform: scale(1);
  opacity: 1;
}
```

## Key Points

- Shrink underlying screens to roughly 90% when overlays appear to imply depth
- Combine with dimming layers to establish depth
- Use strong ease-out for the modal to feel responsive

## See Also

- `Examples/04-transitions-between-states.html` for modal demos
- `references/principles/spatial-modeling.md`
