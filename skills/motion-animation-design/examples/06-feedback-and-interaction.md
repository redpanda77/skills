# Feedback & Interaction

How the interface responds after user actions.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Hover effect** | Visual response when pointer rests over an element. | Trigger tweens on `mouseenter` and `mouseleave`. |
| **Press / Tap feedback** | Quick response while an element is being pressed. | `pointerdown` scale 0.96, restore on `pointerup`. |
| **Hold to confirm** | Press-and-hold with progress fill before confirming. | Play tween on `pointerdown`, reverse on `pointerup`. |
| **Drag** | Element follows the pointer, may continue with inertia. | `pointermove` with `quickTo` for smooth tracking. |
| **Drag to reorder** | Dragged item changes position while others make room. | Combine pointer events with FLIP-style transforms. |
| **Swipe to dismiss** | Horizontal swipe moves an item offscreen and removes it. | After x threshold, animate to outside the screen. |
| **Rubber-banding** | Boundary effect: movement gains resistance and snaps back. | Use a damped function to limit pointer delta. |
| **Shake / Wiggle** | Fast side-to-side motion signals an error or refusal. | Alternating `x` keyframes. |
| **Ripple** | Circular wave expands from the interaction point. | Create a circle and animate `scale` plus `autoAlpha`. |

## Common CSS

```css
.actor {
  width: clamp(86px, 15vw, 138px);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  border-radius: 8px;
  color: #fff;
  background: #2254d6;
  box-shadow: 0 20px 46px rgba(34, 84, 214, .24);
  font: 800 28px/1 monospace;
  will-change: transform, opacity;
}

.line-path {
  position: absolute;
  width: min(520px, 72%);
  height: 2px;
  background: #ddd6ca;
}

.card {
  width: min(360px, 80vw);
  min-height: 210px;
  padding: 18px;
  border: 1px solid #ddd6ca;
  border-radius: 8px;
  background: #fffefa;
  box-shadow: 0 18px 50px rgba(23, 23, 23, .12);
}

.card-line {
  height: 12px;
  margin-top: 12px;
  border-radius: 999px;
  background: #ddd6ca;
}

.stack {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.tile {
  width: 66px;
  height: 66px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  color: #fff;
  background: #0b7a55;
  box-shadow: 0 14px 30px rgba(11, 122, 85, .18);
  font: 800 17px/1 monospace;
}

.toast {
  width: 260px;
  padding: 16px;
  border: 1px solid #ddd6ca;
  border-radius: 8px;
  background: #fffefa;
  box-shadow: 0 18px 50px rgba(23, 23, 23, .12);
}
```

## Animation Snippets

### Hover effect

```js
const tl = gsap.timeline();
tl.to(".actor", {
  y: -22,
  scale: 1.08,
  boxShadow: "0 30px 70px rgba(34,84,214,.32)",
  duration: .5
}).to(".actor", { y: 0, scale: 1, duration: .5 });
```

### Press / Tap feedback

```js
const tl = gsap.timeline();
tl.to(".actor", { scale: .9, duration: .12, ease: "power2.out" })
  .to(".actor", { scale: 1, duration: .34, ease: "back.out(2.6)" });
```

### Hold to confirm

```html
<div class="card">
  <b>Hold to confirm</b>
  <div class="card-line" style="overflow:hidden;background:#ddd6ca">
    <span style="display:block;width:100%;height:100%;background:#c0362c;transform:scaleX(0);transform-origin:left"></span>
  </div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".card-line span", { scaleX: 1, duration: 1.25, ease: "none" });
```

### Drag

```html
<div class="line-path"></div>
<div class="actor">DR</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 170, y: -60, duration: .55 })
  .to(".actor", { x: -90, y: 90, duration: .6, ease: "power2.out" });
```

### Swipe to dismiss

```html
<div class="toast">
  <b>Notification</b>
  <div class="card-line"></div>
  <div class="card-line short"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".toast", { x: 420, rotation: 7, autoAlpha: 0, duration: .72, ease: "power3.in" });
```

### Rubber-banding

```html
<div class="line-path"></div>
<div class="actor">RB</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 130, duration: .45 })
  .to(".actor", { x: 190, duration: .32, ease: "power4.out" })
  .to(".actor", { x: 0, duration: .7, ease: "elastic.out(1, .42)" });
```

### Shake / Wiggle

```js
const tl = gsap.timeline();
tl.to(".actor", {
  keyframes: [{ x: -18 }, { x: 18 }, { x: -14 }, { x: 14 }, { x: -8 }, { x: 0 }],
  duration: .44,
  ease: "none"
});
```

### Ripple

```html
<div class="actor round">Tap</div>
<div class="actor round" style="position:absolute;background:#2254d6;opacity:.25"></div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".actor:nth-child(2)", { scale: .1, autoAlpha: .55 }, { scale: 2.5, autoAlpha: 0, duration: .8, ease: "power2.out" });
```
