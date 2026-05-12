---
title: Vertical Language Models (VLM) and SLM Fine-tuning
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [llm, fine-tuning, vertical-language-models, slm]
sources: []
related_entity: [[cjzafir]]
author: [[cjzafir]]
---

# Vertical Language Models (VLM) and SLM Fine-tuning

**Vertical Language Models (VLMs)** in this context refer to small-to-medium sized models (7B-15B parameters) that are fine-tuned for specific vertical niches, outperforming general SoTA models in those specific benchmarks. This is distinct from Vision-Language Models.

## Key Claims from CJ Zafir

1. **Small models beat SoTA**: 7B-15B niche-focused VLMs are beating state-of-the-art general LLMs in their specific benchmarks
2. **Cost-effective training**: Built a 350M-parameter dataset for $300 using:
   - Codex 5.5 (Extra High) as orchestrator and quality gate
   - DeepSeek v4 Pro + Kimi 2.6 as execution engines
   - No synthetic or templated datasets
3. **6B model result**: Post-trained a 6B dense model in 15 days, beating Sonnet 4.6 and Gemini 3 Flash
4. **Business model**: SLM fine-tuning agencies charging $10k-$20k one-time fees are viable

## Technical Stack

| Component | Purpose |
|-----------|---------|
| Codex 5.5 (Extra High) | Planning SFT dataset scope, quality gates |
| DeepSeek v4 Pro | Execution engine for handwritten examples |
| Kimi 2.6 | Execution engine for handwritten examples |
| Qwen 3.5 / Gemma 4 | Base models for enterprise SLM fine-tuning |

## Business Opportunity

- SLM fine-tuning agency model: $10k-$20k one-time fee
- Use Qwen 3.5 or Gemma 4 as base models
- Total post-training cost under $1000
- 10x lower cost vs general LLMs
- No privacy issues (on-premise control)
- Full control over the model

## Related Concepts

- [[fine-tuning-llm-libraries-2026]]
- [[qwen3-6-consumer-gpu-tuning]]
- [[gemma-4-drafter]]

## Entities

- [[cjzafir]] — Author of the original tweet