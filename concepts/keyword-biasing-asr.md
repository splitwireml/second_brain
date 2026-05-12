---
title: Keyword List Biasing (ASR)
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[granite-speech-4-1-2b-plus]]
---

# Keyword List Biasing (ASR)

Keyword List Biasing (KWB) is an ASR technique that lets users provide a list of keywords (names, technical terms, domain-specific vocabulary) to improve recognition accuracy for those terms. The keywords are included directly in the prompt.

## How It Works

```
Can you transcribe the speech into a written format? Keywords: IBM, Granite, Watson, semantic
```

Users can provide single keywords or a list. Keywords don't need to actually appear in the audio — this makes it suitable for batch processing with recurring domain-specific terms.

## Effectiveness

Measured by **Keyword F1 score** — precision/recall of correctly recognized keywords. The granite-speech-4.1-2b-plus model shows large improvements with KWB enabled:

| Dataset | Without KWB | With KWB | Δ |
|---------|:----------:|:--------:|:--:|
| Gigaspeech | 74.2 | **84.1** | +9.9 |
| LS Clean | 89.1 | **96.1** | +7.0 |
| LS Other | 78.2 | **93.0** | +14.8 |
| SPGISpeech | 80.8 | **92.5** | +11.7 |
| VOX | 93.9 | **96.3** | +2.4 |
| TED LIUM | 87.9 | **94.9** | +7.0 |
| Earnings22 | 68.8 | **81.5** | +12.7 |
| CV-en | 74.6 | **91.5** | +16.9 |
| CV-de | 78.5 | **92.9** | +14.4 |
| CV-es | 83.1 | **93.9** | +10.8 |
| CV-fr | 74.5 | **90.6** | +16.1 |
| CV-pt | 90.0 | **95.0** | +5.0 |

KWB is particularly impactful for earnings calls, technical lectures, and domain-specific content where specialized vocabulary is otherwise frequently misrecognized.

## Related Concepts

- [[granite-speech-4-1-2b-plus]] — model implementing keyword list biasing
- [[speaker-attributed-asr]] — speaker labeling mode
- [[word-level-timestamps-asr]] — word timing mode

## References

- [Contextual Biasing for ASR in Speech LLM with Common Word Cues and Bias Word Position Prediction (arXiv:2604.12398)](https://arxiv.org/abs/2604.12398)
