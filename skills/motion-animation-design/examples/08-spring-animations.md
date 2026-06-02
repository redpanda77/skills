# Spring Animations

Motion described by physical properties like tension, mass, and damping.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Spring** | Motion described by physical properties. | `elastic` and `back` eases approximate spring behavior. |
| **Stiffness / Tension** | How strongly the spring pulls toward its target. | Increase ease intensity or shorten duration. |
| **Damping** | How quickly motion loses energy after overshooting. | `elastic.out(1, damping)` simulates different feels. |
| **Mass** | How heavy the object feels in motion. | Lengthen duration and reduce sharpness to imply weight. |
| **Bounce** | Motion overshoots or hits a surface, then rebounds. | `bounce.out` or `back.out`. |
| **Perceptual duration** | Time when users feel animation is done, even if tiny settling continues. | Keep late spring oscillation small. |
| **Momentum** | Motion carries existing velocity after release. | Use pointer velocity to set target or distance. |
| **Velocity** | Current speed and direction, often drives next animation. | Track pointer delta over time. |
| **Interruptible animation** | Can be redirected mid-flight without snapping. | `overwrite: 'auto'` or `quickTo`. |

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

.line-path {
  position: absolute;
  width: min(520px, 72%);
  height: 2px;
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

### Spring

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -220 }, { x: 190, duration: 1, ease: "elastic.out(1, .42)" });
```

### Stiffness / Tension

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -220 }, { x: 190, duration: .85, ease: "elastic.out(1.3, .32)" });
```

### Damping

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -220 }, { x: 190, duration: 1.2, ease: "elastic.out(1, .18)" });
```

### Mass

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -220 }, { x: 190, duration: 1.55, ease: "power2.out" });
```

### Bounce

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -220 }, { x: 190, duration: 1.05, ease: "bounce.out" });
```

### Perceptual duration

```js
const tl = gsap.timeline();
tl.to(".actor", { y: -120, duration: .35, ease: "power3.out" })
  .to(".actor", { y: -128, scale: 1.015, duration: .8, ease: "elastic.out(1, .22)" });
```

### Momentum

```html
<div class="line-path"></div>
<div class="actor">V</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 130, duration: .35, ease: "power2.in" })
  .to(".actor", { x: 260, autoAlpha: .2, duration: .55, ease: "power3.out" });
```

### Interruptible animation

```html
<div class="line-path"></div>
<div class="actor">I</div>
```

```js
const tl = gsap.timeline();
tl.to(".actor", { x: 220, duration: .8, ease: "power2.inOut" })
  .to(".actor", { x: -180, duration: .55, ease: "power3.out", overwrite: "auto" }, "-=.35");
```
