---
title: ingest-anything Embeddings Architecture
created: 2026-05-14
updated: 2026-05-14
type: concept
tags: [agent, architecture, embedding, open-source]
sources: [raw/articles/ingest-anything-readme-2026-05-14.md, raw/articles/ingest-anything-reference-2026-05-14.md]
related_entity: [[ingest-anything]]
author: [[Claude]]
---

## What It Is

The embedding layer of [[ingest-anything]] is a thin wrapper (27 lines in `embeddings.py`) that bridges Chonkie's `AutoEmbeddings` into LlamaIndex's `BaseEmbedding` interface.

## Architecture

```
embedding_model (str)
    ↓
ChonkieAutoEmbedding(model_name)
    ↓ extends BaseEmbedding
    ↓
AutoEmbeddings.get_embeddings(model_name)
    ↓ returns Chonkie BaseEmbeddings instance
    ↓
embed() / embed_batch()
```

**Key insight:** The `embedding_model` string is passed directly to `AutoEmbeddings.get_embeddings()`. There is NO validation or provider registry in ingest-anything itself — it's entirely delegated to Chonkie.

## What This Means

1. **Any model Chonkie supports, ingest-anything supports** — the coupling is tight
2. **No custom embedding class injection** — you cannot pass your own `BaseEmbedding` instance directly; you must go through the string → Chonkie → wrapper path
3. **Local models work IF Chonkie supports them** — Sentence Transformers and Model2Vec are local-first; OpenAI/Cohere/Jina require API keys
4. **The wrapper is synchronous-first** — `_aget_embedding` just calls `_get_embedding` (no native async)

## Practical Limits

- You cannot bypass Chonkie's AutoEmbeddings
- You cannot pass a pre-instantiated embedding model
- The model name must be resolvable by Chonkie's registry
- No support for custom embedding dimensions or pooling strategies at the ingest-anything level

## Relevance to Custom Local Embeddings

Whether a custom local embedding model works depends entirely on whether `AutoEmbeddings.get_embeddings("your-model-name")` resolves. Chonkie's `AutoEmbeddings` class determines what strings it accepts. Local Sentence Transformers models installed via huggingface should work because Chonkie wraps sentence-transformers. But **non-standard local embedding servers** (e.g., Ollama embeddings, vLLM embeddings endpoint, custom FastAPI embedding server) likely do NOT work because they aren't in Chonkie's provider registry.

## See Also

- [[ingest-anything]] — the parent project
- [[vector-database-ingestion]] — broader concept of document → vector store pipelines
- [[local-embedding-models]] — alternatives for running embeddings locally

## Related

- [[ingest-anything-leann-2026-05-14]]
