---
name: implementation-gsap
description: GSAP implementation for complex timelines, scroll-driven animations, and advanced sequencing.
---

# GSAP Implementation

GSAP is the industry standard for complex animation timelines. Use it when CSS or Framer Motion cannot express the animation.

## When to Use GSAP

- Complex choreographed timelines with multiple sequenced elements
- Scroll-driven animations with scrub control
- Advanced sequencing with precise timing control
- Animations that require plugins (morphing, physics, scroll-trigger)

## Basic Timeline

```javascript
gsap.timeline()
  .from(".hero-headline", { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" })
  .from(".hero-subtext", { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" }, "-=0.45")
  .from(".hero-cta", { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" }, "-=0.45");
```

## Key Points

- GSAP timelines allow precise control over sequencing and overlap
- The `"-=0.45"` syntax overlaps the next animation by 0.45 seconds
- Use `gsap.from()` for entrance animations and `gsap.to()` for exit animations
- GSAP is powerful but heavy. Use it only for complex timelines that CSS cannot express

## Complementary Skill

For GSAP-specific patterns, canonical syntax, and best practices, install the official GSAP skill: [github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills). It provides eight modular skills covering core API, timelines, ScrollTrigger, plugins, utilities, React integration, performance, and Vue/Svelte support. This skill covers the motion design decisions; the GSAP skill covers the library-specific implementation.
