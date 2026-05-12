---
title: Next-Token Diffusion for Speech
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [model, genai, speech]
sources: [raw/articles/microsoft-vibevoice-2026.md, raw/articles/vibevoice-architecture-analysis-2026-04-10.md, raw/articles/vibevoice-quantizations-mlx-apple-silicon-2026-04-10.md]
---

# Next-Token Diffusion Framework for Speech

## Definition

A hybrid speech generation architecture that combines an **LLM for textual/context understanding** with a **diffusion head for acoustic generation**. Used in [[vibevoice]].

## How It Works

1. **LLM component** processes text input and understands context, dialogue flow, and semantics
2. **Diffusion head** takes the LLM's output and generates high-fidelity acoustic details (the actual sound)
3. Both components operate on continuous speech tokens at **7.5 Hz** (see [[continuous-speech-tokenizers]])

## Why This Architecture

- **Pure autoregressive TTS** (VALL-E, NaturalSpeech): Good at language understanding but diffusion can produce higher audio quality
- **Pure diffusion TTS**: High quality but lacks language understanding
- **Next-token diffusion**: Best of both — LLM handles "what to say and how to express it," diffusion handles "how it sounds"

## Code-Level Implementation (VibeVoice-Realtime)

From the codebase:

- **Two LMs**: `language_model` (lower Qwen2.5 layers for text encoding) + `tts_language_model` (upper Qwen2.5 layers for speech generation). Separated deliberately to prevent accidental mixing.
- **`VibeVoiceDiffusionHead`** — takes LM hidden states and generates acoustic details via diffusion
- **DPM-Solver** scheduler (`DPMSolverMultistepScheduler`) with configurable inference steps (default: 5)
- **`BinaryClassifier`** — 2-layer MLP that predicts EOS from the last hidden state, deciding when a speech segment ends
- **`AudioStreamer`** / `AsyncAudioStreamer` — yields audio chunks as they're generated for real-time playback
- **`forward_lm()`** — base text LM step (prefill or incremental)
- **`forward_tts_lm()`** — single TTS LM step that splices in LM hidden states + adds type embedding (text=1/speech=0)
- **Unified `forward()` is disabled by design** — enforces staged pipeline usage

## Key Benefits

- **Long-form coherence:** LLM maintains context across 90+ minutes of speech
- **Multi-speaker support:** Up to 4 distinct speakers in VibeVoice-TTS
- **Style control:** LLM can adapt tone, emotion, pacing based on text context
- **Computational efficiency:** 7.5 Hz tokenization reduces compute requirements

## See Also

- [[vibevoice]] — VibeVoice; primary implementation of next-token diffusion speech
- [[continuous-speech-tokenizers]] — 7.5 Hz tokenizers that feed into the diffusion architecture

## Related

- [[vibevoice]] — primary implementation
- [[continuous-speech-tokenizers]] — tokenization approach
