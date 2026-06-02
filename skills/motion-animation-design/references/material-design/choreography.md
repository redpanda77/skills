---
name: material-design-choreography
description: Material Design transition choreography — sequencing, transformation, and focal elements for coordinated motion sequences.
---

# Choreography

Transition choreography is a coordinated motion sequence that holds the user's focus while an interface adapts.

## Sequencing

Sequencing refers to the order in which the different parts of an animation occur. A good sequence helps users understand what has changed on a screen, if elements were added or removed, and adds focus to anything important about the following interaction.

### Element Types

UI elements in a sequence are categorized as:
- **Outgoing elements** — exit the screen
- **Incoming elements** — enter the screen
- **Persistent elements** — start and end on screen

The persistent element (container) holds continuity. The outgoing element (list item content) exits. The incoming element (details page content) enters.

### Fade Types

To achieve sequencing, three fading types can be used:

**Fade** — A fade creates a smooth sequence between elements that fully overlap each other, such as photos inside of a card or another container. An element fades in (appears) or fades out (disappears) to show or hide the element behind it.

**Cross-fade** — A cross-fade transitions two elements simultaneously: one fades into view while the other fades out. During a portion of the sequence, both elements are shown together, along with anything that is behind them. This overlap of partially transparent elements can result in messy and distracting frames.

**Fade through** — A fade through entails an outgoing element fading out entirely before an incoming element fades in. A fade through can be used to minimize overlapping partially transparent elements and create a cleaner transition.

### Peak Velocity

All fading types are coordinated with the peak velocity of a transition. Peak velocity refers to the fastest moment in a transition.

- **Fades and cross-fades** are applied when a transition is at peak velocity. This sequencing hides the unwanted effect of partially transparent overlapping frames during the transition.
- **Fade through**: outgoing elements finish fading out at the point of peak velocity; then, incoming elements fade in. This sequencing hides the empty frame during the transition when both the outgoing and incoming content are transparent, making for a more seamless transition.

## Transformation

Transformation describes specific animations of a transitioning element. For example, changing size, position, and opacity are types of transformations that an element or group of elements can undergo.

### Simple Transformations

Simple transitions involve seamlessly transforming the properties that change from one state to the next. For example, a switch component's color and position seamlessly animating by moving from left to right and fading from one state to another.

### Complex Transformations

Complex layout changes use a shared transformation to create smooth transitions from one layout to the next. Elements are grouped together and transform as a single unit, rather than animating independently. This avoids multiple transformations overlapping and competing for attention.

Grouped elements are sequenced with one of three fading types: fade, cross-fade, or fade through.

**Do**: Minimize the number of elements that move independently. Transformation of the group provides continuity while individual elements fade in or out.

**Don't**: Animate multiple elements simultaneously in relation to each other. Individual movements of the elements compete for attention and divide focus.

**Don't**: Move multiple elements independently. The various moving parts shift abruptly and make it difficult to focus.

### Transitions with Animated Containers

When a group of elements are contained by clearly defined borders during a transition, such as a card or set of dividers, the container transforms. The element group maintains its aspect ratio, scaling by width to fit and pin to top of the container.

Continuity is created by animating a group in unison with its container. The group scales to match the container's width.

### Transitions without Animated Containers

When an element group is not contained by clearly defined borders, a shared transformation can create a smooth transition. For example, a pair of icons within a floating action button can rotate in unison to create continuity.

The icons transition within the container while rotating clockwise. In tandem with a vertical stepper, incoming and outgoing elements move up and down as a group.

## Focal Elements

A focal element in a transition is a persistent element that is significant to the overall hierarchy of elements in a transition. Like animated containers, focal elements enhance continuity by seamlessly transforming in appearance.

### Focal Element Conflicts

Some transitions will place a focal element in the path of other elements. In these cases, avoid using a focal element and apply a fade instead.

**Caution**: Use caution if a focal element overlaps with other elements in motion as it can create a disorganized transition.

**Do**: A focal element with a fade can simplify overlapping motion.
