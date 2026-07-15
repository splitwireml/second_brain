---
title: Dograh Self-Hosted Voice Pipeline Stack
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [audio, asr, tts, llm, inference, gpu, deployment]
sources: [raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]
related_entity: [[dograh]]
author: Mohammed Ali Athar
confidence: high
---

# Dograh Self-Hosted Voice Pipeline Stack

A proposed self-hosted architecture where [[dograh]] fronts a split STT → LLM → TTS voice pipeline running on the same VM, while each inference stage remains independently deployable, streamable, and replaceable.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Target stack

- **Control plane / workflow layer:** [[dograh]]
- **ASR layer:** NVIDIA Speech NIM using Parakeet / Nemotron families
- **LLM layer:** [[sglang]] serving a Gemma 12B-class GGUF checkpoint
- **TTS layer:** ideally [[sglang-omni]] with swappable [[chatterbox]] checkpoints

## What is already strong

**Dograh fit:** Dograh already models the split-pipeline pattern internally, creating separate STT, TTS, and LLM services in its non-realtime run path, and its BYOK model configuration exposes provider/base-URL settings for self-hosted endpoints.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

**ASR fit:** NVIDIA Speech NIM is explicitly designed as a set of independent speech microservices that can be chained by an application. Its ASR matrix offers low-latency streaming and higher-throughput profiles, which maps well to a production voice-agent stack.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

**Runtime pattern fit:** [[sglang-omni]] matches the desired systems design very well: per-stage schedulers, process/GPU placement, streaming edges, and multiple transport backends.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## What is not yet solved

### 1. Gemma GGUF on SGLang needs validation
General GGUF support exists in SGLang/Unsloth workflows, but Gemma GGUF support — especially Gemma 3 GGUF — still shows enough issue history that it should be treated as a risk item rather than an assumption.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

### 2. Chatterbox on SGLang-Omni is not an off-the-shelf path yet
The requested runtime/model pairing is the biggest stack mismatch. Chatterbox is a viable TTS model family, but no native SGLang-Omni support path was found in the current public docs or source tree.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

### 3. GPU compatibility is not the same as deployment viability
Architecturally, RTX 30-series and datacenter GPUs can satisfy the compute-capability floor for NVIDIA NIM. In practice, one-VM co-location will be constrained by VRAM budgets, selected model profiles, and concurrency goals.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Recommended implementation order

1. **Prove the control plane first**
   - bring up Dograh
   - point it at mock or temporary local endpoints
   - verify a full STT → LLM → TTS flow through Dograh
2. **Lock ASR**
   - choose Parakeet CTC vs Nemotron ASR Streaming based on language and diarization needs
   - validate streaming quality and memory footprint
3. **Lock LLM**
   - smoke-test the exact Gemma GGUF candidate on SGLang
   - if unstable, start with a better-supported checkpoint format while preserving the same OpenAI-compatible interface
4. **Lock TTS**
   - either serve Chatterbox behind a thin OpenAI-compatible shim first
   - or adopt a supported SGLang-Omni TTS family as the initial production baseline
5. **Only then package the whole stack as one-run deploy**
   - pinned images
   - env-driven model selection
   - preflight GPU checks
   - healthchecks and startup ordering
   - end-to-end smoke tests

## Recommended near-term verdict

The architecture is sound. The low-risk path is **Dograh + NIM ASR + SGLang LLM + a pragmatic TTS wrapper/service first**, then move toward **SGLang-Omni + Chatterbox** once the Chatterbox runtime support question is settled.^[raw/articles/dograh-voice-pipeline-stack-2026-06-19.md]

## Related

- [[dograh]]
- [[chatterbox]]
- [[sglang]]
- [[sglang-omni]]
- [[tts]]
- [[llm-serving]]
