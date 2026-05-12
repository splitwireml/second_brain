---
title: Mixture of Experts (MoE)
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [architecture, moe, llm, training, efficiency]
sources: []
---

# Mixture of Experts (MoE)

**Mixture of Experts (MoE)** is a neural network architecture where different subsets of parameters ("experts") are activated per input token via a learned router, enabling massive parameter counts with sub-linear inference cost.

## How It Works

A gating/router network selects K of N experts for each token. Only K expert networks compute during the forward pass.

For a model with N=256 experts and K=8 active per token:
- Active parameters: ~K/N of total FFN parameters
- Example: 256 experts, top-8 routing → ~3.1% of FFN params active per token

## Relationship to MoT

[[mixture-of-transformers]] (MoT) applies similar sparse routing principles specifically to the vision pathway, rather than the FFN layers.

## Examples

- [[minimax-m27]] — 256 experts, top-8 routing, 230B total / 10B active
- [[hy-embodied-0-5]] — MoT architecture (4B total / 2.2B active)
- Mixtral 8x7B — 8 experts, top-2 routing
- DBRX — 16 experts, top-4 routing
- [[flash-moe]] — Qwen 3.5 397B (512 experts, K=10, pruned to K=4); 209 GB on disk streaming via Apple's unified memory; 2-bit quantization cuts to 120 GB

## See Also

- [[mixture-of-transformers]]
- [[hy-embodied-0-5]]
- [[minimax-m27]]
