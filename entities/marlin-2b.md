---
title: Marlin-2B
created: 2026-06-11
updated: 2026-06-11
type: entity
tags: [model, vision-language, computer-vision, video-segmentation]
sources: [raw/articles/thread-HappyyPablo-2056839665551024474.md]
---

# Marlin-2B

[[marlin-2b]] is an open 2B-parameter vision-language model for video understanding, released by [[happyy-pablo]] to extract structured information from videos with dense captioning and temporal grounding primitives.

## What it does

The thread presents two core APIs:

- `marlin.caption()` returns a structured Scene + Events JSON with second-level timestamps
- `marlin.find()` returns `(start, end)` timestamps for natural-language queries over a video

That makes the model useful for indexing video libraries, captioning short-form video, and giving agents a compact description of what happened and when inside a clip.

## Positioning

According to the source, Marlin-2B is the strongest open model in its weight class on dense captioning benchmarks like DREAM-1K and CaReBench, beating larger Tarsier-2 variants and landing near [[gemini]] 2.5 Flash / Pro on the specific tasks of captioning and temporal grounding.

## Why it matters

The practical angle is not just “small open VLM,” but “small open VLM tuned for agent loops.” The author explicitly says the model is fast enough to run inline inside an agent loop, which makes it more relevant to operational video systems than general multimodal demos.

## Related

- [[happyy-pablo]]
- [[vision-language-models]]
- [[computer-vision]]
- [[video-segmentation]]
- [[gemini]]
