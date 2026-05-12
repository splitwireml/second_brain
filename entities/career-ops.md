---
title: Career-Ops
created: 2026-04-13
updated: 2026-04-15
type: entity
tags: [agent, tools, open-source]
sources: [raw/articles/santifer-career-ops-2026-04-13.md]
---

# Career-Ops

AI-powered job search automation built on Claude Code. Developed by Santiago (@santifer), who used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role — then open-sourced the entire system.

## Overview

Career-Ops is an agentic job search pipeline that turns Claude Code into a job hunting command center. It scrapes career portals, evaluates offer fit via a 6-block A-F scoring system, generates ATS-optimized PDFs, and tracks everything in a Markdown-based pipeline.

## Key Facts

- **Author:** Santiago (@santifer) — former founder, Head of Applied AI
- **Repo:** github.com/santifer/career-ops
- **License:** MIT
- **Version:** 1.3.0
- **Stack:** Claude Code + Node.js + Playwright + Go TUI
- **Viral:** @DataChaz (Charly Wargnier) posted about it April 6, 2026 — 235 likes, 48 RTs

## Features

| Feature | Description |
|---------|-------------|
| Auto-Pipeline | Paste URL → evaluation + PDF + tracker |
| 6-Block Eval | Role summary, CV match, level, comp, personalization, STAR prep |
| Portal Scanner | 45+ companies (Anthropic, OpenAI, Stripe, etc.) via Ashby/Greenhouse/Lever |
| Batch Mode | Parallel `claude -p` workers for multiple offers |
| Dashboard TUI | Go + Bubble Tea terminal UI |
| Human-in-the-Loop | System recommends; user decides. Never auto-submits. |

## Pre-configured Companies

Anthropic, OpenAI, Mistral, Cohere, LangChain, ElevenLabs, PolyAI, Retool, Temporal, n8n, Salesforce, Twilio, Gong, and 30+ more across AI labs, voice AI, enterprise, and LLMOps.

## Services

- AI job search system setup — install and configure a [[career-ops]]-style pipeline for a candidate's target role list, job boards, and personal workflow
- Resume/CV tailoring workflow — generate role-specific application packets using the evaluation and personalization flow from [[ai-job-search-automation]]
- Application triage and scoring — score inbound job links so the candidate only spends time on high-fit roles instead of spraying applications
- Career pipeline dashboard setup — stand up a searchable tracker for jobs, decisions, personalized CVs, and follow-up status
- Human-in-the-loop application ops — keep the candidate as final approver while the agent handles scanning, drafting, prep materials, and organization

## Related

- [[ai-job-search-automation]] — the broader pattern Career-Ops implements
- [[autoresearch]] — similar AI workflow loop pattern (Karpathy-inspired autonomous testing)
- [[paperclip-orchestrator]] — agent orchestration with human-in-the-loop approval
- [[paperclipai-paperclip]] — multi-agent platform Career-Ops runs on top of
