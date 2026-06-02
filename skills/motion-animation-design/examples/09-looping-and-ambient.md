# Looping & Ambient Motion

Continuously running background motion.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Marquee** | Content scrolls continuously in a loop. | `repeat: -1` with `ease: 'none'`. |
| **Loop** | Animation repeats for a set count or indefinitely. | `repeat: -1` for an infinite loop. |
| **Alternate (yoyo)** | Each repeat plays in the opposite direction. | `repeat: -1, yoyo: true`. |
| **Orbit** | One element revolves around another. | Set `transformOrigin` to the orbit center. |
| **Pulse** | Subtle repeating scale or opacity change. | Combine `scale`, `autoAlpha`, `repeat`, and `yoyo`. |
| **Float** | Small vertical drift to keep an element from feeling static. | `yoyo` tween on `y`. |
| **Idle animation** | Subtle motion shown while an element is not actively used. | Long duration, small values, infinite `yoyo`. |

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

.actor.round {
  border-radius: 999px;
}

.marquee {
  display: flex;
  width: max-content;
  gap: 20px;
  font: 900 clamp(38px, 8vw, 84px)/1 monospace;
  white-space: nowrap;
  color: #171717;
}

.orbit {
  position: relative;
  width: 240px;
  height: 240px;
  border: 1px dashed rgba(23, 23, 23, .24);
  border-radius: 999px;
}

.orbit .sun,
.orbit .moon {
  position: absolute;
  border-radius: 999px;
}

.orbit .sun {
  width: 70px;
  height: 70px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: #c17a12;
}

.orbit .moon {
  width: 28px;
  height: 28px;
  left: calc(50% - 14px);
  top: -14px;
  background: #2254d6;
  transform-origin: 14px 134px;
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
```

## Animation Snippets

### Marquee

```html
<div class="marquee">
  <span>MOTION</span>
  <span>VOCABULARY</span>
  <span>GSAP</span>
  <span>MOTION</span>
  <span>VOCABULARY</span>
  <span>GSAP</span>
</div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".marquee", { x: 220 }, { x: -520, duration: 4, ease: "none", repeat: -1 });
```

### Loop

```js
const tl = gsap.timeline();
tl.to(".actor", { rotation: 360, duration: 1.2, ease: "none", repeat: -1 });
```

### Alternate (yoyo)

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 180, scale: 1.18, duration: .7, repeat: 3, yoyo: true, ease: "power2.inOut" });
```

### Orbit

```html
<div class="orbit">
  <div class="sun"></div>
  <div class="moon"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".moon", { rotation: 360, duration: 2, ease: "none", repeat: -1 });
```

### Pulse

```js
const tl = gsap.timeline();
tl.to(".actor", { scale: 1.18, autoAlpha: .58, duration: .58, repeat: 4, yoyo: true, ease: "sine.inOut" });
```

### Float

```js
const tl = gsap.timeline();
tl.to(".actor", { y: -34, duration: 1.2, repeat: -1, yoyo: true, ease: "sine.inOut" });
```

### Idle animation

```html
<div class="stack">
  <div class="tile">I</div>
  <div class="tile">D</div>
  <div class="tile">L</div>
  <div class="tile">E</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile", {
  y: -16,
  rotation: (i) => [-2, 1, -1, 2][i],
  duration: 1.4,
  stagger: .12,
  repeat: -1,
  yoyo: true,
  ease: "sine.inOut"
});
```
