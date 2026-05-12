---
title: GPT Image 2 Prompting
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [prompting, genai, image-generation, openai]
sources: [raw/articles/matt-van-horn-gpt-image-2-prompting-2047016569923064055.md]
related_entity: [[matt-van-horn]]
author: [[matt-van-horn]]
---

# GPT Image 2 Prompting

Community-discovered prompting patterns for OpenAI's GPT Image 2 model, synthesized via /last30days research workflow. The model jumped 250+ ELO on LMArena (biggest single-release gap ever recorded in image generation).

## Key Findings

1. **Use thinking models**: GPT-5.4 Thinking and GPT-5.4 Pro produce significantly better outputs than non-thinking models for complex image generation
2. **Quote literal text**: Double-quote exact text for near-perfect typography rendering (engages the high-accuracy text rendering engine)
3. **The model thinks**: GPT Image 2 plans, searches the web for references, critiques its own output, and iterates before rendering — prompts can carry more context
4. **Aspect-ratio hack**: API has no dedicated ratio control; append exact pixel dimensions (e.g., "Output in exactly 1774px x 887px (2:1 ratio)")
5. **Prompt order**: Scene → Subject → Details → Constraints → intended use (ad, UI mock, infographic, editorial photo)
6. **Text-to-image works; image-to-image is broken**: Reference-image editing still yellow-tints and loses instruction following

## Prompt Format Insights

- First words carry highest visual weight — lead with style, not subject
- Sequential-weighting matters
- For character consistency sheets: single prompt, eight moments, same person across all shots (no LoRA or ControlNet needed)

## Related

- [[prompt-engineering-patterns]] — general prompting patterns
- [[openai]] — GPT Image 2 provider
