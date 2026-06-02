---
name: layout-explorer-template
description: Template for exploring layout and composition options for a screen before detailed design.
---

# UI Layout & Composition Explorer

## Use Case

Design reviews with PMs, breaking creative blocks, or presenting multiple directions before Figma.

## How to Use

1. Fill in the Screen Context below.
2. Generate three layout concepts, a recommended direction, grid spec, and edge cases.
3. Use the concepts as a review structure so feedback stays specific.

## Screen Context

- **Screen / Page Name:** [e.g., User Dashboard, Product Detail Page, Onboarding Step 2, Empty State]
- **Platform:** [Web desktop / Web responsive / iOS / Android / Tablet]
- **Primary User Goal:** [what is the user trying to accomplish?]
- **Secondary Goals:** [what else might the user need?]
- **Content Elements (Required):** [list everything that must appear]
- **Content Elements (Optional):** [list anything that could be conditionally shown]
- **Design Constraints:** [e.g., must fit above the fold, fixed header at 64px, fixed sidebar at 240px]
- **Visual Style:** [minimal / data-dense / editorial / card-based / full-bleed / etc.]
- **Reference Products:** [mention 2-3 products with a UI you admire for this type of screen]

## Output Structure

### Layout Concept A - Hierarchy-First

Describe a layout that prioritizes the most important content element above all else.
- Grid system, number of columns, key component placement, visual weight distribution
- How the eye moves through the screen (top to bottom / left to right)

### Layout Concept B - Density-Optimized

Describe a layout that maximizes content density without feeling overwhelming.
- How content is grouped, where whitespace is strategically preserved
- Scroll behavior

### Layout Concept C - Progressive Disclosure

Describe a layout that reveals complexity progressively — shows essentials first, details on demand.
- What is shown by default vs. hidden behind expand/collapse or drill-down

### Recommended Layout

Based on the user goal and constraints, recommend ONE layout direction and explain why it best serves the primary task.

### Grid Specification

- Number of columns, gutter width, margin, baseline grid unit (4pt or 8pt)
- How the grid adapts at each breakpoint (if responsive)

### Visual Hierarchy Breakdown

For the recommended layout, rank every content element from highest to lowest visual weight and explain how that hierarchy is achieved (size, color, position, whitespace, contrast).

### Above-the-Fold Priority List

List exactly what must be visible without scrolling and why.

### Edge Cases to Design For

- **Empty state:** what does this screen look like with no data?
- **Error state:** what if data fails to load?
- **Long content:** what if a title or label is 3x longer than expected?
- **First-time user vs. returning user:** should the layout differ?

## Pro Tips

- Output is a written brief — you still need to execute in Figma or code.
- Progressive disclosure needs engineering partnership on what collapses or expands.
- Prioritize empty and error states from the Edge Cases section; they drive trust.
