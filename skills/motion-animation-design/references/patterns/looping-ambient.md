---
name: pattern-looping-ambient
description: Subtle looping and ambient motion for marquees, pulses, and floating elements.
---

# Looping & Ambient Motion

Subtle motion that plays while an element is waiting to be interacted with.

## Approach

Very slow, linear, subtle.

## CSS

```css
.float {
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.pulse {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.marquee {
  animation: scroll 10s linear infinite;
}
```

## Key Points

- Marquees: linear, infinite
- Pulses: gentle opacity or scale changes
- Float: gentle, continuous up-and-down drift
- Keep ambient motion very subtle so it does not distract

## See Also

- `Examples/09-looping-and-ambient.html` for ambient demos
