---
title: Hermes Auxiliary Model Configuration
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [hermes-agent, inference, cost-optimization]
sources: [raw/2026-04-21-HowHermesAgent.md]
related_entity: [[hermes-agent]]
author: [[onchain-ai-garage]]
---

# Hermes Auxiliary Model Configuration

Hermes Agent silently runs 8 background tasks on every user request — *auxiliary models* — for tasks like context compression, web page summarization, image analysis, and memory writes. These tasks either inherit the user's expensive frontier model or fall back to Gemini Flash via OpenRouter's auto-detect chain, generating often-surprising background costs. Configuring these models selectively can cut auxiliary spend by 85–90%.

> "Most people never mess with [auxiliary models], but it could save you a lot of money and could improve your Hermes agent performance." — [[onchain-ai-garage]], April 2026

## The 8 Auxiliary Tasks

| Task | Trigger | Default Behavior | Priority |
|------|---------|-----------------|----------|
| **Compression** | Context fills to threshold | Inherited by main model or Gemini Flash via auto | 🔴 Highest |
| **Flush Memories** | Session end (`/new`, `/end`) | Inherited or Gemini Flash | 🔴 High |
| **Web Extract** | Every web page summarized | Inherited or Gemini Flash | 🟡 Medium |
| **Vision** | Every image / browser screenshot | Inherited or Gemini Flash | 🟡 Medium |
| Session Search | Past session search | Auto (OpenRouter → Gemini Flash) | 🟢 Lower |
| Skills Hub | Query matched to installed skill | Auto | 🟢 Lower |
| MCP Dispatch | MCP tool call routing | Auto | 🟢 Lower |
| Approval | Risky command classification (smart approval) | Auto | 🟢 Lower |

Top four by spend: **Compression > Flush Memories > Web Extract > Vision**.

## Default Cost Flow

With OpenRouter configured, all auxiliary tasks default to `auto`, which walks: **OpenRouter → New Portal → Codex → Gemini Flash 3**. Users see small Gemini Flash charges accumulating silently even when they never explicitly use Gemini Flash.

## Configuration Location

`~/.hermes/config.yaml` (WSL/Linux path; Mac path differs). Around line 100, `auxiliary:` section:

```yaml
auxiliary:
  vision:
    provider: OpenRouter
    model: google/gemini-2.5-flash
  compression:
    provider: OpenRouter
    model: moonshotai/kimi-k2
  web_extract:
    provider: Anthropic
    model: claude-haiku-4.5
  flush_memories:
    ...
```

Top-level `compression:` and `auxiliary.compression:` both exist — if both set, `auxiliary.compression` wins.

## Per-Task Model Recommendations

| Task | Recommended Models | Rationale |
|------|-------------------|-----------|
| **Compression** | Kimi K2, Claude Haiku 4.5, Gemini 2.5 Flash | Clean summaries, long-context handling |
| **Flush Memories** | GPT-4o Mini, Gemini 2.5 Flash | Small, fast, structured extraction |
| **Web Extract** | Claude Haiku 4.5, Gemini Flash | Factual preservation for research |
| **Vision** | GLM-5V Turbo, GPT-4o, Gemini 2.5 Flash | Must be multimodal |

## Local Model Support

Any local provider with an HTTP endpoint: **Ollama, LM Studio, vLLM, Llama.cpp**. Configure in `config.yaml`:

```yaml
auxiliary:
  compression:
    base_url: http://localhost:11434  # Ollama example
    model: qwen3-4b
    api_key: placeholder  # not used
    timeout: 120
```

`base_url` overrides `provider`. `api_key` field required but not validated for local endpoints.

## Live Demo Results (Compression)

| Model | Cost per Pass | Context Size |
|-------|--------------|--------------|
| Claude Opus 4.6 (Anthropic API) | **$0.13** | ~50K tokens |
| Kimi K2 (OpenRouter) | **$0.019** | ~50K tokens |
| **Savings** | **~85%** | — |

At 15 compressions/day: Opus → ~$60/mo vs Kimi K2 → ~$9/mo. Local model → ~$0/mo.

## Key Takeaways

1. **Audit your auxiliary spend** — small Gemini Flash charges on your OpenRouter bill are likely from aux tasks
2. **Match model to task** — don't use Opus for compression; Haiku/Kimi/Flash are sufficient
3. **Go local for zero-cost background work** — local models work for all aux tasks
4. **Update config per-task** — `auxiliary.compression` overrides top-level `compression`
5. **Restart session after config changes** — Hermes only reads config at session start

## Related Concepts

- [[hermes-agent]] — The agent this optimization applies to
- [[ai-cost-optimization]] — Broader AI cost optimization patterns (RTK, Caveman, Bleap)
- [[hermes-skills-workflow]] — Hermes workflow patterns by [[0xJeff]]
- [[three-tier-local-model-routing]] — Local/cloud model routing for agent architectures
- [[model-shortcuts]] — Named aliases for provider/model pairs in Hermes
