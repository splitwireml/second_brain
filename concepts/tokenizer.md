---
title: Tokenizer
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [llm, ai, local-llm, tokenizer]
sources: [raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]
---

## Overview

A **tokenizer** converts raw text into token IDs that a language model can process. Models do not read text directly — they read numbers representing text chunks.

## How Tokenization Works

Text is split into tokens (subword units), each mapped to an integer ID. Example:

```
"Local LLMs are useful." 
→ ["Local", " LL", " Ms", " are", " useful", "."]
→ [1234, 5678, 9012, 3456, 7890, 23]
```

Different tokenizers split text differently. Some use byte-pair encoding (BPE), others use WordPiece or SentencePiece.

## Critical Property: Match Requirement

The tokenizer must match the model it was trained with. Using the wrong tokenizer produces incorrect token IDs, damaging output quality or breaking the model completely.

Tokenizers also define special tokens:
- Beginning of text (BOS)
- End of text (EOS)
- User/assistant/system markers
- Padding token

## Common Mistakes

Beginners often underestimate the tokenizer's importance. Even a powerful model performs poorly if text is converted into incorrect token IDs.

## Related Concepts

- [[local-llm]] — Tokenizers essential for local model operation
- [[model-architecture]] — Architecture includes vocabulary size
- [[chat-template]] — Template controls how special tokens are used

## Sources

^[raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]