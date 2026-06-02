# Scroll

Scroll-driven or scroll-related motion.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Scroll reveal** | Elements animate in when they enter the viewport. | Use `IntersectionObserver` to trigger `gsap.from`. |
| **Scroll-driven animation** | Animation progress mapped directly to scroll position. | Map scroll progress to `timeline.progress`. |
| **Parallax** | Foreground and background layers move at different speeds. | Give each layer a different `y` movement ratio. |
| **Page transition** | Transition when moving between pages or routes. | Use a timeline to manage out before in. |
| **View transition** | Browser or framework visually connects two view states. | The View Transitions API pairs with CSS or JS motion. |

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

.ghost {
  opacity: .2;
  background: transparent;
  border: 2px dashed #171717;
  color: #171717;
  box-shadow: none;
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
  height: 100%;
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

### Scroll reveal

```html
<div class="stack" style="align-content:center">
  <div class="tile">1</div>
  <div class="tile">2</div>
  <div class="tile">3</div>
  <div class="tile">4</div>
  <div class="tile">5</div>
  <div class="tile">6</div>
</div>
```

```js
const tl = gsap.timeline();
tl.from(".tile", { y: 90, autoAlpha: 0, stagger: .1, duration: .6 });
```

### Scroll-driven animation

```html
<div class="line-path"></div>
<div class="dot"></div>
<input id="progress" type="range" min="0" max="100" value="0" style="position:absolute;bottom:36px;width:min(420px,80vw)">
```

```js
const tl = gsap.timeline({ paused: true })
  .fromTo(".dot", { x: -240 }, { x: 240, rotation: 720, duration: 1, ease: "none" });

document.querySelector("#progress").addEventListener("input", (event) => {
  tl.progress(event.target.value / 100);
});
```

### Parallax

```html
<div class="actor ghost" style="position:absolute;width:280px;height:180px">BG</div>
<div class="actor" style="position:absolute">FG</div>
```

```js
const tl = gsap.timeline();
tl.to(".ghost", { y: -50, duration: 1.1, ease: "none" }, 0)
  .to(".actor:not(.ghost)", { y: -170, duration: 1.1, ease: "none" }, 0);
```

### Page transition

```html
<div class="phone">
  <div class="phone-screen">
    <div class="drawer" style="height:100%;background:#fffefa">Page A</div>
    <div class="drawer" style="height:100%;background:#e9efe7">Page B</div>
  </div>
</div>
```

```js
gsap.set(".drawer:nth-child(2)", { xPercent: 100 });

const tl = gsap.timeline();
tl.to(".drawer:nth-child(1)", { xPercent: -35, autoAlpha: .25, duration: .65 })
  .to(".drawer:nth-child(2)", { xPercent: 0, duration: .65 }, "<");
```

### View transition

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
