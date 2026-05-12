---
updated: 2026-04-17
title: MiniMax-M2.7 — Hugging Face Page
source: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
type: huggingface
---

# MiniMax-M2.7 — Hugging Face Page

**Source:** https://huggingface.co/MiniMaxAI/MiniMax-M2.7
**Retrieved:** 2026-04-15
**Type:** Model card / official documentation

## Summary

MiniMax-M2.7 is an open-weight language model from MiniMax (a Chinese AI company) optimized for agentic tasks, coding, and professional productivity. It is notable for being the company's first model to actively participate in its own evolution — writing its own skills, optimizing its own training harness, and autonomously improving a programming scaffold over 100+ rounds (+30% performance). It supports Agent Teams (multi-agent collaboration), native tool calling, and 196K context length.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Developer | MiniMax (MiniMaxAI org on HuggingFace) |
| Model name | MiniMax-M2.7 |
| Release date | 2026-04-09 (on HF) |
| License | Modified MIT |
| Architecture | Transformer, FP8, safetensors |
| Context length | 196K tokens max |
| Tool calling | Native (MiniMax M2 toolcall parser) |
| Reasoning format | `<think>...</think>` appended to output |
| Deployment | vLLM, SGLang, Transformers, NVIDIA NIM, ModelScope |
| Downloads (as of 2026-04-15) | ~85,549 |
| Likes (as of 2026-04-15) | 740 |

## Key Capabilities

### Agentic / Self-Evolution
- Recursively builds and improves its own agent harness
- Writes RL skills (2,000+ token skills), updates memory, optimizes learning loops
- Autonomous programming scaffold optimization: 100+ rounds, +30% performance
- Supports **Agent Teams** — multi-agent collaboration with stable role identity

### Coding / Software Engineering
- SWE-Pro: **56.22%** (matches GPT-5.3-Codex)
- SWE Multilingual: **76.5**
- Multi SWE Bench: **52.7**
- VIBE-Pro: **55.6%** (near Opus 4.6)
- Terminal Bench 2: **57.0%**
- NL2Repo: **39.8%**
- Claimed: sub-3-minute production incident recovery

### Professional Productivity
- GDPval-AA ELO: **1495** (highest among open-weight models, surpasses GPT 5.3)
- Word/Excel/PPT multi-round editing with editable deliverables
- Toolathon accuracy: **46.3%** (global top tier)
- MM Claw end-to-end: **62.7%** (close to Sonnet 4.6)
- 97% skill compliance across 40+ complex skills
- MLE Bench Lite (22 ML competitions): **66.6% medal rate** (2nd after Opus-4.6 and GPT-5.4)

### Entertainment / Character
- Strengthened character consistency and emotional intelligence
- Open-sourced [OpenRoom](https://github.com/MiniMax-AI/OpenRoom) — interactive web GUI AI demo at [openroom.ai](https://openroom.ai)

## Inference Recommendations

**Parameters:** `temperature=1.0`, `top_p=0.95`, `top_k=40`

**System prompt:**
```
You are a helpful assistant. Your name is MiniMax-M2.7 and is built by MiniMax.
```

**Hardware requirements:**
- 220 GB for weights
- 240 GB per 1M context tokens (KV Cache)
- Recommended: 96G×4 GPU (400K token KV cache) or 144G×8 GPU (3M token KV cache)

**vLLM deployment (4-GPU):**
```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2.7 --trust-remote-code \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think
```

**SGLang deployment (4-GPU):**
```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2.7 \
    --tp-size 4 \
    --tool-call-parser minimax-m2 \
    --reasoning-parser minimax-append-think \
    --port 8000 --mem-fraction-static 0.85
```

## Benchmark Summary

| Benchmark | Score | Notes |
|-----------|-------|-------|
| SWE-Pro | 56.22% | Matches GPT-5.3-Codex |
| SWE Multilingual | 76.5 | |
| Multi SWE Bench | 52.7 | |
| VIBE-Pro | 55.6% | Near Opus 4.6 |
| Terminal Bench 2 | 57.0% | |
| NL2Repo | 39.8% | |
| GDPval-AA ELO | 1495 | Highest open-weight; surpasses GPT 5.3 |
| Toolathon | 46.3% | Global top tier |
| MM Claw | 62.7% | Close to Sonnet 4.6 |
| MLE Bench Lite medal rate | 66.6% | 22 ML competitions; 2nd after Opus-4.6/GPT-5.4 |

## Links

- HF Model: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
- Blog post: https://www.minimax.io/news/minimax-m27-en
- GitHub: https://github.com/MiniMax-AI/MiniMax-M2.7
- MiniMax Agent: https://agent.minimax.io/
- API Platform: https://platform.minimax.io/
- OpenRoom (interactive demo): https://openroom.ai
- ModelScope: https://modelscope.cn/models/MiniMax/MiniMax-M2.7
- NVIDIA NIM: https://build.nvidia.com/minimaxai/minimax-m2.7

## MiniMax Company Context

MiniMax is a Chinese AI company founded by Baidu alumni. The company has built a full AI product suite across text (M2 series), speech (Speech 2.6), video (Hailuo), and music (Music 2.6). MiniMax has raised significant funding and positions itself as an "AI-native" organization — notably, M2.7 was used to accelerate the company's own internal model development cycle, handling ~30-50% of the RL team's workflow.

## Observations

- M2.7 is one of the most aggressive open-weight models in terms of agentic self-improvement claims — it autonomously ran 100+ rounds of scaffold optimization
- The benchmark claims are impressive but largely self-reported; third-party evaluation limited
- Modified MIT license — proprietary restrictions possible; check the LICENSE file
- Tool calling parser (`minimax_m2`) is custom — not compatible with the standard OpenAI function calling format without vLLM/SGLang post-processing
- The model uses `<think>` tags for reasoning, appended to the output (not interleaved like some reasoning models)
- 196K context is competitive but shorter than some recent open models (e.g., 1M token上下文 models)