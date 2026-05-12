---
title: "Higgsfield + Claude Creative Agency Stack"
created: "2026-05-05"
updated: 2026-05-10
type: concept
tags: [higgsfield, claude, creative, ai-agent, automation, workflow]
sources: [raw/articles/xarticle-nateherk-2051295831965367297.md]
related_entity: [[nate-herk]]
---

# Higgsfield + Claude Creative Agency Stack

Turn Claude into a full creative production agency using Higgsfield's model layer + Claude's agent layer + systematic knowledge injection + generation tracking + scheduled automation routines.

## Core Stack

**Higgsfield** = model layer. Access to Nano Banana 2, GPT Image 2, Marketing Studio, Veo, Kling, Seedance via one account.

**Claude** = agent layer. In Claude chat via custom MCP, or in Claude Code via CLI + agent skills. CLI preferred for serious work (MCPs burn tokens with full tool context).

**Workflow**: Claude ideates → prompts Higgsfield → generates asset → writes result back to project.

## Brand Demo (Murmur Headphones)

Single prompt: "Build me a headphone brand from scratch. Do the research. Build the product catalog. For each product generate a photo, an Instagram ad, and a UGC video."

Output in ~5 minutes:
- Brand: Murmur (positioning, target buyer, voice, visual identity)
- 3 products: over-ear, wireless earbuds, open-back wired
- Product photo for each
- Instagram ad for each
- UGC video for each (model wearing headphones, looks human but not quite there yet)

Production time vs studio: ~5 min vs 1 week + paid actress.

## Marketing Studio + Hyper-Motion

Marketing Studio: branded ad creative mode. Drop in product, pick avatar, pick format (UGC, unboxing, hyper-motion).

Hyper-Motion: fast cuts, zooms, tight detail shots. 2 iterations, no fancy prompting.

Pattern: give reference product image, Claude must match exactly → consistent outputs.

## Subject Matter Expertise Injection

**Key insight**: Agent is wrapper, expertise is engine. Without domain knowledge, you get generic outputs.

Method:
1. Deep research prompt (best strategies for organic advertising 2026, platform-specific tactics)
2. Claude produces `advertising-masterclass.md` (617 lines, cheat sheet, platform breakdown, attention frameworks, hook patterns, CTA structures)
3. File lives in project, every agent reads it
4. Tag doc with `@` in prompts to pull into context

Generalize: drop relevant expertise docs (Twitter threads, YouTube transcripts, Perplexity research, internal SOPs) into project as markdown. Reference in prompts. Agent reads on every run.

Same pattern: lead gen → cold email frameworks, newsletter → writer's playbook, sales → call breakdowns.

## Generation Tracker

Google Sheets via GWS CLI. Pull all assets (45 at time of demo), log: product, style, image/video, model, prompt, status, result URL.

Single source of truth for prompt performance + conversion tracking.

Claude reads sheet + research doc → ideates variations (new value props, headlines, avatars, styles) → writes to Creative Slate tab.

Loop: pick priority rows → generate prompts → send to Higgsfield → mark complete when landed.

## Skill/Recipe Pattern

One-off outputs = AI slot machine. Reference images + exact prompt preservation = consistent outputs.

Build skills: find best generation, copy exact prompt, tell Claude "turn this into a skill in `.claude/skills`" → recipe lives for future hyper-motion requests.

**Skill = recipe. Recipes make pancakes that come out the same every time.**

## Scheduled Routines

Claude routines = prompts on schedules.

Sunday night routine:
1. Read Google Sheet
2. Pull performance data from Meta/TikTok
3. Analyze what's working/not
4. Add 50 new generation ideas to sheet

Monday morning routine:
1. Read sheet
2. Pick 30 blank-status rows
3. Generate prompts → send to Higgsfield
4. Mark complete when results land

30 new creative pieces ready to review Monday. Repeat Thursday + Friday. Scale 50 → 100 → 200/week.

Bottleneck shifts from creativity/production → deciding which winners to scale.

Automation pipeline: outputs → Potato/Meta Ads Manager for automatic posting. Whole loop runs without you.

## Wrap

Not magic. Research + model + sheet + skills + schedule.

Each piece boring alone. Stacked = creative team that doesn't sleep, doesn't get tired, doesn't get stuck on prompt syntax.

## Sources

- [[nate-herk]] — X Article (2051644586502615163); 139 likes, 7 RTs; Tue May 05 2026