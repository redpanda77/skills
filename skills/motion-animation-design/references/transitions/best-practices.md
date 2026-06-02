---
name: transitions-best-practices
description: Best practices for writing CSS transitions — explicit properties, avoiding all, shorthand rules, and hover on touch devices.
---

# CSS Transitions Best Practices

## Always Write Out `ease` Explicitly

`ease` is the default timing-function, but a lot of people think it is `linear`. Being explicit about it prevents confusion.

```css
.box {
  transition: transform 0.2s ease;
}
```

## Never Use the `all` Keyword

We often transition a few properties at once, like `transform` and `opacity`. Being explicit about what property we are transitioning ensures that we do not transition any other property that might potentially change.

## Shorthand with `transition-property`

If you are animating a lot of properties with the same duration and easing, you can define it once with shorthand and complement with `transition-property`:

```css
/* More repetition */
.button {
  transition:
    color 0.2s ease,
    background-color 0.2s ease,
    border-color 0.2s ease;
}

/* Less repetition, more consistency */
.button {
  transition: 0.2s ease;
  transition-property: color, background-color, border-color;
}
```

## Avoid Shorthand for `transition-delay`

Reading `transition: transform 0.2s ease 1s` is confusing. When you see `transition-delay: 1s` you know exactly what it does.

## Disable Hover on Touch Devices

Many CSS transitions are triggered by hovering. On touch devices, tapping an interactive element also triggers the hover state, which is usually accidental and annoying.

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    background: blue;
  }
}
```

In Tailwind v3, enable `hoverOnlyWhenSupported` in your config:

```javascript
// tailwind.config.js
module.exports = {
  future: {
    hoverOnlyWhenSupported: true,
  },
}
```

In Tailwind v4, this is the default behavior.

## Tailwind Configuration

Tailwind v4 handles hover-on-touch automatically. For v3, enable `hoverOnlyWhenSupported` in config:

```javascript
// tailwind.config.js
module.exports = {
  future: {
    hoverOnlyWhenSupported: true,
  },
}
```
