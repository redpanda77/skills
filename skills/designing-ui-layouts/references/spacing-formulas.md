---
name: spacing-formulas
description: Detailed spacing formulas and base value rules for UI layout design.
---

# Spacing Formulas

## Base Value

The base value is the foundation of the layout system. Default: **multiples of 8**.

- Most screen sizes are divisible by 8.
- Used by both Material Design and HIG.
- Provides ample numerical values for scaling.

## Geometric Progression

Use geometric progression to narrow down spacing choices and focus on a limited set of core values.

| Value | Use Case |
|-------|----------|
| 4 pt | Tight spacing, small gaps |
| 8 pt | Default minimum spacing |
| 16 pt | Standard margin/padding |
| 32 pt | Large sections, major separation |

## Layout Properties

### Spacing
- **Margin:** Space in relation to other surrounding components.
- **Padding:** Space between the UI component and its children.

### Dimensions
- **Width / Height:** Size of the component.
- **Border:** Component stroke.
- **Radius:** Corner radius (circle or sphere).

### Position
- **X / Y:** Horizontal and vertical position.
- **Z:** Z-axis (layering).

## Compromises

When strict formula adherence is impossible (common with dynamic screen sizes):
- **Always prioritize spacing (margin and padding) over dimensions.**
- Document any exceptions and the rationale.
