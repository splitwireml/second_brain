---
title: Prompt Engineering Patterns - 10 High-Impact Templates
created: 2026-04-09
updated: 2026-04-13
type: concept
tags: [marketing, method, monetization, opportunity, llm]
sources: [raw/articles/x-10-prompts-40-hours.md, raw/articles/prajwal-tomar-ai-cinematic-landing-page-2026-04-09.md, raw/articles/stijn-feijen-claude-seedance-makeugc-system-2026-04-13.md]
---

# Prompt Engineering Patterns - 10 High-Impact Templates

## Core Principle

The gap isn't in the AI model — it's in how you ask. Engineers and founders who get 10x results from the same tools use **structured, constraint-driven prompts** that force the model into specific reasoning modes rather than open-ended generation.

Key insight: telling the model *how* to think, not just *what* to write.

## The 10 Patterns

### 1. Human Writing Filter
**Use before publishing any AI-generated text.**
Forces the model to self-edit by highlighting every change and explaining why. The "flag anything still robotic" catch-all prevents the model from stopping at surface-level edits.

```
Rewrite this. Remove filler phrases. Vary sentence length. Add contractions.
Use specific details. Highlight every change and explain why.
Flag anything still robotic: [TEXT]
```

### 2. Hook Generator
**Solves the blank page problem for content creation.**
Generates 20 hooks across 5 proven frameworks (curiosity gap, bold claim, statistic, story opener, controversial take). The 1-10 virality rating with justification forces ranking, not just listing. This same pattern appears directly in [[ai-ugc-ad-scaling-system]], where [[stijn-feijen]] uses Claude to generate multiple TikTok ad angles before turning the best ones into scripts for [[seedance-2-0]] and [[makeugc]].

```
Generate 20 scroll-stopping hooks for [TOPIC] using:
curiosity gap, bold claim, statistic, story opener, controversial take.
Rate each 1-10 on virality with a one-line justification.
```

### 3. SEO Content Brief
**Replaces $500+ agency briefs.**
Comprehensive brief in one prompt: search intent, word count, H2/H3 structure, competitor gaps, meta description, internal linking targets, featured snippet strategy, schema markup.

```
Generate a full content brief for [KEYWORD].
Include: search intent, word count, H2/H3 structure, competitor gaps,
meta description, internal linking targets,
featured snippet strategy, schema markup.
```

### 4. SaaS Idea Validation
**First-principles analysis before writing code.**
Forces the model to evaluate market size, competition, defensibility, give a build/no-build verdict, scope an MVP with timeline, and identify the 3 riskiest assumptions to test first.

```
Validate this idea with first-principles analysis.
Market size, competition, defensibility, build/no-build verdict.
MVP scope with timeline. The 3 riskiest assumptions to test first: [IDEA]
```

### 5. Objection Handler
**Surfaces the buyer's internal resistance.**
Lists 15 objections before buying [PRODUCT], with one-liner counters categorized by type (price, trust, timing, competition) and placement suggestions on the page.

```
List 15 objections people have before buying [PRODUCT].
For each: one-liner counter for copy.
Categorize by type (price, trust, timing, competition).
Suggest exactly where to place each counter on the page.
```

### 6. Brutal Code Review
**Pre-push review from a hostile senior dev perspective.**
Uses adversarial framing ("HATES this implementation") to surface issues the author is blind to. More effective than "review this code" because the adversarial framing removes the model's tendency to be diplomatic.

```
Do a git diff. Pretend you're a senior dev who HATES this implementation.
Tear it apart — what would you criticize, refactor, or reject in a PR review?
```

### 7. Task Prioritization
**Converts a to-do list into an execution plan.**
Forces delegation and automation flagging, identifies the single unblocking task, and adds buffer time. Turns 10 seconds of input into a 7-day plan.

```
Turn this task list into a 7-day execution plan.
Flag what I can delegate. Flag what I can automate.
Identify the one task that unblocks everything else.
Add buffer time: [TASKS]
```

### 8. Production Bug Debug
**Systematic replacement for 2 hours of Googling.**
10 diagnostic steps, environment diff checklist, logging strategy, and monitoring setup. Forces a process rather than guessing.

```
Walk me through a systematic debug process with 10 diagnostic steps.
Include an environment diff checklist, a logging strategy, and how to set up monitoring
to catch this next time. Error: [ERROR]
```

### 9. Above-the-Fold Landing Page Copy
**3-second value communication.**
Generates headline, subheadline, CTA, social proof line in 3 variations (benefit-led, curiosity-led, social-proof-led) with hero image direction for each. Designed for A/B testing.

```
Write above-the-fold copy for [PRODUCT] that communicates value in 3 seconds.
Headline, subheadline, CTA text, social proof line.
3 variations: benefit-led, curiosity-led, social-proof-led.
Hero image direction for each.
```

### 10. Digital Product Generator
**Monetizes expertise into products.**
10 product ideas from a given skill, with pricing, format, build time, revenue-vs-effort ranking, and cross-sell identification. Designed to find the one product that pays for the AI subscription for a year.

```
Generate 10 digital product ideas I can build from my expertise in [SKILL].
Include pricing, format, estimated build time.
Rank by revenue vs effort.
Identify which products cross-sell with each other.
```

## Reported Results (6 weeks)

| Metric | Before | After |
|--------|--------|-------|
| Token cost/month | $180 | $40 |
| First drafts/week | 2 | 7 |
| 3-hour tasks | 3 hours | 25 min |
| Time saved/month | — | 40+ hours |
| Money saved/month | — | $140 |

## Why These Work

All 10 prompts share these structural properties:

1. **Specific output format** — tells the model exactly what shape the answer should take (list of 15, 3 variations, 10 diagnostic steps)
2. **Constraint-driven** — limits scope with explicit boundaries (categorize by type, rate 1-10, rank by revenue vs effort)
3. **Adversarial or role-based framing** — assigns the model a persona (senior dev who hates it) that breaks default politeness
4. **Actionable deliverable** — every prompt produces something you can immediately use (a brief, a plan, counters for a page)
5. **No open-ended "tell me about"** — every prompt starts with a verb that forces generation, not explanation

## Related Concepts

- [[research-code-agent-cli-automation]] — Claude Code CLI interfaces where the brutal code review prompt applies
- [[gsd-2-ai-vibe-coding-framework]] — Framework that could incorporate these prompt patterns
- [[vibe-kanban-agent-spawning]] — Orchestration system where prompt patterns could be templated
- [[ai-ugc-ad-scaling-system]] — marketing execution pattern where hook and script prompts drive daily creative testing

## Web Design & UI Prompting Patterns

Source: [Prajwal Tomar thread](https://x.com/prajwaltomar_/status/2042247977142755767) (April 2026). Built a cinematic landing page with 3D mouse tracking, WebGL shaders, scroll animations using Lovable + GSAP + Three.js + Spline — zero manual code.

These patterns are specific to **AI-driven web/UI generation** (Lovable, v0, etc.) and differ from the text/business patterns above:

### The Specificity Rule

The entire thesis: vague prompts produce generic-looking pages. Specificity with exact values makes AI output look "designed."

| Vague (fails) | Specific (works) |
|---------------|-----------------|
| "cool hero section" | "Full-screen hero, black background, grain overlay 3% opacity, CSS perspective: 1200px, GSAP ScrollTrigger with rotateX: 8, scale: 0.92, y: -60" |
| "Make it look cool" | "font-light, letter-spacing 0.2em, clamp(10px, 1.2vw, 13px), color #BFBFBF" |
| "Add a scroll animation" | "GSAP ScrollTrigger, scrub: true, rotateX: 8, scale: 0.92, ease: power2.out" |

### Pattern: Paste Code, Don't Describe

For complex effects (WebGL shaders, Three.js components), paste the full implementation into the prompt instead of describing it. AI integrates pasted code flawlessly but struggles to generate complex effects from description alone.

### Pattern: Use Real Assets, Not Placeholders

Upload actual backgrounds/images and specify CSS properties (`bg-cover bg-center bg-no-repeat`). This single change takes output from "AI-generated" to "designed."

### Pattern: Define Z-Space Relationships

Tell AI how sections layer in 3D space with explicit z-index stacking:
```
Hero (sticky, z-0) → Projects (relative, z-10) → Features (relative, z-20) → Contact (relative, z-30)
```

### Pattern: Expect 80%, Iterate the Rest

First pass is never perfect. Typical fixes: min-height adjustments, preloading order, z-index gaps. Iterate on the remaining 20% rather than regenerating.
