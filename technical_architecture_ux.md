# Treats By Tayjah - Technical Architecture & UX Foundation

## 🏗️ CSS Architecture

### Design System Variables
**File**: `src/styles/design-system.css`
- **Colors**:
  - `--bg-primary`: Soft warm white (e.g., `#FAF8F5`) for an appetizing, clean background.
  - `--bg-secondary`: Light blush/pastel pink (e.g., `#FDF3F1`) for section contrast.
  - `--primary-color`: Elegant deep terracotta or warm chocolate (e.g., `#8B4513`) for primary buttons and CTA.
  - `--text-primary`: Dark charcoal (e.g., `#2D2D2D`) for readability.
- **Typography Scale**: Base 16px (1rem), using a 1.250 (Major Third) scale for elegant headers.
- **Spacing System**: Base 4px grid. 
  - `--space-4`: 16px (padding)
  - `--space-8`: 32px (section gaps)

### Layout Framework
**File**: `src/styles/layout.css`
- **Container**: Max-width of `1024px` centered to keep images from getting too stretched on large monitors.
- **Grid Patterns**:
  - **Menu/Treats Grid**: CSS Grid with `auto-fit` (minimum 300px width) for beautiful, responsive photo displays of cakes and cookies.
  - **Hero**: Flexbox centered, 100vh on mobile, 80vh on desktop.
- **Responsive Utilities**: Mobile-first design. All foundational CSS starts at 320px width, scaling up gracefully via `min-width` breakpoints (768px, 1024px).

## 🎨 UX Structure

### Information Architecture (Sitemap & Page Flow)
**Single-Page Application (SPA) Flow** to reduce friction and bounce rates:
1. **Header**: Sticky navigation with "Gallery", "Menu", "About", and a high-contrast "Order Now" CTA.
2. **Hero Section**: High-resolution video loop or image of a signature Tayjah cake. Trust badge clearly visible: "5/5 Food Hygiene Rating | Based in Manchester (M14)".
3. **Menu Highlights (The Bakes)**: 3-column layout featuring Custom Cakes, Cupcakes, and Cookies.
4. **Visual Gallery**: Integrated Instagram/TikTok grid showing recent work.
5. **About the Baker**: Tayjah's story, reinforcing the bespoke, local, and home-based artisan narrative.
6. **Inquiry / Order Form**: The conversion point. Simple form fields requesting event date, guest count, and design ideas.
7. **Footer**: Social links, contact info, and repeat location/hygiene rating.

### Content Hierarchy & Visual Weight
- **H1 (Hero)**: "Bespoke Bakes for Every Occasion in Manchester" - Largest text, highest contrast.
- **H2 (Section Headers)**: e.g., "Our Signature Treats", "Meet Tayjah". Secondary importance, centered.
- **CTAs**: Solid `--primary-color` background with white text, using subtle hover animations (e.g., slight lift or scale up).

### Accessibility Foundation
- **Keyboard Navigation**: All interactive elements (Form inputs, CTAs, Gallery items) will have clear `:focus-visible` outlines.
- **Screen Reader Support**: Use of semantic HTML5 tags (`<main>`, `<section>`, `<nav>`). Images of cakes will have descriptive `alt` tags (e.g., "Three-tiered custom wedding cake with floral piping").
- **Color Contrast**: Ensuring the terracotta text on the pastel backgrounds meets WCAG 2.1 AA minimum contrast ratios.

## 💻 Developer Implementation Guide

### Priority Order for Phase 3
1. **Foundation Setup**: Initialize the CSS variables (colors, typography).
2. **Layout Structure**: Build the main `<main>` container and responsive section wrappers.
3. **Component Base**: Build the reusable Button components and Form inputs.
4. **Content Integration**: Map out the HTML structure utilizing the Brand Identity copy.
5. **Interactive Polish**: Add smooth scrolling for anchor links and hover states on the gallery grid.

---
**ArchitectUX**: Antigravity
**Foundation Date**: 2026-05-25
**Developer Handoff**: Ready for Frontend implementation.
**Double Check Note**: Verified inclusion of 5/5 Hygiene rating in Hero section, social links integration mapped to Gallery section, and local M14 targeting embedded in the Information Architecture.
