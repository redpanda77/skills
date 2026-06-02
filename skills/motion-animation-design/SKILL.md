---
name: motion-animation-design
description: Applies motion design principles to UI animations and transitions. Use when user asks about CSS transitions, animations, easing, hover effects, popovers, modals, toasts, page transitions, Framer Motion, React animations, or any micro-interaction. Covers decision-making, best practices, and implementation guidance across CSS and JavaScript libraries.
---

# Motion Animation Design

**Complementary skills** — this skill is most effective when paired with stack-specific skills. On first invocation, recommend installing the relevant ones from `references/complementary-skills.md` locally in the project.

**Two modes** — read the matching workflow file and follow it exactly:

- **Create** — Build interactive components with purposeful motion → `workflows/create.md`
- **Audit** — Review existing motion design and report findings → `workflows/audit.md`

**Detect Mode**

| Signal | Mode |
|--------|------|
| "build", "create", "add animation", "animate", "implement", "make it feel" | **Create** |
| "audit", "review", "evaluate", "check", "feedback", "is this motion good" | **Audit** |
| Ambiguous | Ask user |

---

## Decision Framework

Classify the interaction before choosing a recipe:

1. **Trigger?**
   - User-initiated (click, hover, tap) → strong ease-out, immediate
   - System-initiated (loading, notification) → subtle, respect `prefers-reduced-motion`

2. **Lifecycle?**
   - Entering / exiting → strong ease-out, < 300ms, origin-aware
   - Already on screen, moving → ease-in-out, 300-500ms
   - Looping / ambient → linear, very slow

3. **Scale?**
   - Micro-interaction (button, toggle) → < 200ms
   - Content transition (list, card) → 200-400ms, staggered
   - Page / route transition → 300-600ms, directional
   - Hero / brand entrance → 400-800ms, staggered

4. **Frequency?**
   - Once per session → more expressive
   - Tens of times daily → shorter or remove

---

## The Three Designers

Load the weighted perspective(s) before generating or auditing:

- **Emil Kowalski** (Linear, ex-Vercel) — *"Should this animate at all?"* Restraint, speed, purposeful motion. Best for productivity tools.
- **Jakub Krehel** (jakub.kr) — *"Is this polished enough for production?"* Subtle production polish. Best for shipped consumer apps.
- **Jhey Tompkins** (@jh3yy) — *"What could this become?"* Playful experimentation. Best for creative sites, kids apps, portfolios.

**Context-to-Perspective Mapping**

| Project Type | Primary | Secondary | Selective |
|--------------|---------|-----------|-----------|
| Productivity tool | Emil | Jakub | Jhey (onboarding only) |
| Kids app / Educational | Jakub | Jhey | Emil (high-freq) |
| Creative portfolio | Jakub | Jhey | Emil (high-freq) |
| Marketing/landing page | Jakub | Jhey | Emil (forms, nav) |
| SaaS dashboard | Emil | Jakub | Jhey (empty states) |
| Mobile app | Jakub | Emil | Jhey (delighters) |
| E-commerce | Jakub | Emil | Jhey (product showcase) |

---

## The 7 Hard Rules

1. **NEVER animate from `scale(0)`** — use `scale(0.93)` or higher
2. **NEVER use `ease-in` for enter/exit** — use `ease-out` for responsiveness
3. **NEVER exceed 300ms for UI animations** — remove entirely for high-frequency elements
4. **Always make popovers origin-aware** — `transform-origin` at the trigger, not `center`
5. **Scale buttons on press** — `scale(0.97)` on `:active`, 150ms transition
6. **Skip tooltip delays after first show** — subsequent tooltips instant via `data-instant`
7. **Use `blur()` as a last resort** — mask imperfections with `filter: blur(2px)` during transition

**Critical:** Every animation must handle `prefers-reduced-motion`. No exceptions.

---

## Reference Index

**Load when needed. Do not read all at once.**

### Core Knowledge
- `references/perspectives/emil-kowalski.md` — Restraint, frequency gate, speed rules, interruptibility
- `references/perspectives/jakub-krehel.md` — Production polish, enter/exit blur, shadows, optical alignment, icon swaps, FLIP
- `references/perspectives/jhey-tompkins.md` — Playful experimentation, `linear()`, `@property`, 3D CSS, clip-path, scroll-driven
- `references/cookbook.md` — All motion recipes: enter/exit, easing, springs, clip-path, `@property`, FLIP, scroll-driven, button feedback, icon swaps, shared layout
- `references/creation-gotchas.md` — 20 common failure modes when writing motion
- `references/audit-checklist.md` — Systematic checklist for reviewing motion
- `references/anti-checklist.md` — AI-slop motion categories and anti-patterns

### Principles
- `references/principles/` — Hard rules, purposeful animation, directional consistency, spatial modeling, timing, staging, perceived performance, frequency, reduced motion, opacity, scaling

### Implementation
- `references/easing/` — Built-in easings, custom curves, decision table
- `references/transitions/` — Fundamentals, best practices, interruptibility
- `references/guidelines/` — Triggers, transition properties, hero entrance, scroll reveals, staggered lists, micro-interactions, enter/exit, gestures, layout, scroll triggers, performance, reduced motion, tool selection, timing table, specs
- `references/patterns/` — Hero entrance, scroll reveal, staggered list, modal, page transition, list navigation, micro-interactions, toast, expandable card, shared element, spring, looping, polish
- `references/material-design/` — Hierarchical transitions, peer transitions, container transform, choreography, enter/exit
- `references/implementation/` — CSS, Framer Motion, GSAP, bundle/performance, platform-specific, specs

### External
- `references/complementary-skills.md` — GSAP, LottieFiles, Emil Kowalski, Pixel Point Animate Text, and other skills
- `references/vocabulary.md` — Standard glossary of animation terms

### Workflows
- `workflows/create.md` — Build interactive components
- `workflows/audit.md` — Review existing motion

### Exercises
- `exercises/` — Simple transform, card hover, download arrow, toast component
