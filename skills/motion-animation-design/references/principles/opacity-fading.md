---
name: principles-opacity-fading
description: Fading in and out with opacity for softening state changes, toggle transitions, menu openings, and seamless layer transitions.
---

# Opacity Fading

Fading in and out with opacity is a basic yet powerful principle. Utilizing this technique alone can make a significant difference.

## Core Technique

Shift transparency between 0% and 100% to soften state changes. When transitioning from the current screen to the next, fade out irrelevant elements and let the next part fade in.

You can achieve this by turning the opacity value from 100 to 0 (or 0 to 100) in any design or prototyping tool.

## Toggle Transition

While the abrupt transition feels disconnected, adding the opacity effect feels smoother and more appealing. The toggle slider with a fade effect provides clear feedback on the state change.

## Menu Opening

Rather than abruptly cropping the menu from bottom to top, utilizing a fade animation offers a gentler and more fluid transition. This enhances user engagement with the menu.

## Page-to-Page State Changes

A common example of using fade animation to transition from one state to another. This is typically combined with scale and vertical movement for a more dynamic effect.

## Layered Continuity (Advanced)

This technique seamlessly integrates interactions between two screen layers or sequences. By using this method, scene transitions become virtually undetectable to users.

### Profile View Example

The "Profile view" layer seamlessly moves while transitioning to the next state. This fluid transition is achieved by utilizing two "Profile view" layers — both small and large.

By incorporating a scaling effect and smoothly fading between the two layers, the transition appears as though a singular title layer seamlessly bridges both screen states. While it appears as a smooth animation to viewers, it is achieved by transitioning between the smaller and larger text layers, creating a seamless illusion.

## Implementation

```css
.fade-enter {
  opacity: 0;
  transition: opacity 0.3s ease-out;
}

.fade-enter.is-visible {
  opacity: 1;
}

.fade-exit {
  opacity: 1;
  transition: opacity 0.3s ease-out;
}

.fade-exit.is-hidden {
  opacity: 0;
}
```

## Key Takeaway

For layered continuity, duplicate components at different sizes and crossfade between them to create the illusion of a single element bridging two states.
