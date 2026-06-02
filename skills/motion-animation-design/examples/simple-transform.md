---
name: exercise-simple-transform
description: Move a box 20% upwards on hover. Learn the hover flicker problem and the child-element solution.
---

# Exercise: Simple Transform

## Goal

Move a box 20% upwards on hover. You can choose your own duration and easing.

## The Problem

When you hover on the box and move it up, the cursor may no longer be on the box, causing the hover state to flicker on and off.

## The Solution

Animate a child element instead. The parent stays in place, so the hover state remains active.

```jsx
export default function SimpleTransformTransition() {
  return (
    <div className="box">
      <div className="box-inner" />
    </div>
  );
}
```

```css
.box {
  height: 56px;
  width: 56px;
}

.box:hover .box-inner {
  transform: translateY(-20%);
}

.box-inner {
  height: 100%;
  width: 100%;
  background: #fad655;
  border-radius: 50%;
  transition: transform 200ms ease;
}
```

## Key Takeaways

- Use `transition: transform 200ms ease` on the element being animated
- Apply the hover state to the parent, but animate the child
- This prevents the hover flicker problem
- See `Examples/06-feedback-and-interaction.html` for interaction demos
