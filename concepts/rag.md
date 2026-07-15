---
title: Retrieval-Augmented Generation (RAG)
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [llm, inference, ai]
sources: [raw/articles/google-ai-optimization-guide-2026.md]
---

## Definition

**Retrieval-Augmented Generation (RAG)** is a technique for improving AI response quality by grounding the model in authoritative, up-to-date content retrieved from an external source (in Google's case, the web Search index). Also referred to as "grounding" in Google's documentation.

## How Google Uses It

Google's AI search features (AI Overviews, AI Mode) use RAG in this specific way:

1. A user query arrives
2. Google's core Search ranking systems retrieve relevant web pages from the Search index
3. The AI model reviews the specific information from those retrieved pages
4. A synthesized response is generated showing prominent, clickable links to the supporting source pages

This means the quality of AI search responses is directly constrained by what the traditional Search index contains. If a page is not indexed or not crawlable, it cannot be used for grounding — regardless of its quality.

## Relevance to This Wiki

RAG is the mechanism that makes traditional SEO relevant for AI search. Content that is:
- Well-structured and crawlable
- Contains unique, non-commodity information
- On a technically sound site with good Page Experience

...is more likely to be (1) retrieved by ranking systems and (2) selected as a grounding source for AI responses.

## Key Implication: No Special Files Needed

Because RAG relies on the existing Search index, Google's official guidance is that websites do NOT need to create llms.txt files, AI-specific markup, or structured data for AI search. The retrieval happens through the same crawling and indexing systems that power regular Search.

## Related Concepts

- [[generative-ai-search-optimization]] — where RAG is the core mechanism
- [[inference]] — LLM inference that RAG augments with retrieval