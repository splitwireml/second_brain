---
title: Video Generation
created: 2026-05-31
updated: 2026-07-21
type: concept
tags: [ai-video, diffusion, generation, video, video-generation]
sources: [raw/articles/gpt-image-2-seedance-2-character-consistency-workflow-2075327959586537848.md, raw/articles/14-second-ai-vlog-method.md]
---

# Video Generation

AI models that generate video from text, images, or video prompts. Key players: [[minimax]], [[seedance-2-0]], [[ltx-2-3]], [[kling]], [[higgsfield]]. Used for [[ai-ugc]], marketing content, and [[ai-3d-scroll-websites]]. A source-described reference-first workflow combines [[gpt-image-2-prompting]] with Seedance 2.0 to reduce identity drift across a multi-shot sequence; the implementation claims are not independently verified. ^[raw/articles/gpt-image-2-seedance-2-character-consistency-workflow-2075327959586537848.md]

The 14-second AI vlog source adds a lighter-weight production pattern: repeat a fixed cast block across independent shots, inspect each generation, and hard-cut the accepted clips. It is a workflow recommendation, not evidence that a particular model or connector will reliably maintain identity or render legible product labels. ^[raw/articles/14-second-ai-vlog-method.md]

## Related Concepts

- [[ai-video]] — AI video more broadly
- [[minimax]] — video generation platform
- [[seedance-2-0]] — Seedance video model
- [[ai-ugc]] — video for UGC
- [[character-consistent-ai-video-workflow]] — reference-first identity locking across image and video generation
- [[14-second-ai-vlog-method]] — short synthetic-UGC sequence with manual QC
