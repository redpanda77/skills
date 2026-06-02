---
name: safe-areas
description: Safe area guidelines and platform-specific layout rules for UI design.
---

# Safe Areas and Guides

## Safe Areas

A safe area defines the region within a view that is not covered by toolbars, tab bars, or other system views.

### Rules
- Position all views within the safe area to avoid obstruction.
- Extend backgrounds and full-screen artwork to the edges of the display.
- Scrollable layouts must continue to the bottom and sides of the screen.
- Controls and navigation components (sidebars, tab bars) appear on top of content, not on the same plane.

### Platform-Specific Features
- **iPhone:** Avoid Dynamic Island and camera housing.
- **Mac:** Respect camera housing on some models.
- **tvOS:** Account for overscan insets (screen bezel area).

## Layout Guides

Layout guides define rectangular regions to help position, align, and space content.

### Types
- **System-defined:** Predefined margins and readable text width constraints.
- **Custom:** Define your own for complex layouts.

## Extending Safe Areas for Custom Views

If a container view controller displays custom content over a child view controller:
- Modify the child's `additionalSafeAreaInsets` to exclude the overlaid areas.
- Example: Custom views along the bottom and right edges require extending the bottom and right insets.

## Background Extensions

When content does not span the full window, use a background extension view to provide the appearance of content behind the control layer (e.g., beneath sidebars or inspectors).

## Resources

For templates including guides and safe areas per platform, see Apple Design Resources.
