---
title: Local AI Maxxing
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [local-ai, hermes-agent, inference, apple-silicon, agent, knowledge-management, workflow]
sources: [raw/articles/xarticle-httpstco3v4gw8yf31-2051305175961272810.md, raw/articles/xarticle-im-local-ai-maxxing-my-hermes-agent-will-help-2051305175961272810.md]
author: [[witcheer]]
---

# Local AI Maxxing

## Definition

Local AI maxxing is the practice of building a personal AI research and inference stack that runs entirely on your own hardware — eliminating cloud API dependency, compounding knowledge in a personal wiki, and using an agent (Hermes Agent) to autonomously research, document, and benchmark local AI capabilities.

Coined by [[witcheer]] in May 2026; described as a pivot from a split DeFi+AI research agent to a single-mission local AI documentation system.

## Core Thesis

The quality gap between local and cloud models is closing faster than most people expect. The hardware is cheaper than you think. The tools are mature enough to build real workflows on. You don't need to be an expert to start — you build the system that will make you one.

## Five-Layer Architecture

### Layer 1: The Wiki

A structured personal knowledge base at `~/wiki/` following [[karpathy-llm-wiki]] principles:

- **Page types:** concepts (gguf, kv-cache, quantisation), entities (ollama, models, people), setups (apple silicon guides), comparisons (side-by-side analyses), raw source material
- **Standardized frontmatter:** title, created, updated, type, 16-category tags, source URLs
- **Growth model:** 5 seed pages → 30+ by month end → 100+ by quarter end
- **Compounding:** wiki gets smarter every day without manual maintenance

### Layer 2: The Research Pipeline

11 daily cron jobs delivering findings to Telegram:

| Time | Job |
|------|-----|
| 7am | Morning scan — HF papers, trending models, new GGUF uploads |
| 8:30am | Hardware + setup intel — Apple Silicon tips, inference guides |
| 9am+ | Model tracker + breaking news (runs multiple times) |
| 2pm | Deep research — HF papers, GGUF tracker, full model cards, arxiv |
| 6pm | Benchmark + quantisation research |
| 8pm | **Compounding step** — best finding → new wiki page |
| 9pm | Health check — monitoring, DB maintenance, model rotation |
| Sun 8am | Weekly synthesis — wiki lint, orphan detection, gap analysis |
| Mon/Wed/Fri 1pm | Quiz — questions from wiki + model catalog |

### Layer 3: HuggingFace as Primary Intelligence Source

Treating HuggingFace as "the GitHub of AI" — model cards more reliable than blog posts, free rich API. Four scripts:

- **hf-papers.sh** — daily papers filtered by 30+ local AI keywords
- **hf-trending.sh** — trending text models sorted by weekly likes
- **hf-gguf-tracker.sh** — new GGUF uploads (all / known quantisers / new uploaders)
- **hf-model-card.sh** — full metadata + README + benchmarks for any model

arxiv is secondary (catches papers HF curation misses).

### Layer 4: The Model Stack

Cloud + local hybrid:

- **Interactive:** glm-5.1 via Z.AI ($21/month)
- **Cron:** glm-4.7
- **Local fallback:** ollama on Mac Mini M4 16GB

Local benchmarks on Mac Mini M4:
- gemma 3 4B — 36.7 tok/s (context compression; 2x faster than qwen3.5-4B)
- qwen3.5-9B — 13.5 tok/s (daily driver)
- gemma 3 12B — benchmarked
- ministral 3 8B — benchmarked

Key insight: `OLLAMA_KEEP_ALIVE=5m` auto-unloads idle models from RAM. 16GB allows 1 model at a time comfortably, 2 small models if needed.

Scripts:
- **auto-bench.sh** — cold + warm benchmarks any ollama model; builds personal leaderboard
- **ollama-rotate.sh** — removes unused models after 30 days; protects essentials (gemma3:4b, qwen3.5:9b)

### Layer 5: Cleanup

Weekly launchd job:
- Prune sessions > 7 days
- Clear cron output
- Clean Chrome cache (browser-harness skill for JS-heavy pages)
- Vacuum state DB when > 200MB (was 794MB after 3 months; vacuumed back down)

## Key Insights

1. **Clean separation:** Oz is a researcher, not a writer. The human writes; the agent structures and finds. 50-80% rewriting on AI drafts vs. 0% on self-written drafts.

2. **Single mission:** Archiving 17 DeFi skills and 3 months of research to focus entirely on local AI. One wiki. One loop.

3. **Knowledge compounds:** huggingface → research pipeline → wiki → weekly audit → quiz. Every day grows. Every week gets cleaned. Nothing gets lost.

4. **Hardware economics:** Mac Mini M4 16GB is sufficient for local inference workflows with proper model management (auto-unload, rotation, quantization).

## Related Concepts

- [[karpathy-llm-wiki]] — the knowledge compounding pattern this builds on
- [[local-llm]] — self-hosted LLM deployment; eliminates API costs and cloud dependency
- [[hermes-agent]] — the agent framework (Oz runs on Hermes)
- [[ollama]] — local inference runtime used on Mac Mini
- [[auto-bench]] — personal model benchmarking (if documented as concept)
- [[knowledge-graph-rag]] — graph layer on wiki for multi-hop questions
- [[three-tier-local-model-routing]] — hybrid local/cloud pattern (fast triage → compression → heavy fallback → Claude)

## Sources

- [X Article by @witcheer (2051305175961272810)](https://x.com/witcheer/status/2051305175961272810) — Mon May 04 2026; 110 likes, 8 RT; 11,349 chars
