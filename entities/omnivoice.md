---
title: OmniVoice
created: 2026-04-10
updated: 2026-04-10
type: entity
tags: [speech, model, oss-ai, inference, genai]
sources: [raw/articles/omnivoice-huggingface-2026.md, raw/articles/omnivoice-arxiv-2604-00688.md]
---

# OmniVoice

**OmniVoice** is a massively multilingual zero-shot text-to-speech (TTS) model developed by Xiaomi's k2-fsa team. Released in March 2026, it supports over **600 languages** — the broadest language coverage among zero-shot TTS models.

## Key Specifications

| Attribute | Value |
|-----------|-------|
| **Developer** | Xiaomi (k2-fsa team) |
| **Release** | March 2026 |
| **Parameters** | ~0.6B (initialized from Qwen3-0.6B) |
| **Architecture** | Diffusion language model-style discrete NAR |
| **Tokenizer** | Higgs-audio 8-codebook acoustic tokens |
| **Training Data** | 581k hours multilingual speech |
| **Languages** | 600+ |
| **License** | Apache 2.0 |
| **Inference Speed** | RTF 0.025 (40x faster than real-time) |

## Architecture

OmniVoice uses a **single-stage discrete non-autoregressive (NAR)** architecture with:

- **Diffusion language model objective** — discrete masked diffusion with bidirectional Transformer backbone
- **Full-codebook random masking** — stochastic masking across all 8 codebooks for efficient training
- **LLM initialization** — initialized from Qwen3-0.6B weights for superior intelligibility
- **Direct text-to-acoustic mapping** — bypasses cascaded pipelines (no text→semantic→acoustic error propagation)

This contrasts with conventional two-stage TTS systems that suffer from error propagation and information bottlenecks.

## Capabilities

### Voice Cloning
- Zero-shot cloning from **3-10 seconds** reference audio
- Optional `ref_text` (auto-transcribed via Whisper if not provided)
- Can pre-compute `voice_clone_prompt` for reuse (avoids re-encoding reference audio)

### Voice Design
- Generate voices via attribute descriptions (no reference audio needed)
- Supported attributes: gender, age, pitch, style (whisper), English accent, Chinese dialect
- Example: `"female, low pitch, british accent"`

### Fine-Grained Control
- **Non-verbal symbols** — inline tags like `[laughter]`, `[sigh]`
- **Pronunciation correction** — via pinyin or phonemes
- **Duration/speed control** — fixed output duration or speed factor

## Installation & SDK

```bash
# PyPI (stable release)
pip install omnivoice

# Or from source
pip install git+https://github.com/k2-fsa/OmniVoice.git
```

**Python API:**
```python
from omnivoice import OmniVoice
import torch

model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="mps",  # or "cuda:0"
    dtype=torch.float16
)

# Voice cloning
audio = model.generate(
    text="Hello world",
    ref_audio="reference.wav",
    ref_text="Transcription of reference"
)

# Voice design
audio = model.generate(
    text="Hello world",
    instruct="female, low pitch, british accent"
)
```

**CLI Tools:**
- `omnivoice-demo` — Gradio web UI
- `omnivoice-infer` — Command-line generation
- `omnivoice-infer-batch` — Multi-GPU batch inference

## Platform Support

| Platform | Support | Notes |
|----------|---------|-------|
| **NVIDIA GPU** | ✅ Full | CUDA with float16 |
| **Apple Silicon (MPS)** | ✅ Yes | PyTorch MPS backend, float16 required |
| **MLX** | ❌ No | No quantized MLX variants available |
| **GGUF/Quantization** | ❌ No | Must run at full precision |

## Memory Requirements

| Precision | VRAM/RAM | Notes |
|-----------|----------|-------|
| **float16** | 6-8 GB | Recommended minimum |
| **float32** | 10-12 GB | Not recommended |

**Apple Silicon recommendations:**
- 8 GB unified memory: ⚠️ Barely usable (heavy swapping)
- 16 GB unified memory: ✅ Comfortable
- 24 GB+ unified memory: ✅ Ideal for batch inference

## Repositories & Resources

- **GitHub:** https://github.com/k2-fsa/OmniVoice
- **HuggingFace:** https://huggingface.co/k2-fsa/OmniVoice
- **Paper:** arXiv:2604.00688 (OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models)
- **Demo:** https://huggingface.co/spaces/k2-fsa/OmniVoice

## See Also

- [[vibevoice]] — VibeVoice; primary alternative ASR/TTS system
- [[omnivoice-vs-vibevoice-comparison]] — Detailed comparison of both systems

## Related Concepts

- [[vibevoice]] — Microsoft's voice AI family (TTS + ASR, MLX support, 10 languages)
- [[omnivoice-vs-vibevoice-comparison]] — Detailed comparison
- [[continuous-speech-tokenizers]] — VibeVoice's 7.5 Hz tokenizer approach (contrasts with OmniVoice's 8-codebook discrete tokens)
- [[next-token-diffusion-speech]] — VibeVoice's next-token diffusion (differs from OmniVoice's discrete masked diffusion)
