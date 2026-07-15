---
title: Shortcut
created: 2026-07-15
updated: 2026-07-15
type: entity
tags: [product, ai-agent, ai-tools, ai-business, finance]
sources: [raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]
---

# Shortcut

Shortcut is a source-described agent for spreadsheet and finance workflows. In [[peter-wang]]'s article, it is positioned as a focused competitor to Claude for Excel: its advantage comes from a narrow domain, a lean [[model-agnostic-agent-harness]], and a feedback loop built around the workflows customers actually need. These are claims reported by the local source, not independently audited here. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

## Evidence reported in the article

- Shortcut's internal finance-task evals are reported as 40% cheaper and 17% more accurate than Claude for Excel when both use the same base model, Opus 4.8.
- The reported efficiency difference is 37 versus 61 tool calls per task and 3.7M versus 7.1M input tokens, with the article attributing the result to more efficient tools and lighter context.
- The product routes different work to different models: the article reports using Sol for general spreadsheet work, Gemini Flash for image/PDF perception, GLM 5.2 for cost-sensitive tasks, and a production worker model called Pivot trained from Qwen3.5-27B.
- The team turns customer workflows into benchmarks and evals, then feeds the resulting research back into the product. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

## Related

- [[peter-wang]]
- [[model-agnostic-agent-harness]]
- [[ai-cost-optimization]]
- [[loop-engineering]]
- [[claude]]
- [[qwen]]
