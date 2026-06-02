---
name: guidelines-transition-properties
description: Standard properties to animate in UX — opacity, position, scale, color, shape, blur, rotation — and their use cases.
---

# Transition Properties

While animations can get very complex, there are a few standard properties that we might animate in a UX context:

- **Opacity** — fading in or out to suggest a change in state or replacement
- **Position** — moving from one place to another
- **Scale** — growing or shrinking
- **Color** — changing state or emphasis
- **Shape** — morphing from one form to another
- **Blur** — softening focus or masking imperfections
- **Rotation** — spinning or turning

In combination, these are enough to easily communicate clear feedback to the user.

## Position and Movement Path

When an object moves from one place to another around the screen, we need to decide:
- Start position
- End position
- Movement path

An arc path often looks more natural than a diagonal path, which ignores the regularity of the layout.

## Material Design Toggle Example

Google's Material Design toggle switch uses multiple properties simultaneously for a short (100ms) microinteraction:
- Button moves from one side to the other (position)
- Button color changes from gray to purple (color)
- A purple halo fades in — starts as a small translucent circle, enlarges, blurs, and fades out (scale, blur, opacity)

## Add to Cart Arc

When adding an item to the cart, a small animated checkmark moves from the Add to Bag button to the cart icon in the bottom right. The movement path is an arc rather than a perfectly straight diagonal line.

However, this animation is long and very likely to be annoying with repetition, as it is an exaggerated motion across the entire screen.

## Opacity and Performance

Changing the opacity is a common transition, but on a lot of platforms it will be computationally expensive (resulting in suboptimal performance and smoothness), especially when many elements change all at once.

## Shape Morphing

A circular button might expand to become a rounded rectangle card or a modal. In that case, use a transparent mask that expands in size and fades out in one motion.

### iOS App Store Card

Tapping on a card opens it to a full-screen element with additional details — an example of a growing animation combined with shape morphing.

## Key Takeaways

- Only animate `transform` and `opacity` for GPU-composited motion
- Avoid animating `width`, `height`, `margin`, `padding`, or `top`/`left` — they force layout recalculation
- An arc path often looks more natural than a diagonal path
- Changing opacity on many elements at once can be computationally expensive
