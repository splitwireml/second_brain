---
title: Recursive Language Models
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [llm, reasoning, agent]
sources: [raw/articles/xarticle-recursive-language-models-clearly-explained-2048757569775378858.md]
related_entity: [[akshay-pachaar]]
author: [[akshay-pachaar]]
---

# Recursive Language Models

Recursive Language Models (RLMs) are an MIT-proposed solution to **context rot** — the degradation of LLM reasoning quality as context length grows, even when the context window itself is not exceeded.

## The Problem: Context Rot

Context rot is a *reasoning failure*, not a window failure. Modern LLMs with 1M-token context windows still produce garbage on 50K-token documents. The issue:

- Frontier models ace **needle-in-a-haystack** retrieval benchmarks (finding a hidden sentence in filler text)
- But they collapse on tasks requiring **counting, classification, or reasoning across** thousands of entries
- RLMs address this gap

## How RLMs Work

### 1. Separate Query from Context

In a standard LLM call, query and full context ride together in one prompt. RLMs break this assumption:

- Context lives in an external **runtime memory slot** (a "variable")
- The root model sees only the question and a set of **tools**
- Think of a Jupyter notebook: you load a dataframe once into `df`, and every subsequent cell references it without re-uploading

### 2. The Model Gets Tools

The root model cannot read `ctx` directly. The paper gives it four tools covering every data-analyst access pattern:

- **Peek**: view first 2,000 chars to understand structure
- **Grep**: regex-based filtering to isolate relevant lines
- **Partition**: split context into smaller chunks
- **Recurse**: call itself recursively on those chunks

### 3. Strategy Emerges from the Task

Traditional agent frameworks hardcode decomposition steps (a human picks the order and fallback policy upfront). RLMs do the opposite — the root model decides how to break the problem down **based on what it discovers** as it probes the context.

## Concrete Example

Question: *"Among users 12345, 67890, and 11111, how many questions are about billing?"* (5,000 tickets)

An RLM handles it differently:

1. **Peeks** at structure: "Each line has Date, User ID, Question"
2. **Greps** for target users, reducing 5,000 lines to 50
3. **Spawns** a recursive call: "Classify each as billing or other"
4. **Returns** final result — root context stayed small throughout

## Why RLMs Matter

| Benefit | Description |
|---------|-------------|
| No context rot | Accuracy holds regardless of document size |
| Unlimited context | 10M tokens? Just partition more |
| Interpretable | See exactly what the model did |
| Cost-efficient | Smaller calls beat one massive API call |
| Future-proof | As LLMs improve, RLMs improve automatically |

RLMs treat context as data to be programmatically explored — combining code execution and language reasoning. It is not summarization, and it is not a rigid agent. The model decides how to decompose based on what it discovers.

## Relationship to Other Concepts

RLMs extend [[karpathy-llm-wiki]] foundation and relate to [[knowledge-graph-rag]] — both address the problem of making LLMs reason across large knowledge bases rather than treating all tokens equally.

## See Also

- [[llm]] — the finite resource RLMs optimize
- [[knowledge-graph-rag]] — graph traversal as an alternative approach to multi-hop reasoning
- [[karpathy-llm-wiki]] — the wiki knowledge base concept that inspired structured context management
- [[agent-teams]] — multi-agent patterns that similarly decompose tasks across model instances
