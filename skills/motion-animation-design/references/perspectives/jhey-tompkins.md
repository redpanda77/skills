---
name: perspective-jhey-tompkins
description: Playful experimentation, CSS innovation, and creative learning. Best for creative sites, kids apps, and portfolios. Jhey asks "What could this become?"
---

# Jhey Tompkins — Playful Experimentation

Jhey Tompkins (@jh3yy) represents **playful experimentation and CSS innovation**. His philosophy is best for creative sites, kids apps, and portfolios where delight and discovery are the goals.

**The question he asks:** *"What could this become?"*

## Core Principles

### Duration is Context-Dependent
> "Duration is all about timing, and timing has a big impact on the movement's naturalness."

For creative/kids/playful contexts, duration is whatever serves the effect. The 300ms productivity rule doesn't apply here.

### Easing as Communication
Each easing curve communicates something to the viewer. **Context matters more than rules.**

| Easing | Feel | Good For |
|--------|------|----------|
| `ease-out` | Fast start, gentle stop | Elements entering view (arriving) |
| `ease-in` | Gentle start, fast exit | Elements leaving view (departing) |
| `ease-in-out` | Gentle both ends | Elements changing state while visible |
| `linear` | Constant speed | Continuous loops, progress indicators |
| `spring` | Natural deceleration | Interactive elements, professional UI |

**The Context Rule**:
> "You wouldn't use 'Elastic' for a bank's website, but it might work perfectly for an energetic site for children."

Brand personality should drive easing choices. A playful brand can use bouncy, elastic easing. A professional brand should use subtle springs or ease-out.

### The linear() Function
CSS `linear()` enables bounce, elastic, and spring effects in pure CSS:

```css
:root {
  --bounce-easing: linear(
    0, 0.004, 0.016, 0.035, 0.063, 0.098, 0.141 13.6%, 0.25, 0.391, 0.563, 0.765,
    1, 0.891 40.9%, 0.848, 0.813, 0.785, 0.766, 0.754, 0.75, 0.754, 0.766, 0.785,
    0.813, 0.848, 0.891 68.2%, 1 72.7%, 0.973, 0.953, 0.941, 0.938, 0.941, 0.953,
    0.973, 1, 0.988, 0.984, 0.988, 1
  );
}
```

Use Jake Archibald's linear() generator for custom curves: https://linear-easing-generator.netlify.app/

### Stagger Techniques
`animation-delay` only applies once (not per iteration). Approaches:

1. **Different delays with finite iterations** — Works for one-time sequences
2. **Pad keyframes** to create stagger within the animation:

```css
@keyframes spin {
  0%, 50% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

3. **Negative delays** for "already in progress" effects:

```css
.element { animation-delay: calc(var(--index) * -0.2s); }
```

This makes animations appear mid-flight from the start — useful for staggered continuous animations.

### CSS Custom Properties & @property

#### Type Specification Unlocks Animation
The `@property` rule lets you declare types for CSS variables, enabling smooth interpolation:

```css
@property --hue {
  initial-value: 0;
  inherits: false;
  syntax: '<number>';
}

@keyframes rainbow {
  to { --hue: 360; }
}
```

**Available types**: length, number, percentage, color, angle, time, integer, transform-list

**Why this matters**: Without `@property`, CSS sees custom properties as strings. Strings can't interpolate — they just swap. With a declared type, the browser knows how to smoothly transition between values.

#### Decompose Complex Transforms
Instead of animating a monolithic transform (which can't interpolate curved paths), split into typed properties:

```css
@property --x { syntax: '<percentage>'; initial-value: 0%; inherits: false; }
@property --y { syntax: '<percentage>'; initial-value: 0%; inherits: false; }

.ball {
  transform: translateX(var(--x)) translateY(var(--y));
  animation: throw 1s;
}

@keyframes throw {
  0% { --x: -500%; }
  50% { --y: -250%; }
  100% { --x: 500%; }
}
```

This creates curved motion paths that would be impossible with standard transform animation — the ball arcs through space rather than moving in straight lines.

#### Scoped Variables for Dynamic Behavior
CSS custom properties respect scope, enabling powerful patterns:

```css
.item { --delay: 0; animation-delay: calc(var(--delay) * 100ms); }
.item:nth-child(1) { --delay: 0; }
.item:nth-child(2) { --delay: 1; }
.item:nth-child(3) { --delay: 2; }
```

Use scoped variables to create varied behavior from a single animation definition.

## 3D CSS

### Think in Cuboids
> "Think in cubes instead of boxes" — Jhey Tompkins

Complex 3D scenes are assemblies of cube-shaped elements (like LEGO). Decompose any 3D object into cuboids.

### Essential Setup
```css
.scene {
  transform-style: preserve-3d;
  perspective: 1000px;
}
```

### Responsive 3D
Use CSS variables for dimensions and `vmin` units:

```css
.cube {
  --size: 10vmin;
  width: var(--size);
  height: var(--size);
}
```

## Clip-Path Animations

### Why clip-path?
- Hardware-accelerated rendering
- No layout shifts
- No additional DOM elements needed
- Smoother than width/height animations

### Basic Syntax
```css
clip-path: inset(top right bottom left);
clip-path: circle(radius at x y);
clip-path: polygon(coordinates);
```

### Image Reveal Effect
```css
.reveal {
  clip-path: inset(0 0 100% 0); /* Hidden */
  animation: reveal 1s forwards cubic-bezier(0.77, 0, 0.175, 1);
}

@keyframes reveal {
  to { clip-path: inset(0 0 0 0); } /* Fully visible */
}
```

### Tab Transitions
Duplicate tab lists with different styling. Animate the overlay's clip-path to reveal only the active tab — creates smooth color transitions without timing issues.

### Scroll-Driven with clip-path
```javascript
const clipPathY = useTransform(scrollYProgress, [0, 1], ["100%", "0%"]);
const motionClipPath = useMotionTemplate`inset(0 0 ${clipPathY} 0)`;
```

### Text Mask Effect
Stack elements with complementary clip-paths:
```css
.top { clip-path: inset(0 0 50% 0); }    /* Shows top half */
.bottom { clip-path: inset(50% 0 0 0); } /* Shows bottom half */
```
Adjust values on mouse interaction for seamless transitions.

## Scroll-Driven Animations

### The Core Problem
Scroll-driven animations are tied to scroll **speed**. If users scroll slowly, animations play slowly. This feels wrong for most UI — you want animations to trigger at a scroll position, not be controlled by scroll speed.

### Duration Control Pattern
Use two coordinated animations:
1. **Trigger animation**: Scroll-driven, toggles a custom property when element enters view
2. **Main animation**: Traditional duration-based, activated via Style Query

This severs the connection between scroll speed and animation timing — the animation runs over a fixed duration once triggered, regardless of how fast the user scrolled.

### Progressive Enhancement
Always provide fallbacks:
```javascript
// IntersectionObserver fallback for browsers without scroll-driven animation support
if (!CSS.supports('animation-timeline', 'scroll()')) {
  // Use IntersectionObserver instead
}
```

## Learning Philosophy

### Filter Ideas Later, Not During Creation
- Don't filter ideas based on "usefulness" too early — make first, judge later
- Document random creative sparks — keep notebooks everywhere, including by your bed

### CSS Art is Not Useless
- CSS art teaches real skills: clip-path, layering, complex shapes
- What you learn making "useless" things transfers directly to production work

### Let Ideas Drive Learning
- Don't ask "How do I learn X?" — ask "How do I make Y?"
- Let the project drive which techniques you learn

### Experiment After Tutorials
- Tutorials teach techniques; experimentation teaches problem-solving
- Following tutorials without experimenting is just copying

### The Struggle is Learning
- Giving up when something doesn't work is the real failure
- The struggle is where learning happens

## When to Apply Jhey's Lens

Use Jhey as the **primary** lens for:
- Creative portfolios
- Kids apps / educational
- Marketing/landing pages with delight moments

Use Jhey as the **secondary** lens for:
- Productivity tools (onboarding only)
- SaaS dashboards (empty states)
- Mobile apps (delighters)
- E-commerce (product showcase)

## See Also

- `references/patterns/looping-ambient.md` — ambient motion
- `references/patterns/scroll-reveal.md` — scroll-triggered effects
- `references/patterns/polish-effects.md` — blur, shimmer, line drawing
- `references/anti-checklist.md` — patterns Jhey would flag
