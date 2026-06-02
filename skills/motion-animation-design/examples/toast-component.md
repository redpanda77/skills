---
name: exercise-toast-component
description: Build a toast component with CSS transitions. Learn stacking, inverted index, and interruptibility.
---

# Exercise: Toast Component

## Goal

Build a toast component that animates each time a toast changes position. Use CSS transitions, not CSS animations.

## Why CSS Transitions?

When we add a toast while the one before is still animating, existing toasts smoothly shift to their new positions with CSS transitions. This does not happen with CSS animations because they are not interruptible.

## The Solution

Stack all toasts with `position: absolute` and `bottom: 0`. Use a CSS variable `--index` to calculate `translateY` for each toast.

```jsx
function Toaster() {
  const [toasts, setToasts] = useState(0);

  return (
    <div className="wrapper">
      <div className="toaster">
        {Array.from({ length: toasts }).map((_, i) => (
          <Toast key={i} index={toasts - (i + 1)} />
        ))}
      </div>
      <button onClick={() => setToasts(toasts + 1)}>Add toast</button>
    </div>
  );
}

function Toast({ index }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => { setMounted(true); }, []);

  return (
    <div
      className="toast"
      style={{ "--index": index }}
      data-mounted={mounted}
    >
      <span className="title">Event Created</span>
      <span className="description">Monday, January 3rd at 6:00pm</span>
    </div>
  );
}
```

```css
.toaster {
  position: absolute;
  left: 50%;
  bottom: 80px;
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  width: 356px;
  transform: translateX(-50%);
  --gap: 16px;
}

.toast {
  position: absolute;
  bottom: 0;
  width: 100%;
  opacity: 0;
  transform: translateY(100%);
  transition: opacity 400ms ease, transform 400ms ease;
}

.toast[data-mounted="true"] {
  transform: translateY(calc(var(--index) * (100% + var(--gap)) * -1));
  opacity: 1;
}
```

## Key Takeaways

- Invert the index so the newest toast is at the bottom: `index = toasts - (i + 1)`
- Use `translateY(calc(var(--index) * (100% + var(--gap)) * -1))` to stack toasts
- Multiply by `-1` to get a negative translateY value, which moves the element up
- Choose `ease` for an elegant, soft feel. For a small toast, 400ms feels smooth; anything below feels too fast
- Use `data-mounted` for enter animation. The default state is `translateY(100%)`, and the mounted state applies the calculated position
- This can also be solved without JavaScript state using the `@starting-style` CSS at-rule
- See `Examples/01-entrances-and-exits.html` for enter/exit demos
