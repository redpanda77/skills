---
name: exercise-download-arrow
description: Animate two arrows simultaneously on hover. Learn grid stacking and precise translate values.
---

# Exercise: Download Arrow

## Goal

Move the arrow down when you hover over the button, but there is actually another one coming from the top at the same time.

## The Solution

Use `display: grid` with `grid-area: 1 / 1` to stack both arrows in the same cell. Use `overflow: hidden` on the button.

```css
.download-button {
  display: grid;
  place-items: center;
  overflow: hidden;
  height: 40px;
  width: 40px;
  border-radius: 50%;
}

.download-button svg {
  grid-area: 1 / 1;
  transition: transform 200ms cubic-bezier(0.785, 0.135, 0.15, 0.86);
}

.download-button svg:first-of-type {
  transform: translateY(-150%);
}

.download-button:hover svg:first-of-type {
  transform: translateY(0);
}

.download-button:hover svg:last-of-type {
  transform: translateY(150%);
}
```

## Key Takeaways

- `display: grid` with `grid-area: 1 / 1` puts multiple elements in the same grid cell
- The first arrow starts at `translateY(-150%)` — more than `-100%` because the arrow is smaller than the button
- On hover, the first arrow moves to `translateY(0)` and the second arrow moves to `translateY(150%)`
- `ease-in-out-circ` (`cubic-bezier(0.785, 0.135, 0.15, 0.86)`) creates a snappy feel
- See `Examples/06-feedback-and-interaction.html` for interaction demos
