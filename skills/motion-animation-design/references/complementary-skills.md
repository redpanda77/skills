---
name: complementary-skills
description: Additional skills that pair well with motion-animation-design for specific stacks, tools, or advanced use cases.
---

# Complementary Skills

These skills extend or specialize the motion-animation-design skill for specific libraries, frameworks, or advanced use cases. Install them alongside this skill when the project or request calls for their stack.

---

## GSAP

**Repository:** [github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills)

**When to use:** The user is working with GSAP (GreenSock Animation Platform) or asks for GSAP-specific implementations, timelines, ScrollTrigger, or advanced sequencing.

**What it covers:** Official AI skills for GSAP that instruct coding agents on correct GreenSock Animation Platform usage, best practices, and common animation patterns. Includes eight modular skills covering core API, timelines, ScrollTrigger, plugins, utilities, React integration, performance optimization, and Vue/Svelte lifecycle support.

**Why install it:** While `motion-animation-design` covers general principles and references GSAP in `references/implementation/gsap.md`, the GSAP skill provides canonical code patterns, quick-reference snippets, and agent-specific instructions for generating proper GSAP syntax across 40+ agent platforms.

**Installation:** Installable via CLI, plugin marketplaces, or manual directory copy. See the repository for instructions.

---

## LottieFiles Motion Design

**Repository:** [github.com/LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)

**When to use:** The user is creating UI animations, designing micro-interactions, building loading/success/error states, animating illustrations, planning scroll-triggered animations, or establishing brand motion identity.

**What it covers:** Universal motion design principles for AI agents. Philosophy-first and implementation-agnostic — works with any animation system (CSS, Framer Motion, GSAP, Lottie, Spring, etc.). Covers fundamental pillars, Disney's 12 principles adapted for UI, emotion-to-motion mapping, narrative structure, timing and easing tables, entrance/exit animations, state feedback, ambient/continuous motion, and an 8-step checklist.

**Why install it:** While `motion-animation-design` covers UI motion principles and implementation, the LottieFiles skill provides a broader motion-director philosophy ("think like motion directors") with Disney principles, motion personality archetypes, and the 1/3 Rule for choreography. It complements this skill by adding narrative and emotional layers to motion decisions.

**Installation:**
```bash
npx skills add LottieFiles/motion-design-skill
# Or:
npx skills add https://github.com/lottiefiles/motion-design-skill --skill motion-design
```

---

## Emil Kowalski's Skill

**Repository:** [emilkowal.ski/skill](https://emilkowal.ski/skill)

**When to use:** The user is working on animations, design, code, performance, or wants a broader interface design perspective. Especially useful for animation reviews and when you want Emil's own curated principles directly from his articles.

**What it covers:** A resource drawing from Emil Kowalski's personal articles on animations, design, code, performance, and more. It helps designers and engineers craft improved interfaces. Works with Claude Code, Codex, Cursor, and more.

**Why install it:** This skill already includes Emil's perspective in `references/perspectives/emil-kowalski.md`, but the original skill provides the author's own curated selection of principles and advice. The creator suggests applying it selectively rather than keeping it active constantly — animation reviews are a prime use case.

**Installation:**
```bash
npx skills add emilkowalski/skill
```

---

## Pixel Point — Animate Text

**Repository:** [pixel-point/animate-text](https://github.com/pixel-point/animate-text)
**Website:** [pixelpoint.io/skills/animate-text](https://pixelpoint.io/skills/animate-text)

**When to use:** The user wants beautiful text animations — kinetic typography, type reveals, staggered character/word animations, or any text-centric motion.

**What it covers:** Beautiful text animations, ready for any stack. Compatible with Remotion, Motion, GSAP, WAAPI, or comparable libraries. Provides clear animation specs including pacing, curves, transitions, and styling details rather than ambiguous directions.

**Why install it:** While `motion-animation-design` covers general motion principles and enter/exit animations, the Animate Text skill provides dedicated, production-ready text animation patterns with precise timing and curve specifications. Use it when the user specifically asks for text motion, kinetic typography, or type reveals.

**Installation:**
```bash
npx skills add pixel-point/animate-text --skill animate-text
```

---

## How to Reference These Skills

1. Detect the user's stack or request (e.g., "GSAP timeline", "ScrollTrigger", "GreenSock")
2. If the complementary skill is available, load it and let it drive the implementation details
3. Continue using `motion-animation-design` for the design decisions (timing, easing, context weighting, accessibility)
4. The complementary skill provides the library-specific syntax; this skill provides the motion design judgment

---

## Suggesting Installation

When the user is working with a stack covered by a complementary skill but doesn't have it installed, suggest it:

> **GSAP:** "For GSAP-specific patterns and syntax, I recommend installing the official GSAP skill from [github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills). It provides canonical code patterns and best practices for timelines, ScrollTrigger, and plugins. I'll continue using motion-animation-design for the design decisions (timing, easing, accessibility) while you install it."

> **LottieFiles:** "For broader motion-director philosophy — Disney principles, motion personality archetypes, and emotion-to-motion mapping — I recommend installing the LottieFiles motion-design skill from [github.com/LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill). It complements the principles here with narrative and emotional layers."

> **Emil Kowalski:** "For Emil's own curated principles on interface design, animation, and performance, I recommend installing his skill from [emilkowal.ski/skill](https://emilkowal.ski/skill). It's especially useful for animation reviews and restraint-focused design decisions."

> **Pixel Point Animate Text:** "For dedicated text animation patterns with precise timing and curve specs — kinetic typography, type reveals, staggered character animations — I recommend installing the Animate Text skill from [pixelpoint.io/skills/animate-text](https://pixelpoint.io/skills/animate-text). It works with Remotion, Motion, GSAP, or WAAPI."
