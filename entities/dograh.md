---
title: Dograh
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [platform, open-source, audio, ai-agent, deployment]
sources: [raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]
confidence: high
---

# Dograh

Dograh is an open-source voice-agent platform built around Pipecat, with WebRTC/telephony entrypoints, a workflow builder, and organization-scoped model configuration for speech-to-speech or split STT/LLM/TTS pipelines.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Why it matters

For this research, Dograh is the orchestration/control plane rather than the inference engine itself. The important finding is that it already supports separate STT, TTS, and LLM services and can target self-hosted OpenAI-compatible endpoints through provider-specific `base_url` fields.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Practical role in the stack

- Front door for browser calls and telephony
- Workflow orchestration and analytics
- Provider routing for BYOK model stacks
- Can sit in front of a custom self-hosted pipeline without first requiring invasive backend changes

## Related

- [[dograh-self-hosted-voice-pipeline-stack]]
- [[sglang]]
- [[llm-serving]]
