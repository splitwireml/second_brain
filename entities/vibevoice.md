---
title: VibeVoice — Microsoft Open-Source Voice AI
created: 2026-04-10
updated: 2026-04-10
type: entity
tags:
  - oss-ai
  - model
  - genai
  - speech
sources:
  - raw/articles/microsoft-vibevoice-2026.md
  - raw/articles/vibevoice-architecture-analysis-2026-04-10.md
  - raw/articles/vibevoice-quantizations-mlx-apple-silicon-2026-04-10.md
  - raw/articles/vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10.md
---

# VibeVoice — Microsoft Open-Source Frontier Voice AI

## Overview

VibeVoice is a family of open-source frontier voice AI models from Microsoft, covering both **Text-to-Speech (TTS)** and **Automatic Speech Recognition (ASR)**. 38k+ GitHub stars, MIT license.

**Core innovation:** Continuous speech tokenizers (Acoustic + Semantic) at **7.5 Hz** frame rate — ultra-low rate preserves audio fidelity while enabling efficient long-sequence processing. Combined with a **next-token diffusion framework** (LLM for context + diffusion head for acoustics).

## Models

| Model | Size | Purpose | Status |
|---|---|---|---|
| VibeVoice-ASR-7B | 7B | 60-min single-pass speech recognition | Active, in Transformers |
| VibeVoice-TTS-1.5B | 1.5B | 90-min multi-speaker TTS (4 speakers) | Weights on HF, code removed |
| VibeVoice-Realtime-0.5B | 0.5B | Streaming real-time TTS | Active, Colab demo |

### VibeVoice-ASR (7B)

- **60-minute single-pass** processing (64K token context) — no chunking
- Structured output: **Who** (speaker diarization), **When** (timestamps), **What** (content)
- **Customized hotwords** for domain-specific accuracy
- **50+ languages** supported natively
- **vLLM inference** supported
- Finetuning code available
- Integrated into Hugging Face Transformers (March 2026)

### VibeVoice-TTS (1.5B)

- Up to **90 minutes** of synthesized speech with **4 distinct speakers**
- Accepted as **Oral at ICLR 2026**
- ⚠️ **Code removed Sept 2025** due to misuse; weights still on Hugging Face

### VibeVoice-Realtime (0.5B)

- Streaming text input, robust long-form generation
- **Experimental speakers**: 9 languages (DE, FR, IT, JP, KR, NL, PL, PT, ES) + 11 English style voices

## Timeline

- **2025-08-25:** TTS model open-sourced
- **2025-09-05:** TTS code removed (misuse concerns)
- **2025-12-03:** Realtime-0.5B released
- **2025-12-16:** Experimental multilingual speakers added
- **2026-01-21:** ASR-7B released with finetuning code
- **2026-03-06:** ASR added to Hugging Face Transformers

## Repo Structure — Not Just Models

The repo is a **research-grade model library with production serving capabilities**, organized in four layers:

### Layer 1 — Python SDK (`vibevoice/`)
- `pip install -e .` — installable package
- `vibevoice.modular.*` — model definitions (Transformers-compatible)
- `vibevoice.processor.*` — audio/text processors
- `vibevoice.schedule.*` — DPM solver diffusion scheduler
- Import and use: `from vibevoice.modular import VibeVoiceASRForConditionalGeneration`

### Layer 2 — Demo Applications (`demo/`)
- **Gradio web UI** for ASR — audio upload, transcription with speaker diarization, hotwords, segment playback
- **FastAPI + WebSocket server** for Realtime TTS — streaming audio delivery to browser, 25 voice presets (9 languages + 11 English styles), CFG/steps controls
- **CLI batch inference** — transcribe files, directories, or HF datasets with automatic batching
- **Colab notebook** for Realtime TTS
- **Voice presets** — `.pt` files with prefilled prompts for instant voice switching

### Layer 3 — Production Server (`vllm_plugin/`)
- **vLLM plugin** — registers VibeVoice ASR as a multimodal model
- **OpenAI-compatible REST API** — `vllm serve` on port 8000, accepts audio in chat completions
- **Data parallel deployment** — nginx load balancer + multiple vLLM workers for multi-GPU throughput
- **Tensor parallel** support — split 7B model across GPUs
- **One-click launcher** — installs deps, downloads model, generates tokenizer files, starts server
- API accepts: `{"messages": [{"role": "user", "content": [{"type": "audio_url", "audio_url": {"url": "meeting.mp3"}}]}]}`

### Layer 4 — Fine-tuning (`finetuning-asr/`)
- LoRA fine-tuning using PEFT + Transformers Trainer
- Toy dataset included, inference script for LoRA-adapted models

## Quantizations & Apple Silicon (16GB Mac Mini)

### MLX — Native Apple Silicon (via `mlx-audio`)

**Realtime TTS 0.5B** — all variants run comfortably on 16GB:
- **4-bit** — 733 MB — best balance, recommended
- **5-bit** — 855 MB
- **8-bit** — 1.22 GB
- **fp16** — 2.14 GB — full precision, still fits

**ASR 7B** — the big one, tight on 16GB:
- **4-bit** — 5.71 GB — recommended, leaves ~5-6 GB for KV cache
- **5-bit** — 6.67 GB — works, but close on 60-min audio
- **6-bit** — 7.62 GB — borderline, may swap on long audio
- **bf16** — ~16.7 GB — won't fit

**Usage:**
```bash
pip install -U mlx-audio

# TTS
python -m mlx_audio.tts.generate \
  --model mlx-community/VibeVoice-Realtime-0.5B-4bit \
  --text "Hello" --voice en-Carter_man

# ASR
python -m mlx_audio.stt.generate \
  --model mlx-community/VibeVoice-ASR-4bit \
  --audio "meeting.wav"
```

### GGUF Quantizations (TTS 1.5B only)

The TTS 1.5B model (code removed from repo) has GGUF quantizations via `gguf-org/vibevoice-gguf` and `wsbagnsv1/VibeVoice-1.5B-gguf`. Sizes range from 3.2 GB (Q2_K) to 5.4 GB (BF16). Uses `gguf-connector` (pip install gguf-connector, then `ggc v6`). No GGUF for ASR 7B yet.

### Verdict for 16GB Mac Mini
- **Realtime TTS**: trivially easy, even fp16 fits. 4-bit at 733 MB is overkill.
- **ASR 7B**: 4-bit (5.71 GB) is the sweet spot. 5-bit works but be careful with long audio. Split 60-min files into 20-30 min chunks if hitting memory pressure.

## Architecture

The key architectural insight is the **7.5 Hz continuous speech tokenizer** — conventional audio tokenizers operate at much higher rates (50-100 Hz), making long-form processing computationally expensive. By compressing to 7.5 Hz while preserving fidelity, VibeVoice can process 60 minutes of audio in a single forward pass.

The **next-token diffusion framework** combines:
1. An LLM that understands textual context and dialogue flow
2. A diffusion head that generates high-fidelity acoustic details

This hybrid approach is different from pure autoregressive TTS (like VALL-E) and pure diffusion TTS — it leverages the LLM's language understanding while using diffusion for quality.

## Video Ingestion Pipeline

VibeVoice ASR is used by the `video-ingestion` skill to transcribe video content for wiki ingestion:

1. [[reclip-video-downloader]] downloads audio via ReClip API (`format: "audio"`)
2. VibeVoice ASR transcribes the MP3 → JSON with speaker + timestamp segments
3. Markdown transcription saved to `raw/transcripts/`
4. Standard wiki ingestion

See the `video-ingestion` skill for the full pipeline.

## Related Concepts

- [[continuous-speech-tokenizers]] — VibeVoice's 7.5 Hz VAE tokenizer approach
- [[next-token-diffusion-speech]] — VibeVoice's next-token diffusion architecture
- [[vibevoice-vs-insanely-fast-whisper-comparison]] — ASR comparison with Whisper CLI wrapper
- [[omnivoice]] — Xiaomi's multilingual TTS competitor (600+ languages, no MLX, incompatible voice clone formats)
- [[omnivoice-vs-vibevoice-comparison]] — Detailed side-by-side comparison of both systems
- [[reclip-video-downloader]] — Upstream of the video ingestion pipeline
- [[insanely-fast-whisper]] — Whisper CLI wrapper; alternative ASR option when VibeVoice isn't suitable (CUDA-only machines, quick transcriptions)

## Links

- GitHub: https://github.com/microsoft/VibeVoice
- Project Page: https://microsoft.github.io/VibeVoice/
- Hugging Face: https://huggingface.co/microsoft/VibeVoice
