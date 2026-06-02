---
name: principles-perceived-performance
description: The right animation makes an interface feel faster, even when it is not.
---

# Perceived Performance

The right animation makes an interface feel faster, even when it is not.

- A faster-spinning spinner makes the app seem to load faster even when load times are identical
- A dropdown with `ease-out` at 300ms feels faster than the same dropdown with `ease-in` at 300ms
- Choose easing before shortening duration

## Easing Over Duration

Easing affects perceived performance more than actual duration. A well-chosen easing curve can make a 400ms animation feel faster than a 200ms animation with poor easing.

**Always choose the right easing first, then adjust duration if needed.**
