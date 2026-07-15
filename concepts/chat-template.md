---
title: Chat Template
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [agent, llm, ai, local-llm]
sources: [raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]
---

## Overview

A **chat template** (or chat template) tells the runtime how to format conversation messages before sending them to the model. It wraps user input, system prompts, and assistant responses in the specific token structure the model was trained on.

## Why It Matters

Instruction-tuned models are trained on specific message structures. Using the wrong template causes:

- System prompt being ignored
- Wrong response style
- Model continuing user message instead of answering
- Failure to stop properly
- Strange role markers appearing
- Reduced overall capability

## Example Formats

A simple user/assistant format:
```
User: Explain tokens.
Assistant:
```

May need to become:
```
<|system|>You are helpful.<|user|>Explain tokens.<|assistant|>
```

## Common Mistake

The same model can feel dramatically better or worse depending on the chat template used. The weights are identical — only the prompt formatting changed.

For instruct models, prompt formatting IS part of performance.

## Related Concepts

- [[local-llm]] — Chat templates essential for local inference
- [[tokenizer]] — Tokenizer must support the template's special tokens
- [[model-architecture]] — Architecture defines how special tokens are interpreted

## Sources

^[raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]