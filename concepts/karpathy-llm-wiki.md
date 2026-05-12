---
title: Karpathy LLM Wiki
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [rag, knowledge-management, llm]
sources: [raw/articles/akshay-pachaar-wiki-vs-graph-falkordb-2026-04-23.md]
author: [[akshay-pachaar]]
---

## Definition

Karpathy's LLM wiki is a personal knowledge base pattern where an LLM continuously maintains a directory of markdown files — reading source documents, writing summaries, building cross-links, and organizing concepts. The LLM acts as the compiler and curator; humans rarely edit directly.

## Core Pattern

1. **Data ingest:** Source documents (articles, papers, repos, datasets, images) go into a `raw/` directory
2. **Compilation:** An LLM incrementally "compiles" a wiki — summaries, backlinks, concept categorization, article writing
3. **IDE:** Obsidian as the frontend for viewing raw data, compiled wiki, and visualizations
4. **Q&A:** Once the wiki is large enough (~100 articles, ~400K words), the LLM can answer complex questions against it without needing separate RAG infrastructure

## Strength

The wiki stores knowledge that "sits still" — a page on how attention works is as useful today as a year ago. You never rebuild context from scratch.

## Limitation

Breaks for questions spanning multiple entity types simultaneously (e.g., "which authors moved from Google to Anthropic between 2022 and 2024 and what did they publish after?"). The answer lives in connections between entities — a pattern no single wiki page can capture unless pre-written. This is the gap [[knowledge-graph-rag]] fills.

## Related Concepts

- [[knowledge-graph-rag]] — the extension: graph traversal layer on top of the wiki foundation
- [[obsidian-ai-second-brain]] — similar pattern, Obsidian-based, contested "5 minute" claim
- [[artem-zhutov]] — X creator who compared LLM wikis vs NotebookLM for personal knowledge management; LLM wikis superior for deep research and team settings, NotebookLM better for personal Q&A at lower cost
