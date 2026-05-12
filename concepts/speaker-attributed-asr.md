---
title: Speaker Attributed ASR
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[granite-speech-4-1-2b-plus]]
---

# Speaker Attributed ASR

Speaker Attributed ASR (SAA) is a transcription mode that labels each speaker turn in a multi-speaker conversation with tags like `[Speaker 1]:` and `[Speaker 2]:`, in order of appearance. This combines speech recognition with speaker diarization — determining *who* spoke *when*.

## How It Works

The model is prompted to output speaker labels inline with the transcript:

```
[Speaker 1]: Hello how are you [Speaker 2]: I'm fine and how are you feeling [Speaker 1]: I feel wonderful
```

Speakers are numbered by order of appearance — the first speaker is always `[Speaker 1]`, the second is `[Speaker 2]`, etc.

## Evaluation Metric

The standard metric is **Word Diarization Error Rate (WDER)** — the percentage of words attributed to the wrong speaker. Lower is better.

## Benchmark: granite-speech-4.1-2b-plus

| Model | FISHER | CALLHOME English | AMI-SDM | GALE |
|-------|:------:|:----------------:|:-------:|:----:|
| VibeVoice ASR | 2.8 | 7.1 | 27.4 | 44.8 |
| **granite-speech-4.1-2b-plus** | **0.9** | **2.2** | **14.6** | **30.2** |

Evaluated on 2–5 minute speech segments.

## Training Data

SAA training data was created by concatenating audio segments from datasets with known speaker identification (e.g., Multilingual-Librispeech). Segments with alternating speakers were joined to create long multi-speaker samples for training.

## Related Concepts

- [[granite-speech-4-1-2b-plus]] — model that implements SAA as a prompt-controlled mode
- [[word-level-timestamps-asr]] — another rich transcription mode from the same model
- [[keyword-biasing-asr]] — keyword list biasing for ASR

## References

- [Speaker Attributed ASR Using Speech Aware LLMs (arXiv:2604.11269)](https://arxiv.org/abs/2604.11269)
