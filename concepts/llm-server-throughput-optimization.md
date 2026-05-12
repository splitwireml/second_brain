---
title: LLM Server Throughput Optimization — Multi-Instance Llama.cpp + Nginx
created: 2026-04-11
updated: 2026-04-13
type: concept
tags: [inference, optimization, llama.cpp, llm, performance]
sources: [raw/transcripts/2026-04-11-Your-local-LLM-is-10x-slower.md]
author: [[alex-ziskind]]
---

**Presented by** [[alex-ziskind]] in "Your Local LLM is 10x Slower" (2026-04-11).

# LLM Server Throughput Optimization

> Running a single Llama.cpp instance wastes GPU capacity. Multiple instances + nginx round-robin = 10x throughput gain.

Single-instance LLM serving leaves most GPU compute idle. The bottleneck shifts to how many concurrent requests a single server can handle — and Llama.cpp's default configuration is conservative. This technique scales throughput by orders of magnitude using only Llama.cpp, nginx, and Python.

## The Core Problem

Ollama runs Llama.cpp with overhead — ~100 tok/s on the same hardware where:
- **Llama Server directly:** ~124 tok/s (single instance)
- **Single concurrent request via Llama Server:** ~120 tok/s
- **128 concurrent requests:** ~240 tok/s
- **16 instances × 64 parallel × 1024 concurrency:** ~1,226 tok/s

Single-instance throughput doesn't scale with concurrency. Requests queue and starve each other.

## The Solution: Horizontal Scaling via Nginx Round-Robin

Architecture:

```
Client → nginx (port 8000, round-robin) → Llama Server instances (ports 8080-8095)
                                        → Llama Server instances
                                        → Llama Server instances...
```

1. **Start N Llama Server instances** on sequential ports (e.g., 8080–8095)
2. **Set `--parallel N`** on each instance (internal request queuing per server)
3. **nginx** distributes incoming requests across instances round-robin
4. Clients point to nginx instead of any single Llama Server

## Key Parameters

| Parameter | What it controls | Typical values |
|-----------|------------------|----------------|
| `--parallel` | Concurrent requests per Llama Server instance | 32–128 |
| `--ctx-size` | Context window size (VRAM usage) | 2048–8192 |
| `--batch-size` | Prompt processing batch | 512–2048 |
| `instances` | Number of Llama Server processes | 1–16 |
| `concurrency` | Total concurrent client connections | 128–1024 |

## Benchmark Results (Mac Studio, Qwen3-4B)

| Configuration | Throughput |
|--------------|------------|
| Ollama | 100 tok/s |
| Llama Server (1 instance) | 124 tok/s |
| 1 instance, 128 concurrent | 240 tok/s |
| 16 instances, parallel=64, concurrency=1024 | **1,226 tok/s** |

10x improvement over Ollama, 10x over single-instance Llama Server.

## Llama Throughput Lab

Python tool that automates parameter sweeping across instances, parallel, and concurrency to find the optimal configuration for a given machine.

**Repo:** Search for "Llama Throughput Lab" on GitHub

Features:
- Single-request baseline test
- Concurrent request test
- Full sweep (308+ parameter combinations)
- Auto-starts/stops multiple Llama Server instances
- Configures nginx round-robin automatically

## Use Cases That Need This

- **Code assistants** — multiple agents querying simultaneously
- **Batch image/video analysis** — thousands of frames processed in parallel
- **RAG pipelines** — many concurrent retrieval requests
- **Agent orchestration** — planning + implementation agents running in parallel

## Related

- [[vibevoice]] — VibeVoice ASR for transcribing video content
- [[1-bit-bonsai-bitnet-fine-tuning]] — 1-bit quantization (BitNet b1.58) for running LLMs at extreme memory reduction on consumer hardware
- [[reclip-video-downloader]] — ReClip for downloading video sources
