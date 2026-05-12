---
title: Insanely Fast Whisper — Thin CLI Wrapper for Whisper
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [oss-ai, tools, speech, genai]
sources: [raw/articles/insanely-fast-whisper-technical-analysis-2026-04-10.md, raw/articles/vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10.md]
---

# Insanely Fast Whisper

## What It Is

A ~180-line CLI wrapper around HuggingFace's `transformers.pipeline("automatic-speech-recognition")`. No custom model, no custom inference engine — just convenience defaults (Flash Attention 2, chunking, batching) plus speaker diarization via pyannote.

**Default model:** `openai/whisper-large-v3` (NOT v3-turbo). Any Whisper checkpoint supported via `--model-name`.

## How Speed is Achieved

Three optimizations on standard Transformers:
1. **Flash Attention 2** (`--flash True`) — ~10x over fp32 (CUDA only, not on MPS)
2. **30-second chunking** — `chunk_length_s=30`
3. **Parallel batching** — 24 chunks by default (`--batch-size 24`)

## Apple Silicon Support

Works with `--device-id mps`, but:
- FA2 doesn't work on MPS — falls back to SDPA
- Default batch size 24 will OOM — use `--batch-size 4` (~12GB VRAM)
- Still faster than raw fp32, but not by the FA2 margin

## Comparison with [[vibevoice]]

See [[vibevoice-vs-insanely-fast-whisper-comparison]] for detailed comparison.

### Fundamental Difference
These are **not comparable products** — they solve the same problem (speech-to-text) with fundamentally different approaches:

| Dimension | IFW | VibeVoice-ASR |
|---|---|---|
| What it is | ~180-line CLI wrapper | Full model library with SDK, vLLM server, demos |
| Model | OpenAI Whisper large-v3 (1.5B) | Qwen2.5-7B + VAE speech tokenizers (8B effective) |
| Speed source | Flash Attention 2 + chunking + batching | 7.5 Hz ultra-low speech tokenization |
| Context | 30-second chunks (re-assembled) | 60-minute single pass (64K tokens) |
| Diarization | External pyannote (separate model, HF token) | Built-in (Who/When/What in one model) |
| Apple Silicon | PyTorch MPS (memory-hungry, no FA2) | MLX (native, memory-efficient) |
| Fine-tuning | Not supported | LoRA available |
| Deployment | CLI only | CLI, SDK, REST API, Gradio, WebSocket |

### Verdict for 16GB Mac Mini
**VibeVoice-ASR MLX 4-bit is better suited for Apple Silicon:**
- MLX > MPS (native framework, unified memory)
- 7.5 Hz = ~27K tokens for 60 min vs Whisper's 120 chunks
- Built-in diarization (no extra ~1.5 GB pyannote model)
- Single-pass long audio vs chunked re-assembly

## See Also

- [[vibevoice]] — VibeVoice entity; ASR alternative with 7.5 Hz tokenizers and MLX support
- [[vibevoice-vs-insanely-fast-whisper-comparison]] — Detailed comparison of both systems

## Links

- GitHub: https://github.com/Vaibhavs10/insanely-fast-whisper
- PyPI: `pipx install insanely-fast-whisper`
