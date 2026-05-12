---
title: AboveSpec
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [person, x-creator, content-creator, local-llm, moe, llm]
sources: [raw/articles/above-spec-moe-35b-rtx4060ti-2026-05-01.md]
---

# AboveSpec

X creator (@above_spec) posting about local LLM inference, MoE architectures, and GPU optimization. Focuses on practical benchmarks for consumer hardware — specifically making large MoE models run on 8 GB VRAM GPUs via llama.cpp offload strategies.

## Known Work

### 35B MoE on RTX 4060 Ti 8GB (May 2026)
Thread demonstrating that a 35B-parameter MoE model (Qwen3.6-35B-A3B) can run on an RTX 4060 Ti 8 GB at 41 tok/s (16k context) and 24 tok/s (200k context) using:
- **MoE offload**: Only 3 B active params per token on GPU; cold expert FFNs offloaded to system RAM via `-ngl 99 -ncmoe 99`
- **q8_0 KV cache**: ~10 KB/token, fitting 200k context in ~2 GB VRAM with FlashAttention
- **llama.cpp** with TurboQuant KV cache compression

Key claims:
- RTX 3070 8 GB owners should not write the card off — the real bottleneck is host-RAM bandwidth (~3 B active × Q4 ≈ 1.5 GB/token streaming from DDR5), and the 3070 actually has higher memory bandwidth than the 4060 Ti (448 vs 288 GB/s)
- 64 GB RAM + MoE offload is arguably the new home-LLM sweet spot for 8 GB GPU owners
- TurboQuant KV cache from @no_stp_on_snek (TheTom) enables fitting all 262k context, though token generation gets slower

Command used:
```
~/llama-cpp-turboquant/build/bin/llama-server \
  --model ~/models/unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_S.gguf \
  --mmproj ~/models/unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F32.gguf \
  --alias qwen3.6-35b-a3b \
  --host 127.0.0.1 --port 8080 \
  --ctx-size 200000
```

Also tested chained agent calls with real data dependency (search_flights → pick cheapest → book_flight with flight_id) using Hermes agent.

## Related

- [[mixture-of-experts]] — MoE architecture enabling sparse activation
- [[qwen3-6-27b]] — Related Qwen model family
- [[llama-cpp]] — Inference engine used
- [[local-llm]] — Home LLM inference category
- [[inference-kernel-optimization]] — GPU kernel optimization context
