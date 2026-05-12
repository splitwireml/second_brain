---
title: MiniMax
created: 2026-04-15
updated: 2026-04-15
type: entity
tags: [AI-company, model, agent, oss-ai]
sources: [raw/articles/minimax-m27-huggingface-2026-04-15.md]
---

# MiniMax

> Chinese AI company building a full-stack AI product suite (text, speech, video, music) and positioned as an "AI-native organization" — using its own models to accelerate model development.

**Founded:** ~2021-2022 (by Baidu alumni)
**Headquarters:** China
**Products:** MiniMax Agent (agentic platform), Hailuo (video), MiniMax Speech (TTS), MiniMax Music, MiniMax M2 text models
**Website:** [minimax.io](https://www.minimax.io)
**HF Org:** [MiniMaxAI](https://huggingface.co/MiniMaxAI)
**Blog:** [minimax.io/news](https://www.minimax.io/news)

## Overview

MiniMax is a Chinese AI company notable for its full-stack AI suite spanning text generation (M2 series), speech synthesis (Speech 2.6), video generation (Hailuo), and music generation (Music 2.6). The company positions itself as "AI-native" — meaning it uses its own AI systems (including M2.7) to accelerate internal model development, claiming that M2.7 now handles 30-50% of the RL team's workflow.

## M-Series Text Models

| Model | Release | Context | Notes |
|-------|---------|---------|-------|
| MiniMax-M2 | 2025 | 128K? | Base model |
| MiniMax-M2.1 | 2025 | 128K? | Improved instruction following |
| MiniMax-M2.5 | ~2026-03 | 196K | Mid-tier agent model |
| **MiniMax-M2.7** | 2026-04-09 | 196K | Flagship; self-evolution capable |

## Key Differentiators

### AI-Native Organization
MiniMax claims M2.7 participates in its own development cycle — writing RL skills, optimizing training harnesses, and autonomously improving a programming scaffold over 100+ rounds (+30% performance). Human researchers intervene only for "critical decisions."

### Agent Teams
M2.7 supports native multi-agent collaboration with stable role identity — multiple instances can collaborate autonomously on complex tasks with consistent поведение (behavior).

### Open Source / Open Weight
- M2.7 model weights are publicly downloadable on HuggingFace and ModelScope
- Open-sourced [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) (Model Context Protocol server)
- Open-sourced [OpenRoom](https://github.com/MiniMax-AI/OpenRoom) — interactive web-based AI demo

## Business Model

MiniMax monetizes via:
- **MiniMax Agent** — agentic AI platform at [agent.minimax.io](https://agent.minimax.io)
- **MiniMax API** — pay-per-token API at [platform.minimax.io](https://platform.minimax.io)
- Token plan subscriptions

No open-source license for commercial use (modified MIT — see model pages for restrictions).

## Related

- [[minimax-m27]] — flagship model entity
- [[open-montage]] — open-source video production system; mentions MiniMax as a video provider
- [[agent-teams]] — concept for multi-agent collaboration with stable role identity
- [[model-self-evolution]] — concept describing models that participate in their own training/development
- [[vllm]] — recommended deployment engine for M2.7
- [[sglang]] — alternative deployment engine for M2.7
