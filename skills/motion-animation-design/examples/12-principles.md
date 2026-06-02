# Principles to Know

Rules for when and how to animate.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Purposeful animation** | Motion aids understanding, feedback, or navigation. | Define the job of the motion before writing the tween. |
| **Anticipation** | Small preparatory motion before the main action. | Move slightly opposite first, then toward the target. |
| **Follow-through** | Parts continue moving slightly after the main body stops. | Stagger child elements so they finish at different moments. |
| **Squash & stretch** | Shape compresses or stretches during movement. | Pair `scaleX` and `scaleY` in opposite directions. |
| **Perceived performance** | Motion makes waiting feel shorter. | Use short motion to bridge state changes. |
| **Frequency of use** | More often an animation appears, shorter it should be. | Shorten duration on common paths. |
| **Spatial consistency** | Motion preserves spatial logic across states. | Keep direction, source, and destination consistent. |
| **Hardware acceleration** | Use properties easier for GPU to composite. | Prioritize `x`, `y`, `scale`, and `opacity`. |
| **Reduced motion** | Respect system settings requesting less motion. | `matchMedia('(prefers-reduced-motion)')`. |

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

.shimmer {
  width: min(420px, 82vw);
  display: grid;
  gap: 14px;
}

.skeleton {
  height: 20px;
  border-radius: 999px;
  background: linear-gradient(90deg, #dfd8cd, #f8f4ed, #dfd8cd);
  background-size: 220% 100%;
}
```

## Animation Snippets

### Purposeful animation

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

### Anticipation

```js
const tl = gsap.timeline();
tl.to(".actor", { x: -32, duration: .18, ease: "power2.out" })
  .to(".actor", { x: 190, duration: .62, ease: "expo.out" });
```

### Follow-through

```html
<div class="stack">
  <div class="tile">H</div>
  <div class="tile">E</div>
  <div class="tile">Y</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile", { x: 130, duration: .52, stagger: .06, ease: "power3.out" })
  .to(".tile", { x: 110, duration: .45, stagger: .05, ease: "elastic.out(1, .36)" });
```

### Squash & stretch

```html
<div class="actor round">SQ</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { y: -120, scaleX: .82, scaleY: 1.22, duration: .38, ease: "power2.out" })
  .to(".actor", { y: 0, scaleX: 1.28, scaleY: .76, duration: .28, ease: "power2.in" })
  .to(".actor", { scale: 1, duration: .48, ease: "elastic.out(1, .34)" });
```

### Perceived performance

```html
<div class="shimmer">
  <div class="skeleton" style="width:82%"></div>
  <div class="skeleton"></div>
  <div class="skeleton" style="width:64%"></div>
  <div class="skeleton" style="width:92%"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".skeleton", { backgroundPosition: "-220% 0", duration: 1.2, repeat: -1, ease: "none" });
```

### Frequency of use

```html
<div class="stack">
  <div class="tile">Often</div>
  <div class="tile">Rare</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile:nth-child(1)", { y: -18, duration: .16, yoyo: true, repeat: 1 })
  .to(".tile:nth-child(2)", { y: -90, scale: 1.2, duration: .72, yoyo: true, repeat: 1 }, 0);
```

### Spatial consistency

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

### Hardware acceleration

```js
const tl = gsap.timeline();
tl.to(".tile", { x: 160, autoAlpha: .58, duration: .8, stagger: .08, ease: "power3.inOut" });
```

### Reduced motion

```html
<div class="stack">
  <div class="tile">Full</div>
  <div class="tile">Less</div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".tile:nth-child(1)", { x: 150, rotation: 180, duration: .7 })
  .to(".tile:nth-child(2)", { autoAlpha: .45, duration: .22 }, 0);
```
