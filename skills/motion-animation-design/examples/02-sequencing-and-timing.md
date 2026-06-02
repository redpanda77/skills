# Sequencing & Timing

How multiple elements queue, delay, and synchronize.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Keyframes** | Key states at specific moments; in-between frames generated automatically. | `gsap.to` supports a `keyframes` array. |
| **Interpolation / Tween** | Generated in-between values from start to end state. | `fromTo` for explicit start and end values. |
| **Stagger** | Group of elements starts one after another, creating a cascade. | `stagger: { each, from }` controls timing and origin. |
| **Orchestration** | Multiple animated parts arranged into one coherent sequence. | Timeline position parameters let actions overlap precisely. |
| **Delay** | A planned wait before an animation begins. | Prefer timeline positions for readable delay management. |
| **Duration** | Time from start to finish. | UI motion often sits between 0.18 and 0.6 seconds. |
| **Fill mode** | Whether animation keeps first or last frame after playback. | GSAP tweens typically preserve final inline styles. |
| **Stepped animation** | Motion divided into discrete steps instead of continuous movement. | `ease: steps(n)` simulates discrete states. |

## Common CSS

```css
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
  will-change: transform, opacity;
}

.stack {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.line-path {
  position: absolute;
  width: min(520px, 72%);
  height: 2px;
  background: #ddd6ca;
}

.dot {
  width: 18px;
  height: 18px;
  border-radius: 999px;
  background: #c0362c;
  box-shadow: 0 0 0 8px rgba(192, 54, 44, .12);
}
```

## Animation Snippets

### Keyframes

```js
const tl = gsap.timeline();
tl.to(".actor", {
  keyframes: [
    { x: -160, y: 0, rotation: 0, backgroundColor: "#2254d6", duration: .01 },
    { x: 0, y: -100, rotation: 45, backgroundColor: "#c0362c", duration: .45 },
    { x: 160, y: 0, rotation: 0, backgroundColor: "#0b7a55", duration: .45 }
  ],
  ease: "power2.inOut"
});
```

### Interpolation / Tween

```html
<div class="line-path"></div>
<div class="dot"></div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".dot", { x: -240 }, { x: 240, duration: 1.25, ease: "power1.inOut" });
```

### Stagger

```html
<div class="stack">
  <div class="tile">1</div>
  <div class="tile">2</div>
  <div class="tile">3</div>
  <div class="tile">4</div>
  <div class="tile">5</div>
  <div class="tile">6</div>
  <div class="tile">7</div>
  <div class="tile">8</div>
</div>
```

```js
const tl = gsap.timeline();
tl.from(".tile", {
  y: 80,
  autoAlpha: 0,
  scale: .65,
  stagger: { each: .08, from: "start" },
  duration: .52
});
```

### Orchestration

```html
<div class="stack">
  <div class="tile">1</div>
  <div class="tile">2</div>
  <div class="tile">3</div>
  <div class="actor">GO</div>
</div>
```

```js
const tl = gsap.timeline();
tl.from(".tile", { y: 70, autoAlpha: 0, stagger: .08, duration: .45 })
  .from(".actor", { scale: .3, autoAlpha: 0, duration: .55, ease: "back.out(2)" }, "-=.18")
  .to(".tile", { x: (i) => (i - 1) * 22, rotation: (i) => (i - 1) * 8, duration: .5 }, "<");
```

### Delay

```html
<div class="stack">
  <div class="tile">1</div>
  <div class="tile">2</div>
  <div class="tile">3</div>
  <div class="tile">4</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile", { y: -72, yoyo: true, repeat: 1, duration: .34, stagger: .22 });
```

### Duration

```html
<div class="stack">
  <div class="tile">.2</div>
  <div class="tile">.8</div>
  <div class="tile">1.4</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile:nth-child(1)", { y: -110, duration: .22 }, 0)
  .to(".tile:nth-child(2)", { y: -110, duration: .8 }, 0)
  .to(".tile:nth-child(3)", { y: -110, duration: 1.4 }, 0);
```

### Fill mode

```html
<div class="actor">END</div>
<div class="actor ghost">START</div>
```

```js
const tl = gsap.timeline();
tl.set(".ghost", { x: -180 })
  .fromTo(".actor:not(.ghost)", { x: -180, autoAlpha: .2 }, { x: 180, autoAlpha: 1, duration: 1, ease: "power2.inOut" });
```

### Stepped animation

```html
<div class="ticker" data-value="0">0</div>
```

```js
const obj = { value: 0 };
const tl = gsap.timeline();
tl.to(obj, {
  value: 10,
  duration: 1.2,
  ease: "steps(10)",
  onUpdate: () => document.querySelector(".ticker").textContent = Math.round(obj.value)
});
```
