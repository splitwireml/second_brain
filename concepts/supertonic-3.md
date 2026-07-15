---
title: Supertonic 3
created: 2026-05-16
updated: 2026-05-16
type: concept
tags: [model, local-llm, on-device, onnx, speech, tts]
sources: [raw/articles/supertonic-3-huggingface-2026-05-16.md]
related_entity: [[supertone]]
---

# Supertonic 3 — Lightning Fast, On-Device, Accurate TTS

**Supertonic 3** is an open-weight text-to-speech model from [[supertone]]. At **99M parameters** across ONNX assets, it is dramatically smaller than 0.7B–2B class open TTS systems. Runs entirely on CPU — no GPU required — making it practical for local, browser, and edge deployment.

## Context: The TTS Landscape

For comparison across the local speech stack:
- [[vibevoice]] — Microsoft's open-source ASR+TTS with continuous speech tokenizers (7.5 Hz frame rate), MLX-native
- [[omnivoice]] — Xiaomi's 600+ language zero-shot TTS, diffusion-based, Apache 2.0
- [[insanely-fast-whisper]] — Whisper wrapper for ASR, supports any Whisper checkpoint

## Key Specifications

| Attribute | Value |
|-----------|-------|
| **Developer** | [[supertone]] Inc. |
| **Parameters** | ~99M (ONNX) |
| **Architecture** | ONNX Runtime, CPU-only inference |
| **Languages** | 31 (expanded from 5 in v2) |
| **License** | OpenRAIL-M |
| **Library** | `supertonic` Python SDK |

## What's New in Supertonic 3

- **31 languages**: expanded from 5-language Supertonic 2 release
- **More stable reading**: fewer repeat/skip failures on short and long utterances
- **Higher speaker similarity**: improved across the shared-language set
- **Expression tags**: supports `<laugh>`, `<breath>`, `<sigh>` inline tags

## Performance

### Reading Accuracy
Competitive WER/CER range against much larger open TTS models such as VoxCPM2, while preserving lightweight on-device deployment.

### Runtime Footprint
Runs fast on CPU — even compared with larger baselines on A100 GPU. Uses substantially less memory. No GPU required.

### Model Size Comparison
~99M parameters vs 0.7B–2B class systems. Smaller size means faster download, startup, and on-device inference.

## Supported Languages

`en`, `ko`, `ja`, `ar`, `bg`, `cs`, `da`, `de`, `el`, `es`, `et`, `fi`, `fr`, `hi`, `hr`, `hu`, `id`, `it`, `lt`, `lv`, `nl`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sv`, `tr`, `uk`, `vi`

## Quick Start

```bash
pip install supertonic
```

```python
from supertonic import TTS

tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="M1")

text = "A gentle breeze moved through the open window."
wav, duration = tts.synthesize(text, voice_style=style, lang="en")

tts.save_audio(wav, "output.wav")
print(f"Generated {duration:.2f}s of audio")
```

## Positioning vs Alternatives

| Model | Size | Languages | GPU Required | Architecture |
|-------|------|-----------|--------------|--------------|
| **Supertonic 3** | 99M | 31 | ❌ CPU | ONNX |
| [[omnivoice]] | ~600M | 600+ | ✅ GPU | Diffusion NAR |
| [[vibevoice]]-Realtime | 500M | 10 | ⚠️ MLX/CUDA | Next-token diffusion |

Supertonic 3 is the lightweight leader for CPU-only, browser, and edge scenarios. [[omnivoice]] leads on language count. [[vibevoice]] offers ASR + TTS with MLX Apple Silicon support.

## Related

- [[tts]] — TTS concept overview
- [[supertone]] — the company behind Supertonic 3
- [[vibevoice]] — Microsoft TTS/ASR with MLX support
- [[omnivoice]] — Xiaomi 600+ language TTS
- [[onnx-runtime]] — the inference engine Supertonic 3 uses