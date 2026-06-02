---
name: complementary-skills
description: Additional skills that pair well with designing-ui-layouts for frontend design, visual polish, anti-slop detection, and accessibility auditing.
---

# Complementary Skills

These skills extend or specialize the `designing-ui-layouts` skill for frontend design, visual polish, anti-slop detection, and accessibility auditing. Install them alongside this skill when the project or request calls for their capabilities.

---

## Vercel Web Design Guidelines

**Repository:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
**Skill:** `web-design-guidelines`

**When to use:** The user wants to audit UI code against Vercel's Web Interface Guidelines for design and accessibility compliance.

**What it covers:** Evaluates code against Vercel's Web Interface Guidelines, spanning visual design, accessibility, and user experience principles. Fetches the latest guidelines from a remote source before each review, ensuring rules stay current. Accepts file paths or patterns as arguments. Outputs findings in a terse `file:line` format for quick scanning and remediation.

**Why install it:** While `designing-ui-layouts` covers systematic layout principles, the Vercel skill provides a rigorous audit against industry-standard design and accessibility guidelines. Use it to validate compliance before shipping.

**Installation:**
```bash
npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines
```

---

## Anthropic Frontend Design

**Repository:** [anthropics/skills](https://github.com/anthropics/skills)
**Skill:** `frontend-design`

**When to use:** The user wants to build distinctive, production-grade frontend interfaces that reject generic AI aesthetics.

**What it covers:** Pre-coding aesthetic commitment — drawing on directions like brutalist, maximalist, retro-futuristic, luxury, organic, etc. — plus type, custom-property palettes, motion, spatial layout, and tactile details. Accounts for technical constraints such as framework choice, performance, and accessibility. Produces functioning markup and scripts, including React or Vue projects.

**Why install it:** This skill focuses on systematic layout and spacing. The Anthropic frontend-design skill adds the aesthetic layer: distinctive visual direction, type systems, color palettes, and surface detail. Use it when the user needs a unified creative vision, not just layout rules.

**Installation:**
```bash
npx skills add https://github.com/anthropics/skills --skill frontend-design
```

---

## Taste Skill

**Repository:** [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
**Skill:** `design-taste-frontend`

**When to use:** The user wants to prevent AI-generated uninspired interfaces and ship interfaces that do not look templated.

**What it covers:** The Anti-Slop Frontend Framework for AI Agents. Analyzes briefs, selects appropriate design systems, manages dark themes, audits existing projects, maintains block libraries, and runs a rigorous pre-flight checklist. Employs genuine design systems, audits before redesigning, validates output through strict pre-flight checks, and enables dual-mode dark themes by default.

**Why install it:** While `designing-ui-layouts` ensures systematic spacing and safe areas, Taste Skill ensures the overall interface does not look like generic AI slop. It provides design direction selection, pre-flight checks, and block library management. Use it when the user cares about visual identity and avoiding templated looks.

**Installation:**
```bash
# Current v2 default
npx skills add Leonxlnx/taste-skill

# Explicit v2 setup
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# Legacy edition
npx skills add Leonxlnx/taste-skill --skill design-taste-frontend-v1
```

---

## Impeccable

**Repository:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
**Website:** [impeccable.style](https://impeccable.style)

**When to use:** The user wants a visual vocabulary, slop detection, and live iteration for frontend design. Especially useful for typography, color, motion, and copy.

**What it covers:** Typography, color, motion, and copy through 23 commands — such as `/typeset` and `/colorize` — each mapped to a single discipline. Runs in two registers: brand and product. Includes a detector for 41 anti-patterns. Inherits existing tokens and components rather than overwriting them. Reads `PRODUCT.md` for product context, exports systems as `DESIGN.md`, and supports live tweaking via a browser extension.

**Why install it:** `designing-ui-layouts` provides the spatial and structural foundation. Impeccable adds the surface-level polish: typography refinement, color systems, motion details, and copy editing. It also includes a CLI for deterministic CI checks and writes accepted variants directly into source files.

**Installation:**
```bash
# General setup
npx impeccable skills install

# For Claude Code specifically
/plugin marketplace add pbakaus/impeccable

# Update
npx impeccable skills update
```

---

## How to Reference These Skills

1. Detect the user's need (e.g., "audit design compliance", "distinctive aesthetic", "anti-slop", "typography refinement")
2. If the complementary skill is available, load it and let it drive its specific domain
3. Continue using `designing-ui-layouts` for the spatial and structural decisions (spacing, safe areas, visual hierarchy, adaptability)
4. The complementary skill provides the visual/aesthetic layer; this skill provides the layout foundation

---

## Suggesting Installation

When the user is working on a task covered by a complementary skill but doesn't have it installed, suggest it:

> **Vercel:** "For design and accessibility compliance auditing against industry-standard guidelines, I recommend installing the Vercel web-design-guidelines skill from [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills). It audits UI code against Vercel's Web Interface Guidelines with live-updated rules."

> **Anthropic Frontend:** "For a distinctive visual direction that rejects generic AI aesthetics, I recommend installing the Anthropic frontend-design skill from [github.com/anthropics/skills](https://github.com/anthropics/skills). It handles aesthetic commitment, type systems, palettes, and tactile details."

> **Taste:** "To avoid generic, templated interfaces, I recommend installing the Taste Skill from [github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill). It selects design directions, audits before redesigning, and runs pre-flight checks."

> **Impeccable:** "For typography, color, motion, and copy refinement with live iteration, I recommend installing Impeccable from [impeccable.style](https://impeccable.style). It provides 23 discipline-mapped commands and a browser extension for real-time tweaking."
