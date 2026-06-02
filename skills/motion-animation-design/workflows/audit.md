---
name: workflow-audit
description: Review existing motion design and produce a per-designer report. Reconnaissance first, then a full audit, then a structured report.
---

# Workflow: Audit Mode

Review existing motion design and produce a per-designer report. Reconnaissance first, then a full audit, then a structured report. Never apply rules blindly.

## Required Reading

Read as you reach each step (not all upfront):
1. `references/audit-checklist.md` — your systematic guide (STEP 2)
2. The weighted designer file(s) — `references/perspectives/emil-kowalski.md`, `references/perspectives/jakub-krehel.md`, `references/perspectives/jhey-tompkins.md` (STEP 2)
3. `references/principles/reduced-motion.md` — mandatory every audit (STEP 2)
4. `references/anti-checklist.md` — the quality gate: AI-slop motion categories + anti-patterns to flag (STEP 2)
5. `references/cookbook.md` — reference when making specific implementation recommendations

---

## STEP 1: Context Reconnaissance (DO THIS FIRST)

Before auditing any code, understand the project context.

### Gather Context

Check these sources:
1. **CLAUDE.md** — Any explicit context about the project's purpose or design intent
2. **package.json** — What type of app? (Next.js marketing site vs Electron productivity app vs mobile PWA)
3. **Existing animations** — Grep for `motion`, `animate`, `transition`, `@keyframes`. What durations are used? What patterns exist?
4. **Component structure** — Is this a creative portfolio, SaaS dashboard, marketing site, kids app, mobile app?

### Motion Gap Analysis (CRITICAL - Don't Skip)

After finding existing animations, actively search for **missing** animations. These are UI changes that happen without any transition:

**Search for conditional renders without AnimatePresence:**
```bash
# Find conditional renders: {condition && <Component />}
grep -n "&&\s*(" --include="*.tsx" --include="*.jsx" -r .

# Find ternary UI swaps: {condition ? <A /> : <B />}
grep -n "?\s*<" --include="*.tsx" --include="*.jsx" -r .
```

**For each conditional render found, check:**
- Is it wrapped in `<AnimatePresence>`?
- Does the component inside have enter/exit animations?
- If NO to both → this is a **motion gap** that needs fixing

**Common motion gap patterns:**
- `{isOpen && <Modal />}` — Modal appears/disappears instantly
- `{mode === "a" && <ControlsA />}` — Controls swap without transition
- `{isLoading ? <Spinner /> : <Content />}` — Loading state snaps
- `style={{ height: isExpanded ? 200 : 0 }}` — Height changes without CSS transition
- Inline styles with dynamic values but no `transition` property

**Where to look for motion gaps:**
- Inspector/settings panels with mode switches
- Conditional form fields
- Tab content areas
- Expandable/collapsible sections
- Toast/notification systems
- Loading states
- Error states

### State Your Inference

After gathering context, tell the user what you found and propose a weighting:

```
## Reconnaissance Complete

**Project type**: [What you inferred — e.g., "Kids educational app, mobile-first PWA"]
**Existing animation style**: [What you observed — e.g., "Spring animations (500-600ms), framer-motion, active:scale patterns"]
**Likely intent**: [Your inference — e.g., "Delight and engagement for young children"]

**Motion gaps found**: [Number] conditional renders without AnimatePresence
- [List the files/areas with gaps, e.g., "Settings panel mode switches", "Loading states"]

**Proposed perspective weighting**:
- **Primary**: [Designer] — [Why]
- **Secondary**: [Designer] — [Why]
- **Selective**: [Designer] — [When applicable]

Does this approach sound right? Should I adjust the weighting before proceeding with the full audit?
```

Use the Context-to-Perspective Mapping table in `SKILL.md` to propose the weighting.

### Wait for User Confirmation

**STOP and wait for the user to confirm or adjust.** Do not proceed to the full audit until they respond.

If `AskUserQuestion` is available, present the decision as tappable options:
- **Confirm weighting** — Proceed with the proposed primary/secondary/selective designers
- **Adjust primary** — Swap which designer is primary (e.g., prioritize delight over restraint)
- **Adjust secondary** — Change the secondary lens while keeping primary
- **Rebuild weighting** — The project type inference was wrong; start over

Otherwise ask in plain text: "Does this weighting sound right, or should I adjust?"

If they adjust (e.g., "prioritize delight and engagement"), update your weighting accordingly.

---

## STEP 2: Full Audit (After User Confirms)

Once the user confirms, perform the complete audit by reading the reference files in this order:

### 2a. Read the Audit Checklist First
**Read `references/audit-checklist.md`** — Use this as your systematic guide. It provides the structured checklist of what to evaluate.

### 2b. Read Designer Files for Your Weighted Perspectives
Based on your context weighting, read the relevant designer files:
- **Read `references/perspectives/emil-kowalski.md`** if Emil is primary/secondary — Restraint philosophy, frequency rules, decision frameworks
- **Read `references/perspectives/jakub-krehel.md`** if Jakub is primary/secondary — Production polish philosophy, what to check
- **Read `references/perspectives/jhey-tompkins.md`** if Jhey is primary/secondary — Playful experimentation philosophy, opportunities to surface

### 2c. Read Topical References as Needed
- **Read `references/principles/reduced-motion.md`** — MANDATORY. Always check for prefers-reduced-motion. No exceptions.
- **Read `references/anti-checklist.md`** — Apply this as the audit's quality gate. AI-slop categories at the top (pulsing indicators, hover-scale-on-everything, stagger-spam, etc.) trigger findings; perspective-specific and general anti-patterns sit below. Each category includes a frequency heuristic so single intentional uses don't trip the gate.
- **Read `references/guidelines/performance.md`** — If you see complex animations, check for GPU optimization issues
- **Read `references/cookbook.md`** — Reference when making specific implementation recommendations

---

## STEP 3: Output Format

The audit produces a structured report. The default is a **terminal-formatted markdown report**.

### Default behavior — write the report inline

Print the report as decorated markdown with:

1. **Executive summary** — 3-line summary: Critical / Important / Opportunities count
2. **Per-lens sections** — Each weighted designer gets their own section with:
   - Findings (categorized by severity)
   - What's working well (don't just criticize)
   - `Through [Designer]'s lens:` summary
3. **Motion gaps** — Separate section for missing animations
4. **Implementation recommendations** — Code fixes for each finding, drawn from `references/cookbook.md`

### Severity Levels

- **🔴 Critical** — Must fix. Missing `prefers-reduced-motion`, animating layout properties, no exit animations, motion gaps in primary UI, animating keyboard-initiated actions, high-frequency animations
- **🟡 Important** — Should fix. Exit as prominent as enter, missing blur, animating from `scale(0)`, default easing, wrong transform-origin
- **🟢 Opportunities** — Nice to have. Optical alignment, oklch gradients, spring animations, button press feedback, tooltip delay pattern

### Report Template

```markdown
# Motion Audit Report

## Executive Summary
- 🔴 {N} Critical findings
- 🟡 {N} Important findings
- 🟢 {N} Opportunities

## Motion Gaps
[List of conditional renders without animation, with file locations]

## Through Emil's Lens (Primary)
### Findings
- [Critical/Important] ...
### Working Well
- ...

## Through Jakub's Lens (Secondary)
### Findings
- [Critical/Important] ...
### Working Well
- ...

## Implementation Recommendations
For each finding, provide:
- What to change
- Why (with designer reference)
- Recommended code (from cookbook)
```

---

## Agent Gotchas (Self-Check Before Writing the Report)

Common failure modes during report generation:

- **Don't summarize per-lens findings.** Each section needs its own findings + working-well items + the `Through [Designer]'s lens:` summary.
- **Don't skip motion gaps.** Missing animations are often worse than poorly-tuned animations.
- **Don't flag single intentional uses.** The anti-checklist heuristics are designed to catch *frequency* and *uniformity*, not isolated instances.
- **Don't apply Emil's 300ms rule universally.** Check context weighting first — Jakub/Jhey may approve longer durations for polish or effect.
- **Don't forget to report what's working well.** An audit that only criticizes is less useful than one that validates good decisions too.

---

## Success Criteria

- [ ] Context gathered (CLAUDE.md, package.json, existing animations, structure)
- [ ] Motion gap analysis run — conditional renders checked for missing animation
- [ ] Weighting proposed and confirmed by the user
- [ ] Audit checklist worked through systematically
- [ ] Anti-checklist applied — AI-slop categories checked against the codebase
- [ ] Accessibility checked — prefers-reduced-motion verified (mandatory)
- [ ] Report follows the template with full per-lens sections
- [ ] What's working well is reported alongside findings
