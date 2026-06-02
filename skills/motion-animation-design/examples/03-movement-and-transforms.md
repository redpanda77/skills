# Movement & Transforms

Position, size, angle, and spatial feel.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Translate** | Movement along X or Y axis. | Prefer `x` and `y` transform aliases. |
| **Scale** | Element grows or shrinks as a whole. | `scaleX` / `scaleY` for single-axis control. |
| **Rotate** | Element turns around a chosen point. | `rotation` uses degree values. |
| **Skew** | Slanted transform that gives speed or distortion. | `skewX` / `skewY` with `clearProps` when needed. |
| **3D tilt / Flip** | Rotation around X/Y axis to create depth. | `rotationX` / `rotationY` with `perspective`. |
| **Perspective** | Depth setting that controls 3D strength. | Set `perspective` on the parent container. |
| **Transform origin** | Anchor point for scaling or rotation. | `transformOrigin: 'left top'`. |
| **Origin-aware animation** | Transition expands from trigger source, not center. | Set `transformOrigin` based on trigger position. |

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
  will-change: transform, opacity, filter, clip-path;
}

.actor.round {
  border-radius: 999px;
}

.line-path {
  position: absolute;
  width: min(520px, 72%);
  height: 2px;
  background: #ddd6ca;
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

.stack {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.trigger {
  position: absolute;
  left: 50%;
  bottom: 72px;
  transform: translateX(-50%);
  padding: 10px 14px;
  border: 0;
  border-radius: 8px;
  color: #fff;
  background: #171717;
}

.popover {
  width: 220px;
  padding: 16px;
  border: 1px solid #ddd6ca;
  border-radius: 8px;
  background: #fffefa;
  box-shadow: 0 18px 50px rgba(23, 23, 23, .12);
  transform-origin: 20% 100%;
}
```

## Animation Snippets

### Translate

```html
<div class="line-path"></div>
<div class="actor">XY</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 180, y: -90, duration: .65 })
  .to(".actor", { x: -160, y: 110, duration: .65 });
```

### Scale

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { scale: .32, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: .72, ease: "power3.out" });
```

### Rotate

```js
const tl = gsap.timeline();
tl.to(".actor", { rotation: 360, duration: 1.1, ease: "power2.inOut" });
```

### Skew

```js
const tl = gsap.timeline();
tl.to(".actor", { skewX: 24, x: 120, duration: .38, ease: "power2.in" })
  .to(".actor", { skewX: 0, x: 0, duration: .62, ease: "elastic.out(1, .42)" });
```

### 3D tilt / Flip

```js
const tl = gsap.timeline();
tl.to(".actor", { rotationY: 180, duration: .75, ease: "power3.inOut" })
  .to(".actor", { rotationX: 360, duration: .75, ease: "power3.inOut" });
```

### Perspective

```html
<div class="stack">
  <div class="tile">300</div>
  <div class="tile">900</div>
</div>
```

```js
gsap.set(".tile:first-child", { transformPerspective: 300 });
gsap.set(".tile:last-child", { transformPerspective: 900 });

const tl = gsap.timeline();
tl.to(".tile", { rotationY: 65, duration: .8, ease: "power3.inOut" });
```

### Transform origin

```html
<div class="stack">
  <div class="tile">L</div>
  <div class="tile">C</div>
  <div class="tile">R</div>
</div>
```

```js
gsap.set(".tile:nth-child(1)", { transformOrigin: "left bottom" });
gsap.set(".tile:nth-child(2)", { transformOrigin: "center center" });
gsap.set(".tile:nth-child(3)", { transformOrigin: "right top" });

const tl = gsap.timeline();
tl.to(".tile", { rotation: 70, scale: 1.18, duration: .78, ease: "back.out(1.6)" });
```

### Origin-aware animation

```html
<div class="popover">
  <b>Popover</b>
  <div class="card-line"></div>
  <div class="card-line short"></div>
</div>
<button class="trigger">Trigger</button>
```

```js
const tl = gsap.timeline();
tl.from(".popover", {
  y: 90,
  scale: .35,
  autoAlpha: 0,
  duration: .62,
  ease: "back.out(1.8)",
  transformOrigin: "50% 100%"
});
```
