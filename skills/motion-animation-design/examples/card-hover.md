---
name: exercise-card-hover
description: Reveal a hidden project description on hover. Learn overflow hidden, calc, and focus-visible.
---

# Exercise: Card Hover

## Goal

Start with a hidden description of a project and reveal it when you hover over the card. Use a transform only.

## The Problem

A simple `translateY(100%)` does not work because there is additional margin around the description. We also need to handle keyboard navigation.

## The Solution

Use `overflow: hidden` on the card, `calc()` for precise positioning, and `:focus-visible` for accessibility.

```css
.card {
  width: 340px;
  height: 340px;
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  text-decoration: none;
}

.card-description {
  --margin: 6px;
  margin: var(--margin);
  transform: translateY(calc(100% + var(--margin) + 1px));
  transition: transform 500ms cubic-bezier(0.19, 1, 0.22, 1);
}

.card:hover .card-description,
.card:focus-visible .card-description {
  transform: translateY(0);
}
```

## Key Takeaways

- `overflow: hidden` prevents the description from being visible outside the card bounds
- `calc()` accounts for margins and borders for precise positioning
- `:focus-visible` applies only during keyboard navigation, unlike `:focus` which also applies on click
- A strong easing like `ease-out-expo` (`cubic-bezier(0.19, 1, 0.22, 1)`) creates an elegant feel
- 500ms might feel long in theory, but the steep easing curve at the beginning makes it feel snappy
- See `Examples/06-feedback-and-interaction.html` for interaction demos
