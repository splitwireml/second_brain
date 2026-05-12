---
title: Oz (Hermes Agent Persona)
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [hermes-agent, ai-agent, local-ai, apple-silicon, workflow]
sources: [raw/articles/xarticle-httpstco3v4gw8yf31-2051305175961272810.md, raw/articles/xarticle-im-local-ai-maxxing-my-hermes-agent-will-help-2051305175961272810.md]
author: [[witcheer]]
---

# Oz (Hermes Agent Persona)

## Definition

Oz is the name [[witcheer]] gave to their personal Hermes Agent instance, configured via SOUL.md as a single-mission local AI research assistant. The name and identity are deliberately chosen to distinguish this agent from generic "assistant" personas — Oz is a researcher first, not a writer or content creator.

## Identity Configuration

Oz's SOUL.md defines a single mission:

```
you are Oz, a personal AI assistant for Witcheer,
a Local AI practitioner and builder.

your primary mission:
research and document everything about running AI locally.
you maintain a structured wiki at ~/wiki/ and deliver daily research
findings via Telegram.
```

One mission. One wiki. One research loop. Everything else is support infrastructure.

## Role Separation

Key operational insight from the X Article: Oz is not a writer. Oz is a researcher.

- Oz produces structured research findings, model benchmarks, and wiki pages
- Witcheer reads the research and writes the content
- This eliminated 50-80% rewriting on AI-generated drafts
- Clean separation: research (agent) vs. writing (human)

## Architecture

Oz runs on:

- **Mac Mini M4** (16GB unified memory) — dedicated local AI workstation, 24/7
- **Hermes Agent** — Nous Research open-source agent framework
- **Interactive model:** glm-5.1 via Z.AI ($21/month)
- **Cron model:** glm-4.7
- **Local fallback:** ollama models (gemma 3 4B, qwen3.5-9B, gemma 3 12B, ministral 3 8B)

## Related Concepts

- [[hermes-agent]] — the agent framework Oz runs on
- [[local-ai-maxxing]] — the five-layer architecture Oz operates within
- [[karpathy-llm-wiki]] — the knowledge compounding pattern Oz's wiki follows


## Sources

- [X Article: I'm Local AI Maxxing (2051305175961272810)](https://x.com/witcheer/status/2051305175961272810) — Mon May 04 2026; 110 likes, 8 RT
