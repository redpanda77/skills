# Entrances & Exits

Animation vocabulary for how elements appear, leave, or are revealed.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Fade in / Fade out** | An element appears or disappears through opacity. | `autoAlpha` handles both opacity and visibility. |
| **Slide in** | Element moves in from outside the viewport or container edge. | Use `x` / `y` instead of `left` / `top`. |
| **Scale in** | Element grows from a smaller size into place, often with fade. | Combine `scale` and `autoAlpha` in one tween. |
| **Pop in** | Snappy entrance with a small overshoot before settling. | `back.out(1.8)` is a quick way to make a pop. |
| **Reveal** | Content is uncovered by a mask, clip, or cover moving away. | `clipPath` or a moving cover layer both work well. |
| **Enter / Exit** | Paired animations for adding or removing an element. | Sequence enter and exit in a timeline. |

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

.line-path {
  position: absolute;
  width: min(520px, 72%);
  height: 2px;
  background: #ddd6ca;
}

.mask-window {
  width: min(420px, 80vw);
  height: 260px;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(135deg, #2254d6, #0b7a55);
}

.mask-window .cover {
  position: absolute;
  inset: 0;
  background: #171717;
}
```

## Animation Snippets

### Fade in / Fade out

```js
// Fade in
const tl = gsap.timeline();
tl.fromTo(".actor", { autoAlpha: 0 }, { autoAlpha: 1, duration: .65 });

// Fade out
const tl = gsap.timeline();
tl.to(".actor", { autoAlpha: .12, duration: .65, delay: .25 });
```

### Slide in

```html
<div class="line-path"></div>
<div class="actor">→</div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { x: -360, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: .85, ease: "expo.out" });
```

### Scale in

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { scale: .32, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: .72, ease: "power3.out" });
```

### Pop in

```js
const tl = gsap.timeline();
tl.fromTo(".actor", { scale: .2, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: .78, ease: "back.out(2.4)" });
```

### Reveal

```html
<div class="mask-window">
  <div class="cover"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".cover", { xPercent: 104, duration: 1, ease: "expo.inOut" });
```

### Enter / Exit

```js
const tl = gsap.timeline();
tl.from(".actor", { y: 120, autoAlpha: 0, scale: .82, duration: .55 })
  .to(".actor", { y: -120, autoAlpha: 0, scale: .82, duration: .45, ease: "power2.in", delay: .45 });
```
