# Transitions Between States

How states, views, and elements connect.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Crossfade** | One element fades out while another fades in. | Animate one `autoAlpha` to 0 while the other goes to 1. |
| **Continuity transition** | Preserves visual identity so users understand it's the same object. | Transforming one node feels better than replacing it. |
| **Morph** | One shape smoothly turns into another. | Without MorphSVG, `borderRadius` and `scale` approximate it. |
| **Shared element transition** | Same element moves from one location to another, changing size. | Measure start and end rects, then animate the transform. |
| **Layout animation** | Elements animate to new positions after layout changes. | FLIP idea: First, Last, Invert, Play. |
| **Accordion / Collapse** | Content expands or collapses smoothly. | Measure target height when animating to auto. |
| **Direction-aware transition** | Forward and backward use opposite directions. | Set `x` direction based on navigation direction. |

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

.ghost {
  opacity: .2;
  background: transparent;
  border: 2px dashed #171717;
  color: #171717;
  box-shadow: none;
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

.card-line.short {
  width: 62%;
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

.phone {
  width: min(320px, 78vw);
  height: 420px;
  border: 1px solid rgba(23, 23, 23, .16);
  border-radius: 28px;
  background: #f4efe5;
  padding: 18px;
  box-shadow: inset 0 0 0 8px #171717, 0 24px 60px rgba(23, 23, 23, .12);
  overflow: hidden;
}

.phone-screen {
  height: 100%;
  border-radius: 20px;
  background: #fffefa;
  overflow: hidden;
  position: relative;
}

.drawer {
  width: 100%;
  height: 68%;
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 18px;
  border: 1px solid #ddd6ca;
  border-radius: 8px;
  background: #fffefa;
  box-shadow: 0 18px 50px rgba(23, 23, 23, .12);
}
```

## Animation Snippets

### Crossfade

```html
<div class="actor" style="position:absolute;background:#2254d6">A</div>
<div class="actor" style="position:absolute;background:#c0362c">B</div>
```

```js
gsap.set(".actor:nth-child(2)", { autoAlpha: 0 });

const tl = gsap.timeline();
tl.to(".actor:nth-child(1)", { autoAlpha: 0, duration: .7 })
  .to(".actor:nth-child(2)", { autoAlpha: 1, duration: .7 }, "<");
```

### Continuity transition

```html
<div class="card">
  <b>Same object</b>
  <div class="card-line"></div>
  <div class="card-line short"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".card", { width: "min(560px, 86vw)", minHeight: 310, x: 20, duration: .8, ease: "power3.inOut" });
```

### Morph

```html
<div class="actor round">M</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { width: 260, height: 96, borderRadius: 32, backgroundColor: "#0b7a55", duration: .78, ease: "power3.inOut" })
  .to(".actor", { width: 132, height: 132, borderRadius: 8, backgroundColor: "#6d4cc2", duration: .78, ease: "power3.inOut" });
```

### Shared element transition

```html
<div class="actor ghost" style="position:absolute;left:16%;top:24%">A</div>
<div class="actor ghost" style="position:absolute;right:14%;bottom:16%;width:220px;height:150px">B</div>
<div class="actor" style="position:absolute;left:16%;top:24%">A</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor:not(.ghost)", {
  left: "calc(86% - 220px)",
  top: "calc(84% - 150px)",
  width: 220,
  height: 150,
  duration: 1,
  ease: "power3.inOut"
});
```

### Layout animation

```html
<div class="stack">
  <div class="tile">A</div>
  <div class="tile">B</div>
  <div class="tile">C</div>
  <div class="tile">D</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile:nth-child(1)", { x: 234, duration: .7, ease: "power3.inOut" }, "<")
  .to(".tile:nth-child(2)", { x: -78, duration: .7, ease: "power3.inOut" }, "<")
  .to(".tile:nth-child(3)", { x: -78, duration: .7, ease: "power3.inOut" }, "<")
  .to(".tile:nth-child(4)", { x: -78, duration: .7, ease: "power3.inOut" }, "<");
```

### Accordion / Collapse

```html
<div class="card">
  <b>Accordion</b>
  <div class="card-line"></div>
  <div class="card-line short"></div>
  <div class="extra">
    <div class="card-line"></div>
    <div class="card-line short"></div>
    <div class="card-line"></div>
  </div>
</div>
```

```js
gsap.set(".card", { height: 92, overflow: "hidden" });

const tl = gsap.timeline();
tl.to(".card", { height: 260, duration: .72, ease: "power3.inOut" });
```

### Direction-aware transition

```html
<div class="phone">
  <div class="phone-screen">
    <div class="drawer">Forward</div>
  </div>
</div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".drawer", { xPercent: 100 }, { xPercent: 0, duration: .55 })
  .to(".drawer", { xPercent: -100, duration: .55, delay: .35 });
```
