---
name: pattern-scroll-reveal
description: IntersectionObserver + CSS transition for scroll-triggered element reveals.
---

# Scroll Reveal

Reveal elements as they enter the viewport. Do not re-animate when scrolling back.

## Approach

IntersectionObserver + CSS transition.

## CSS

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

## Key Points

- Use `once: true` behavior so elements do not jitter when scrolling back and forth
- Disconnect the observer after the first trigger
- Transition: `0.5s ease-out` on `opacity` and `transform`
- Start from `translateY(24px)` and `opacity: 0`

## See Also

- `Examples/05-scroll.html` for scroll demos
- `references/guidelines/scroll-reveals.md`
