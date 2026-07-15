---
title: Chatterbox
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [model, tts, audio, open-source]
sources: [raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]
confidence: high
---

# Chatterbox

Chatterbox is Resemble AI's open-source TTS family. The most relevant variants here are Chatterbox-Turbo (350M, English, low-latency, paralinguistic tags) and the larger general/multilingual Chatterbox checkpoints used for broader voice-cloning tasks.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Relevance to this stack

Chatterbox is viable as a standalone TTS runtime today, but it is not currently listed as a supported SGLang-Omni model family. That makes it a runtime/integration decision rather than a model-quality decision.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Important distinctions

- **Turbo**: best fit for low-latency English voice agents
- **Multilingual / normal variants**: broader language support, more general cloning use cases
- **Current gap**: no out-of-the-box SGLang-Omni backend was found for Chatterbox

## Related

- [[tts]]
- [[sglang-omni]]
- [[dograh-self-hosted-voice-pipeline-stack]]
