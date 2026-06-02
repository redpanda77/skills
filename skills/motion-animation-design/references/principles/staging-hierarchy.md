---
name: principles-staging-hierarchy
description: Rank elements by importance when transitioning multiple elements. Group similar items, sequence by priority, and hide irrelevant groups.
---

# Staging and Hierarchy

When transitioning multiple elements, rank them by importance to help users focus on key interactions. Instead of transitioning all at once, sequence them by priority.

## Core Principle

If all the elements on a screen animated simultaneously, it would feel busy and complicated.

## Grouping and Ranking

1. **Group similar items together** — cluster related elements before sequencing
2. **Rank these groups by importance** — evaluate components by significance so attention stays focused on critical interactions
3. **Hide irrelevant groups** — conceal nonessential clusters to reduce distraction
4. **Sequence by priority** — animate the most important element first, then secondary elements

## Profile View Example

In a page-to-page transition where a "Profile view" card expands to fill the screen:

- **Primary elements:** The "Profile view" card and the supporting chart (these exist in both states)
- **Secondary elements:** Less important information that follows after the primary elements

If all elements animated simultaneously, it would feel busy. The cascading transition prioritized by importance creates a more polished experience.

## Music App Example

Music apps have complicated transitions when collapsing the player view. A seamless transition can be achieved by focusing on the cover and title layer:

1. The album cover and primary title animate first (scale down and fade)
2. The player overlay minimizes (slide down)
3. Secondary elements appear after the primary animation completes

This way, the cover scale animation does not distract from the other elements.

## Implementation Guidelines

- Evaluate components by significance so attention stays focused on critical interactions
- Cluster related objects before sequencing
- Conceal nonessential clusters to reduce distraction
- During player view collapses, animate the artwork and primary title first
- Let secondary controls exit downward, then introduce the minimized title afterward

## Choreography in Interface Animation

Just like in ballet choreography, the main idea is to guide the user's attention in one fluid direction during the transition from one state to another.

### Equal Interaction

Equal interaction means that the appearance of all objects obeys one particular rule.

- The appearance of all cards is perceived as one flow that guides user's attention in one direction (top to bottom)
- If the order is not followed, the user's attention will be scattered
- The appearance of all elements at once would look bad

For tabular views, the user's focus should be directed diagonally. Revealing each element one by one is a poor idea — it makes animation excessively long and the user's attention zigzag-like.

### Subordinate Interaction

Subordinate interaction means there is one central object which attracts all user's attention, and all other elements are subordinate to it.

- This type of animation gives the sense of order and draws more attention to the main content
- If several elements are animated, clearly define the sequence of their motion
- Animate as few objects as possible at one time

## Arc Movement

When moving objects transform their size disproportionally, they should move along an arc rather than in a straight line. This makes the movement more natural.

- **Vertical out:** object starts moving horizontally and ends with vertical movement
- **Horizontal out:** object begins moving vertically and ends with horizontal movement

The path of the object's movement along the curve must coincide with the main axis of the scrolling interface. If the interface scrolls up and down, the card unfolds in a Vertical out way — first to the right, then down.

## Object Collision

If the paths of moving objects intersect, they cannot move through each other:
- They should leave enough space for the movement of another object by slowing down or accelerating
- Or they just push away other objects
- Since all objects in the interface lie in one plane, no solid objects should pass through each other

Alternatively, the moving object can rise above other objects, but again no dissolving or movement through other objects.

## Choreography in Interface Animation

Just like in ballet choreography, the main idea is to guide the user's attention in one fluid direction during the transition from one state to another.

### Equal Interaction

Equal interaction means that the appearance of all objects obeys one particular rule.

- The appearance of all cards is perceived as one flow that guides user's attention in one direction (top to bottom)
- If the order is not followed, the user's attention will be scattered
- The appearance of all elements at once would look bad

For tabular views, the user's focus should be directed diagonally. Revealing each element one by one is a poor idea — it makes animation excessively long and the user's attention zigzag-like.

### Subordinate Interaction

Subordinate interaction means there is one central object which attracts all user's attention, and all other elements are subordinate to it.

- This type of animation gives the sense of order and draws more attention to the main content
- If several elements are animated, clearly define the sequence of their motion
- Animate as few objects as possible at one time

## Arc Movement

When moving objects transform their size disproportionally, they should move along an arc rather than in a straight line. This makes the movement more natural.

- **Vertical out:** object starts moving horizontally and ends with vertical movement
- **Horizontal out:** object begins moving vertically and ends with horizontal movement

The path of the object's movement along the curve must coincide with the main axis of the scrolling interface. If the interface scrolls up and down, the card unfolds in a Vertical out way — first to the right, then down.

## Object Collision

If the paths of moving objects intersect, they cannot move through each other:
- They should leave enough space for the movement of another object by slowing down or accelerating
- Or they just push away other objects
- Since all objects in the interface lie in one plane, no solid objects should pass through each other

Alternatively, the moving object can rise above other objects, but again no dissolving or movement through other objects.

## Key Takeaway

The challenge lies in finding the right balance between subtlety and emphasis. Prioritize what matters, group related elements, and sequence them deliberately.
