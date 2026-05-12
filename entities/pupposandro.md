---
title: pupposandro
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [person, llm, inference]
sources: [raw/articles/pupposandro-claude-landscape-2026-04-20.md]
---

# pupposandro

X creator (@pupposandro) focused on LLM inference optimization and local model deployment.

## Overview

Published speculative decoder research showing 207 tok/s with Qwen3.5-27B on RTX 3090 using DFlash block-diffusion draft. Co-authored with @davideciffa. Built a standalone C++/ggml implementation (~2000 LOC) achieving 3.43x over autoregressive baseline.

## Key Claims

- 207.6 tok/s peak with DFlash (5.46x over AR) on Qwen3.5-27B Q4_K_M
- HumanEval 10-prompt bench: 129.5 tok/s mean at DDTree budget=22
- 128K context fits on 24 GB RTX 3090
- Only ggml, no libllama dependency

## Related

- [[dflash]] — Block diffusion draft method used
- [[qwen3-6-27b]] — The model being accelerated
- [[llama-cpp]] — Related inference engine
