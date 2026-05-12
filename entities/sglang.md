---
title: SGLang
created: 2026-04-15
updated: 2026-04-15
type: entity
tags: [inference, platform, tools]
sources: [raw/articles/minimax-m27-huggingface-2026-04-15.md]
---

# SGLang

> High-throughput LLM inference engine with RadixAttention for efficient KV cache reuse. Recommended deployment target for [[minimax-m27]].

**GitHub:** [sgl-project/sglang](https://github.com/sgl-project/sglang)
**License:** Apache 2.0

SGLang is an open-source inference framework optimized for serving complex LLM workloads. It provides RadixAttention (automatic KV cache reuse across requests), continuous batching, tensor parallelism, and expert parallelism. Recommended alongside vLLM for [[minimax-m27]].

## MiniMax M2.7 Deployment (SGLang)

```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2.7 \
    --tp-size 4 \
    --tool-call-parser minimax-m2 \
    --reasoning-parser minimax-append-think \
    --port 8000 --mem-fraction-static 0.85
```

**Hardware:** 220 GB for weights + 240 GB per 1M KV cache tokens. Recommended: 96G×4 GPU (400K token KV cache).

## Related

- [[minimax-m27]] — model SGLang is used to deploy
- [[vllm]] — alternative inference engine
