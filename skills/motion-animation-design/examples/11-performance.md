# Performance

Making animation smooth instead of stuttering.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Frame rate (FPS)** | How many frames are drawn per second. | Avoid expensive work on every frame. |
| **Jank** | Visible stutter when browser cannot draw frames in time. | Reduce layout and paint pressure. |
| **Dropped frame** | A frame missed its drawing deadline, causing a hitch. | Keep `requestAnimationFrame` work lightweight. |
| **Compositing** | GPU moves or fades separate layers without repainting. | Prefer `transform` and `opacity` for animated properties. |
| **will-change** | CSS hint that tells browser an element is about to animate. | Use only on elements that will actually move. |
| **Layout thrashing** | Repeated reads/writes to layout properties force recalculation. | Avoid animating `width` / `top` / `left` when transforms work. |

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
  will-change: transform, opacity;
}

.ticker {
  font: 900 clamp(58px, 13vw, 120px)/1 monospace;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0;
}
```

## Animation Snippets

### Frame rate (FPS)

```html
<div class="stack">
  <div class="tile" style="height:46px">1</div>
  <div class="tile" style="height:62px">2</div>
  <div class="tile" style="height:78px">3</div>
  <div class="tile" style="height:94px">4</div>
  <div class="tile" style="height:46px">5</div>
  <div class="tile" style="height:62px">6</div>
  <div class="tile" style="height:78px">7</div>
  <div class="tile" style="height:94px">8</div>
  <div class="tile" style="height:46px">9</div>
  <div class="tile" style="height:62px">10</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile", { scaleY: 1.18, duration: .55, stagger: .03, repeat: 1, yoyo: true, ease: "sine.inOut" });
```

### Jank

```js
const tl = gsap.timeline();
tl.to(".tile", {
  scaleY: (i) => i % 3 === 0 ? .42 : 1.2,
  duration: .18,
  stagger: .03,
  repeat: 4,
  yoyo: true,
  ease: "steps(2)"
});
```

### Dropped frame

```js
const tl = gsap.timeline();
tl.to(".tile", {
  scaleY: (i) => i % 3 === 0 ? .42 : 1.2,
  duration: .18,
  stagger: .03,
  repeat: 4,
  yoyo: true,
  ease: "steps(2)"
});
```

### Compositing

```js
const tl = gsap.timeline();
tl.to(".tile", { x: 160, autoAlpha: .58, duration: .8, stagger: .08, ease: "power3.inOut" });
```

### will-change

```html
<div class="actor" style="will-change:transform">WC</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 180, rotation: 20, duration: .62 })
  .to(".actor", { x: 0, rotation: 0, duration: .62 });
```

### Layout thrashing

```js
const tl = gsap.timeline();
tl.to(".tile", { width: 122, duration: .35, stagger: .1, ease: "steps(4)" })
  .to(".tile", { width: 66, duration: .35, stagger: .1, ease: "steps(4)" });
```
