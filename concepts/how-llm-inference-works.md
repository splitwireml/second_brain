---
title: How LLM Inference Works
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [llm, inference, optimization, transformer, quantization, kv-cache, gpu, efficiency]
sources: [raw/articles/xarticle-how-llm-inference-works-akshay-pachaar-2050941458614751327.md]
related_entity: [[akshay-pachaar]]
references:
  - https://github.com/vllm-project/vllm
  - https://github.com/NVIDIA/TensorRT-LLM
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
---

# How LLM Inference Works

A first-principles explanation of the LLM inference pipeline, covering tokenization, embedding, attention layers, the prefill/decode split, KV caching, and quantization. By [[akshay-pachaar]].

## Overview

LLM inference is the process of running a trained large language model to generate output from an input prompt. Despite appearing simple — you type, words stream back — the underlying pipeline involves two architecturally distinct phases with different hardware bottlenecks, both running on the same GPU in the same request.

## The Inference Loop

An LLM predicts **just one token** at a time. It takes the input prompt, predicts the next token, appends that token to the prompt, and repeats. This auto-regressive loop continues until a stop token is reached or `MAX_STEPS` is hit.

The non-obvious part: **the first token is expensive; subsequent tokens are cheap** (after the first). This is the key to understanding all inference optimization.

## Step 1: Tokenization

Text is converted to integer IDs via **Byte Pair Encoding (BPE)**. Starting from raw characters, the tokenizer iteratively merges the most common adjacent pair until a vocabulary of ~50,000 tokens is formed.

Common words (e.g., "the") map to a single token. Rare words (e.g., "unhappiness") are split into subword pieces ("un" + "happi" + "ness").

**Practical impact:** Languages underrepresented in the tokenizer's training data produce more tokens per sentence, increasing cost and latency proportionally.

## Step 2: Embedding

Each integer token ID is looked up in an embedding table — a matrix of shape `[vocab_size, hidden_dim]`. The result is a vector (e.g., 4,096-dim) per token.

These vectors are not random; training nudges semantically similar tokens to be near each other in this high-dimensional space ("king" ≈ "queen", "python" ≈ "snake" along one axis).

Position information is injected here (e.g., via **RoPE** — Rotary Position Embedding), since self-attention itself has no notion of token order.

## Step 3: Transformer Layers

Vectors pass through a stack of transformer layers (often 32+). Each layer applies:

1. **Self-attention** — tokens "look at" each other to decide what context to gather
2. **Feed-forward network** — processes the aggregated information per token

In self-attention:
- Each token produces **Q** (query), **K** (key), **V** (value) vectors via learned weight matrices
- A token's query scores against every other token's key via dot-product → softmax → weighted sum of values
- This is the mechanism by which context (e.g., "in Paris") influences prediction (e.g., "is the capital of France")

After 32+ layers of this, the model has rich representations that incorporate full-prompt context.

## Step 4: Vocabulary Projection

After the final transformer layer, the last token's vector is projected back to vocabulary size and softmaxed, producing a probability distribution over all possible next tokens. One token is sampled from this distribution.

## The Two Phases: Prefill vs Decode

Generating a response is **two tasks with totally different bottlenecks**:

### Prefill Phase

The entire input prompt is processed **in parallel** before the first token is generated. All tokens' Q, K, V are computed simultaneously — a matrix-matrix multiplication that GPUs excel at.

- **Bottleneck:** Compute-bound (arithmetic throughput)
- **Metric:** Time to First Token (TTFT) — the idle wait before streaming begins

```python
# Prefill: all tokens processed in parallel
hidden = embed(prompt_tokens) + positions
for layer in model.layers:
    Q, K, V = project(hidden)      # for ALL tokens at once
    hidden  = attention(Q, K, V) + hidden
    hidden  = feedforward(hidden) + hidden
    cache_kv(layer, K, V)          # save for decode phase
first_token = sample(project_to_vocab(hidden[-1]))
```

### Decode Phase

After the first token, the model enters a **token-by-token loop**:

```python
# Decode: one token per iteration
token = first_token
while token != STOP:
    x = embed(token) + position(steps)
    for layer in model.layers:
        q, k, v = project(x)
        K_all, V_all = caches[layer].append(k, v)
        x = layer.forward(q, K_all, V_all, x)
    token = sample(project_to_vocab(x))
    yield token
```

- Each step: one query vector × matrix of cached K/V keys (tiny arithmetic)
- But: GPU must load **all weight matrices** + **all cached K/V** from memory for that tiny computation
- **Bottleneck:** Memory-bandwidth-bound — chip waits on memory, not compute

> **This is why decode is memory-bound, prefill is compute-bound.** Same model, same GPU, same request — totally different performance characteristics.

- **Metric:** Inter-Token Latency (ITL) — gap between consecutive tokens; low ITL = fast-feeling model

## KV Cache

Without KV caching, generating N tokens would require recomputing attention over the entire growing sequence at each step (O(n²) in sequence length). The KV cache stores K and V matrices per layer, reusing them across decode steps.

**Size:** ~1 MB per token per 13B parameter model. A 4K-context burns ~4 GB VRAM just for the cache.

**Cache growth problem:** Long contexts bloat the KV cache → can starve batch size or exceed GPU memory.

**Optimization approaches:**
- **Quantize cache** to INT8/INT4 (asymmetric Q8-K + Turbo-V / TurboQuant)
- **Sliding window attention** (drop tokens outside window)
- **Grouped-query attention (GQA)** — share K/V across heads
- **PagedAttention** (vLLM) — OS-style virtual memory paging for KV cache

## Frontier: Shrinking the Cache at the Architecture Level

DeepSeek V4-Pro (late 2025) redesigns attention itself to minimize cache from the start, using a hybrid of sparse and dense compressed attention. At 1M token context: ~10% of prior cache size, ~27% of per-token compute.

## Quantization

Training needs FP32 precision; **inference does not**. Production typically runs FP16/BF16 (halves memory, ~2× throughput). Aggressive setups use INT8 or INT4.

**7B model memory footprint:**
| Precision | Memory |
|-----------|--------|
| FP32 | 28 GB |
| FP16 | 14 GB |
| INT8 | 7 GB |
| INT4 | 3.5 GB |

INT4 enables a 7B model on a laptop GPU. Methods like **GPTQ** and **AWQ** use per-channel scaling factors to minimize accuracy loss from compression. Well-done INT4 is within ~1% of the original on most benchmarks.

## Full Pipeline Summary

1. **Tokenize** — text → integer IDs
2. **Embed** — IDs → vectors with position info
3. **Prefill** — all layers over all input tokens in parallel (compute-bound, populates KV cache)
4. **Decode loop** — one token per iteration: project Q, attend over cached K/V, feed-forward, sample (memory-bound)
5. **Detokenize** — token IDs → characters → streamed to screen

Modern serving frameworks ([[vllm]], TensorRT-LLM, TGI) wrap this with:
- **Continuous batching** — interleaves requests from multiple users on same GPU step
- **Speculative decoding** — small draft model proposes tokens, large model verifies
- **PagedAttention** — OS-style KV cache memory management

## Practical Takeaways

| Concern | Metric | Bottleneck |
|---------|--------|------------|
| Long input prompt | TTFT | Compute |
| Long output | ITL | Memory |
| Long context | Both | KV cache |

- **Quantization is the highest-leverage knob** — FP16 → INT8 often halves latency with minimal quality loss
- **GPU utilization can be misleading** — prefill at 100% GPU ≠ decode is efficient; decode at 30% GPU utilization is normal
- **Context length is not free** — doubling context bloats KV cache and reduces batch capacity
