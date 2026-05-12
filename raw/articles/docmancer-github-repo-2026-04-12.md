---
updated: 2026-04-17
title: docmancer GitHub Repository
source: https://github.com/docmancer/docmancer
type: github
---

# docmancer GitHub Repository

> **Source:** https://github.com/docmancer/docmancer
> **Downloaded:** 2026-04-12
> **License:** MIT
> **Python:** 3.11–3.13

## Overview

Local-first RAG knowledge base for AI coding agents. Fetches docs from web sources, chunks/embeds locally with FastEmbed, stores in Qdrant, exposes retrieval via plain markdown skill files — no MCP, no server, no API keys for core functionality.

## Key Facts

- **Embedding:** FastEmbed BAAI/bge-small-en-v1.5 (384-dim dense) + Qdrant/bm25 (sparse BM25)
- **Vector store:** Qdrant (local, on-disk HNSW)
- **Chunk size:** 800 chars, 120 char overlap
- **Retrieval:** Hybrid dense+sparse via Qdrant Reciprocal Rank Fusion (RRF)
- **Fetch sources:** GitBook, Mintlify, Docusaurus, MkDocs, Sphinx, ReadTheDocs, VitePress, ReadMe.io, Next.js, generic web
- **Discovery strategies:** llms-full.txt > llms.txt > robots.txt sitemap > sitemap.xml > platform-specific sitemaps > nav crawl
- **Content extraction:** Trafilatura primary, markdownify fallback
- **Optional deps:** Playwright (browser fallback), Anthropic (LLM judge), Langfuse (telemetry), Ragas (LLM eval)
- **Core dependencies:** pydantic, qdrant-client, fastembed, httpx, trafilatura, beautifulsoup4

## Files Examined

- `docmancer/core/config.py` — chunk_size=800, chunk_overlap=120, retrieval_limit=5, score_threshold=0.35
- `docmancer/core/chunking.py` — markdown-aware chunking: header prefixes, table atomicity, code block atomicity, bullet list grouping, small chunk merging
- `docmancer/connectors/embeddings/fastembed.py` — FastEmbedDenseEmbedding + FastEmbedSparseEmbedding, thread-local lazy loading
- `docmancer/connectors/vector_stores/qdrant.py` — hybrid RRF retrieval, dense+sparse named vectors, BM25 IDF modifier
- `docmancer/connectors/fetchers/pipeline/discovery.py` — 6-strategy discovery chain, nav crawl BFS
- `docmancer/connectors/fetchers/pipeline/detection.py` — platform detection via headers/URL/HTML/body signals
- `docmancer/connectors/fetchers/pipeline/extraction.py` — trafilatura + markdownify fallback, admonition→blockquote, code fence language preservation
- `docmancer/eval/metrics.py` — MRR, hit_rate, recall_at_k, chunk_overlap (whitespace token), latency p50/p95/p99
- `docmancer/eval/runner.py` — run_eval, run_eval_with_judge
- `docmancer/agent.py` — DocmancerAgent class: ingest_documents, ingest_url, query, query_with_trace
- `docmancer/core/models.py` — Document, Chunk, RetrievedChunk pydantic models