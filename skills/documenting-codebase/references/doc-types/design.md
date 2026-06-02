---
name: doc-design
description: How to create DESIGN.md — the design system inventory. Use when documenting colors, typography, spacing, elevation, and component specs.
---

# Creating DESIGN.md

## Overview
DESIGN.md is the canonical design system inventory. It documents every token, typographic choice, spacing value, elevation shadow, and component variant. It lives in `docs/DESIGN.md`.

## Core Principle
DESIGN.md is the contract between design and engineering. Every token must be traceable to a real CSS variable or config value.

## When to Create
- The project has a custom design system or theme
- `globals.css`, `tailwind.config.js`, or a theme file exists
- UI components have multiple variants
- Mobile constraints exist (touch targets, safe areas, dark mode)

## Step-by-Step Creation

### 1. Inventory Color Tokens

Read the theme config file (e.g., `globals.css`, `tailwind.config.js`, `theme.ts`).

List every token in tables:

```markdown
## 1. Color Palette

### 1.1 Base Semantic Tokens

| Token | Light Value | Dark Value | Usage |
|-------|-------------|------------|-------|
| `--background` | `0 0% 100%` | `222.2 84% 4.9%` | Page background |
| `--foreground` | `222.2 84% 4.9%` | `210 40% 98%` | Primary text |
| `--primary` | `221.2 83.2% 53.3%` | `217.2 91.2% 59.8%` | Buttons, links, focus |
```

**Categories to inventory:**
- Base semantic (background, foreground, primary, secondary, muted, accent, destructive, border, input, ring)
- Context (home, srs, learn, review — or whatever contexts the app has)
- State (loading, empty, error, success, warning, info, selected, active, hover, focus, disabled)
- Custom (quiz, rating, any domain-specific tokens)

**Rules:**
- Always include both light and dark values
- Always include a usage column
- Group by category, not by file order
- Note any bugs (e.g., "BUG IN DARK MODE — should be X")

### 2. Inventory Typography

Read font imports and CSS rules:

```markdown
## 2. Typography

| Role | Font | Weight | Size | Line Height | Usage |
|------|------|--------|------|-------------|-------|
| Display | Satoshi | 600 | 1.75rem | 1.2 | Page titles |
| Headline | Satoshi | 600 | 1.5rem | 1.3 | Section headers |
| Body | Satoshi | 400 | 1rem | 1.5 | Descriptions |
| Chinese | Noto Sans SC | 400 | 1.125rem | 1.6 | Chinese text |
```

**Rules:**
- One row per typographic role
- Include font family, weight, size, line height, and usage
- Note mobile constraints (e.g., minimum 16px on inputs to prevent iOS zoom)

### 3. Inventory Spacing and Radius

```markdown
## 3. Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--space-sm` | `0.5rem` | Tight padding, chip gaps |
| `--space-md` | `1rem` | Standard gap, card internal spacing |
| `--space-lg` | `1.5rem` | Card padding, section gaps |

## 4. Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | `0.5rem` | Buttons, inputs, small controls |
| `--radius-md` | `0.7rem` | Cards, containers |
| `--radius-lg` | `1rem` | Modals, large panels |
| `--radius-full` | `9999px` | Badges, pills, avatars |
```

### 4. Inventory Elevation

```markdown
## 5. Elevation

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle hover |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.08)` | Card hover, ambient lift |
| `--shadow-lg` | `0 12px 24px rgba(0,0,0,0.12)` | Modals, floating elements |
| `--shadow-3d-primary` | `0 2px 0 hsl(var(--primary) / 0.3)` | 3D button depth |
```

### 5. Inventory Component Specs

Use GitNexus to understand component hierarchies before documenting:

```bash
# 360-degree view of shared primitives
npx gitnexus context Button
npx gitnexus context Card

# Impact analysis to find all consumers
npx gitnexus impact Button --direction upstream
```

For each major component, list variants in a table:

```markdown
## 6. Component Specs

### 6.1 Buttons

| Variant | Background | Text | Border | Radius | Shadow |
|---------|------------|------|--------|--------|--------|
| Primary | `--primary` | `--primary-foreground` | none | `--radius-sm` | `--shadow-3d-primary` |
| Secondary | `--secondary` | `--secondary-foreground` | none | `--radius-sm` | none |
| Outline | `--background` | `--foreground` | `--border` | `--radius-sm` | none |
| Destructive | `--destructive` | `--destructive-foreground` | none | `--radius-sm` | `--shadow-3d-destructive` |

### 6.2 Cards

| Variant | Background | Border | Radius | Shadow |
|---------|------------|--------|--------|--------|
| Default | `--card` | `--border` | `--radius-md` | `--shadow-sm` |
| Hover | `--card` | `--border` | `--radius-md` | `--shadow-md` |
```

**Rules:**
- Use GitNexus to understand component hierarchies before documenting
- One section per component (Button, Card, Input, Modal, Badge, etc.)
- Only document components with >2 variants
- Use token references, not raw values

### 6. Document Mobile Constraints

```markdown
## 7. Mobile Constraints

- `text-base` (16px) minimum on all mobile inputs to prevent iOS zoom.
- `user-select: none` on surfaces, `user-select: text` on inputs.
- Touch targets minimum 44px.
- Respect safe areas (`env(safe-area-inset-*)`).
- Dark mode at system level; theme switching in Settings.
```

## Verification Checklist
- [ ] Every color token has light and dark values
- [ ] Every token has a usage description
- [ ] Typography includes mobile constraints
- [ ] Spacing and radius are listed with values
- [ ] Elevation shadows are documented
- [ ] Component specs use token references, not raw values
- [ ] Mobile constraints are documented
- [ ] File is updated with date
