---
name: dimensions-and-ratios
description: Aspect ratios, incremental sizing, and dimension guidelines for UI components.
---

# Dimensions and Aspect Ratios

## Aspect Ratios

Use aspect ratios for images, videos, and large sections.

### Recommended Ratios

| Ratio | Common Use |
|-------|------------|
| 16:9 | Videos, banners |
| 3:2 | Photos |
| 4:3 | Standard photos, iPad screens |
| 1:1 | Square images, avatars |
| 3:4 | Portrait photos |
| 2:3 | Portrait images |

### Formulas

```
Width = Aspect Ratio * Height
Height = Width / Aspect Ratio
```

**Example:** An image with a width of 104 pt and a 3:4 aspect ratio:
```
Height = 104 / (3/4) = 138.67 pt
```

## Incremental Sizing and Positioning

Use increments of the base value (default: 80 pt) to determine size and position.

- Position a UI element at `80 pt * 1x` from the top of the screen.
- Use increments of 80 points to set the width and height of container cells.

## Radius and Borders

- Use the base value (multiples of 8) for corner radius and border widths when possible.
- Ensure border values do not compromise the spacing system.

## Compromise Rule

If a component's exact dimensions conflict with the spacing system:
- **Prioritize spacing (margin/padding) over exact dimensions.**
- Document any exceptions.
