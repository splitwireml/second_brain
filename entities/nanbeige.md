---
title: Nanbeige
created: 2026-07-24
updated: 2026-07-24
type: entity
tags: [llm, model, inference, local-llm, lightweight]
sources: [raw/articles/thread-0xSero-2080003696885154280.md]
---

# Nanbeige

Nanbeige is named by [[0xsero]] as a candidate for the 4–8 GB hardware tier in a source-described local-model recommendation list. The post suggests it could help with tagging workloads; the surrounding replies raise practical questions about its thinking behavior and cache/harness requirements. These are source-reported observations, not independent benchmarks.

## Source Details

- **Hardware tier:** 4–8 GB.
- **Proposed use:** tagging or similar lightweight local work.
- **Follow-up evidence:** one reply reports that it may require two KV-cache instances for its two loop passes; another says it needs the right harness and otherwise behaves like a typical 3B model.

## Related

- [[0xsero]] — source author and local-model recommender.
- [[local-llm-size-tradeoffs]] — hardware-fit and quality/speed tradeoffs.
- [[qwen3-6-27b]] — neighboring model in the same hardware-oriented list.
