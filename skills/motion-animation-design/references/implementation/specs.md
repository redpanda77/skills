---
name: implementation-specs
description: How to communicate animation specifications to engineering teams — timelines, motion comps, and format considerations.
---

# Communicating Animation Specs

If the engineering team does not get meaningful, clear specs from the design team, there is very little chance that it will build exactly what the designer had in mind.

## What Not to Do

It is not good enough to hand over a compiled video file from some video software and expect the developer to go frame by frame, trying to figure out all the subtleties of the easing curves.

## The Timeline Approach

Especially for complex animations with multiple movements happening all at once, a timeline is the most effective way to share animation characteristics with the engineering team.

Show all the different elements that will move, with:
- The type of properties that will change
- The easing curves for each particular element
- Durations in milliseconds, not frames

Along with a noninteractive exported video of the animation (known as a motion comp).

## What to Include

An animation timeline should include:
1. **All elements** that will move
2. **Triggers** — what starts each animation
3. **Transition types** — opacity, position, scale, etc.
4. **Durations** — in milliseconds
5. **Easing curves** — in the format the engineering team prefers

## Format Considerations

Easing is one of the most challenging aspects to communicate to an engineering team, as every platform has different ways of specifying an easing curve:
- CSS uses `cubic-bezier` format
- iOS and Android use named easing curves
- Adobe After Effects uses incoming and outgoing percentage values

Speak with your development team so that you can specify these values in a way that they can be most easily translated into code.

## Technical Reality Check

It is highly recommended that you talk to your development team before getting to this level of polish, as technical realities may make some choices difficult or impossible.

Ensure that you use the format that is easiest for them:
- `cubic-bezier` format vs. named curves like `EaseInOut`
- CSS transitions vs. keyframe animations
- JavaScript libraries vs. pure CSS

## Key Takeaway

Tiny details matter in animation. A tenth of a second makes a big difference. Get the specs right, and users may appreciate your animation as it enhances the learnability of the UI. Get it half a second wrong, and the animation will feel jarring and annoying.
