---
title: Continuous Speech Tokenizers
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [model, oss-ai, speech, genai]
sources: [raw/articles/microsoft-vibevoice-2026.md, raw/articles/vibevoice-architecture-analysis-2026-04-10.md, raw/articles/vibevoice-quantizations-mlx-apple-silicon-2026-04-10.md]
---

# Continuous Speech Tokenizers

## Definition

Speech tokenizers convert raw audio waveforms into discrete token sequences that LLMs can process. **Continuous speech tokenizers** produce tokens at a much lower frame rate than conventional approaches while preserving audio fidelity.

## Key Innovation: 7.5 Hz Frame Rate

Conventional audio tokenizers operate at **50-100 Hz** (50-100 tokens per second of audio). VibeVoice's continuous speech tokenizers (Acoustic + Semantic) operate at just **7.5 Hz** — roughly **7-13x fewer tokens** for the same audio duration.

### Why This Matters

- **Long-form processing becomes feasible:** 60 minutes of audio at 50 Hz = 180K tokens. At 7.5 Hz = 27K tokens — fits in standard 64K context windows
- **Computational efficiency:** Fewer tokens = less compute for both training and inference
- **No quality loss:** The continuous representation preserves audio fidelity despite the lower rate

### Two Tokenizer Types

1. **Acoustic tokenizer** — captures prosody, timbre, speaker characteristics
2. **Semantic tokenizer** — captures linguistic content, meaning

## Architecture Context

Used in VibeVoice's **next-token diffusion framework**:
- LLM processes semantic tokens (text understanding, dialogue flow)
- Diffusion head generates acoustic tokens (high-fidelity audio)
- 7.5 Hz rate makes 60-min single-pass ASR and 90-min TTS possible

## VibeVoice Implementation Details

From the codebase, the tokenizers are VAE-based:

- **Acoustic tokenizer** — VAE encoder outputs 64-dim features; uses `sample()` for stochastic or `.mean` for deterministic output; controlled by `VIBEVOICE_USE_MEAN=1` env var
- **Semantic tokenizer** — VAE encoder outputs 128-dim features; always uses `.mean` (deterministic)
- **Streaming support** — both tokenizers support `VibeVoiceTokenizerStreamingCache` for chunk-by-chunk encoding of long audio (60s segments)
- **Connector** — `SpeechConnector` projects tokenizer output to LM hidden size: `fc1 -> RMSNorm -> fc2` (no activation)

## Comparison with Alternatives

| Approach | Frame Rate | Long-form Capability |
|---|---|---|
| Conventional (EnCodec, DAC) | 50-100 Hz | Requires chunking |
| VibeVoice continuous | 7.5 Hz | Single-pass 60+ min |

## See Also

- [[vibevoice]] — VibeVoice; primary implementation of continuous speech tokenizers at 7.5 Hz
- [[next-token-diffusion-speech]] — Next-token diffusion architecture used by VibeVoice

## Related

- [[vibevoice]] — primary implementation
- [[next-token-diffusion-speech]] — the framework using these tokenizers
