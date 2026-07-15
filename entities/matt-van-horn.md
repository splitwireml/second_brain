---
title: Matt Van Horn
created: 2026-04-23
updated: 2026-06-29
type: entity
tags: [person, content-creator, x-creator]
sources: [raw/articles/matt-van-horn-gpt-image-2-prompting-2047016569923064055.md, raw/articles/xarticle-mvanhorn-2052422567181611010.md, raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md, raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]
---

# Matt Van Horn (@mvanhorn)

X creator and research synthesizer who uses wide-source sweeps across X, Reddit, YouTube, TikTok, Instagram, and GitHub to compress noisy AI discourse into operator-ready frameworks and command patterns.

## Key Work

- **GPT Image 2 prompting research** (April 2026): ran a `/last30days` sweep on prompting GPT Image 2, pulled examples across Reddit, X, YouTube, TikTok, Instagram, GitHub, and HN, and distilled them into reusable visual prompting patterns.
- **Loop taxonomy and command library** (June 2026): mapped the practical difference between `/goal`, `/loop`, and scheduled routines, then compiled fifteen concrete loop patterns people are actually using across Claude Code, Codex, Reddit, TikTok, and GitHub.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md]
- **Cross-platform sourcing as product method**: repeatedly treats social engagement as a discovery surface but grounds the final synthesis in concrete commands, shipped tools, and attributed examples rather than trend-summary fluff.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md]
- **Memory-budget discipline for agents** (June 2026): argues that always-loaded memory and `CLAUDE.md` should stay brutally small, that skill-specific lessons belong in skills rather than global memory, and that recall should come from query-time retrieval rather than dumping more context into every session.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

## Distinctive Themes

- Uses `/last30days`-style aggregation to turn scattered community anecdotes into structured operator playbooks.
- Focuses on actionable command surfaces, especially where agent workflows can be copied directly into [[claude-code]] or [[codex]].
- Recurrently frames AI workflows as systems design problems: define the control primitive, add a verifier, then bound the budget.
- Distinguishes **push memory** (always injected context such as auto-memory and `CLAUDE.md`) from **pull memory** (query-time retrieval), and treats scarcity as a feature rather than a bug.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

## Related

- [[loop-engineering]]
- [[goal-primitive]]
- [[claude-code]]
- [[codex]]
- [[prompt-engineering-patterns]]
- [[agent-memory-architecture]]
- [[karpathy-claude-md]]
