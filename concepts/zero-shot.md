---
title: Zero-Shot
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [zero-shot, deep-learning, model]
sources: []
---

## Overview

Zero-shot capability refers to an AI model's ability to perform tasks it was never explicitly trained on, using generalization from its pre-training distribution. The model leverages learned representations, prompting, or auxiliary information (like language descriptions) to handle novel tasks.

## Canonical Examples

- **CLIP** — zero-shot image classification: given a new label set (e.g., "a photo of a cat" vs "a photo of a dog"), CLIP classifies without any fine-tuning on those classes
- **GPT-4/Vision** — answer questions about images never seen during training
- **SAM (Segment Anything)** — segment any object in any image, including objects never seen during training
- **In-context learning** — LLMs solve entirely novel reasoning tasks given few-shot examples at inference time

## Relationship to Few-Shot and Fine-Tuning

- **Zero-shot**: no examples, relies on pre-training generalization
- **Few-shot**: 1–10 examples at inference to steer behavior
- **Fine-tuning**: update weights on task-specific data

## Why Zero-Shot Matters

- No labeled data needed
- No training compute
- Instant generalization to new domains
- Foundation model property — scales with model size and pre-training quality

## Limitations

- Tasks too far from pre-training distribution may fail completely
- Zero-shot performance typically below fine-tuned specialists
- Sensitive to prompt formulation

## Related Concepts

- [[training-free]] — zero-shot is the primary example of training-free capability
- [[segmentation]] — SAM is the canonical zero-shot segmentation model
- [[efficiency]] — zero-shot avoids training compute entirely
