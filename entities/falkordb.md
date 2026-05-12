---
title: FalkorDB
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [database, graphrag, open-source, knowledge-graph]
sources: [raw/articles/akshay-pachaar-wiki-vs-graph-falkordb-2026-04-23.md]
---

## Overview

FalkorDB is an open-source graph database using GraphBLAS sparse matrix adjacency matrices for high-performance graph traversal. 4,024 GitHub stars (April 2026). Positioned as the "Knowledge Graph for LLM" — combining graph traversal with built-in vector search for unified GraphRAG workloads.

## Key Facts

| Property | Value |
|----------|-------|
| Language | C |
| License | source-available (NOASSERTION) |
| Stars | 4,024 |
| Topics | graph-database, graphrag, knowledge-graph, realtime-database, cloud-database |
| GitHub | github.com/FalkorDB/FalkorDB |

## Architecture

**Sparse matrix core:** Most graph databases follow pointer-chains through memory (O(n) traversal per hop). FalkorDB stores the entire graph as a sparse adjacency matrix (zeros and ones), reducing multi-hop traversal to matrix multiplication — enabling parallel CPU execution and reuse of decades of linear algebra research.

**Performance claim (unverified):** Seven-hop query returning in 350ms vs. timeout on pointer-chain databases.

**GraphRAG built-in:** Most GraphRAG setups combine a graph DB + vector DB separately. FalkorDB embeds vector search natively — graph traversal + similarity search in a single query.

## Interfaces

- **Query language:** Cypher
- **Deployment:** Docker
- **Client SDKs:** Python, JavaScript, Rust, Java, Go, any Redis client

## Multi-Tenancy

Open source and multi-tenant by default — one instance hosts thousands of separate graphs without spinning up separate servers.

## Related

- [[knowledge-graph-rag]] — concept this database is optimized for
- [[leann-vector-database]] — privacy-first vector DB alternative
- [[karpathy-llm-wiki]] — the wiki foundation this extends
