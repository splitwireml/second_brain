---
title: Memory Decay (Mem0)
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [ai-agents, memory, recency-ranking, mem0, llm, search-ranking]
sources: [raw/articles/xarticle-mem0ai-2026.md]
related_entity: [[mem0ai]]
---

# Memory Decay (Mem0)

Recency-aware ranking system for AI agent memory. Introduced by [[mem0ai]] in Mem0 to solve the "freshness problem" in long-running AI agents — where old memories compete equally with recent context, creating noise.

## Overview

Memory Decay adds a soft re-rank at search time based on when memories were last accessed:

- **Boost**: Recently accessed memories get up to 1.5× scaling factor
- **Dampen**: Idle memories get dampened toward 0.3× (5× spread between fresh and stale)
- **No deletion**: Nothing gets hidden or deleted; stale memories still surface when genuinely relevant
- **Search-time only**: No reindexing, no migration, add API unchanged

## Technical Details

- Per-project toggle via dashboard or SDK (`client.project.update({decay: true})`)
- Each memory tracks up to last 20 access timestamps
- Candidate pool widens slightly at search time for reordering headroom
- Public scores clamped to [0, 1] — existing API contracts preserved
- Reinforcement runs fire-and-forget on bounded executor — no latency impact
- Memories predating the toggle use last-update timestamp as fallback

## Use Cases

- **Coding agents**: Keep current sprint context on top
- **Personal assistants**: Prioritize recent user activities (e.g., this month's breakfast routine)
- **Support bots**: Surface recent relevant tickets; old resolved issues don't drown current ones

## Roadmap

- Category-aware weighting (health facts weighted higher than misc observations)
- Per-project auto-tuning based on actual access patterns

## Sources

- X Article by [[mem0ai]]: https://x.com/i/status/2052770549307498535 (122 likes, 15 RTs, May 08 2026)
- Docs: https://docs.mem0.ai/platform/features/memory-decay
- Dashboard: https://app.mem0.ai