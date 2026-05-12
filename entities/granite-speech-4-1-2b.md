---
title: granite-speech-4.1-2b
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, llm, oss-ai, transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[ibm-granite]]
---

# granite-speech-4.1-2b

Base Granite Speech model (non-plus variant). Unlike [[granite-speech-4-1-2b-plus]], this model provides **punctuation and capitalization** in transcripts, AST (Automatic Speech Translation), keyword-biased recognition, and **Japanese** language support.

WER performance is slightly better than the plus variant (5.33 vs 5.71 average), likely because it focuses resources on raw ASR quality rather than splitting capability across three modes.

## Related Entities

- [[granite-speech-4-1-2b-plus]] — plus variant with speaker attribution and timestamps
- [[granite-speech-4-1-2b-nar]] — non-autoregressive variant
- [[granite-4-0-1b-base]] — LLM backbone
