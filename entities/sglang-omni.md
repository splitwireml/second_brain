---
title: SGLang-Omni
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [platform, inference, tts, multimodal, open-source]
sources: [raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]
confidence: high
---

# SGLang-Omni

SGLang-Omni is a multi-stage serving framework built on SGLang for audio and multimodal pipelines. Its core design is per-stage scheduling, explicit stage placement, streaming edges, and configurable inter-stage transport.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Why it matters

Architecturally, SGLang-Omni is an excellent fit for split-stage voice systems because each stage can be tuned and placed independently. The problem in this research is not the runtime pattern; it is current model support for the requested Chatterbox checkpoints.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Current support relevant here

Public support focuses on Higgs Audio, Fish Speech S2-Pro, Voxtral TTS, Qwen3-TTS, and MOSS-TTS rather than Chatterbox.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Related

- [[sglang]]
- [[chatterbox]]
- [[dograh-self-hosted-voice-pipeline-stack]]
