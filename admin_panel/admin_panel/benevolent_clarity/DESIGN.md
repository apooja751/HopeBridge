---
name: Benevolent Clarity
colors:
  surface: '#f7faf9'
  surface-dim: '#d8dbda'
  surface-bright: '#f7faf9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f3'
  surface-container: '#eceeee'
  surface-container-high: '#e6e9e8'
  surface-container-highest: '#e0e3e2'
  on-surface: '#181c1c'
  on-surface-variant: '#3f4949'
  inverse-surface: '#2d3131'
  inverse-on-surface: '#eff1f0'
  outline: '#6f7979'
  outline-variant: '#bec9c8'
  surface-tint: '#13696a'
  primary: '#006162'
  on-primary: '#ffffff'
  primary-container: '#2c7a7b'
  on-primary-container: '#c1ffff'
  inverse-primary: '#89d3d4'
  secondary: '#576060'
  on-secondary: '#ffffff'
  secondary-container: '#d8e1e1'
  on-secondary-container: '#5b6465'
  tertiary: '#81472a'
  on-tertiary: '#ffffff'
  tertiary-container: '#9e5f40'
  on-tertiary-container: '#fff0eb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a5eff0'
  primary-fixed-dim: '#89d3d4'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f50'
  secondary-fixed: '#dbe4e4'
  secondary-fixed-dim: '#bfc8c8'
  on-secondary-fixed: '#151d1d'
  on-secondary-fixed-variant: '#404849'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb693'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#6e381c'
  background: '#f7faf9'
  on-background: '#181c1c'
  surface-variant: '#e0e3e2'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  button-text:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  container-max: 1280px
---

## Brand & Style

The design system is anchored in a philosophy of "Transparent Empathy." As a donation management platform, the interface must balance the rigor of financial oversight with the warmth of humanitarian aid. The style is a hybrid of **Minimalism** and **Soft Modernism**, utilizing generous whitespace and a "Glass-Organic" approach. 

The UI evokes trust through structural clarity and accessibility. By employing heavy rounding and a soft, mint-infused palette, the system sheds the coldness typical of financial software, replacing it with an airy, optimistic atmosphere that encourages engagement from both donors and administrators.

## Colors

The palette is led by **Deep Teal**, a color associated with stability and wisdom. This is reserved for primary actions and active states to provide a strong visual anchor. 

The background is not a flat white but a subtle **Mint-to-White linear gradient** (180-degree), which reduces eye strain and reinforces the "Bridge" metaphor—moving from a cool, calm start to a clean, transparent finish. 

Status colors are vibrant and high-contrast, ensuring that critical donation alerts or verification milestones are immediately legible against the soft background.

## Typography

This design system utilizes **Manrope** for headlines to provide a modern, geometric, and professional character. Its balanced proportions make large numerals (critical for donation amounts) look prestigious and clear. 

For body copy and functional labels, **Inter** is used for its exceptional legibility and neutral tone. Primary text uses a deep slate-grey to maintain high contrast without the harshness of pure black, while secondary text is softened to a medium grey to establish a clear information hierarchy.

## Layout & Spacing

The system follows a **Fluid Grid** logic with a maximum container width for desktop viewing. Content is organized on an 8px rhythmic scale, ensuring all components align harmoniously. 

The layout philosophy emphasizes "Air." Margins between major sections are generous (lg/xl units) to prevent the management dashboard from feeling cluttered. Elements should span a 12-column system, with standard cards typically occupying 3, 4, or 6 columns depending on the data density required.

## Elevation & Depth

Visual hierarchy is achieved through **Ambient Shadows** and light tonal layering. Instead of heavy black shadows, the system uses a diffused, low-opacity shadow with a slight Teal tint (`rgba(44, 122, 123, 0.08)`) to make cards appear as if they are floating gently above the mint background.

Hints of **Glassmorphism** should be applied to navigation bars and overlays. Use a `backdrop-filter: blur(12px)` with a semi-transparent white fill (`rgba(255, 255, 255, 0.7)`) to maintain context of the background gradient while ensuring the foreground content remains the priority.

## Shapes

The shape language is defined by a consistent **16px radius (Level 2)**. This heavy rounding is applied to all primary containers, including cards, buttons, and input fields. 

This specific radius is chosen to communicate friendliness and safety. Small elements like checkboxes or tags should maintain a proportional 4px-8px radius, but any element that acts as a container for data or a primary touchpoint must adhere to the signature 16px curve.

## Components

### Buttons
Primary buttons use the Deep Teal fill with white text and a 16px radius. Hover states should introduce a slight lift (elevation increase) rather than just a color change. Secondary buttons use a Teal outline with a very soft mint ghost fill.

### Cards
Cards are the primary vehicle for information. They must be Crisp White (#FFFFFF) with a 16px radius and the signature diffused teal-tinted shadow. Padding inside cards should be a minimum of 24px (md) to maintain the airy aesthetic.

### Input Fields
Inputs should have a subtle 1px border in a light grey-teal, which transitions to a 2px Deep Teal border on focus. The 16px rounding ensures they feel integrated with the rest of the UI.

### Status Chips
Chips for "Urgent" or "Verified" should use a low-opacity version of the status color for the background (e.g., 10% opacity) with the full-vibrant color for the text and a small leading icon.

### Progress Bars
For donation goals, use a thick 12px track. The "unfilled" portion should be the light background mint, while the "filled" portion uses a vibrant Emerald Green to symbolize growth and completion.