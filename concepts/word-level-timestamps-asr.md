---
title: Word-Level Timestamps (ASR)
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[granite-speech-4-1-2b-plus]]
---

# Word-Level Timestamps (ASR)

Word-level timestamps in ASR attach a time tag after each word indicating when that word ended in the audio. This enables precise alignment between transcript text and audio for applications like subtitle generation, search-within-audio, and conversational AI.

## Timestamp Format

The model outputs `[T:N]` tags after each word, where `N` is an integer in centiseconds (1/100th of a second), modulo 1000:

```
hello [T:45] world [T:82]
```

The modulo 1000 means timestamps "roll over" every 10 seconds. Applications must track a rollover counter `R` to reconstruct absolute time:

- **Encoding**: `N = round(t * 100) mod 1000`
- **Decoding**: `t = N/100 + 10R`

## Evaluation Metric

**Accumulated Averaging Shift (AAS)** measures the mean absolute error between predicted and reference timestamps in milliseconds. Lower is better.

## Benchmark: granite-speech-4.1-2b-plus

Outperforms Qwen3-FA, CrisperWhisper, Canary-v2, and WhisperX on most datasets:

| Model | En Avg (ms) | ML Avg (ms) |
|-------|:-----------:|:-----------:|
| Qwen3-FA | 42.7 | 33.3 |
| CrisperWhisper | 53.7 | 50.1 |
| Canary-v2 | 105.0 | – |
| WhisperX | 89.2 | 101.0 |
| **granite-speech-4.1-2b-plus** | **38.8** | **29.8** |

## Training Data

Timestamps use Montreal Forced Aligner (MFA) — a GMM-HMM forced alignment tool — to generate word-level alignments for most datasets. For AMI-IHM, Switchboard, and TIMIT, native timestamp annotations are used. MFA alignments are validated against CTC speech encoder forced alignments; only samples with the lowest alignment error are retained (top 95% English, top 70% non-English).

## Limitations

- Works well on audio segments up to **5 minutes** (vs. 9 minutes for ASR/SAA modes)
- Non-English timestamp accuracy is lower than English (MLS-fr/de/es/pt and CV-fr/de/es/pt have higher AAS)

## Related Concepts

- [[granite-speech-4-1-2b-plus]] — model implementing timestamp generation as a prompt-controlled mode
- [[speaker-attributed-asr]] — another rich transcription mode from the same model
- [[keyword-biasing-asr]] — keyword list biasing for ASR

## References

- [In-Sync: Adaptation of Speech Aware LLMs for ASR with Word Level Timestamp Predictions (arXiv:2604.22817)](https://arxiv.org/abs/2604.22817)
