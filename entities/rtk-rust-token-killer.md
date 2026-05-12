---
title: RTK Rust Token Killer
created: 2026-04-12
updated: 2026-04-12
type: entity
tags: [tools, llm, optimization]
sources: [raw/articles/noisyb0y1-ai-cost-optimization-2026-04-10.md]
---

# RTK Rust Token Killer

Terminal-side token filter for AI coding sessions. Sits between terminal output and the AI context window, stripping noise (logs, progress bars, ANSI codes, test output) before tokens are counted. Achieves ~70% input token reduction in a typical 30-minute Claude Code session.

## Related Concepts

- [[ai-cost-optimization]] — input token efficiency via terminal filtering; rtk-rust-token-killer is the input-side half of the token reduction stack
- [[caveman-claude-skill]] — complementary output-side compression; together with RTK, input tokens -70% and output tokens -75%
