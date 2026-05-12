---
title: docmancer
created: 2026-04-12
updated: 2026-04-12
type: entity
tags: [tools]
sources: [raw/articles/docmancer-github-repo-2026-04-12.md]
---

# docmancer

Local-first RAG knowledge base for AI coding agents. Fetches documentation from web sources, chunks and embeds it locally using FastEmbed (no API key required), stores vectors in a local Qdrant instance, and exposes retrieval to agents via plain markdown skill files installed into each agent's config directory.

## Key Facts

- **License:** MIT
- **Python:** 3.11–3.13
- **Install:** `pipx install docmancer --python python3.13`
- **No server required** — CLI-only, works offline after ingestion
- **No embedding API key** — FastEmbed runs entirely locally
- **Shared index** — all agents on the same machine share the same Qdrant store

## Architecture

See [[local-rag-for-coding-agents]] for the full retrieval pipeline breakdown.

## Supported Sources

GitBook, Mintlify, Docusaurus, MkDocs, Sphinx, ReadTheDocs, VitePress, ReadMe.io, Next.js, and generic web documentation. Auto-detected via HTTP headers, URL patterns, `<meta name="generator">` tags, and HTML body signals.

URL discovery priority: `/llms-full.txt` → `/llms.txt` → robots.txt sitemap → `/sitemap.xml` → platform-specific sitemaps → nav crawl.

## Retrieval Configuration

- **Chunk size:** 800 characters (configurable)
- **Chunk overlap:** 120 characters
- **Retrieval limit:** 5 chunks default
- **Score threshold:** 0.35 minimum relevance
- **Embedding model:** `BAAI/bge-small-en-v1.5` (384-dim dense via FastEmbed)
- **Sparse model:** `Qdrant/bm25` (local BM25 via FastEmbed)
- **Vector store:** Qdrant with hybrid dense+sparse RRF fusion

## Eval System

Built-in eval pipeline tracks MRR, Hit Rate, Recall@K, Chunk Overlap, and latency percentiles. Requires manually-authored golden dataset. Optional LLM-as-judge mode via `--judge` flag requires API key. See [[local-rag-for-coding-agents]] for metric definitions.

## Competitive Position

- vs cloud RAG (Zep, Weaviate Cloud): free, no rate limits, fully offline
- vs dumping full docs in context: ~1K tokens per query vs full site token cost
- vs raw sitemap scraper: markdown-aware chunking, hybrid retrieval, eval framework
- Weaknesses: no re-ranker, no BM25 tuning, no query expansion, char-based chunking (not token-based)

## Related

- [[local-rag-for-coding-agents]] — the core concept/technique this implements
- [[leann-vector-database]] — alternative local vector DB approach
- [[ai-cost-optimization]] — docmancer's no-API-key embedding model fits this pattern
- [[byterover-vs-docmancer-vs-skill-graph-content-engine]] — comparison with ByteRover and markdown skill-graph workflows
