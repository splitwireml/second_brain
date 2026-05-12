---
title: vllm-mlx
created: 2026-04-27
updated: 2026-04-27
type: entity
tags: [apple-silicon, llm, local-llm, multimodal, inference, openai, anthropic, speech]
sources:
  - raw/articles/github-waybarrios-vllm-mlx-2026-04-27.md
url: https://github.com/waybarrios/vllm-mlx
related_entity: []
---

# vllm-mlx

A vLLM-style inference server for Apple Silicon Macs. Ships continuous batching, paged KV cache, prefix caching, and SSD-tiered cache, and exposes both OpenAI `/v1/*` and Anthropic `/v1/messages` from a single process. Runs LLMs, vision models, audio, and embeddings on Metal with unified memory — no model conversion step required.

## Setup

```bash
# Install
pip install vllm-mlx

# Audio extras
pip install vllm-mlx[audio]
brew install espeak-ng
python -m spacy download en_core_web_sm

# From source
git clone https://github.com/waybarrios/vllm-mlx.git
cd vllm-mlx
pip install -e .

# Serve a model
vllm-mlx serve mlx-community/Llama-3.2-3B-Instruct-4bit --port 8000 --continuous-batching
```

## Key Features

- **Dual API support**: OpenAI `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/rerank`, `/v1/responses` + Anthropic `/v1/messages` (streaming, tool use, system prompts)
- **Continuous batching**: high throughput for concurrent requests
- **Paged KV cache**: memory-efficient with prefix sharing; SSD-tiered cache via `--ssd-cache-dir`
- **Warm prompts**: preload popular prefixes at startup (`--warm-prompts`) for 1.3–2.25x TTFT improvement
- **Multimodal**: text + image + video + audio from one server; supports Gemma 3/4, Qwen3-VL, Pixtral, Llama vision
- **Native TTS**: 11 voices, 15+ languages via Kokoro, Chatterbox, VibeVoice, VoxCPM
- **STT**: Whisper family with RTF up to 197x on M4 Max
- **MCP Tool Calling**: 12 parsers (OpenAI, Anthropic, Gemini, Qwen, DeepSeek, Gemma, and more)
- **Reasoning extraction**: Qwen3, DeepSeek-R1 via `--reasoning-parser`
- **MoE expert reduction**: `--moe-top-k` for +7–16% on Qwen3-30B-A3B
- **Speculative decoding**: `--mtp` for Qwen3-Next
- **Structured output**: JSON Schema via `response_format` (lm-format-enforcer)
- **Prometheus metrics**: `/metrics` endpoint with `--metrics`
- **Built-in benchmarker**: `vllm-mlx bench-serve` with CSV/JSON output

## Architecture

vllm-mlx layers on top of MLX primitives (mlx-lm, mlx-vlm, mlx-audio, mlx-embeddings) and exposes vLLM-inspired serving features — continuous batching, paged KV cache, prefix cache, and SSD tiering — via Metal on Apple Silicon. No model conversion is needed; models load directly from mlx-community formats.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           vllm-mlx Server                               │
│   OpenAI /v1/*  ·  Anthropic /v1/messages  ·  /v1/rerank  ·  /metrics   │
└─────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Continuous batching · Paged KV cache · Prefix cache · SSD tiering      │
└─────────────────────────────────────────────────────────────────────────┘
        ┌─────────────┬────────────┴────────────┬─────────────┐
        ▼             ▼                         ▼             ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│    mlx-lm     │ │   mlx-vlm     │ │   mlx-audio   │ │mlx-embeddings │
│    (LLMs)     │ │  (Vision)     │ │  (TTS + STT)  │ │ (Embeddings)  │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   MLX · Metal kernels · Unified memory                  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Performance (M4 Max)

| Model | Tok/s | Memory |
|-------|------:|-------:|
| Qwen3-0.6B-8bit | 417.9 | 0.7 GB |
| Llama-3.2-3B-Instruct-4bit | 205.6 | 1.8 GB |
| Qwen3-30B-A3B-4bit | 127.7 | ~18 GB |

| Whisper model | RTF | Use case |
|--------------|----:|----------|
| whisper-tiny | 197x | Real-time / low latency |
| whisper-large-v3-turbo | 55x | Quality + speed |
| whisper-large-v3 | 24x | Highest accuracy |

## See Also

[[apple-silicon-inference]] · [[mlx]] · [[vllm]] · [[llm-serving]] · [[multimodal-models]] · [[tts]] · [[speech-to-text]]
