---
name: guidelines-scroll-reveals
description: Scroll-triggered reveal animations using IntersectionObserver with once:true behavior.
---

# Scroll-Triggered Reveals

Reveal elements as they enter the viewport. Use `IntersectionObserver` with `once: true` so elements do not jitter when scrolling back and forth.

## Implementation

- Transition: `0.5s ease-out` on `opacity` and `transform`
- Start from `translateY(24px)` and `opacity: 0`
- Disconnect the observer after the first trigger

## CSS Example

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}

.reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

## JavaScript

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

## Principle

Elements that animate in and out as you scroll back and forth feel jittery and unintentional. The `once: true` behavior is important for a polished feel.

## See Also

- `Examples/05-scroll.html` for scroll demos
- `references/patterns/scroll-reveal.md` for full implementation
