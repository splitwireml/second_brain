---
title: Caveman Claude Skill
created: 2026-04-12
updated: 2026-04-12
type: entity
tags: [llm, optimization, skill]
sources: [raw/articles/noisyb0y1-ai-cost-optimization-2026-04-10.md]
---

# Caveman Claude Skill

Claude response compression mode that reduces output verbosity by 65–87% by stripping filler, articles, and explanatory fragments. Used alongside token filtering to minimize output token count per session.

## Related Concepts

- [[ai-cost-optimization]] — token efficiency via output compression; caveman-claude-skill is one half of the token reduction stack (input filter + output compression)
- [[rtk-rust-token-killer]] — complementary input-side token filter; used together with caveman-claude-skill for maximum cost reduction
