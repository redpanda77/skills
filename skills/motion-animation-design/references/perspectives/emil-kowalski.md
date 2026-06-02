---
name: perspective-emil-kowalski
description: Restraint, speed, and purposeful motion. Best for productivity tools. Emil asks "Should this animate at all?"
---

# Emil Kowalski — Purposeful Restraint

Emil Kowalski (Linear, ex-Vercel) represents **restraint, speed, and purposeful motion**. His philosophy is best for productivity tools where users prioritize speed over delight.

**The question he asks:** *"Should this animate at all?"*

## Core Principles

### The Frequency Gate
Before adding any animation, ask how often the user triggers it:

| Frequency | Recommendation |
|-----------|----------------|
| Rare (monthly) | Delightful, expressive motion welcome |
| Occasional (daily) | Subtle, fast motion |
| Frequent (100s/day) | No animation or instant transition |
| Keyboard-initiated | Never animate |

### Speed Rules
- UI animations should be **under 300ms** — 180ms feels more responsive than 400ms
- The faster an animation, the less it gets in the way of the user's task
- Remove animations entirely for elements seen tens of times daily

### Origin-Aware Animations
Animations should originate from their logical source:

```css
/* Dropdown from button should expand from button, not center */
.dropdown {
  transform-origin: top center;
}
```

**Component library support:**
- Base UI: `--transform-origin` CSS variable
- Radix UI: `--radix-dropdown-menu-content-transform-origin`

### Scale on Press
Add immediate tactile feedback:

```css
button:active {
  transform: scale(0.97);
}
```

### Don't Animate from scale(0)
```jsx
// BAD: Unnatural motion
initial={{ scale: 0 }}

// GOOD: Natural, gentle motion
initial={{ scale: 0.9, opacity: 0 }}
animate={{ scale: 1, opacity: 1 }}
```

### Tooltip Delay Pattern
First tooltip in a group: delay + animation. Subsequent tooltips: instant.

```css
[data-instant] {
  transition-duration: 0ms;
}
```

### Blur as a Bridge
When state transitions aren't smooth enough, add blur to mask imperfections:

```css
.transitioning {
  filter: blur(2px);
}
```

## CSS Transitions vs Keyframes

### Interruptibility Problem
CSS keyframes can't be interrupted mid-animation. When users rapidly trigger actions, elements "jump" to new positions rather than smoothly retargeting.

**Solution**: Use CSS transitions with state-driven classes:

```jsx
useEffect(() => {
  setMounted(true);
}, []);
```

```css
.element {
  transform: translateY(100%);
  transition: transform 400ms ease;
}
.element.mounted {
  transform: translateY(0);
}
```

### Direct Style Updates for Performance
CSS variables cause style recalculation across all children. For frequent updates (drag operations), update styles directly:

```javascript
// BAD: CSS variable (expensive cascade)
element.style.setProperty('--drag-y', `${y}px`);

// GOOD: Direct style (no cascade)
element.style.transform = `translateY(${y}px)`;
```

### Momentum-Based Dismissal
Use velocity (distance / time) instead of distance thresholds:

```javascript
const velocity = dragDistance / elapsedTime;
if (velocity > 0.11) dismiss();
```

Fast, short gestures should work — users shouldn't need to drag far.

### Damping for Natural Boundaries
When dragging past boundaries, reduce movement progressively. Things in real life slow down before stopping.

## Spring Physics

### Key Parameters
| Parameter | Effect |
|-----------|--------|
| **Stiffness** | How quickly spring reaches target (higher = faster) |
| **Damping** | How quickly oscillations settle (higher = less bounce) |
| **Mass** | Weight of object (higher = more momentum) |

### Spring for Mouse Position
```javascript
const springConfig = { stiffness: 300, damping: 30 };
const x = useSpring(mouseX, springConfig);
const y = useSpring(mouseY, springConfig);
```

Use `useSpring` for any value that should interpolate smoothly rather than snap — nothing in the real world changes instantly.

### Interruptibility
Great animations can be interrupted mid-play:
- Framer Motion supports interruption natively
- CSS transitions allow smooth interruption before completion
- Test by clicking rapidly — animations should blend, not queue

## Easing Philosophy

- **Built-in CSS easing lacks strength** — `ease`, `ease-in-out` are too weak for professional results
- Always use custom Bezier curves from easing.dev or easings.co
- **Context matters**: A playful brand can use bouncy easing; a professional brand should use subtle springs or ease-out

## When to Apply Emil's Lens

Use Emil as the **primary** lens for:
- Productivity tools (Linear, Raycast)
- SaaS dashboards
- High-frequency workflows
- Forms, navigation, data entry

Use Emil as the **selective** lens for:
- Kids apps (only for high-frequency game interactions)
- Creative portfolios (only for high-frequency interactions)
- Marketing pages (only for forms, nav)

## See Also

- `references/principles/frequency-of-use.md` — frequency rule
- `references/principles/purposeful-animation.md` — purposeful motion
- `references/principles/hard-rules.md` — hard rules including scale and timing
- `references/anti-checklist.md` — AI-slop patterns Emil would flag
