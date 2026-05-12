---
title: Gemma 4
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [model, llm, google, oss-ai, inference, moe]
sources: [raw/articles/google-multi-token-prediction-gemma-4.md]
---

# Gemma 4

Google's open-weight model family (Apache 2.0). Over 60 million downloads in the first few weeks after launch. Delivers "unprecedented intelligence-per-parameter" across workstation, mobile, and cloud.

## Model Sizes

| Model | Architecture | Target Hardware |
|-------|-------------|-----------------|
| 31B | Dense | Workstations, consumer GPUs |
| 26B | MoE (mixture-of-experts) | Personal computers, consumer GPUs |
| E2B | Dense | Edge devices |
| E4B | Dense | Edge devices |

## Multi-Token Prediction (MTP) Drafters

Gemma 4 ships with MTP drafters — lightweight speculative decoding companions that pair with each model size. Up to **3× speedup** with no quality degradation.

Key technical details:
- Draft models share the target model's KV cache — no recalculation of context
- For E2B/E4B edge models: efficient clustering technique in the embedder to accelerate logit calculation
- On 26B MoE + Apple Silicon: ~2.2× speedup at batch sizes 4–8 (vs batch size 1 which has routing challenges)
- On Nvidia A100: similar gains with larger batch sizes

## Deployment

Apache 2.0 license. Available on:
- [[huggingface]] (model weights)
- [[vllm]] (recommended for high-throughput serving)
- [[sglang]] (recommended for complex inference graphs)
- MLX (Apple Silicon)
- Ollama
- Google AI Edge Gallery (Android/iOS)

## Relationships

- Part of the [[google]] AI model ecosystem (alongside SigLIP, Stitch, etc.)
- MTP drafters are a form of [[speculative-decoding]] — lightweight drafter + target model verification
- The 26B MoE variant relates to the broader [[mixture-of-experts]] architecture pattern
- Complementary to [[block-diffusion-speculative-decoding]] (DFlash) — both are speculative decoding techniques but DFlash drafts entire blocks in parallel while MTP drafts autoregressively
- [[turboquant-kv-cache-compression]] is a complementary optimization (KV cache compression vs MTP draft acceleration)
- Inference optimization stack: [[llm-server-throughput-optimization]], [[inference-kernel-optimization]]

## See Also

- [[gemma-4-mtp-drafters]] (concept page)
- [[speculative-decoding]] (concept page)
- [[block-diffusion-speculative-decoding]] — alternative speculative decoding via block diffusion (DFlash)
- [[pflash-speculative-prefill]] — speculative prefill for TTFT reduction
- [[mixture-of-experts]] — MoE architecture context for 26B variant
