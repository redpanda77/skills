---
name: principles-timing-and-speed
description: A speed from 100ms to 500ms is ideal for most cases. Balance speed for in-page transitions vs page-to-page transitions.
---

# Timing and Speed

The right animation speed provides practical feedback and a meaningful experience. Transitions that are too slow can bore users, while overly fast transitions lack meaning.

## Context-Dependent Duration Guidelines

| Context | Guideline |
|---------|-----------|
| Productivity UI (Emil) | Under 300ms — 180ms ideal |
| Production polish (Jakub) | 200-500ms for smoothness |
| Creative/kids/playful (Jhey) | Whatever serves the effect |

**Do not universally flag or cap durations.** Check the context weighting first.

## Core Guidelines

A speed from 100ms to 500ms is ideal and suitable for most cases. You can follow this as a guideline, but customize it to suit your product. That is another way to create a distinctive product from others.

## In-Page Transitions

Quick actions, such as toggle sliders, are important to have proper speed to provide feedback to people. Since this is an in-page transition, it should be slightly faster than the page-to-page animation.

- Toggle slider: 100-200ms
- Button press feedback: 150ms
- Dropdown/modal enter: 200-300ms

## Page-to-Page Transitions

For page-to-page transitions with many elements, there needs to be some context so people do not feel disconnected from each state. This may be slightly slower than the in-page transition.

- Page transition: 300-600ms
- Hero entrance: 500-800ms
- Scroll reveal: 400-500ms

However, that does not necessarily mean slowing down your animation speed. Proper speed is still crucial to ensure that your product does not feel slow.

## Timing Reference Table

| Animation Type | Duration | Easing |
|----------------|----------|--------|
| Micro-interaction (press, hover) | 100-200ms | ease, ease-out |
| Button feedback | 150ms | ease-out |
| Dropdown / modal enter | 200-300ms | strong ease-out |
| Toast enter | 200-300ms | strong ease-out |
| List stagger gap | 60-100ms per item | ease-out |
| Scroll reveal | 400-500ms | ease-out |
| Hero entrance | 500-800ms | ease-out, staggered |
| Page transition | 300-600ms | ease-out, crossfade |
| Ambient loop | 3-8s | linear |

## Key Takeaway

UI animations should generally stay under 300ms. Remove animations entirely for elements seen tens of times daily — they become annoying and slow the interface.

## Platform-Specific Durations

Different platforms and devices have different optimal durations:

- **Mobile devices:** 200–300ms (Material Design Guidelines)
- **Tablets:** 400–450ms (30% longer than mobile due to larger screen size)
- **Wearables:** 150–200ms (30% shorter due to smaller screen)
- **Web:** 150–200ms (about 2× shorter than mobile, as users expect instant page transitions)

The reason is simple: the size of the screen affects the distance objects travel. Larger screens = longer path = longer duration. Smaller screens = shorter path = shorter duration.

## Size Affects Duration

Regardless of platform, the duration should depend not only on the traveled distance but also on the size of the object:
- **Smaller elements** or animations with small changes should move faster
- **Larger and complex elements** look better when they last a little longer

Among moving objects of the same size, the first one to stop is the object that has passed the shortest distance.

## List Items

List items (news cards, email lists, etc.) should have a very short delay between appearances:
- Each occurrence should last from **20 to 25 ms**
- The slower emergence of elements may annoy the user

## Bounce Effect

When objects collide, the energy of collision must be evenly distributed. It is better to exclude the bounce effect. Use it only in exceptional cases when it makes sense.

## Motion Blur

The movement of objects should be clear and sharp — do not use motion blur in interface animation. It is difficult to reproduce on modern mobile devices and is not used in interface animation at all.

## Perceived Performance

A faster-spinning spinner makes the app seem to load faster, even when load times are identical. Easing affects perceived performance more than actual duration. A dropdown with `ease-out` at 300ms feels faster than the same dropdown with `ease-in` at 300ms.

**Choose easing before shortening duration.**

## Platform-Specific Durations

Different platforms and devices have different optimal durations:

- **Mobile devices:** 200-300ms (Material Design Guidelines)
- **Tablets:** 400-450ms (30% longer than mobile due to larger screen size)
- **Wearables:** 150-200ms (30% shorter due to smaller screen)
- **Web:** 150-200ms (about 2x shorter than mobile, as users expect instant page transitions)

The size of the screen affects the distance objects travel. Larger screens = longer path = longer duration. Smaller screens = shorter path = shorter duration.

## Size Affects Duration

Regardless of platform, the duration should depend not only on the traveled distance but also on the size of the object:
- **Smaller elements** or animations with small changes should move faster
- **Larger and complex elements** look better when they last a little longer

Among moving objects of the same size, the first one to stop is the object that has passed the shortest distance.

## List Items

List items (news cards, email lists, etc.) should have a very short delay between appearances:
- Each occurrence should last from **20 to 25 ms**
- The slower emergence of elements may annoy the user

## Bounce Effect

When objects collide, the energy of collision must be evenly distributed. It is better to exclude the bounce effect. Use it only in exceptional cases when it makes sense.

## Motion Blur

The movement of objects should be clear and sharp — do not use motion blur in interface animation. It is difficult to reproduce on modern mobile devices and is not used in interface animation at all.
