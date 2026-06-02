---
name: principles-scaling-dynamics
description: Scaling introduces dynamic, vibrant, and directional elements to transitions. Used with fade for overlays, album covers, and card expansions.
---

# Scaling Dynamics

Scaling introduces a dynamic, vibrant, and directional element to transitions.

## Core Technique

When transitioning to the next screen, scale down existing components and layers from 100% to 90%, along with fading out effects. When displaying an overlay, scale down the current screen. This gives the impression of the overlay sliding from a higher layer, highlighting the connectivity between states.

Scaling is typically used along with the opacity fading principle.

## Overlay and Layer Transitions

Incorporating a scale effect with fading gives objects a more dynamic, livelier presence. The transition has a graceful motion, as if the layers are gliding in and out from top to bottom.

### Scale with Vertical Movement

A common usage combines scale with fade:
- Scale up from 0.9 to 1.0 while fading in
- Scale down from 1.0 to 0.9 while fading out

## Text Layer Examples

### Active/Inactive States

The active and inactive layers can be highlighted using scale and a slight fade-out:
- Active layer scales up to 1.0 with full opacity
- Inactive layers scale down to 0.9 with slightly reduced opacity

### Card and Text Transitions

A lively transition can be achieved by scaling text and card layers simultaneously. This creates a sense of depth and hierarchy.

## Music App Example

A familiar instance of scaling can be seen in music apps during album cover transitions:
- As the music player overlay shrinks, the album cover smoothly scales down to a thumbnail size
- This creates a seamless connection between the playing view and the minimized state

## Comment Overlay Example

When opening an overlay, scale down and show a slight peek of the previous screen to imply there is a layer in the background. This is a default overlay style of iOS.

## Implementation

```css
.scale-fade-enter {
  opacity: 0;
  transform: scale(0.95);
  transition: opacity 0.3s ease-out, transform 0.3s ease-out;
}

.scale-fade-enter.is-visible {
  opacity: 1;
  transform: scale(1);
}

.underlay-scale {
  transform: scale(1);
  transition: transform 0.3s ease-out;
}

.overlay-open .underlay-scale {
  transform: scale(0.9);
}
```

## Key Takeaways

- Never animate from `scale(0)` — use `scale(0.93)` or higher
- `scale(0)` feels wrong because it looks like the element comes out of nowhere
- A higher initial value resembles the real world more — like a deflated balloon, even when deflated it has a visible shape
- Scale is typically paired with opacity fading for maximum effect
