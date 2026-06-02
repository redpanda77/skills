---
name: pattern-staggered-list
description: Staggered list animation with CSS transition-delay or Framer Motion staggerChildren.
---

# Staggered List

Animate several items one after another with a small delay between each.

## Approach A: CSS transition-delay

```css
.list-item {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.3s ease-out, transform 0.3s ease-out;
}

.list-item.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.list-item:nth-child(1) { transition-delay: 0ms; }
.list-item:nth-child(2) { transition-delay: 80ms; }
.list-item:nth-child(3) { transition-delay: 160ms; }
```

## Approach B: Framer Motion staggerChildren

```jsx
const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.08 }
  }
};

const item = {
  hidden: { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0 }
};

<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map(i => (
    <motion.li key={i} variants={item} />
  ))}
</motion.ul>
```

## Key Points

- Keep gaps tight: 60-100ms between items
- For dynamic collections, multiply the item index to set inline delays
- Longer pauses make the group feel sluggish

## See Also

- `Examples/02-sequencing-and-timing.html` for stagger demos
- `references/guidelines/staggered-lists.md`
