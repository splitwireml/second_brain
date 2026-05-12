---
title: Knowledge Graph RAG
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [rag, knowledge-graph, database]
sources: [raw/articles/akshay-pachaar-wiki-vs-graph-falkordb-2026-04-23.md]
author: [[akshay-pachaar]]
---

## Definition

Knowledge Graph RAG (GraphRAG) augments LLM responses by retrieving facts from a structured graph of entities and relationships rather than (or in addition to) embedding-based vector similarity search. The graph encodes *how* things connect; vector search encodes *what* things mean. Combined, they can answer questions like "which authors moved from Google to Anthropic between 2022 and 2024" — queries that require multi-hop traversal across a relationship graph, not just semantic similarity.

## Core Claim

Traditional RAG works on knowledge that "sits still" — a Markdown page on attention mechanisms is as useful today as a year ago. The LLM reads sources, extracts ideas, writes articles, and keeps them cross-linked. This breaks for questions spanning multiple entity types simultaneously, because no single page encodes those cross-entity patterns.

A knowledge graph encodes relationships as first-class data. Questions about movement between organizations, publication timelines, or network proximity become graph traversals — not document retrievals.

## Wiki vs. Graph Layer Model

The argument is that wikis and graphs occupy *different layers*, not competing roles:

- **Wiki:** stores what something *is* (descriptions, facts, articles)
- **Graph:** stores how everything *connects* (relationships, hops, paths)

Neither alone is sufficient. A wiki page can describe "authors who moved from Google to Anthropic" only if someone pre-wrote that article. A graph can answer the question directly — and ten variations of it — without anyone authoring a page first.

## FalkorDB as Implementation

[[falkordb]] implements this by storing the graph as a sparse matrix (GraphBLAS), making multi-hop traversal parallelizable via linear algebra. This is contrasted with pointer-chain graph databases where each hop is sequential memory access.

FalkorDB also embeds vector search, so graph traversal + semantic similarity happen in one query — rather than orchestrating a separate graph DB + vector DB.

## Confirmed

- Graph traversal as matrix multiplication is a documented GraphBLAS approach (academic basis exists)
- FalkorDB is open-source (4K stars, C, GitHub)

## Likely (unverified source claims)

- 350ms for seven-hop query vs. timeout on pointer-chain databases — no independent benchmark confirmed

## Related Concepts

- [[local-rag-for-coding-agents]] — local RAG patterns for codebases
- [[leann-vector-database]] — vector DB with graph-accelerated recomputation
- [[karpathy-llm-wiki]] — the wiki foundation this extends
