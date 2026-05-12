---
title: granite-speech-4.1-2b-nar
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, llm, oss-ai, transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[ibm-granite]]
---

# granite-speech-4.1-2b-nar

Non-autoregressive variant of Granite Speech 4.1 2B, designed for higher throughput inference. Uses a novel NAR (Non-autoregressive) architecture based on transcript editing rather than sequential token generation.

Average WER: 5.44 (between the base 5.33 and plus 5.71).

## Related Entities

- [[granite-speech-4-1-2b]] — base autoregressive variant
- [[granite-speech-4-1-2b-plus]] — plus variant with speaker attribution and timestamps
- [[granite-4-0-1b-base]] — LLM backbone

## References

- [NLE: Non-autoregressive LLM-based ASR by Transcript Editing (arXiv:2603.08397)](https://arxiv.org/abs/2603.08397)
