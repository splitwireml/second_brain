---
title: granite-speech-4.1-2b-plus
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, llm, oss-ai, benchmark, transcription, audio, speech]
sources: [raw/articles/ibm-granite-granite-speech-4-1-2b-plus-2026-04-28.md]
related_entity: [[ibm-granite]]
---

# granite-speech-4.1-2b-plus

IBM Granite Speech 4.1 2B Plus is an open-source speech-aware LLM for ASR with speaker attribution and word-level timestamps, released April 28, 2026 on HuggingFace. Based on [[granite-4-0-1b-base]], it is a 2B-parameter seq2seq model (16-layer speech encoder + 40-layer LLM decoder) supporting English, French, German, Spanish, and Portuguese.

## Model Modes

The model supports three modes controlled by prompt changes:

1. **ASR mode** — plain speech-to-text transcription
2. **Speaker Attributed ASR (SAA)** — adds `[Speaker N]:` tags before each speaker turn
3. **Word-level timestamps** — adds `[T:N]` timestamp tags after each word (centiseconds, modulo 1000 = 10s rollover)

Unlike [[granite-speech-4-1-2b]] (non-plus), the plus model does **not** provide punctuation and capitalization — it instead provides richer transcription metadata (speaker labels, word timings).

A non-autoregressive variant, [[granite-speech-4-1-2b-nar]], offers higher throughput.

## Architecture

- **Speech encoder**: 16-layer convolutional encoder (input_dim=160, hidden_dim=1024, 8 heads, dim_head=128, max_pos_emb=512, downsample_rate=5)
- **LLM decoder**: 40-layer GraniteForCausalLM (hidden_size=2048, num_attention_heads=16, num_key_value_heads=4, intermediate_size=4096, max_position_embeddings=4096)
- **Projector**: 2-layer BLIP-2 QFormer (encoder_hidden_size=2048, hidden_size=1024, 16 cross-attention heads)
- **Audio token index**: 100352
- **Vocab size**: 100,353 (text), 100,353 total with audio tokens
- **dtype**: bfloat16
- **Base model**: [[granite-4-0-1b-base]]

## Benchmark Results

### ASR (WER % — lower is better)

| Model | Average WER | AMI | Earnings22 | Gigaspeech | LS Clean | LS Other | SPGISpeech | Tedlium | Voxpopuli |
|-------|:-----------:|:---:|:---------:|:---------:|:-------:|:-------:|:----------:|:-------:|:---------:|
| **granite-speech-4.1-2b-plus** | 5.71 | 8.63 | 8.68 | 10.38 | 1.44 | 3.06 | 3.72 | 3.89 | 5.9 |
| granite-speech-4.1-2b | 5.33 | 8.09 | 8.37 | 9.8 | 1.33 | 2.5 | 3.78 | 3.07 | 5.7 |
| granite-speech-4.1-2b-nar | 5.44 | 8.03 | 8.44 | 10.16 | 1.28 | 2.77 | 3.33 | 3.62 | 5.86 |

Evaluated using speculative decoding on the HuggingFace Open ASR Leaderboard.

### Keyword List Biasing (Keyword F1 % — higher is better)

| Mode | Gigaspeech | LS-C | LS-O | SPGISpeech | VOX | TED_LIUM | Earnings22 | CV-en | CV-de | CV-es | CV-fr | CV-pt |
|------|:----------:|:----:|:----:|:----------:|:---:|:--------:|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Without KWB | 74.2 | 89.1 | 78.2 | 80.8 | 93.9 | 87.9 | 68.8 | 74.6 | 78.5 | 83.1 | 74.5 | 90.0 |
| With KWB | **84.1** | **96.1** | **93.0** | **92.5** | **96.3** | **94.9** | **81.5** | **91.5** | **92.9** | **93.9** | **90.6** | **95.0** |

### Speaker Attributed ASR (WDER % — lower is better)

| Model | FISHER | CALLHOME English | AMI-SDM | GALE |
|-------|:------:|:----------------:|:-------:|:----:|
| VibeVoice ASR | 2.8 | 7.1 | 27.4 | 44.8 |
| **granite-speech-4.1-2b-plus** | **0.9** | **2.2** | **14.6** | **30.2** |

Evaluated on 2–5 minute speech segments. WDER = Word Diarization Error Rate.

### Word-level Timestamps (AAS ms — lower is better)

| Model | AMI-I | AMI-S | LS-C | LS-O | VOX | CV | MLS | TMT | En Avg | MLS-fr | MLS-es | MLS-de | MLS-pt | CV-fr | CV-es | CV-de | CV-pt | ML Avg |
|-------|:-----:|:-----:|:----:|:----:|:---:|:---:|:---:|:---:|:------:|:------:|:------:|:------:|:------:|:-----:|:-----:|:-----:|:-----:|:------:|
| Qwen3-FA | 48.1 | 82.5 | 27.8 | 29.3 | 41.0 | 48.4 | 34.3 | 29.9 | 42.7 | 38.1 | 27.0 | 31.2 | 26.3 | 30.3 | 40.0 | 29.4 | 34.2 | 33.3 |
| CrisperWhisper | 55.7 | 64.3 | 35.9 | 40.1 | 47.2 | 97.4 | 46.4 | 42.7 | 53.7 | 35.6 | 28.0 | 31.2 | 36.8 | 62.9 | 58.9 | 60.9 | 83.8 | 50.1 |
| Canary-v2 | 127.8 | 129.7 | 92.5 | 89.2 | 109.9 | 110.3 | 94.3 | 86.1 | 105.0 | 85.0 | 81.1 | 80.2 | – | 86.8 | 88.5 | 91.5 | – | – |
| WhisperX | 107.1 | 150.2 | 71.7 | 72.0 | 78.8 | 91.2 | 79.2 | 63.6 | 89.2 | 117.3 | 84.7 | 132.2 | 75.0 | 104.2 | 88.1 | 126.8 | 79.5 | 101.0 |
| **granite-speech-4.1-2b-plus** | **43.4** | 69.0 | **11.4** | **14.6** | 80.2 | **43.3** | **24.3** | **24.5** | **38.8** | 45.4 | **23.0** | 41.3 | 47.1 | **18.6** | **19.3** | **19.5** | **24.2** | **29.8** |

AAS = Accumulated Averaging Shift (mean absolute timestamp error in milliseconds).

## Supported Languages

English, French, German, Spanish, Portuguese

## Usage

```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

MODEL_NAME = "ibm-granite/granite-speech-4.1-2b-plus"
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForSpeechSeq2Seq.from_pretrained(MODEL_NAME, device_map=device, dtype=torch.bfloat16)
```

Requires `transformers>=5.8`, `torch`, `torchaudio`, `datasets`, `accelerate`, `torchcodec`.

## Key Papers

- [Speaker Attributed ASR](https://arxiv.org/abs/2604.11269)
- [Word Level Timestamp Predictions](https://arxiv.org/abs/2604.22817)
- [Keyword Biasing for ASR](https://arxiv.org/abs/2604.12398)
- [Granite-Speech paper](https://arxiv.org/abs/2505.08699)
- [Self-Speculative Decoding for LLM-based ASR](https://arxiv.org/abs/2603.11243)
- [Non-autoregressive ASR by Transcript Editing](https://arxiv.org/abs/2603.08397)

## Infrastructure

Trained on IBM Blue Vela supercomputing cluster (NVIDIA H100 GPUs). Training completed in ~5 days on 32 H100 GPUs.

## Related Entities

- [[ibm-granite]] — parent model family
- [[granite-speech-4-1-2b]] — non-plus variant with punctuation/capitalization
- [[granite-speech-4-1-2b-nar]] — non-autoregressive variant
- [[vibevoice]] — Microsoft open-source voice AI (ASR + TTS); [[granite-speech-4-1-2b-plus]] benchmarks compare favorably on WDER and timestamp accuracy
- [[omnivoice]] — Xiaomi multilingual TTS alternative

## Related Concepts

- [[speaker-attributed-asr]] — technique for labeling speakers in ASR output
- [[word-level-timestamps-asr]] — word-level timestamp generation in speech recognition
- [[keyword-biasing-asr]] — keyword list biasing technique for enhancing ASR recognition of domain-specific terms
- [[continuous-speech-tokenizers]] — speech tokenization approaches; granite-speech uses encoder-level audio encoding
