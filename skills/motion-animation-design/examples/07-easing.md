# Easing

How speed accelerates, decelerates, or stays constant.

## Terms

| Term | Definition | GSAP Tip |
|------|-----------|----------|
| **Easing** | Curve describing how speed changes over time. | Ease is the tone of motion. |
| **Ease-out** | Starts quickly, slows into the end. | `power3.out` / `expo.out` for entrances. |
| **Ease-in** | Starts slowly, accelerates toward the end. | `power2.in` for elements leaving. |
| **Ease-in-out** | Slow, speeds up, then slows again. | `power3.inOut` for panel movement. |
| **Linear** | Constant speed from start to finish. | `ease: 'none'`. |
| **Cubic-bezier** | Timing curve controlled by Bezier handles. | CSS uses `cubic-bezier`; GSAP can use `CustomEase`. |
| **Asymmetric easing** | Acceleration and deceleration have different personalities. | Combine different in/out curves. |

## Common CSS

```css
.easing-chart {
  width: min(560px, 86vw);
  height: 320px;
  position: relative;
  border-left: 2px solid #171717;
  border-bottom: 2px solid #171717;
}

.curve {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
}

.chart-dot {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 18px;
  height: 18px;
  border-radius: 999px;
  background: #c0362c;
  transform: translate(-50%, 50%);
}
```

## Animation Snippets

### Easing demo

```html
<div class="easing-chart">
  <svg class="curve" viewBox="0 0 560 320" preserveAspectRatio="none">
    <path d="M0 300 C140 295, 260 40, 560 20" fill="none" stroke="#2254d6" stroke-width="5"/>
  </svg>
  <div class="chart-dot"></div>
</div>
```

```js
function easingDemo(easeName) {
  const tl = gsap.timeline();
  tl.to(".chart-dot", { left: "100%", bottom: "92%", duration: 1.15, ease: easeName });
}

// Usage examples
easingDemo("power2.inOut");
easingDemo("power4.out");
easingDemo("power3.in");
easingDemo("power3.inOut");
easingDemo("none");
easingDemo("back.inOut(1.7)");
easingDemo("expo.out");
```
