---
title: HTML-native design skill
created: 2026-04-21
updated: 2026-04-24
type: concept
tags: [design, skill, agent-tool, vibe-coding, workflow]
sources: [raw/articles/huashu-design-readme-en-2026-04-21.md, raw/articles/huashu-design-skill-md-2026-04-21.md]
related_entity: [[huashu-design]]
---

# HTML-native design skill

A design workflow pattern where an AI coding agent produces finished visual deliverables (HTML prototypes, slides, animations, infographics) through conversation, without the user ever opening a graphical design tool. The agent embodies domain experts (UX designer, animator, slide designer, prototyper) and uses HTML/CSS/JavaScript as the implementation substrate rather than a Figma canvas or After Effects timeline.

## Definition

The agent receives a natural-language design request — "make an iOS prototype for a Pomodoro app, 4 screens, clickable" — and produces a self-contained HTML artifact that the user opens in their browser. The HTML is the medium of implementation, not the medium of delivery (though HTML pages themselves can be the deliverable for web/app contexts). For motion output, the pipeline converts HTML to MP4/GIF with BGM+SFX.

Key constraint (from [[huashu-design]]): **the agent must embody the relevant expert for the task type**. Slides are designed by a slide designer, not a web UI developer. Animations by an animator. The HTML is a common execution substrate that enables the agent to implement across these disciplines.

## Core Principles

### 1. Existing context before blank-page design

Good hi-fi design grows from existing context — brand assets, design systems, UI kits, reference screenshots. Starting from scratch reliably produces generic work. The workflow enforces asking about and gathering these before writing any CSS.

**When context is absent or demand is vague:** enter a structured fallback mode (Design Direction Advisor) that recommends 3 differentiated directions from a philosophy library, generates parallel visual demos, and waits for user selection before proceeding.

### 2. Show assumptions before execution (Junior Designer Workflow)

The agent acts as a *junior designer* reporting to the user-as-manager. Before building, the agent writes out assumptions, placeholders, and reasoning directly into the HTML draft and shows it early. Wrong direction caught early costs 100× less to fix than wrong direction caught at delivery.

### 3. Variations over singular solutions

Design requests always receive 3+ variants across different dimensions (color, layout, interaction pattern, visual style), from by-the-book to novel. The user picks and mixes rather than accepting or rejecting a single proposal.

### 4. Anti AI-slop visual hygiene

AI training corpus produces predictable visual defaults — purple gradients, emoji icons, rounded-corner cards with left border accent, SVG human faces, Inter-as-display, CSS silhouettes substituting for real product photography. These are avoided because they carry zero brand information: every AI-default page looks the same, so no brand is recognizable.

Counter-patterns: `text-wrap: pretty`, CSS Grid, carefully chosen serif display fonts, oklch color system, real photography from Wikimedia/Unsplash, honest placeholders (gray blocks with text labels) over bad implementations.

### 5. Fact verification before assumption (Principle #0)

When a design task mentions a specific product (DJI Pocket 4, Gemini 3 Pro), the first action is a `WebSearch` to confirm existence, release status, and specs — not an assumption from training corpus memory. The cost of a search (~10 seconds) is vastly less than the cost of rework (1-2 hours) when the assumption is wrong.

## Relationship to Vibe Coding

HTML-native design skill is a specific application of the [[vibe-coding]] concept. Where vibe-coding broadly describes natural-language-to-code AI tools, this pattern narrows to *visual design output* specifically: the agent builds in HTML/CSS/JS rather than generating code that renders as the deliverable (e.g., Figma files). The advantage is full expressiveness of the web platform (animation, interactivity, video export) without GUI tooling. The disadvantage is that layer-editable formats (Figma, Keynote) are not native outputs.

## Installation

This is a *pattern* implemented by [[huashu-design]]. To use it:

1. **Install the skill**: `npx skills add alchaincyf/huashu-design`
2. **Configure your agent** to load markdown skills (Claude Code, Cursor, OpenClaw, Hermes all support this natively)
3. **Provide brand assets** when the task involves a specific brand — the pattern enforces a 5-step asset protocol (logo → product shots → UI screenshots → colors/fonts → brand spec)
4. **Verify Playwright** is available if you need clickable prototype verification (`npx playwright install`)

The pattern assumes:
- A coding agent with skill loading capability
- Node.js 18+ for `npx` commands
- Chromium browser for prototype verification and video export
- Internet access for first-run asset download

See [[huashu-design]] for full installation instructions including agent compatibility table, directory structure, and post-install verification.

## Related Concepts

- [[vibe-coding]] — the broader paradigm of natural-language-driven software building
- [[claude-design]] — Anthropic's browser-based design counterpart; GUI vs. conversation, canvas vs. HTML/MP4
- [[prompt-engineering-patterns]] — the prompting discipline that governs agent behavior in these workflows
- [[design-automation]] — general theme of automated visual production
- [[ai-ugc-ad-scaling-system]] — where this pattern intersects with UGC ad workflows
- [[google-labs-code-design]] — Google's design.md format spec for AI coding agents; complementary design-system-to-agent format; both enable design-consistent AI code generation
- [[meng-to]] — designer/educator (@MengTo); DesignCode, Builder OS; 400+ design systems + Claude workflow for template generation; broader context for AI design workflows beyond this specific skill pattern

## Tags

- `vibe-coding` — natural-language-to-code paradigm
- `design` — UI/UX design and visual production
- `skill` — reusable AI workflow modules
