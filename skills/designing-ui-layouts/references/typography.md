---
name: typography-basics
description: Typography basics including vertical rhythm, system fonts, and line-height ratios for UI layout.
---

# Typography Basics

## Vertical Rhythm

Vertical Rhythm is a typographic structure that evenly spaces the baseline of text vertically, regardless of font, size, weight, or margin.

- The vertical space or baseline is determined by the line-height.
- Apply Vertical Rhythm where possible; perfect adherence can be challenging due to varying font properties.

## Line-Height Ratios

The line-height is defined by a unitless ratio multiplied by the font size.

```
Line-Height = Ratio * Font Size
```

| Ratio | Effect |
|-------|--------|
| 1.2 | Tight, compact text |
| 1.3–1.4 | Balanced, readable (recommended) |
| 1.5+ | Spacious, airy |

## System Fonts

Prefer the system typeface of the platform you are building on.

- **Apple:** San Francisco (SF)
- **Google:** Roboto

### Why System Fonts
- **Type Scale:** Predefined for you (e.g., `UIFont.preferredFont(forTextStyle: .headline)`).
- **Dynamic:** Adapt to environment (e.g., SF Text vs. SF Desktop based on size).
- **Universal:** Simple and adaptable for most designs.
- **Quality:** Engineered for legibility and utility.

## Typographic Properties

| Property | Description |
|----------|-------------|
| Typographic Scale | Harmonious pattern for font sizes |
| Font Size | Size of the font |
| Line-Height | Vertical distance between lines of text |
| Paragraph Margin | Distance between paragraphs |
| Character Spacing | Horizontal distance between characters |

## Notes

- Typography is an advanced design topic; this guide covers the basics.
- For a detailed type scale calculator, use external tools to experiment with ratios.
