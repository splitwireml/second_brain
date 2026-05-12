---
title: VibeVoice vs Insanely Fast Whisper Comparison
created: 2026-04-10
updated: 2026-04-10
type: comparison
tags: [comparison, speech, oss-ai]
sources: [raw/articles/vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10.md]
---

# VibeVoice-ASR vs Insanely Fast Whisper

## Fundamental Difference

Not comparable products — they solve speech-to-text with fundamentally different approaches:

| Dimension | Insanely Fast Whisper | VibeVoice-ASR |
|---|---|---|
| What it is | ~180-line CLI wrapper around Transformers pipeline | Full model library with SDK, vLLM server, demos, fine-tuning |
| Model | OpenAI Whisper large-v3 (1.5B params) | Qwen2.5-7B + VAE speech tokenizers (8B effective) |
| Speed source | Flash Attention 2 + 30s chunking + batching | 7.5 Hz ultra-low speech tokenization (7-13x fewer tokens) |
| Context | 30-second chunks (re-assembled) | 60-minute single pass (64K tokens) |
| Output | Plain text + chunk timestamps | Structured: Who + When + What |
| Diarization | External pyannote (separate model, HF token) | Built-in to the model |
| Fine-tuning | Not supported | LoRA available |
| Deployment | CLI only | CLI, SDK, REST API, Gradio, WebSocket |

## Apple Silicon (16GB Mac Mini)

| Metric | IFW (MPS) | VibeVoice-ASR (MLX 4-bit) |
|---|---|---|
| Framework | PyTorch MPS | MLX (native Apple Silicon) |
| Disk size | ~3 GB (fp16) | 5.71 GB (4-bit) |
| VRAM usage | ~12 GB (batch-size 4) | ~8-10 GB |
| FA2 support | No (CUDA only) | N/A (MLX optimized) |
| Long audio (60 min) | 120 chunks x batch 4 = 30 passes | 1 forward pass (~27K tokens) |
| Diarization memory | Extra ~1.5 GB (pyannote) | Built-in, no extra model |

## Verdict

**For Apple Silicon:** VibeVoice-ASR MLX 4-bit is better — MLX > MPS, single-pass long audio, built-in diarization.

**For CUDA servers:** IFW is simpler for quick transcriptions — one command, FA2 optimized, supports any Whisper checkpoint.

## See Also

- [[vibevoice]] — VibeVoice entity page
- [[insanely-fast-whisper]] — Insanely Fast Whisper concept page

## Sources

- [[vibevoice]]
- [[insanely-fast-whisper]]
- Full analysis: raw/articles/vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10.md
