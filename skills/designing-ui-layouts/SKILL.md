---
name: designing-ui-layouts
description: Applies systematic UI layout principles for spacing, safe areas, visual hierarchy, and adaptability. Use when designing a new screen or component, reviewing existing UI for consistency, or adapting layout for different devices. Do NOT use for animation, color theming, or platform-specific code.
---

# Designing UI Layouts

## Core Rules

**NEVER** use random spacing values. Derive all margins and padding from the base value (multiples of 8).
**NEVER** place content outside safe areas. Respect system bars, Dynamic Island, and device-specific features.
**NEVER** mix Material Design and HIG layout principles in the same project.
**NEVER** compromise spacing (margin/padding) to fix dimensions. Spacing takes priority over exact dimensions.

## Workflow: Apply Layout

### Step 0: Explore Layout Options (for new screens)
- For new screens or major redesigns, use the layout explorer template to generate three layout concepts (Hierarchy-First, Density-Optimized, Progressive Disclosure) before applying the systematic layout.
- See `templates/layout-explorer.md`.

### Step 1: Set Base Value
- Choose a base value. Default: multiples of 8.
- Use this for all spacing, dimensions, and typography unless a specific exception is warranted.

### Step 2: Define Spacing System
- Use geometric progression for margins and padding: 8, 16, 32 (and 4 for tight spacing if needed).
- Prioritize spacing over dimensions when compromises are necessary.

### Step 3: Respect Safe Areas
- Position all content within the view's safe area.
- Extend backgrounds and full-screen artwork to the edges of the display.
- Scrollable layouts must continue to the edges of the device screen.
- For custom container views, extend the child view controller's safe area to exclude overlaid content.

### Step 4: Establish Visual Hierarchy
- Group related items using negative space, background shapes, or separator lines.
- Place the most important items near the top and leading side.
- Align components to communicate organization and hierarchy.
- Use progressive disclosure for hidden content.
- Provide sufficient space around controls and group them logically.
- For toolbars, group items by function and place them in the correct area (leading, center, trailing). See `references/toolbars.md`.
- For cards, ensure each card focuses on one thing, uses a grid system, and defines all interaction states. See `references/cards.md`.
- For landing pages, follow the high-converting anatomy: hero, social proof, benefits, details, FAQ, and multiple CTAs. See `references/landing-pages.md`.
- Apply the 5 key composition principles: alignment, proximity, white space, balance, and hierarchy. See `references/layout-composition.md`.
- For detailed visual hierarchy specs, use the visual hierarchy design template. See `templates/visual-hierarchy.md`.
- To audit an existing screen for hierarchy, contrast, and composition problems, use the visual hierarchy audit template. See `templates/visual-hierarchy-audit.md`.

### Step 5: Ensure Adaptability
- Respect system-defined safe areas, margins, and guides.
- Support Dynamic Type and text-size changes.
- Preview on multiple devices, orientations, localizations, and text sizes.
- Scale artwork (without changing aspect ratio) to fit different displays.

## Validation

Before finalizing, verify:
- [ ] All spacing values are multiples of the base value (default 8).
- [ ] No content is placed outside safe areas.
- [ ] Important information is prominent and easy to find.
- [ ] Related items are grouped; unrelated items are separated.
- [ ] Layout is tested for adaptability (device size, orientation, text size).

## Error Handling

If a design spec conflicts with the base value formula:
1. Prioritize spacing (margin/padding) over dimensions.
2. Document the exception and the reason for it.
3. If mixing design systems is unavoidable, choose one primary system and document deviations.

## References

- **Spacing and Formulas:** See `references/spacing-formulas.md`
- **Safe Areas and Guides:** See `references/safe-areas.md`
- **Typography Basics:** See `references/typography.md`
- **Aspect Ratios and Dimensions:** See `references/dimensions.md`
- **Toolbar Guidelines:** See `references/toolbars.md`
- **Layout & Composition Principles:** See `references/layout-composition.md`
- **Card Design Guidelines:** See `references/cards.md`
- **Landing Page Design Guidelines:** See `references/landing-pages.md`
- **Layout Explorer Template:** See `templates/layout-explorer.md`
- **Visual Hierarchy Design Template:** See `templates/visual-hierarchy.md`
- **Visual Hierarchy Audit Template:** See `templates/visual-hierarchy-audit.md`
- **Complementary Skills:** See `references/complementary-skills.md` — Additional skills for frontend design, visual polish, anti-slop detection, and accessibility auditing
