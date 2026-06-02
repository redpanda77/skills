---
name: principles-directional-consistency
description: Motion implies structural context. Document directional logic for menus, overlays, and navigation to maintain consistency across the product.
---

# Directional Consistency

Any movement, scaling, or motion in your product inherently suggests a direction. This indicates the context of your product and is a powerful way to make transitions look consistent.

## Core Principle

It is essential to document detailed directional information:
- When does the element move up or down?
- Which side does your overlay come from?
- How do menus expand?

Well designed products maintain clear and consistent directionality aligned with their context.

## Navigation Structure Examples

### Horizontal Navigation

A typical social media app behavior is to switch the viewing option with horizontal navigation. Swipe or tap the toggle to switch the view.

When scrolling through posts on a horizontally-navigated app, the scrolling direction is vertical (up and down).

### Vertical Navigation

An app with a slightly different layout uses vertical navigation. Swiping up and down is the way to switch the viewing option.

When scrolling through posts on a vertically-navigated app, the scrolling direction is horizontal (left and right).

## Menu Directionality

Even when opening menus or other relevant transitions, you can imply the overall directionality of the app:

- **Vertical browsing app:** Opening the menu implies the vertical browsing experience. Menu elements appear with gentle vertical movement from top to bottom.
- **Horizontal browsing app:** The menu elements appear from left to right, indicating the app's horizontal browsing experience.

## Implementation Guidelines

- Horizontal browsing should trigger horizontal transitions
- Vertical layouts should use vertical motion
- Align menu reveals with the primary navigation axis
- Document your directional logic — where overlays originate, how menus expand, which axis controls navigation

## Key Takeaway

Directionality is not just about the animation itself — it is about the structural context of your entire product. Consistent directionality strengthens the user's mental model and makes the product feel cohesive.
