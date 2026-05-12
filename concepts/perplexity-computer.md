---
title: perplexity-computer
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [ai-agents, perplexity, automation, productivity]
sources: [raw/articles/coreyganim-perplexity-computer-masterclass-2046229817977192594.md]
---

# perplexity-computer

Perplexity Computer is a digital worker inside Perplexity Pro ($20/mo) or Max ($200/mo) that autonomously completes tasks by breaking them into subtasks and routing each to the best specialized AI model.

## Overview

Unlike a chatbot that answers one question at a time, Perplexity Computer takes a goal, plans execution steps, connects to 400+ apps via OAuth, and works autonomously while you sleep. Replaced 2 full-time virtual assistants ($3K+/month in payroll savings for @coreyganim).

## Technical Architecture

### Multi-Model Orchestration (19 models)
Computer routes each subtask to the optimal specialist:

| Model | Role |
|-------|------|
| Claude Opus 4.7 | Core reasoning and coordination |
| GPT-5.2 | Long-context recall, broad web search |
| Gemini | Deep research tasks |
| Grok | Lightweight speed-sensitive operations |
| Nano Banana | Image generation |
| Veo 3.1 | Video production |

### Connectors (400+ OAuth-integrated apps)
Productivity: Gmail, Calendar, Drive, Notion, Slack, Microsoft Teams; Sales: Salesforce, HubSpot; Developer: GitHub, Vercel; Data: Snowflake, PostgreSQL

### Credit System
- Simple tasks: ~30 credits
- Medium tasks: ~100-500 credits  
- Complex tasks: 1,000-5,000+ credits
- Default: auto-refill OFF, $200/month cap, max $400/month total

## Key Features

- **Spaces** — Persistent project environments with context memory; set once, always available
- **Scheduled Tasks** — Recurring workflows (e.g., Monday 8am meeting prep)
- **Subagent Spawning** — Parallel execution for complex tasks
- **Skill Playbooks** — 50+ domain-specific best practices auto-loaded
- **PRD-First Workflow** — Write a PRD in Claude first, then hand to Computer for execution

## Related

- [[coreyganim]] — Author of the masterclass
- [[ai-agent-automation]] — The type of technology used
- [[automation]] — Domain application
