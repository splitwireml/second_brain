---
title: Local RAG for Coding Agents
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [rag, llm, inference]
sources: [raw/articles/docmancer-github-repo-2026-04-12.md]
related_entity: [[docmancer]]
---

# Local RAG for Coding Agents

A retrieval-augmented generation pattern where documentation is fetched, chunked, embedded, and indexed entirely on the local machine — no cloud service, no API key for embeddings, no rate limits. Coding agents query the local index at inference time to ground responses in accurate, up-to-date documentation.

## Core Problem It Solves

AI coding agents hallucinate APIs, CLI flags, and method signatures because their training data has a cutoff and they fill gaps by guessing. Dumping entire doc sites into context burns thousands of tokens and buries the one relevant paragraph. Local RAG indexes docs once, retrieves only relevant chunks at query time.

## Retrieval Pipeline

### 1. Fetch / Discovery

URL discovery strategies in priority order:
1. `/llms-full.txt` — entire docs in a single file (bypasses chunking, ingested as one blob)
2. `/llms.txt` — index of individual page URLs
3. `robots.txt` → Sitemap: directives
4. `/sitemap.xml` or `/sitemap_index.xml`
5. Platform-specific paths (e.g. MkDocs uses `/sitemap.xml.gz`)
6. **Nav crawl** — BFS of `<nav>` links from homepage, falls back to all `<a>` links

### 2. Content Extraction

- **Primary:** Trafilatura with `favor_recall=True` — extracts main content, preserves tables and links
- **Fallback:** markdownify with custom converter that strips nav/header/footer/aside, converts admonition divs to blockquotes, preserves code fence language tags
- Noise elements removed: sidebar, TOC, breadcrumb, pagination, edit-page links, theme footers
- Minimum 30-word threshold for trafilatura output before falling through to markdownify

### 3. Chunking

Markdown-aware chunking (not raw sliding window):
- Sections parsed by markdown headers (`#`–`######`), headers inside fenced code blocks ignored
- Each chunk gets a **header prefix** like `[# > ## Title]` showing its doc tree position
- **Tables** kept atomic — split at row boundaries with header+separator repeated in each piece
- **Fenced code blocks** kept atomic — split at line boundaries with opening fence repeated
- **Bullet lists** split at top-level bullets rather than mid-item when >50% of lines are bullets
- **Small adjacent chunks** (both < chunk_size/2) merged back together
- Plain prose uses sliding window with header prefix subtracted from available space

Config: **800 chars** chunk size, **120 chars** overlap (not token-based).

### 4. Embedding

Two parallel embeddings per chunk:
- **Dense:** `BAAI/bge-small-en-v1.5` via FastEmbed → 384-dimensional vectors (thread-local, lazy-loaded)
- **Sparse (BM25):** `Qdrant/bm25` via FastEmbed → term frequency/inverse document frequency vectors

Both run entirely locally. No API key required.

### 5. Retrieval — Hybrid RRF

Query flow:
1. Embed query text → dense vector + sparse BM25 vector (both computed at query time)
2. Qdrant prefetches top-20 BM25 candidates + top-20 dense candidates
3. **Reciprocal Rank Fusion (RRF)** merges ranked lists: `score = Σ 1/(K + rank_i)` with K=60
4. Returns top-K (default 5) results above score threshold (default 0.35)
5. Dense vectors stored on-disk (HNSW with `memmap_threshold=10000`)

No cross-encoder re-ranking step. No query expansion or HyDE.

## Token Efficiency

Default: **5 chunks × 800 chars ≈ 4,000 characters** (~1,000 tokens) per query response. Tunable via `--limit N`. `--full` flag returns entire chunk bodies (default truncates at 1500 chars).

vs dumping full docs: typically 50–100x token reduction per query.

## Metrics — What They Actually Measure

| Metric | Formula | What it tells you |
|--------|---------|-------------------|
| **MRR** | `1 / rank_of_first_relevant` | Is the best result at position 1? |
| **Hit Rate** | `1.0` if any relevant in top-K, else `0.0` | Did we find anything relevant? |
| **Recall@K** | `found_relevant / total_relevant` | What fraction of all relevant docs did we find? |
| **Chunk Overlap** | whitespace token intersection | Do retrieved chunks actually contain the expected text? |
| **Latency** | p50/p95/p99 per query | How fast is retrieval? |

**Critical caveat:** All metrics require a manually-authored golden dataset. Chunk overlap uses whitespace tokenization, not semantic similarity. MRR/Hit Rate are source-level (not chunk-level) — a correct source can still return the wrong chunk.

## Weaknesses

- **No re-ranker** — RRF is final ranking; no cross-encoder refinement
- **No BM25 parameter tuning** — k1 and b are FastEmbed/Qdrant defaults
- **No query expansion / HyDE** — queries go in as-is
- **Chunk size is characters, not tokens** — 800 chars ≈ 200 tokens for English; very small for complex API docs
- **`llms-full.txt` bypasses chunking** — entire doc site ingested as one blob
- **No version/freshness tracking** — re-ingest required when source docs change
- **No dedup in nav-crawl** — same page under multiple URLs indexed multiple times
- **eval is self-reported** — golden dataset generated from your own content, not real user queries

## Implementations

- [[docmancer]] — local-first, no server, FastEmbed+Qdrant, markdown-aware chunking, eval framework

## Related Concepts

- [[leann-vector-database]] — alternative local vector DB with graph-based selective recomputation
- [[ai-cost-optimization]] — local embedding (no API key) fits the cost optimization pattern
- [[llm-server-throughput-optimization]] — complementary: retrieval is one part of the LLM serving stack
- [[byterover-vs-docmancer-vs-skill-graph-content-engine]] — comparison showing where local RAG differs from vault-linking and markdown workflow systems
