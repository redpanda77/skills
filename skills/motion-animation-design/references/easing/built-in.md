---
name: easing-built-in
description: All built-in CSS easing functions, when to use each, and when to avoid them.
---

# Built-in CSS Easings

## ease-out

Use for **user-initiated interactions** where the element enters or exits the screen. The acceleration at the beginning gives a feeling of responsiveness.

Apply to dropdowns, modals, tooltips, and button presses.

```css
.dropdown {
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
```

## ease-in-out

Use for **elements already on screen** that move to a new position or morph into a new shape. The curve mimics natural acceleration and deceleration, like a car starting and stopping.

Good for: timeline components, page morphs, dynamic islands, any on-screen resize/reposition.

```css
.timeline {
  transition: width 0.3s cubic-bezier(0.65, 0, 0.35, 1);
}
```

## ease

Use for **hover effects** and small, elegant transitions (color, background-color, opacity). Asymmetric: starts faster and ends slower than `ease-in-out`. It is the default timing function for CSS transitions.

```css
.button {
  transition: background-color 0.2s ease;
}
```

## linear

Use only for **constant animations** or time visualization: marquees, progress bars, hold-to-delete interactions, 3D coin rotations. Avoid for UI enter/exit because it feels robotic.

```css
.marquee {
  animation: scroll 10s linear infinite;
}
```

## Why Easing Matters

Completely linear motion looks weird and unnatural to users. An object that moves across the screen at the exact same speed the entire time feels less natural than one that subtly speeds up or down over time.

This impression has a lot to do with how objects move in the physical world. We do not often see things moving at a perfectly steady speed — they tend to accelerate and decelerate when they start and stop moving.

## Easing Terminology

Most frequently, you will want to use an **ease-out** animation — it starts quickly but slows down. This makes the animation feel responsive, but allows the eye time to focus on the element as it comes to rest.

**Ease-in** and **ease-in-out** are sometimes used for elements leaving the screen, but that sort of easing curve can feel unresponsive if the initial motion takes a while to get going.

While the terminology may seem confusing (ease-out is used when something enters the frame, and ease-in is used when something leaves):
- **Ease-out on entrance** means the object slows down before it comes to rest, allowing the eye to predict where it will stop
- **Ease-in on exit** means the object speeds up as it moves out of frame, feeling like it is accelerating away

## Material Design Asymmetric Curve

According to Material Design Guidelines, it is better to use an asymmetric curve to make the movement look more natural and realistic. The end of the curve must be more emphasized than its beginning, so that the duration of acceleration is shorter than that of slowing down.

In this case, the user will pay more attention to the final movement of the element and thus to its new state.

## Ease-in

**Avoid for UI animations.** It starts slow and ends fast, making interfaces feel sluggish. The acceleration at the end is the opposite of what users expect — they want things to settle, not speed up.

Use ease-in only when objects fly out of the screen at full speed and cannot be recalled or returned — such as system notifications or cards being thrown away.

## Why Easing Matters

Completely linear motion looks weird and unnatural to users. An object that moves across the screen at the exact same speed the entire time feels less natural than one that subtly speeds up or down over time.

This impression has a lot to do with how objects move in the physical world. We do not often see things moving at a perfectly steady speed — they tend to accelerate and decelerate when they start and stop moving.

## Easing Terminology

Most frequently, you will want to use an **ease-out** animation — it starts quickly but slows down. This makes the animation feel responsive, but allows the eye time to focus on the element as it comes to rest.

**Ease-in** and **ease-in-out** are sometimes used for elements leaving the screen, but that sort of easing curve can feel unresponsive if the initial motion takes a while to get going.

While the terminology may seem confusing (ease-out is used when something enters the frame, and ease-in is used when something leaves):
- **Ease-out on entrance** means the object slows down before it comes to rest, allowing the eye to predict where it will stop
- **Ease-in on exit** means the object speeds up as it moves out of frame, feeling like it is accelerating away

## Material Design Asymmetric Curve

According to Material Design Guidelines, it is better to use an asymmetric curve to make the movement look more natural and realistic. The end of the curve must be more emphasized than its beginning, so that the duration of acceleration is shorter than that of slowing down.

In this case, the user will pay more attention to the final movement of the element and thus to its new state.
