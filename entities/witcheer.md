---
title: witcheer
created: 2026-05-05
updated: 2026-05-05
type: entity
tags: [person, x-creator, content-creator, local-ai, hermes-agent]
sources: [raw/articles/xarticle-httpstco3v4gw8yf31-2051305175961272810.md, raw/articles/xarticle-im-local-ai-maxxing-my-hermes-agent-will-help-2051305175961272810.md]
---

# witcheer ☯︎

X creator (@witcheer); posts on local AI, inference optimization, and personal agent workflows. Runs a Mac Mini M4 16GB as a dedicated local AI workstation with Hermes Agent.

## Profile

- **Platform:** X/Twitter — @witcheer
- **Hardware:** Mac Mini M4 (16GB unified memory)
- **Agent:** Oz — Hermes Agent (Nous Research) running 24/7
- **Focus:** Local AI — models, quantization, inference engines, hardware optimization, fine-tuning, RAG, agent deployment

## Agent Architecture (Oz)

Oz is configured via Hermes Agent with a single SOUL.md mission: research and document everything about running AI locally. The system runs on:

- **Interactive model:** glm-5.1 via Z.AI ($21/month)
- **Cron model:** glm-4.7
- **Local fallback:** ollama models on Mac Mini M4

Local models in rotation:
- gemma 3 4B — 36.7 tok/s (context compression)
- qwen3.5-9B — 13.5 tok/s (daily driver)
- gemma 3 12B — benchmarked
- ministral 3 8B — benchmarked

## Five-Layer Personal AI Stack

1. **Wiki** — ~/wiki/ structured knowledge base; entity + concept + setup + comparison pages
2. **Research Pipeline** — 11 daily cron jobs (morning scan, hardware intel, model tracker, deep research, benchmark, wiki compounding, health check, weekly synthesis, quiz 3x/week)
3. **HuggingFace primary source** — hf-papers.sh, hf-trending.sh, hf-gguf-tracker.sh, hf-model-card.sh
4. **Model stack** — cloud + local ollama with auto-bench.sh and ollama-rotate.sh
5. **Cleanup** — weekly launchd maintenance job

## Related Entities

- [[hermes-agent]] — Nous Research agent framework Oz runs on
- [[ollama]] — local inference runtime on Mac Mini
- [[karpathy-llm-wiki]] — the knowledge compounding pattern Oz's wiki follows
- [[local-ai-maxxing]] — the pivot/concept from the X Article

## Sources

- [X Article: I'm Local AI Maxxing (2051305175961272810)](https://x.com/witcheer/status/2051305175961272810) — Mon May 04 2026; 110 likes, 8 RT
