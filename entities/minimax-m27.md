---
title: MiniMax-M2.7
created: 2026-04-15
updated: 2026-04-16
type: entity
tags: [model, agent, benchmark, oss-ai]
sources: [raw/articles/minimax-m27-huggingface-2026-04-15.md]
related_entity: [[minimax]]
---

# MiniMax-M2.7

> Open-weight language model from [[minimax]] optimized for agentic coding, professional productivity, and self-directed learning. First model to actively participate in its own evolution cycle.

**Developer:** [[minimax]] (MiniMaxAI org)
**Release date:** 2026-04-09
**License:** Modified MIT
**Context length:** 196K tokens
**Architecture:** Transformer MoE (256 experts, top-8 routing per token), FP8, safetensors
**Parameters:** 230B total | **10B active** per token (~4.3% sparsity — 8 of 256 experts)
**Layers:** 62 | **Hidden size:** 3072 | **Attention heads:** 48×64 | **Vocab:** 200,064
**Deployments:** vLLM, SGLang, Transformers, NVIDIA NIM, ModelScope
**HF:** [MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
**GitHub:** [MiniMax-AI/MiniMax-M2.7](https://github.com/MiniMax-AI/MiniMax-M2.7)
**Blog:** [MiniMax M2.7: Early Echoes of Self-Evolution](https://www.minimax.io/news/minimax-m27-en)

## Key Performance Claims

| Benchmark | Score | Notes |
|-----------|-------|-------|
| SWE-Pro | 56.22% | Matches GPT-5.3-Codex |
| SWE Multilingual | 76.5 | |
| Multi SWE Bench | 52.7 | |
| VIBE-Pro | 55.6% | Near Opus 4.6 |
| Terminal Bench 2 | 57.0% | |
| NL2Repo | 39.8% | |
| GDPval-AA ELO | 1495 | Highest open-weight model; surpasses GPT 5.3 |
| Toolathon | 46.3% | Global top tier |
| MM Claw end-to-end | 62.7% | Close to Sonnet 4.6 |
| MLE Bench Lite medal rate | 66.6% | 22 ML competitions; 2nd after Opus-4.6/GPT-5.4 |

> **Note:** All benchmarks are self-reported by MiniMax; limited third-party independent evaluation available.

## Core Capabilities

### Self-Evolution
M2.7 is MiniMax's first model to actively participate in its own development. During training, M2.7:
- Updates its own memory and builds complex RL skills (2,000+ tokens each)
- Improves its own learning process based on experiment results
- Autonomously ran 100+ rounds of programming scaffold optimization (+30% performance improvement)

Internally, M2.7 handles ~30-50% of the RL team's workflow, including experiment monitoring, log analysis, debugging, code fixes, merge requests, and smoke tests.

### Agent Teams
Native multi-agent collaboration with stable role identity — multiple M2.7 instances can assume distinct roles (e.g., researcher, coder, reviewer) and collaborate autonomously on complex tasks.

### Coding / Software Engineering
- Log analysis, bug troubleshooting, refactoring, code security, ML code generation
- System-level reasoning: monitoring metrics correlation, trace analysis, SRE-level decisions
- Claimed sub-3-minute production incident recovery

### Professional Productivity
- Word/Excel/PPT multi-round editing with editable deliverables
- GDPval-AA ELO 1495 (open-weight leader)
- Toolathon 46.3% accuracy
- 97% skill compliance across 40+ complex skills

## Inference

**Recommended parameters:** `temperature=1.0`, `top_p=0.95`, `top_k=40`

**System prompt:**
```
You are a helpful assistant. Your name is MiniMax-M2.7 and is built by MiniMax.
```

**Hardware requirements:**
- 220 GB for weights
- 240 GB per 1M context tokens (KV Cache)
- Recommended: 96G×4 GPU (400K token KV cache) or 144G×8 GPU (3M token KV cache)

**vLLM deployment:**
```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2.7 --trust-remote-code \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think
```

**SGLang deployment:**
```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2.7 \
    --tp-size 4 --tool-call-parser minimax-m2 \
    --reasoning-parser minimax-append-think \
    --port 8000 --mem-fraction-static 0.85
```

## Tool Calling

MiniMax-M2.7 uses a custom tool calling parser (`minimax_m2` / `minimax-m2`) available in vLLM and SGLang. Native OpenAI SDK tool calling is supported through these inference engines. The model outputs tool calls in a structured format; manual parsing is required when not using vLLM/SGLang.

The model also uses `<think>...</think>` tags for reasoning (appended to output, not interleaved).

## Related

- [[minimax]] — the company that built M2.7
- [[agent-teams]] — multi-agent collaboration concept
- [[model-self-evolution]] — the concept M2.7 exemplifies
- [[open-montage]] — mentions MiniMax as a video provider in its pipeline
- [[vllm]] — deployment engine
- [[sglang]] — deployment engine
- [[research-code-agent-cli-automation]] — mentions `opencode run -m opencode/minimax-m2.7` as a CLI entry point
