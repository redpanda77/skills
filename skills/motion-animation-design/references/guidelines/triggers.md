---
name: guidelines-triggers
description: Types of animation triggers — user actions, hover, gestures, scroll — and what each implies for animation design.
---

# Triggers

The trigger is the event that begins the animation. The purpose of the animation will typically dictate the type of animation or transition.

## User Actions

Oftentimes, the trigger will be a user action: a click or tap on a button might trigger a short loading animation.

- Clicking the Closed Caption button shows an animation as feedback
- Clicking Add to Cart triggers a quick, subtle animation indicating the button is acquired
- This type of animation must have a very fast response time

## Hover

Some complex interactions have subtle triggers — hovering over a video scrubber bar might fade in a preview image of that point in a video.

- The animation trigger is a hover, not a click or gesture
- This animation needs to be slightly delayed to avoid overwhelming users with many flashing previews as they move their mouse
- The delay prevents accidental activation

## Gestures

A gesture such as swiping might show a small animation in the direction of the swipe as a confirmation that the gesture was recognized.

- Swiping on a trackpad causes an animated icon to appear
- The icon serves to confirm the system recognition of the user's action
- The animation direction matches the gesture direction

## Scroll

The trigger can be the act of scrolling down a page, resulting in a traditional preset animation or even parallax motion.

- Be cautious with parallax or scroll-jacking animations, as these are frequently frustrating, dizzying, and annoying
- Some animations trigger as soon as the user scrolls to the appropriate point
- Other motions are parallax effects where movement speed is controlled directly by the user's scroll speed

## Trigger vs. Moving Element

Sometimes the trigger is different from the element that will move:
- Clicking a button might cause a modal popup to slide into view
- Scrolling might cause a hero element to fade in
- Hovering over a card might cause a tooltip to appear

## Multiple Elements

Some animations involve only one moving item; others may consist of several elements moving together or with slight offset timing. In some cases, different parts of a single object will have different animations.

### Hamburger to X Morph

The trigger is tapping the button. The moving elements have subtlety:
- The top and bottom lines rotate into the X shape
- The middle bar fades out at the same time

## Key Takeaway

Keep in mind how frequently users will encounter the animation: the more frequent the animation, the more subtle and shorter you will want it to be.
