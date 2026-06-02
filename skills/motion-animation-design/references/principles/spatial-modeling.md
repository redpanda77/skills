---
name: principles-spatial-modeling
description: Design the invisible space beyond the visible frame. Stack functional layers to create depth on flat displays.
---

# Spatial Modeling

Even though the user interaction area is limited to the device screen, designing the invisible space beyond the visible frame is crucial. Establishing spatiality helps users form a mental model of your product, enhancing their experience.

## Core Principle

Often, designers use multiple functional layers to introduce depth and spatiality to flat screens.

## Music App Example

A music app consists of multiple functional layers:
- The base screen with the music list
- The player overlay that slides up
- The minimized player that docks at the bottom

When the player view collapses, the transition shows how the layers interact:
- The player overlay slides down and shrinks
- The base screen becomes visible again
- The minimized player appears at the bottom

This spatial model helps users understand where things are in the app even when they are not visible.

## Comment Overlay Example

A social media app with a comment overlay demonstrates spatial modeling:

1. The comments overlay slides in from the bottom
2. The existing screen scales down to 90%
3. A dark background layer appears behind the scaled screen

The lowest layer is the dark background, then the scaled screen, then the comment overlay on top. This three-layer stack creates depth and makes the overlay feel like it is floating above the content.

## Different Spatial Models for Different Products

Two apps with the same interactions and layer elements can use different spatial models to create a different feel:

- **Horizontal navigation app:** Posts are below the toggle, layers stack vertically
- **Vertical navigation app:** Posts are to the right of the toggle, layers stack horizontally

By looking beyond just the screen area and understanding the origin of transitions and movements, one can grasp the overarching spatial structure. Building such spatial frameworks significantly enriches the uniqueness of your product's user experience.

## Implementation

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

## Key Takeaways

- When comment overlays slide upward, scale the underlying page downward and dim it to reinforce background placement
- Shrink underlying screens to roughly 90% when overlays appear to imply depth
- Maintain consistent spatial frameworks across the entire application to strengthen identity
- Peek at previous screens during modal presentations to reinforce layer hierarchy
