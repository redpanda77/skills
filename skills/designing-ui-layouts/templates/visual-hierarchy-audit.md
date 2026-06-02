---
name: visual-hierarchy-audit
description: Perform a thorough visual hierarchy audit of a screen or design to diagnose hierarchy, contrast, and composition problems.
---

# Visual Hierarchy Audit

## Use Case

Diagnosing hierarchy, contrast, and composition problems in existing screens or designs. Use when users report issues like "users aren't clicking the CTA," "the page feels cluttered," or "stakeholders say it looks amateur."

## How to Use

1. Fill in the Screen Description and Context below.
2. Perform the audit across all dimensions.
3. Use the Prioritized Fix List to plan improvements.

## Screen Description

[Describe the screen in detail OR paste a written description of what appears on screen. Include: what elements are present, their approximate sizes, colors, positions, and the content they contain.]

## Context

- **Platform:** [Web / iOS / Android]
- **Primary User Goal:** [what should the user do or understand first when they land on this screen?]
- **Secondary Goals:** [what else should the user notice or act on?]
- **Current Problem (if known):** [e.g., "users aren't clicking the CTA," "the page feels cluttered"]
- **Target User:** [brief description]

## Audit Dimensions

### Attention Flow Analysis

- Describe where the eye lands **FIRST** on this screen based on the design as described.
- Map the likely eye movement path through the screen (F-pattern, Z-pattern, center-weighted, etc.).
- Identify the top 3 elements competing for first attention and whether that competition is intentional.

### Hierarchy Scoring

Rate each of the following on a scale of 1–5 (5 = excellent) with a one-sentence rationale:

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Size contrast | [1-5] | [Difference between largest and smallest elements] |
| Color contrast | [1-5] | [Use of color to indicate importance] |
| Spatial hierarchy | [1-5] | [Use of whitespace and proximity to group and prioritize] |
| Typographic hierarchy | [1-5] | [Heading vs. body vs. label differentiation] |
| Focal point clarity | [1-5] | [Is there ONE clear dominant element?] |

### Critical Issues (P1)

List any hierarchy issues that are directly preventing users from achieving their primary goal.

For each:
- **Problem:** [describe the issue]
- **Visual cause:** [why it happens visually]
- **Specific fix:** [what to change]

### Secondary Issues (P2)

List hierarchy issues that reduce clarity but don't block the primary goal.

For each:
- **Problem:** [describe the issue]
- **Visual cause:** [why it happens visually]
- **Specific fix:** [what to change]

### Contrast & Accessibility Flags

- Flag any text/background combinations that are likely failing WCAG AA contrast (describe the pairing).
- Flag any interactive elements that are not visually distinguishable from static content.
- Flag any color-only cues (information conveyed by color alone with no secondary visual indicator).

### Whitespace Assessment

- Is whitespace being used to create hierarchy and breathing room, or is it inconsistent?
- Identify the 2–3 most cramped areas and suggest specific spacing adjustments.

## Prioritized Fix List

Rank the top 5 changes that will have the highest impact on visual clarity.

For each:
- **What to change:** [specific change]
- **Why it matters:** [impact on user goal]
- **Effort:** [quick fix / medium effort / redesign required]

## Before/After Description

For the single highest-impact fix, describe what the element looks like **before** and **after** the change in enough detail that a designer could implement it without a Figma file.

## Pro Tips

- Include layout screenshots for more accurate analysis.
- Specify content priorities clearly so the audit focuses on the right elements.
- For responsive issues, request a breakpoint-specific audit.
- After implementing fixes, re-run the audit to validate improvements.
