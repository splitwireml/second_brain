---
title: ingest-anything
created: 2026-05-14
updated: 2026-05-14
type: entity
tags: [agent, llm, embedding, ingestion-pipeline, local-llm, open-source, vector-database]
sources: [raw/articles/ingest-anything-readme-2026-05-14.md, raw/articles/ingest-anything-reference-2026-05-14.md]
---

## Overview

**ingest-anything** (v1.3.1) is a Python package by [[astra-bertelli]] that provides a smooth pipeline for ingesting non-PDF files (docx, png, csv, json, md, xml, zip) into vector databases. It fills a gap: most ingestion pipelines focus on PDF/markdown, but real-world data comes in many formats.

Built on three pillars:
- **[Chonkie](https://docs.chonkie.ai)** — chunking strategies (7 types) + embedding model dispatch via `AutoEmbeddings`
- **[PdfItDown](https://github.com/AstraBert/PdfItDown)** — converts any file type → PDF for text extraction
- **[LlamaIndex](https://www.llamaindex.ai)** — vector store integrations + data loaders

**GitHub:** https://github.com/AstraBert/ingest-anything | **Stars:** 90 | **License:** MIT

## Architecture

### Three ingestion modes

| Mode | Class | Input | Pipeline |
|------|-------|-------|----------|
| **Text files** | `IngestAnything` | Files or directory | File → PdfItDown → PDF → PyMuPDFRead → Chonkie chunk → embed → vector store |
| **Code files** | `IngestCode` | List of file paths | Code file → SimpleDirectoryReader → Chonkie CodeChunker → embed → vector store |
| **Web data** | `IngestWeb` | URLs | URL → Crawlee scrape → PdfItDown → PDF → PyMuPDFRead → Chonkie chunk → embed → vector store |

### Agent mode

`IngestAgent` is a factory class that creates LlamaIndex agents wrapping the above:
- `IngestAnythingFunctionAgent` / `IngestAnythingReActAgent` — for text/web
- `IngestCodeFunctionAgent` / `IngestCodeReActAgent` — for code

Agents support: custom tools, HyDE query transform, multi-step query decomposition.

## Embedding Models

The `embedding_model` parameter is a string passed to `ChonkieAutoEmbedding`, which wraps Chonkie's `AutoEmbeddings.get_embeddings()`. This is a **LlamaIndex BaseEmbedding subclass** — see [[ingest-anything-embeddings-architecture]].

**Stated support:** Sentence Transformers, OpenAI, Cohere, Jina AI, Model2Vec

**Key mechanism:** `embeddings.py` (27 lines) — creates a Chonkie `AutoEmbeddings` instance from the model name string and wraps it as `BaseEmbedding`. The actual model resolution is delegated to Chonkie.

## Chunking Strategies

7 strategies via `Chonkie`:
- `token` — split by token count
- `sentence` — split by sentences
- `semantic` — split by semantic similarity (threshold default 0.7)
- `sdpm` — Sentence Distance Probability Matrix
- `late` — delayed chunking (embeds first, chunks later)
- `slumber` — LLM-based (Gemini or OpenAI, external API)
- `neural` — finetuned BERT-based chunker

## Vector Store Support

Accepts any `BasePydanticVectorStore` from LlamaIndex. **Tested backends:**
- **Qdrant** — `QdrantVectorStore` (local + cloud)
- **Weaviate** — `WeaviateVectorStore` (cloud)
- **Milvus** — `MilvusVectorStore` (dev dependency)

Since the interface is `BasePydanticVectorStore`, **any LlamaIndex-compatible vector store should work** in theory — including custom/community integrations.

## Constraints

- **Python:** `>=3.10, <3.13` (excludes 3.13+)
- **Dependencies:** `chonkie[all]`, `pydantic`, `pdfitdown`, `llama-index-readers-file`, `crawlee[beautifulsoup]`
- **Chonkie embeds all chunking logic** — you cannot use ingest-anything without Chonkie's AutoEmbeddings

## Research-Confirmed Answers (2026-05-14)

From the 2026-05-14 deep-research on local embeddings + LEANN integration (see [[ingest-anything]] External Research):

- **Custom local HF models work**: Chonkie's `AutoEmbeddings.get_embeddings()` falls through to `SentenceTransformerEmbeddings(model, **kwargs)` for any unrecognized model string. Pass `"BAAI/bge-small-en-v1.5"` or any sentence-transformers-compatible HuggingFace model ID — it works.
- **Ollama/local servers work via LiteLLM**: Use `"litellm://ollama/nomic-embed-text"` format — Chonkie routes it through `LiteLLMEmbeddings` which supports 100+ providers.
- **vllm-mlx works via environment variables**: `"litellm://openai/mlx-community/all-MiniLM-L6-v2-4bit"` + `export OPENAI_API_BASE="http://localhost:8000/v1"`. Chonkie can't pass `api_base` directly, but LiteLLM reads it from env.
- **Model2Vec works**: `"minishlab/potion-base-8M"` (~30MB, no GPU needed) — matched by Chonkie registry pattern.
- **LEANN works as vector store**: PR #224 (`yichuan-w/LEANN`) adds `LeannVectorStore(BasePydanticVectorStore)` — the exact interface ingest-anything accepts. Full code exists; merge status TBD.
- **Combined pipeline viable**: Pass `LeannVectorStore(index_path="./idx", embedding_model="...")` to `IngestAnything(vector_store=...)`. **Critical:** match embedding dimensions between ingest-anything and LEANN.

**What does NOT work:** Custom embedding servers without OpenAI-compatible APIs, direct `BaseEmbedding` instance injection, non-LlamaIndex vector stores.

## External Research
- [2026-05-14 deep-research on ingest-anything + LEANN](/Users/mali/users/mali/research/ingest-anything-leann-2026-05-14/report.md)
