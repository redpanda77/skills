---
name: card-design-guidelines
description: Best practices for designing card UI components, including anatomy, spacing, states, and responsive behavior.
---

# Card Design Guidelines

## Overview

A card is a UI component that creates a visually distinct group of logically related information. It typically consists of a headline, description, and optional image, button, or call-to-action.

## Common Use Cases

- **Product catalogs:** E-commerce (image, title, price, CTA)
- **Content sites:** News, social media (scan, compare, pick)
- **Dashboards:** Group related data for comparison and analysis
- **Collection sites:** Browsing and exploring (Pinterest, Unsplash)
- **Collaborative tools:** Project and file cards (Figma, Miro)
- **Streams / Feeds:** Timelines of events (e.g., Facebook news feed)
- **Discovery:** Allow relevant content to naturally reveal itself (e.g., Behance, Tinder)
- **Workflow / Task management:** Cards representing separate tasks (e.g., Trello)
- **Dialog / Notifications:** Action cards for accept/decline decisions (e.g., AirDrop)

## Card-Based Design Language

Cards are content containers that serve as entry points to more detailed information. They mimic real-world tangible cards (business cards, baseball cards, sticky notes), making them intuitive for users to understand.

### Key Advantages

- **Chunking content:** Cards divide information into meaningful, scannable sections. Users avoid walls of text and can dive into their interests quickly.
- **Easy to digest:** Users can access the content they are interested in and engage in any way they want.
- **Visually pleasing:** Going heavy on images is a strength of card-based design. Images draw the user's eye efficiently and immediately.
- **Good for varying screen sizes:** Cards act as content containers that easily scale up or down, making them ideal for responsive design.
- **Designed for thumbs:** Users intuitively understand the physics of swiping or tapping cards for more information, similar to physical cards.

## Best Practices

### 1. Contrast with Background
- Use an **outlined** style (border) or **elevated** style (shadow) to distinguish the card from the background.

### 2. Balanced Font Sizes
- Maintain visual hierarchy and avoid overly small fonts.
- **Headlines:** 20px–96px+ (depending on card size and context)
- **Subheadline/Subtitle:** 2px–10px smaller than the main headline
- **Body text:** At least 16px (14px only if using a font with larger characters)
- **Button labels:** Not smaller than body text; use Semi-bold/Bold for primary actions
- Limit the number of font sizes; use a type scale tool if needed.

### 3. Spacing System for Paddings
- Define a base unit (commonly **4px** or **8px**) and derive all spacing from it.
- Use the base unit as an increment or multiplier to define a limited set of spacing values.
- Avoid odd numbers (e.g., 5px) because they can cause blurring on 1.5x DPI devices.

### 4. Loading State
- Design a skeleton/loading state that resembles the final content layout as much as possible.
- This reduces user uncertainty about what content to expect.

### 5. Fixed Height
- Define a fixed height for cards when content length varies.
- Leave whitespace for cards with less content; truncate text when content exceeds the limit.

### 6. Grids for Card-Based Layouts
- Use a grid system as the foundation for arranging cards consistently.
- Extend card width to the number of grid columns needed.
- Create a separate grid for each breakpoint and arrange cards accordingly.

### 7. Design for Different Content Lengths
- Cover cases with varying content lengths (e.g., titles, descriptions) in your design.
- This helps developers build the component correctly and avoid breaking alignment.

### 8. Card Interactions and States

Define states for visual feedback based on user interaction:

| State | Description |
|-------|-------------|
| **Default** | Normal state without interaction |
| **Hover** | Mouse cursor over the card |
| **Active** | Primary mouse button pressed down (pressed state) |
| **Focused** | Highlighted via keyboard, voice, or tap (min 3:1 contrast ratio) |
| **Selected** | Card is selected via a selection control |
| **Dragged** | Card is being touched, held, or dragged |

### Patterns

- **Grouped elements:** The entire card is clickable.
- **Individual elements:** Only specific elements inside the card are clickable.

## Design Principles

- **Focus on one thing:** Each card should represent one idea, topic, or product.
- **Clear information order:** Start with the most important details (title, main message), then supporting info.
- **Use the whole card as a link:** Make the entire card clickable rather than just a link inside it.
- **Make cards feel interactive:** Add subtle effects (shadow change, slight animation) on hover to indicate clickability.
- **Light shadowing for depth:** A subtle shadow makes cards appear more three-dimensional.
- **Simple, readable fonts:** Avoid fancy or hard-to-read fonts.
- **Responsiveness:** Cards should adapt and rearrange across desktop, tablet, and mobile.
- **Experiment with styles:** Try different layouts while keeping the user experience in mind.

## Cards and Responsive Design

Cards are excellent for responsive design because they act as content containers that easily scale up or down. Key patterns:

- **Mobile:** Cards stack vertically, like an activity stream.
- **Desktop:** Cards fall into a grid layout.
- **Fixed or variable height:** Set fixed width with variable height based on device type.
- **Grid restructuring:** Card grids can restructure themselves to fit any breakpoint or screen size.

## Cards and Typography

Everything about a card design should be easy to read and understand. Design for maximum readability:

- Opt for simple typefaces and easy-to-read color schemes.
- Place text on solid color backgrounds with sufficient contrast ratios.
- Try to limit the number of typefaces. For most card projects, a single typeface is enough.

## Card System Properties

The following properties are universal to card-based layouts and affect information, affordance, and interaction.

### 1. Matryoshka Effect

Boxing elements within cards creates perceivable chunks, but avoid over-nesting. The aim is to find the right balance through boxing and bounding related data sets to form a cognizable unit.

### 2. Scrolling Accessibility

Swipe gesture is crucial to card design. Most cards employ vertical scroll, but horizontal scroll can provide two-dimensional depth. Be cautious: stacking horizontal scrolling cards can invite accidental and inconvenient flicks and swipes.

### 3. Visual Friction

Cards that transition in response to interactions (like swipe) should offer effective foregrounding of layers without ignoring transitional states. Extend base layers or parent views to full width to act as a freeway to the card's vector.

### 4. Grouping

Mere play of whitespace and visual hierarchy can often group units without an obvious enclosing container. Consider nuances of motion over static design, and reduce guiding lines that don't align with the scroll vector.

### 5. Rack & Carousel

The number of cards and their position is affected by short-term memory load and serial position effect. Choose the right balance of how many cards to accommodate unidirectionally and beyond which point to loop back for a bi-directional scroll.

### 6. Guiding Lines

Closure and continuity are crucial to repeating patterns. With every indentation and padding introduced at the atomic level, the human eye tends to distract itself. Ensure the overall composition of the screen is attended to, not just individual constructs.

### 7. Foregrounding

Cards can be imagined in the same space separated by depth or z-axis. In order to seamlessly translate and transition, cards can afford hierarchy along all three axes. The information most relevant always seems to be closer.

### 8. Form of Action

The card itself being an interactive element can reduce the need for a contemporary primary button, at least on mobile or tap-able devices. Secondary interactions can be designed by pure affordance, keeping in mind the modularity of the construct.

### 9. Card Count

Too many cards within the field of view increase the cognitive load to comprehend and remember all relevant information. The intent to present information in consumable chunks should be a non-compromise when faced with the designer's dilemma to overdo it.

### 10. Alternation

A well-designed feed helps users consume large chunks of information without experiencing visual fatigue. Poor visual alternation can affect users' short-term memory. Alternate layouts to keep users engaged.

## Platform-Specific Patterns

### Apple (iOS, macOS, tvOS)

Apple uses both **translucent and opaque cards** across its platforms. The translucent cards with vibrant visual blurriness communicate a sense of depth and evoke a strong visual hierarchy.

**Example: App Store curated cards**
- Cards feature rich media backgrounds (full-bleed images or videos) with text overlaid directly on the artwork.
- A subtle label (e.g., "WORLD PREMIERE") appears at the top in a smaller, uppercase style to set context.
- The headline is large, bold, and positioned to align with the visual focal point of the background image.
- A short description sits at the bottom, anchored with clear padding to ensure readability against the vibrant background.
- Rounded corners and subtle shadows create a physical, tactile feel.

**Key characteristics:**
- **Depth through translucency:** Background blur and vibrancy effects create layered depth.
- **Text on media:** Headlines and descriptions are placed directly over imagery, relying on contrast and safe text areas rather than separate background containers.
- **Focus states (tvOS):** Cards are optimized for focus — they scale up, gain elevation, and use parallax effects when focused. Increased padding prevents overlap between cards.
- **Offscreen indication:** Cards are displayed partially offscreen to hint that more content is available.

### Google Material Design

- Cards are used broadly for contextual information and feature discovery.
- Predictable card patterns in feeds (e.g., Google Now) encourage exploration.
- Interactive cards in list views (e.g., Google Flights) optimize browsing and decision-making.

### Windows Fluent Design (Tiles)

- Tiles are a form of cards used in grid layouts (e.g., Start Menu).
- Resizable tiles can become inefficient for scanning when scaled, as containers may become empty shells with redundant margins.
- Ensure that resizing preserves affordances and communicates content volume and interaction potential.

## Responsive Checklist

- Does card content look consistent across all breakpoints?
- Are spacing values for gaps consistent?
- Are interactions considered? Do they affect card size and spacing?
- Are long headings/titles handled? How do they affect card content?
