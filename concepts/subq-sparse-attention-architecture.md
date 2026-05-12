---
title: SubQ Sparse Attention Architecture
created: 2026-05-09
updated: 2026-05-10
type: concept
tags: [llm-architecture, sparse-attention, sub-quadratic, subq, ai-research]
sources: [raw/articles/xarticle-subq-2026.md]
---

# SubQ Sparse Attention Architecture

SubQ is a major breakthrough in LLM intelligence — the first model built on a fully sub-quadratic sparse-attention architecture (SSA).

## Key Properties

- **12 million token context window** — first frontier model to achieve this
- **52x faster than FlashAttention** at 1MM tokens
- **Less than 5% the cost of Opus**

## Core Innovation

Standard transformer attention wastes compute by processing every possible relationship between words. Only a small fraction of these relationships actually matter.

SubQ's sparse-attention architecture finds and focuses only on the relationships that matter — achieving nearly 1,000x less compute and a new way for LLMs to scale.

## Context

- Source: [[alex_whedon]] (@alex_whedon) on X
- Tweet: https://x.com/i/status/2051663268704636937
- Company: [[subquadratic]]

## Related Concepts

- [[llm-optimization-interview-notes]]
- [[qwen3-36-27b-sae-fullstack]]
- [[higgsfield-claude-creative-agency]]