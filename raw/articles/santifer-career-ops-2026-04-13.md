---
updated: 2026-04-13
title: Santifer Career-Ops
url: https://github.com/santifer/career-ops
date: 2026-04-13
type: article
source: X post by @DataChaz (Charly Wargnier), 2026-04-06
---

# Career-Ops — AI Job Search Pipeline

**Author:** Santiago (@santifer)
**X Thread:** @DataChaz posted about this on April 6, 2026 — went semi-viral (235 likes, 48 RTs)

## What It Is

An AI-powered job search automation system built on Claude Code. The developer (Santiago) used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role.

## Core Features

- **Auto-Pipeline**: Paste a job URL → full evaluation + ATS-optimized PDF + tracker entry
- **6-Block Evaluation**: Role summary, CV match, level strategy, comp research, personalization, interview prep (STAR+R)
- **45+ Pre-configured Portals**: Anthropic, OpenAI, ElevenLabs, Stripe, LangChain, Mistral, Cohere, etc. across Ashby, Greenhouse, Lever, Wellfound
- **Batch Processing**: Parallel evaluation with `claude -p` workers
- **Dashboard TUI**: Go terminal dashboard to browse/filter/sort pipeline
- **Human-in-the-Loop**: AI evaluates and recommends; the system NEVER auto-submits

## Tech Stack

- Claude Code (agent brain)
- Node.js (scripts, batch orchestration)
- Playwright (PDF generation via HTML template, portal scraping)
- Go + Bubble Tea (TUI dashboard)
- Markdown + YAML + TSV (data)

## Key Stats

- 740+ job listings evaluated
- 100+ personalized CVs generated
- 1 Head of Applied AI role landed
- 14 skill modes (evaluate, scan, PDF, batch, tracker, apply, etc.)
- 45+ companies pre-loaded

## The Viral Post

@DataChaz (Charly Wargnier) posted about it April 6, 2026 with the hook: "this guy built an insane AI job-hunting agent for Claude Code. He used it to rip through 700+ applications and it literally got him hired. AND HE JUST OPEN-SOURCED IT."

**Reactions:**
- "700 apps and got hired? that's the dream right there"
- "how's the quality on the tailored CVs though? curious if it keeps your voice"
- "if this is what it takes to get a job, the whole economy is cooked to a crisp"
- "he should just interview and show them this workflow and offer to automate their SOPs — hired instantly"

## GitHub

- Repo: https://github.com/santifer/career-ops
- Author: santifer (Santiago) — Head of Applied AI, former founder
- License: MIT
- Version: 1.3.0