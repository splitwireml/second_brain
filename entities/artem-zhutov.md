---
title: Artem Zhutov
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [person]
sources: [raw/articles/artem-zhutov-notebooklm-vs-llm-wiki-2045912259210485815.md]
---

# Artem Zhutov

X creator [@ArtemXTech](https://x.com/ArtemXTech). Experiments with AI knowledge management systems and agent workflows.

## Source

[I Replaced Karpathy's LLM Wiki with Something That Actually Works](https://x.com/ArtemXTech/status/2045912259210485815) — A systematic comparison of Karpathy-style LLM wikis vs. NotebookLM for personal knowledge management. Conclusion: LLM wikis are too token-expensive and slow for personal use; NotebookLM is better for personal ingestion. LLM wikis still superior for deep competitive analysis, PhD-level research, and team settings.

## Core Comparison

| | LLM Wiki | NotebookLM |
|--|--|--|
| Ingestion | Slow (44K tokens/question) | Instant (embedding-based) |
| Cost | High (reads full files per query) | Low (~1 min/answer) |
| Maintenance | High (wiki index must be maintained) | None (sources stay raw) |
| Best for | Deep research, team wikis, competitive analysis | Personal knowledge Q&A |
| Token cost | Blows through limits at scale | Fraction of cost |

## The Knowledge Action Loop

Artem's alternative framework: don't just store knowledge — turn it into skills and integrate into daily routines:

1. Create skills from knowledge (e.g., Dalio's 5-step decision-making → daily template)
2. Integrate skills into daily routines
3. Run skills within routines

He built a NotebookLM skill at notebooklm-skill-artemzhutov.netlify.app that does: find videos/articles → add to notebook → ask questions → get answers with citations.

## Key Observations

- The era of free/subsidized tokens is ending; token costs are tightening
- LLM wiki approach is "very costly and very slow" through API
- NotebookLM excels at multi-source synthesis from YouTube/video content
- For Hermes/OpenClaw/Claude Code channels, NotebookLM can synthesize 21 videos into one coherent picture

## Related

- [[notebooklm-py]] — concept page on NotebookLM as alternative
- [[hermes-agent]] — one of the agents Artem tested NotebookLM against
