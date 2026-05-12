---
title: "OpenClaw AI Agent Content Engine"
created: 2026-05-08
updated: 2026-05-10
type: concept
tags: [ai-agent, content, linkedin-growth, openclaw, automation]
sources: []
related_entity: [[MichLieben]]
author: [[MichLieben]]
---

# OpenClaw AI Agent Content Engine

A 5-phase playbook for building an AI-powered content system that grew a LinkedIn account to 30,000+ followers, demonstrated by Max Mitcham (founder of Trigify).

## Key Concepts

### The System Architecture
- **Mac Mini M4** as a dedicated 24/7 server (not VPS/cloud)
- **OpenClaw** as the orchestrator (open-source agentic system for multiple LLMs)
- **Claude Code** for Anthropic models, **Codex** for OpenAI models
- Single GitHub repo containing skills, content, insights, blogs, sales, and reports folders

### Phase 1: Foundation
- Hardware: Mac Mini M4 or repurposed laptop running 24/7
- Software stack: OpenClaw + Claude Code + Codex
- Single GitHub repo for the entire content engine

### Phase 2: First Skill
- Build one skill end-to-end before expanding
- Curation is the moat — quality of resources determines skill quality
- Reverse-engineer top performers using Claude Code Chrome extension
- Test and iterate until drafts come out 70% correct on first pass

### Phase 3: Feedback Loops
- **Meta-skill**: Auto-updates underlying skills after each task
- **Performance loop**: Daily cron pulls post performance data
- **Sales call mining**: Extract topic ideas from real buyer conversations
- **Social listening sweep**: Track trending intent terms across platforms

### Phase 4: Agent Team
- Named agents with defined roles (e.g., Bella as CSO, Rex as marketing lead)
- 9am standup cron: agents review metrics and decide priorities
- Mission Control dashboard: agent status, cron jobs, task board, approve/reject queue

### Phase 5: Content Shipment
- Daily 5-minute workflow: orchestrator suggests 5 angles, human picks one
- Auto-repurpose winning posts across platforms
- LLM-optimized SEO content generates inbound leads ("dead internet theory, except the inbound is real revenue")

## Key Insight
> "Curation is the moat. Knowing what's a great resource and what's noise becomes its own discipline."

## Related
- [[openclaw]]
- [[ai-agent-teams]]
- [[content-automation]]
- [[linkedin-growth]]

## Source
[@MichLieben](https://x.com/MichLieben) | [Tweet 2052742040547729850](https://x.com/i/status/2052742040547729850)