---
name: transitions-fundamentals
description: CSS transitions fundamentals — interpolation, the four properties, and basic syntax.
---

# CSS Transitions Fundamentals

CSS transitions interpolate between an initial and target state. Interpolation is the process of estimating unknown values that fall between known values. In the context of CSS transitions, it is the process of calculating the values between the initial and target state.

## The Four Transition Properties

The `transition` property is shorthand for four properties:

- `transition-property` — the property you want to transition. For example: `transform`, `opacity`, `background-color`, but also `all` to transition all properties
- `transition-duration` — the time it takes for the transition to complete. For example: `200ms`, `1s`
- `transition-timing-function` — the easing you want to apply. For example: `ease`, `ease-in`, `cubic-bezier(0.19, 1, 0.22, 1)`
- `transition-delay` — the time to wait before the transition starts. For example: `200ms`, `1s`

## Basic Syntax

```css
.button {
  /* Transition transform over 200ms with ease and a delay of 100ms */
  transition: transform 200ms ease 100ms;
}

.box {
  /* We can optionally add a delay after the timing-function */
  transition: transform 0.2s ease;
}
```

This means that our transform will be interpolated from one state to another over `0.2s` with the `ease` easing.
