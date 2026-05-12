---
title: landing-page-ai-workflow
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [vibe-coding, prompting, ui-design, workflow, ai-tools, genai, design, website]
sources: [raw/articles/prajwal-tomar-landing-page-ai-workflow-2048742030466339120-2026-04-27.md]
related_entity: [[lovable-dev]]
author: [[prajwal-tomar]]
---

# Landing Page AI Workflow

AI prompting system for building $5,000+ landing pages using vibe-coding. Author: [[prajwal-tomar]].

## Core Principles

1. **Be specific about visual details** — exact values (font size, color hex, letter spacing) over vague descriptions
2. **Describe animations with exact values** — GSAP ScrollTrigger params, timing, easing curves
3. **Specify the layering architecture** — sticky vs relative positioning, z-index values, perspective origins
4. **Upload real assets** — real images stop AI output from looking like AI output
5. **Paste code when needed** — for shaders, custom animations, 3D integrations, paste the component implementation
6. **Iterate on details** — fix one thing at a time with targeted follow-up prompts

## Stack

- [[lovable-dev]] — Builder (React + Tailwind CSS + TypeScript)
- GSAP + ScrollTrigger — Scroll-driven animations, 3D tilt effects
- Spline — 3D model embedding with mouse-tracking parallax
- Three.js — WebGL shader effects (GridDistortion ripple)

## Key Techniques

### Hero Section
- Full-viewport sticky hero with CSS perspective (1200px)
- GSAP ScrollTrigger: `rotateX 8, scale 0.92, y -60` for 3D tilt-back on scroll
- Grain noise SVG overlay at ~3% opacity

### Text Scramble Animation
- Character-by-character reveal: random glyphs → final text over ~3 seconds
- Creates cyberpunk tech feel for headings

### 3D Integration (Spline)
- Paste actual Spline embed code (not natural language description)
- Mouse-tracking parallax at 0.05 multiplier
- Fade in only after text scramble completes for cinematic sequencing

### Section Stacking Architecture
- Hero: sticky, z-index 0
- Projects: relative, z-index 10
- Features: relative, z-index 20
- Contact: relative, z-index 30
- Seamless black-background transitions — no white gaps

### Scroll-Driven Features Section
- 400vh height with sticky inner container
- Content crossfades based on scroll position (not click)
- Step indicators with spinning loaders, dot navigation

### WebGL Shader Effects (Three.js)
- GridDistortion component with mouse-reactive ripple
- Paste entire component implementations directly into prompts

## Outcome

Cinematic scroll-driven landing page with:
- 3D scroll tilt effects (GSAP + CSS perspective)
- Embedded Spline 3D model with mouse tracking
- Character scramble text animations
- WebGL shader distortion (Three.js)
- Scroll-driven content transitions
- Hover image slideshows (1.5s crossfade, 3 images per card)
- Seamless section stacking

## Related Concepts

- [[vibe-coding-in-production]] — Eric Mishra's vibe coding framework
- [[prompt-engineering-patterns]] — Prompt templates including landing page patterns
- [[ai-cinematic-website-design]] — Flux/Hexler → Seedance → Gemini 3.1 workflow for animated marketing sites
- [[clear-graphics-yc-landing-page-framework]] — YC startup landing page conversion patterns

## Related Entities

- [[prajwal-tomar]] — Author and creator
- [[lovable-dev]] — Primary builder platform