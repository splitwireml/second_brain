---
updated: 2026-04-17
title: OmniVoice — HuggingFace Page Summary
source: https://huggingface.co/k2-fsa/OmniVoice
type: huggingface
---

# OmniVoice — HuggingFace Page Summary

**Source:** https://huggingface.co/k2-fsa/OmniVoice
**Accessed:** 2026-04-10

## Key Facts

- **Model ID:** k2-fsa/OmniVoice
- **Pipeline:** text-to-speech
- **Downloads:** 269,789
- **Likes:** 450
- **Tags:** omnivoice, zero-shot, multilingual, voice-cloning, voice-design, text-to-speech
- **License:** Apache 2.0
- **Base Model:** Qwen/Qwen3-0.6B-Base (finetuned)
- **Created:** 2026-03-30
- **Last Modified:** 2026-04-05

## Quick Start

```python
from omnivoice import OmniVoice
import torch

model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cuda:0",
    dtype=torch.float16
)
# Apple Silicon: device_map="mps"

audio = model.generate(
    text="This is a sentence without any voice prompt."
)
```

## Three Generation Modes

1. **Voice Cloning** — ref_audio + ref_text
2. **Voice Design** — instruct (attributes)
3. **Auto Voice** — text only

## Installation

```bash
pip install torch==2.8.0 torchaudio==2.8.0
pip install omnivoice
```

## Sample Rate

## See Also

- [[omnivoice-arxiv-2604-00688]] — OmniVoice paper summary
- [[vibevoice]] — VibeVoice — related open-source voice AI
- [[omnivoice-vs-vibevoice-comparison]] — Comparison of OmniVoice and VibeVoice


Output audio: 24 kHz