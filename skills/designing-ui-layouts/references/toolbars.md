---
name: toolbar-guidelines
description: Toolbar design guidelines for iOS, iPadOS, and macOS, including item placement, grouping, and best practices.
---

# Toolbar Guidelines

## Overview

A toolbar provides convenient access to frequently used commands, controls, navigation, and search. It is arranged horizontally along the top or bottom edge of a view, grouped into logical sections.

**Key distinction:** A toolbar acts on content; a tab bar is for navigating between app areas.

## Types of Toolbar Content

- **Title:** Helps confirm location and differentiate between multiple windows.
- **Navigation controls:** Back, forward, close, search fields.
- **Actions:** Buttons, menus, bar items.

## Best Practices

### Item Selection
- Choose items deliberately to avoid overcrowding. People must distinguish and activate each item.
- Define which items move to the overflow menu as the toolbar narrows.
- **Do NOT add an overflow menu manually.** The system automatically adds it in macOS and iPadOS when items don't fit.
- Add a **More menu** only if necessary. Prioritize less important actions for it.
- Consider letting people customize the toolbar in iPadOS and macOS apps (especially for apps with many items or advanced functionality).

### Appearance
- Reduce the use of custom toolbar backgrounds and tinted controls. Use the content layer and `ScrollEdgeEffectStyle` to distinguish the toolbar from content.
- Avoid applying similar colors to toolbar item labels and content layer backgrounds. Prefer the default monochromatic appearance when content is already colorful.
- Prefer standard components. Ensure custom components have corner radii concentric with the bar's corners.
- Consider temporarily hiding toolbars for a distraction-free experience, but offer reliable ways to restore them.

## Titles

- Provide a concise, useful title for each window (aim for under 15 characters).
- Do NOT title windows with your app name.
- If titling seems redundant, you can leave the title area empty.

## Navigation

- Place navigation controls at the **top** of the window.
- Use standard Back and Close buttons. Prefer standard symbols without text labels.
- If creating custom versions, ensure they look and behave consistently with the system.

## Actions

- Prioritize commands people are most likely to want.
- Ensure the meaning of each control is clear. Prefer simple, recognizable symbols over text, except for actions like "edit" that aren't well-represented by symbols.
- Prefer system-provided symbols **without borders**. The section provides a visible container; the system handles hover and selection states.
- Use the **.prominent style** for one primary action (e.g., Done, Submit). Place it on the trailing side.

## Item Groupings

Position items in three areas: **leading edge**, **center area**, and **trailing edge**.

### Leading Edge
- Return-to-previous-document controls.
- Show/hide sidebar controls.
- View title.
- Document menu (Duplicate, Rename, Move, Export).
- **Not customizable.**

### Center Area
- Common, useful controls.
- View title (if not on leading edge).
- Customizable in macOS and iPadOS.
- Automatically collapses into the system overflow menu when the window shrinks.

### Trailing Edge
- Important items that must remain visible.
- Inspector buttons, search field, More menu.
- Primary action (Done, Submit).
- **Remains visible at all window sizes.**

## Grouping Rules

- Group items logically by function and frequency of use.
- Group navigation controls and critical actions (Done, Close, Save) in dedicated, visually distinct sections.
- Keep consistent groupings and placement across platforms.
- **Minimize the number of groups.** Aim for a maximum of three.
- Keep actions with text labels separate. Insert fixed space between text-labeled buttons to prevent them from appearing to run together.
