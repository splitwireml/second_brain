---
title: clear-graphics-vibe-coding-landing-pages
created: 2026-05-07
updated: 2026-05-07
type: entity
tags: [vibe-coding, website, workflow]
sources: [raw/articles/clear-graphics-vibe-coding-landing-pages-2051737941198647642.md]
---

# clear-graphics-vibe-coding-landing-pages

X Article by [[clear-graphics]] (@clear_graphics); full breakdown of vibe coding startup landing pages (4,154 chars, 74 likes, May 5 2026).

## Summary

The article describes a layered prompting workflow for building beautiful startup landing pages with AI coding agents (Cursor or Claude Code) in 4–6 hours. Key components:

**Tool stack:** Cursor or Claude Code (build) + Tailwind CSS (styling, most-represented in AI training data) + Framer Motion or GSAP (animations, must specify explicitly) + Vercel (hosting, push to GitHub → auto-deploy).

**5-layer prompting strategy:**
1. **Structure** — prompt for the HTML skeleton with all sections (hero, social proof bar, 3 features, testimonial, how it works, pricing, FAQ, CTA); all text as placeholders
2. **Design system** — specify colors (primary + accent), typography (font family, sizes, line height), spacing scale (8/16/24/32/48/64/80px only), section padding
3. **Content** — replace placeholders with real copy; value prop in one sentence, 3 features, social proof
4. **Polish** — add scroll animations (fade-in per section), hover effects on CTAs, logo scroll animation via Framer Motion
5. **Mobile** — fully responsive: stack hero vertically, full-width CTAs, reduce heading sizes 30%, reduce padding to 40px, disable logo animation

**Design principles for good output:**
- **Specificity beats vague** — "dark navy gradient #0a0a1a to #1a1a3e, 56px white headline, #4f46e5 accent only on CTA" produces a designed page; "make it look nice" produces garbage
- **Reference real pages** — "style like Stripe's homepage but with my brand colors" works because AI has seen Stripe in training
- **Consistent spacing** — always specify a spacing scale
- **Limit colors** — 4 colors max throughout; AI picking per-section colors produces incoherence
- **Real screenshots** — replace AI-generated placeholder images with actual product screenshots (AI images always look fake)

**Gap note:** The article acknowledges the gap between vibe-coded and professionally designed pages is smaller than ever, but a "considerably sized gap" still always exists.

## Related

- [[clear-graphics-yc-landing-page-framework]] — same author's 7-pattern YC landing page structure
- [[landing-page-ai-workflow]] — Prajwal Tomar's $5,000+ landing page AI workflow (Lovable + GSAP + Spline + Three.js)
- [[ai-cinematic-website-design]] — high-ticket animated website design with Flux/Hexler + Seedance 2.0 + Gemini 3.1
- [[ai-design-workflow]] — Nate Herk's end-to-end brand pipeline: brainstorm Claude → Claude Design → ship Claude Code + Vercel
- [[vibe-coding-in-production]] — Eric Mishra's framework for responsible vibe coding in production
