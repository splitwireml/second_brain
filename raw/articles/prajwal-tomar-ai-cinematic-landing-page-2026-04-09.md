---
updated: 2026-04-11
type: raw
tags:
  - BFBFBF
title: Prajwal Tomar — Cinematic Landing Page with AI (Specificity-Driven Web Design Prompts)
source_type: tweet-thread
url: https://x.com/prajwaltomar_/status/2042247977142755767
author: Prajwal Tomar (@PrajwalTomar_)
date: 2026-04-09
retrieved: 2026-04-10
---

# Prajwal Tomar — Cinematic Landing Page with AI

**Stats:** 52 likes, 5 retweets

## Thread

**Hook:** "AI can't design clean UI? Just built a cinematic landing page with 3D mouse tracking, WebGL shaders, and scroll animations."

**The Stack:** Lovable (AI builder), GSAP (scroll animations), Three.js (shaders), Spline (3D models).

### 1/ Specificity Over Vague Prompts

"The stack doesn't matter if you're prompting like this: 'Make me a landing page.' You've already lost. SPECIFICITY is what makes AI output look designed instead of generic."

Bad: "cool hero section"
Good: "Full-screen hero, black background, grain overlay 3% opacity, CSS perspective: 1200px, GSAP ScrollTrigger with rotateX: 8, scale: 0.92, y: -60 on scroll."

### 2/ Text Animation

Character scramble effect — random glyphs resolving to final text over 3 seconds. "Don't ask AI to be creative. Give it the exact effect you want and it will execute perfectly."

### 3/ 3D Model Integration

Spline 3D scene, mouse-tracking parallax 0.05 multiplier, fades in after text animation. "Paste the exact Spline embed code into your prompt. Don't make the AI guess."

### 4/ Real Assets

"Stop using AI-generated placeholders. Upload a real dark atmospheric background. Tell it to use bg-cover bg-center bg-no-repeat. This single change takes your page from 'AI-generated' to 'designed' instantly."

### 5/ Scroll Stacking Architecture

```
Hero (sticky, z-0) → tilts back
Projects (relative, z-10) → scrolls over hero
Features (relative, z-20) → scrolls over projects
Contact (relative, z-30) → scrolls over features
```

"You have to tell AI how sections relate in 3D space."

### 6/ WebGL Shader Effects

"You can paste ENTIRE component implementations into your prompt. I gave it a full GridDistortion component with Three.js. Mouse-reactive ripple distortion. Stop describing complex effects. Just paste the code."

### 7/ Iterate on Details

First pass ~80%. Fixes: min-height for last row, preloading for background, z-index for section gaps. "Expect 80% right, then iterate."

### 8/ Prompting Principles

Bad: "Make it look cool" → Good: "font-light, letter-spacing 0.2em, clamp(10px, 1.2vw, 13px), color #BFBFBF"
Bad: "Add a scroll animation" → Good: "GSAP ScrollTrigger, scrub: true, rotateX: 8, scale: 0.92, ease: power2.out"

### 9/ Result

## See Also

- [[html-in-canvas-wicg-proposal]] — HTML in Canvas proposal — visual web integration


3D scroll-tilt, Spline mouse tracking, character scramble, WebGL distortion, scroll transitions, fully responsive. All AI. Zero manual code.

"The gap between 'AI can't design' and 'AI designed THIS?' is literally just your prompts."