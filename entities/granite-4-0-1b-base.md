---
title: granite-4.0-1b-base
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, llm, oss-ai]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[ibm-granite]]
---

# granite-4.0-1b-base

The 1B parameter dense base language model that serves as the LLM backbone for the IBM Granite Speech model family. GraniteForCausalLM architecture with 40 layers, hidden_size=2048, 16 attention heads (4 key-value heads), intermediate_size=4096, max_position_embeddings=4096, vocab_size=100,353.

Used as the base for:
- [[granite-speech-4-1-2b]]
- [[granite-speech-4-1-2b-plus]]
- [[granite-speech-4-1-2b-nar]]

## Related Entities

- [[ibm-granite]] — parent company/family
- [[granite-speech-4-1-2b-plus]] — speech model using this as its LLM backbone
