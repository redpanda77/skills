---
name: perspective-jakub-krehel
description: Subtle production polish, professional refinement. Best for shipped consumer apps. Jakub asks "Is this subtle and polished enough for production?"
---

# Jakub Krehel — Production Polish

Jakub Krehel (jakub.kr) represents **subtle production polish and professional refinement**. His philosophy is best for shipped consumer apps where the bar for polish is high.

**The question he asks:** *"Is this subtle and polished enough for production?"*

## Core Principles

### The Best Animation Goes Unnoticed
> "The best animation is that which goes unnoticed."

If users comment "nice animation!" on every interaction, it's probably too prominent for production. (Exception: kids apps and playful contexts where delight IS the goal.)

### Duration Guidelines
- **200-500ms** for smoothness in production UI
- Smaller elements should animate faster
- Larger and complex elements look better when they last a little longer

### Enter Animation Recipe
A standard enter animation combines three properties:
- **Opacity**: 0 → 1
- **TranslateY**: ~8px → 0 (or calc(-100% - 4px) for full container slides)
- **Blur**: 4px → 0px

```jsx
initial={{ opacity: 0, translateY: "calc(-100% - 4px)", filter: "blur(4px)" }}
animate={{ opacity: 1, translateY: 0, filter: "blur(0px)" }}
transition={{ type: "spring", duration: 0.45, bounce: 0 }}
```

**Why blur?** It creates a "materializing" effect that feels more physical than opacity alone. The element appears to come into focus, not just fade in.

### Exit Animation Subtlety
**Key Insight**: Exit animations should be subtler than enter animations.

When a component exits, it doesn't need the same amount of movement or attention as when entering. The user's focus is moving to what comes next, not what's leaving.

```jsx
// Instead of full exit movement:
exit={{ translateY: "calc(-100% - 4px)" }}

// Use a subtle fixed value:
exit={{ translateY: "-12px", opacity: 0, filter: "blur(4px)" }}
```

**Why this works**: Exits become softer, less jarring, and don't compete for attention with whatever is entering or remaining.

**When NOT to use subtle exits**:
- When the exit itself is meaningful (user-initiated dismissal)
- When you need to emphasize something leaving (error clearing, item deletion)
- Full-page transitions where directional continuity matters

### Spring Animations
Prefer spring animations over linear/ease for more natural-feeling motion:

```jsx
transition={{ type: "spring", duration: 0.45, bounce: 0 }}
transition={{ type: "spring", duration: 0.55, bounce: 0.1 }}
```

**Why `bounce: 0`?** It gives smooth deceleration without overshoot — professional and refined. Reserve bounce > 0 for playful contexts.

### Shadows Instead of Borders
In light mode, prefer subtle multi-layer box-shadows over solid borders:

```css
.card {
  box-shadow:
    0px 0px 0px 1px rgba(0, 0, 0, 0.06),
    0px 1px 2px -1px rgba(0, 0, 0, 0.06),
    0px 2px 4px 0px rgba(0, 0, 0, 0.04);
}

/* Slightly darker on hover */
.card:hover {
  box-shadow:
    0px 0px 0px 1px rgba(0, 0, 0, 0.08),
    0px 1px 2px -1px rgba(0, 0, 0, 0.08),
    0px 2px 4px 0px rgba(0, 0, 0, 0.06);
}
```

**Why shadows over borders?**
- Shadows adapt to any background (images, gradients, varied colors) because they use transparency
- Borders are solid colors that may clash with dynamic backgrounds
- Multi-layer shadows create depth; single borders feel flat
- Shadows can be transitioned smoothly with `transition: box-shadow`

**When borders are fine**:
- Dark mode (shadows less visible anyway)
- When you need hard edges intentionally
- Simple interfaces where depth isn't needed

### Gradients & Color Spaces
- Use `oklch` for gradients to avoid muddy midpoints:

```css
element { background: linear-gradient(in oklch, blue, red); }
```

- **Color hints** control where the blend midpoint appears (different from color stops)
- Layer gradients with `background-blend-mode` for unique effects

**Why oklch?** It interpolates through perceptually uniform color space, avoiding the gray/muddy zone that sRGB hits when blending complementary colors.

### Blur as a Signal
Blur (via `filter: blur()`) combined with opacity and translate creates a "materializing" effect. Use blur to signal:
- **Entering focus**: blur → sharp
- **Losing relevance**: sharp → blur
- **State transitions**: blur during, sharp after

## Optical Alignment

### Geometric vs. Optical
> "Sometimes it's necessary to break out of geometric alignment to make things feel visually balanced."

**Buttons with icons**: Reduce padding on the icon side so content appears centered:

```
[  Icon Text  ] ← Geometric (mathematically centered, feels off)
[ Icon Text   ] ← Optical (visually centered, feels right)
```

**Play button icons**: The triangle points right, creating visual weight on the left. Shift it slightly right to appear centered.

**Icons in general**: Many icon packs account for optical balance, but asymmetric shapes (arrows, play, chevrons) may need manual margin/padding adjustment.

**The rule**: If it looks wrong despite being mathematically correct, trust your eyes and adjust.

## Icon & State Animations

### Contextual Icon Transitions
When icons change contextually (copy → check, loading → done), animate:
- Opacity
- Scale
- Blur

```jsx
<AnimatePresence mode="wait">
  {isCopied ? (
    <motion.div
      initial={{ opacity: 0, scale: 0.8, filter: "blur(4px)" }}
      animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }}
      exit={{ opacity: 0, scale: 0.8, filter: "blur(4px)" }}
    >
      <CheckIcon />
    </motion.div>
  ) : (
    <motion.div ...>
      <CopyIcon />
    </motion.div>
  )}
</AnimatePresence>
```

**Why animate icon swaps?** Instant swaps feel jarring and can be missed. Animated transitions:
- Draw attention to the state change
- Feel responsive and polished
- Give the user confidence their action registered

## Shared Layout Animations

### FLIP Technique via layoutId
Motion's `layoutId` prop enables smooth transitions between completely different components:

```jsx
// In one location:
<motion.div layoutId="card" className="small-card" />

// In another location:
<motion.div layoutId="card" className="large-card" />
```

Motion automatically animates between them using the FLIP technique (First, Last, Inverse, Play).

### Best Practices
- Keep elements with `layoutId` **outside** of `AnimatePresence` to avoid conflicts
- If inside `AnimatePresence`, the initial/exit animations will trigger during layout animation (looks bad with opacity)
- Multiple elements can animate if each has a unique `layoutId`
- Works for different heights, widths, positions, and even component types (card → modal)

## When to Apply Jakub's Lens

Use Jakub as the **primary** lens for:
- Shipped consumer apps
- Mobile apps
- E-commerce
- Marketing/landing pages
- Creative portfolios

Use Jakub as the **secondary** lens for:
- Productivity tools (alongside Emil)
- SaaS dashboards (alongside Emil)
- Kids apps (alongside Jhey)

## See Also

- `references/patterns/polish-effects.md` — blur, shadows, gradients
- `references/patterns/micro-interactions.md` — hover, press, icon swaps
- `references/patterns/shared-element.md` — layoutId transitions
- `references/patterns/spring-animations.md` — spring physics
- `references/anti-checklist.md` — patterns Jakub would flag
