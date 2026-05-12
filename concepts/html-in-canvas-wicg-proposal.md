---
title: HTML-in-Canvas (WICG Proposal)
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [tools, performance]
sources: [https://github.com/WICG/html-in-canvas]
---

# HTML-in-Canvas (WICG Proposal)

> **Date:** 2026-04-10
> **Tags:** frontend, canvas, webgpu, webgl, standards, accessibility, security, performance
> **Source:** https://github.com/WICG/html-in-canvas

---

## Overview

HTML-in-Canvas is a **WICG/WHATWG standards proposal** to allow rendering HTML/CSS content directly into `<canvas>` elements — 2D, WebGL, and WebGPU. Instead of the current painful choice between canvas (full rendering control but no browser features) and DOM (rich features but limited rendering control), this API bridges both worlds.

Created August 2024. ~560 GitHub stars. Actively maintained by Chrome engineers (progers, chrishtr, schenney-chromium, foolip) with contributions from Igalia, Figma, JetBrains, Shopify, and Jake Archibald.

## The Core Problem

High-performance web apps (Figma, tldraw, games, charting libraries) use canvas for rendering control, but lose everything the browser gives for free. This forces a **bad trade-off**: re-implement browser features in JS (expensive, error-prone) or simply don't provide them (inaccessible).

**The Figma example** is iconic: they had to "create a browser inside a browser" — building their own text layout engine, accessibility tree, form handling, and internationalization support from scratch, all on top of canvas.

## How It Works — Three Primitives

### 1. `layoutsubtree` attribute

```html
<canvas id="canvas" layoutsubtree>
  <div id="form_element">
    <form>
      <input type="text" value="Hello">
      <button>Submit</button>
    </form>
  </div>
</canvas>
```

The `layoutsubtree` attribute opts in canvas descendants to layout and hit testing. Children get a stacking context, become containing blocks for all descendants, and have paint containment. They behave as if visible but their rendering only appears when explicitly drawn into the canvas.

**Breaking existing content:** Canvas fallback content (elements inside `<canvas>` tags for old browsers) currently exists for accessibility only. With `layoutsubtree`, ALL descendants become layout participants. Only 0.15% of pages have element nodes below canvas in HTTP Archive data, and 8 of 10 random samples used the pattern `<canvas>fallback text</canvas>` (text-only), so breakage risk is low but non-zero.

### 2. `drawElementImage()` (and WebGL/WebGPU equivalents)

```javascript
const ctx = canvas.getContext('2d');
canvas.onpaint = () => {
  ctx.reset();
  const transform = ctx.drawElementImage(form_element, 0, 0);
  form_element.style.transform = transform.toString();
};
```

- **2D Canvas:** `ctx.drawElementImage(element, x, y)` — draws the element's snapshot
- **WebGL:** `gl.texElementImage2D(...)` — renders HTML as a texture
- **WebGPU:** `queue.copyElementImageToTexture(...)` — copies to GPU texture

The method returns a **CSS transform matrix** that keeps the DOM position synced with the drawn position. This is crucial — browser features like hit testing, accessibility, and intersection observer all rely on the element's DOM location, not where it's drawn in canvas.

The transform formula:
```
T_origin^(-1) * S_css_to_grid^(-1) * T_draw * S_css_to_grid
```

### 3. `paint` event

Fires whenever canvas children change visually. Contains a list of changed elements. Canvas drawing commands in the event appear in the current frame. DOM changes in the paint event show up in the subsequent frame.

```javascript
canvas.onpaint = (event) => {
  for (const changed of event.changedElements) {
    ctx.drawElementImage(changed, 0, 0);
  }
};
canvas.requestPaint(); // Force a paint event (like requestAnimationFrame)
```

**Why a new event?** `requestAnimationFrame` fires too early in the rendering loop. The paint event fires late in "update the rendering" steps, after intersection observer, resize observer, and layout are complete — so canvas updates are in sync with the DOM.

### Worker support via `captureElementImage()`

For `OffscreenCanvas` in workers:

```javascript
const elementImage = canvas.captureElementImage(form_element);
worker.postMessage(elementImage, [elementImage]); // Transferable
```

`ElementImage` is a **Transferable** snapshot object with width, height, and close(). This allows rendering HTML content in workers without main thread blocking.

## What Gets Stripped — Privacy-Preserving Painting

This is one of the most important aspects. The API must not expose security- or privacy-sensitive information via canvas pixel readbacks or timing attacks.

**Stripped from canvas rendering:**
- Cross-origin content (iframes, images from other domains, SVG `<use>`)
- System colors, themes, or OS preferences
- Spelling and grammar markers
- Visited link information (cannot detect browsing history)
- Pending form autofill previews
- Password manager popups

**Still exposed (intentionally, for interactivity):**
- Form control rendering
- Scrollbar appearance
- Text selection
- Caret blink rate
- Find-in-page markers
- Text-fragment markers
- `forced-colors` (high contrast mode — already detectable via media query)

## Practical Use Cases

| Use Case | Why It Matters | Company Interest |
|----------|---------------|-----------------|
| **Chart components** (legends, axes, labels) | Complex multi-line styled text in charting libraries is currently painful | — |
| **Creative tools** (Figma, tldraw) | Co-mingle HTML and WebGL/WebGPU content in infinite canvases | **Figma** explicitly endorsed |
| **Web-based IDEs** | Render HTML/Markdown documentation popups over canvas-rendered editors | **JetBrains** ("crucial for web IDE") |
| **In-game menus/UI** | Rich HTML menus in 3D game scenes without re-implementing forms | — |
| **3D surfaces** | HTML rendered onto 3D objects (cube faces, curved surfaces) | three.js demos exist |
| **Media export** | Screenshot/export HTML content as images/video accurately | **Shopify** (web component screenshots) |
| **WebXR** | DOM content in VR/AR immersive sessions | WebXR community group |
| **Accessibility** | Canvas apps finally get proper a11y trees matching rendered content | W3C ARIA working group excited |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    HTML-in-Canvas Pipeline                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  <canvas layoutsubtree>                                      │
│  └── DOM children (visible to browser, hidden from user)     │
│       ├── layout & style computed normally                   │
│       ├── accessibility tree populated                       │
│       └── hit testing works via DOM position sync            │
│                                                             │
│  Rendering update loop:                                      │
│  1. Browser computes layout/styles for canvas children       │
│  2. Intersection observer steps run                          │
│  3. Snapshot of all children recorded                        │
│  4. paint event fires with list of changed elements          │
│  5. Developer calls drawElementImage() for each element      │
│  6. drawElementImage() returns CSS transform for sync        │
│  7. Developer applies transform to element.style.transform   │
│                                                             │
│  Worker pipeline (OffscreenCanvas):                          │
│  1. Main thread: captureElementImage(element) → ElementImage │
│  2. Transfer ElementImage to worker via postMessage          │
│  3. Worker: ctx.drawElementImage(snapshot, 0, 0)             │
│                                                             │
│  3D contexts (WebGL/WebGPU):                                 │
│  ├── texElementImage2D() — HTML → WebGL texture              │
│  └── copyElementImageToTexture() — HTML → WebGPU texture     │
│                                                             │
│  Privacy-preserving painting:                                │
│  ├── Cross-origin content stripped                           │
│  ├── System colors/themes hidden                             │
│  ├── Spelling/grammar markers removed                        │
│  ├── Visited link info hidden                                │
│  ├── Autofill previews suppressed                            │
│  └── Password manager popups not captured                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Comparison with Existing Workarounds

### html2canvas / dom-to-image / snapdom

These are JS libraries that "reconstruct" the DOM as a canvas image. They're fundamentally different from html-in-canvas:

| | html2canvas | dom-to-image | snapdom | html-in-canvas |
|---|-----------|-------------|---------|----------------|
| **Type** | JS library | JS library | JS library | Browser API |
| **Approach** | Re-implements rendering engine in JS | Serializes DOM to SVG then renders | DOM capture engine | Native browser rendering |
| **CSS support** | Partial — misses fonts, shadows, Grid/Flexbox | Better with transforms/pseudo-elements | Good | Full — it IS the browser |
| **External fonts** | Frequently broken | Sometimes broken | Better | Native |
| **CORS images** | Skipped or broken | Sometimes works | Better | Native |
| **Interactivity** | Static snapshot only | Static snapshot only | Static snapshot only | **Fully interactive** |
| **Accessibility** | None | None | None | Automatic |
| **Performance** | Slow (JS rendering) | Medium (SVG serialization) | Faster | **Native speed** |
| **Animation** | No | No | No | CSS animations work naturally |
| **Privacy** | Can leak cross-origin data | Can leak cross-origin data | Can leak cross-origin data | Privacy-preserving by design |

The key difference: html-in-canvas is **interactive** — forms work, text is selectable, screen readers see it. Libraries like html2canvas only produce static images.

### Snapdom Integration Experiment

The snapdom team (8K stars) has already built an experimental plugin that uses `drawElementImage()` instead of SVG `foreignObject` for DOM capture:

```javascript
import { snapdom } from '@zumer/snapdom'
const result = await snapdom(element, {
  embedFonts: true,
  plugins: [htmlInCanvasPlugin()]
})
```

This bypasses the SVG foreignObject limitation entirely and produces more accurate captures. Live demo at snapdom.dev/labs.html.

## Maturity & Standardization Status

| Aspect | Status |
|--------|--------|
| **WHATWG stage** | Stage 1 — Specification being incubated |
| **WHATWG spec PR** | https://github.com/whatwg/html/pull/11588 (713 additions, 58 commits) |
| **Chromium** | Implemented behind flag (`chrome://flags/#canvas-draw-element`) |
| **Dev Trial** | Chrome 138 (desktop + Android) |
| **Origin Trial** | Planned Chrome 148–151 |
| **Estimated shipping** | 2026 |
| **Firefox** | **Negative** position |
| **WebKit/Safari** | **No signal** |
| **Contributors** | 20 (Google, Igalia, community) |
| **Web Platform Tests** | Yes |
| **TAG Design Review** | https://github.com/w3ctag/design-reviews/issues/1204 |

## Browser Vendor Positions — Deep Dive

### Firefox: Negative

Mozilla's position is **Negative** (issue #1076). Key objections from `@smaug----` (Olli Pettay, Mozilla engineer):

1. **Hit testing complexity** — "Especially hit testing can be rather problematic." When HTML is drawn into canvas with transforms, rotations, or shaders, determining where clicks go is non-trivial.
2. **IME popups** — Input Method Editor popups (for CJK text input) position relative to the element, but the element's visual position in canvas may differ from its DOM position.
3. **Webcompat pressure** — If Chrome ships this first, it creates pressure on other browsers to ship "something" prematurely before proper incubation.
4. **Historical baggage** — Firefox previously had `mozSetImageElement` and `drawWindow()` (internal APIs for rendering DOM to canvas) but removed them due to security/privacy concerns.

Mozilla did acknowledge the problem space is "interesting" and that the WHATWG should explore it.

### WebKit/Safari: No Signal

Apple has not taken a position (issue #630). The proposal was most recently discussed with `@smfr` (Simon Fraser) and `@emilio` (Emilio Cobos, Mozilla) and the design is believed to be implementable in both Gecko and WebKit because it "does not require an out-of-band paint step."

### What Would Change Firefox's Mind?

The Chrome team has been iterating based on feedback:
- Moved from retained-mode to **immediate-mode** API (addresses earlier concerns)
- Added **privacy-preserving painting** to address fingerprinting
- Added **transform synchronization** for hit testing
- The WHATWG spec PR is believed to be implementable in Gecko per conversations with Mozilla engineers

## Accessibility Implications

The W3C ARIA working group discussed this and was **excited**. Key points from the March 2026 meeting:

- Canvas-based rendering is "quite popular on the web, with many productivity tools using canvas"
- Current workaround: apps build a **duplicate, invisible DOM tree** just for screen readers (Miro and Google Docs do this with `.sr-only` styles)
- With html-in-canvas, the DOM elements are natively in the accessibility tree — no duplication needed
- `@jcraig` (ARIA working group): "This is something I'm excited about. We've been wanting something like this for a long time"

**Open a11y questions:**
- How to distinguish between canvas children meant for rendering vs. traditional fallback content?
- Focus ring integration with transformed elements
- High contrast mode (`forced-colors`) support — partially addressed

## Hit Testing & Compositing — The Hard Part

This is the most complex aspect of the proposal. When you draw HTML into canvas, you can:

- **Draw it at a different position** than its DOM location
- **Rotate it, scale it, skew it**
- **Draw it on top of canvas content** or **behind canvas content**
- **Draw multiple copies** of the same element

The solution: `drawElementImage()` returns a CSS transform that you apply to `element.style.transform`. This moves the invisible DOM element to match where it's drawn in canvas. Browser hit testing, accessibility, and intersection observer all use this synced position.

**Complex scenarios still open:**
- **Issue #94** (Jake Archibald): Hit testing and layer ordering — what happens when multiple canvas draw commands overlap the same DOM element?
- **Shader transformations**: If you draw HTML through a WebGL shader that morphs it into an irregular shape (e.g., a fluid simulation), where does a click on the antialiased edge go?
- **CSS animations inside canvas**: The proposal says CSS transforms on canvas children are **ignored for drawing** but continue to affect hit testing/accessibility. This means if an element has a CSS animation, the animation plays in the invisible DOM layer but the canvas gets a static snapshot each paint event.

## Relationship to Pretext

Pretext and html-in-canvas solve related but **different** problems:

| | Pretext | HTML-in-Canvas |
|---|---------|----------------|
| **What it does** | Measure text height without DOM | Render HTML into canvas |
| **Type** | JS library (userland) | Browser API (standard) |
| **Text rendering** | Pure JS arithmetic on cached widths | Actual browser text rendering |
| **Scope** | Text only | Full HTML/CSS (forms, images, layout) |
| **Where it runs** | Any browser today | Chrome behind flag (2026) |
| **Interactivity** | None | Full — forms, selection, scrolling |

**They could complement each other:** Pretext could be used for text layout calculations *before* passing elements to html-in-canvas for actual rendering. But they're not competitors — one is a measurement library, the other is a rendering API.

## Limitations & Open Issues

### Technical
- **Display: contents** (issue #48): DOM trees starting with `display:contents` fail to draw
- **CSS-in-Canvas** (issue #107): Proposes Flexbox layout of canvas renderables, still open
- **Worker access** (issue #96): Jake Archibald opened — need way to access all canvas elements in a worker
- **Backdrop-filter** (issue #79): Using current canvas content as backdrop root for glass effects
- **Removed elements** (issue #85): Need `removedElements` in paint event to clean up
- **ElementImage lifetime** (issue #88): When do snapshots get garbage collected?
- **changedElements as Map** (issue #95): Should it be a Map for easier lookup?

### Browser Support
- **Firefox: Negative** — biggest blocker for cross-browser adoption
- **WebKit: No signal** — Apple hasn't committed either way
- Chrome-only for the foreseeable future

### Privacy/Security
- **Fingerprinting vectors** (issue #82): Kaiido asked to enumerate new fingerprinting surfaces
- **Cross-origin content** (issue #77): Need to surface when cross-origin content has been silently omitted
- **Caret blink rate** is exposed — could theoretically be used for fingerprinting

### Design Decisions
- **Multiple draws of same element**: The last position set is used for hit testing/a11y
- **CSS transforms ignored for drawing**: Element's visual appearance in canvas doesn't reflect its CSS transforms
- **Overflow clipping**: Content overflowing the element's border box is clipped

## API Quick Reference

```javascript
// 2D Canvas — basic
const ctx = canvas.getContext('2d');
canvas.onpaint = (event) => {
  ctx.reset();
  const transform = ctx.drawElementImage(element, x, y, width, height);
  element.style.transform = transform.toString();
};
canvas.requestPaint();

// 2D Canvas — with source rect (crop)
ctx.drawElementImage(element, dx, dy, dwidth, dheight, sx, sy, sw, sh);

// WebGL
gl.texElementImage2D(gl.TEXTURE_2D, 0, gl.RGBA, element, 0);

// WebGPU
queue.copyElementImageToTexture(element, {
  texture: myTexture,
  origin: { x: 0, y: 0 },
});

// Worker transfer
const snapshot = canvas.captureElementImage(element);
worker.postMessage(snapshot, [snapshot]);
// In worker:
const ctx = offscreenCanvas.getContext('2d');
ctx.drawElementImage(snapshot, 0, 0);
snapshot.close(); // Release when done
```

## Historical Context

This isn't the first attempt at this capability:

- **`mozSetImageElement`** — Firefox had an API to use a DOM element as an image source for canvas. Removed due to security concerns.
- **`drawWindow()`** — Firefox internal API for rendering a window region to canvas. Never exposed to the web due to fingerprinting risks (could render any window, including banking sites in iframes).
- **SVG `<foreignObject>`** — Allows HTML inside SVG, which can then be rendered to canvas. Limited CSS support, no interactivity, complex to use.
- **WASM DOM Access** — Repeatedly proposed and rejected. Html-in-canvas is the pragmatic alternative: instead of giving WASM direct DOM access, give canvas the ability to render DOM.

## Related

- [[pretext-text-measurement-engine]] — complementary text rendering optimization techniques
- [[open-higgsfield-ai]] — canvas-based creative tools where HTML-in-canvas rendering could apply

## Next Steps / Follow-Up

- [ ] Track Firefox standards position — any change from Negative?
- [ ] Monitor WebKit/Apple signal on standards-positions issue #630
- [ ] Watch Origin Trial (Chrome 148–151) for real-world adoption data
- [ ] Track CSS-in-Canvas proposal (issue #107) — would add Flexbox to canvas renderables
- [ ] Monitor snapdom's html-in-canvas plugin maturation
- [ ] Evaluate for canvas-heavy projects once Origin Trial is available
- [ ] Watch TAG Design Review outcome (issue #1204)
