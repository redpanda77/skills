# Polish & Effects

Small techniques that make motion feel more refined.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Blur** | Filter that softens elements or adds depth. | `filter: 'blur(12px)'` can be tweened. |
| **Clip-path** | Clipping shape hides or shows part of an element. | Animate `clipPath` such as `inset(...)`. |
| **Mask** | Shape or gradient controls visible area, often with soft edges. | CSS `mask` or gradient masks. |
| **Before / after slider** | Draggable divider compares two layers. | Animate the overlay width. |
| **Line drawing** | SVG path appears as if drawn by a pen. | `strokeDasharray` + `strokeDashoffset`. |
| **Text morph** | Text changes with per-character transition. | Split characters and stagger replacement. |
| **Skeleton / Shimmer** | Placeholder layout with light sweep while loading. | Animate `backgroundPosition` in a loop. |
| **Number ticker** | Number increments or rolls toward a target value. | `onUpdate` and `snap` or rounded text updates. |
| **Tabular numbers** | Digits use equal widths so changing values don't shift layout. | `font-variant-numeric: tabular-nums`. |
| **Typewriter** | Text appears character by character. | Update `textContent` progressively over time. |

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
  will-change: transform, opacity, filter;
}

.mask-window {
  width: min(420px, 80vw);
  height: 260px;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(135deg, #2254d6, #0b7a55);
}

.before-after {
  width: min(520px, 86vw);
  height: 280px;
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  background: repeating-linear-gradient(45deg, #e7e0d3 0 12px, #d5cabb 12px 24px);
}

.after-layer {
  position: absolute;
  inset: 0;
  width: 52%;
  overflow: hidden;
  background: linear-gradient(135deg, #2254d6, #fbfaf6 55%, #c0362c);
}

.divider {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 52%;
  width: 4px;
  background: #171717;
  transform: translateX(-2px);
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

.ticker {
  font: 900 clamp(58px, 13vw, 120px)/1 monospace;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0;
}

.draw-svg {
  width: min(520px, 84vw);
  overflow: visible;
}

.draw-svg path {
  fill: none;
  stroke: #2254d6;
  stroke-width: 10;
  stroke-linecap: round;
  stroke-linejoin: round;
}
```

## Animation Snippets

### Blur

```js
const tl = gsap.timeline();
tl.fromTo(".actor",
  { filter: "blur(18px)", autoAlpha: 0, scale: 1.18 },
  { filter: "blur(0px)", autoAlpha: 1, scale: 1, duration: .85 }
);
```

### Clip-path

```html
<div class="mask-window"></div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".mask-window",
  { clipPath: "inset(0 100% 0 0)" },
  { clipPath: "inset(0 0% 0 0)", duration: .9, ease: "expo.inOut" }
);
```

### Mask

```html
<div class="mask-window" style="-webkit-mask-image:linear-gradient(90deg, transparent, #000 30%, #000 70%, transparent);mask-image:linear-gradient(90deg, transparent, #000 30%, #000 70%, transparent)"></div>
```

```js
const tl = gsap.timeline();
tl.fromTo(".mask-window",
  { x: -140, autoAlpha: .35 },
  { x: 140, autoAlpha: 1, duration: 1.1, ease: "power2.inOut" }
);
```

### Before / after slider

```html
<div class="before-after">
  <div class="after-layer"></div>
  <div class="divider"></div>
</div>
```

```js
const tl = gsap.timeline();
tl.to(".after-layer", { width: "82%", duration: .8, ease: "power3.inOut" })
  .to(".divider", { left: "82%", duration: .8, ease: "power3.inOut" }, "<");
```

### Line drawing

```html
<svg class="draw-svg" viewBox="0 0 520 220">
  <path d="M40 150 C120 20, 190 210, 270 90 S420 30, 480 148"></path>
</svg>
```

```js
const path = document.querySelector(".draw-svg path");
const length = path.getTotalLength();
gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });

const tl = gsap.timeline();
tl.to(path, { strokeDashoffset: 0, duration: 1.35, ease: "power2.inOut" });
```

### Text morph

```html
<div class="ticker">Motion</div>
```

```js
const words = ["Motion", "Meaning", "Memory"];
let index = 0;

const tl = gsap.timeline();
tl.to(".ticker", {
  autoAlpha: 0,
  y: -18,
  duration: .28,
  repeat: 2,
  yoyo: true,
  repeatDelay: .15,
  onRepeat() {
    index = (index + 1) % words.length;
    document.querySelector(".ticker").textContent = words[index];
    gsap.set(".ticker", { y: 18 });
  }
});
```

### Skeleton / Shimmer

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

### Number ticker

```html
<div class="ticker">0000</div>
```

```js
const obj = { value: 0 };
const tl = gsap.timeline();
tl.to(obj, {
  value: 1632,
  duration: 1.25,
  ease: "power3.out",
  onUpdate: () => document.querySelector(".ticker").textContent = Math.round(obj.value).toString().padStart(4, "0")
});
```

### Typewriter

```html
<div class="ticker" style="font-size:clamp(30px,7vw,70px)">Animation</div>
```

```js
const text = "Animation vocabulary";
const box = document.querySelector(".ticker");
box.textContent = "";

const tl = gsap.timeline();
tl.to({}, {
  duration: text.length * .055,
  ease: "none",
  onUpdate() {
    box.textContent = text.slice(0, Math.ceil(this.progress() * text.length));
  }
});
```
