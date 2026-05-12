---
title: iam-shanmukha
created: 2026-05-03
updated: 2026-05-03
type: entity
tags: [person, content-creator, x-creator]
sources: [raw/articles/qwen3-6-35b-rtx4070-12gb-iam-shanmukha-2026-05-01.md]
---

# Shanmukha Vishnu

X creator (@iam_shanmukha). Posts local LLM inference benchmarks, GGUF quantization configs, and llama.cpp/vLLM optimization guides for consumer GPUs.

## Known For

Documented Qwen3.6-35B-A3B (GGUF, Q4_K_M) running at 60 tok/s on RTX 4070 12GB VRAM with 128K context using llama-server with specific flag tuning (`-ngl 999 -ncmoe 25 -fa`, KV cache as q8_0).

## Local LLM Configuration Details

Key findings shared from the Qwen3.6-35B thread:
- `ncmoe` parameter controls MoE expert activation; 25 = ~4GB VRAM usage on 12GB card, 60 = ~4GB, can tune down
- `--fit-target 256` flag (replaces `-ngl 999`) reported to achieve 80+ tok/s on RTX 4070 with IQ4_XS quantization
- Q4_K_XL at ~60 tok/s also achievable with proper flag tuning
- KV cache at q8_0 retains quality close to q8_0 full precision on Qwen models

## Related Entities

- [[qwen3-6-27b]] — Qwen 27B dense model; shanmukha's thread uses the 35B MoE variant
- [[local-llm]] — the broader concept of running LLMs on consumer hardware
- [[above-spec]] — another X creator benchmarking 35B MoE on RTX 4060 Ti 8GB

## Sources

- Qwen3.6-35B-A3B GGUF config thread: https://x.com/iam_shanmukha/status/2050098256424927491
