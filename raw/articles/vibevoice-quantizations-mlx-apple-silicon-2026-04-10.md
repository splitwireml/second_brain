---
updated: 2026-04-11
type: raw
title: VibeVoice Quantizations and MLX Apple Silicon Support
source_url: https://huggingface.co/collections/mlx-community/vibevoice
captured: 2026-04-10
---

# VibeVoice — Quantizations & MLX for Apple Silicon

## MLX Collection (mlx-community) — Native Apple Silicon

The mlx-community has converted both VibeVoice models to MLX format. All use `mlx-audio` for inference.

### Realtime TTS (0.5B) — 5 MLX Variants

| Model | Size | Download | 16GB Mac Mini |
|---|---|---|---|
| VibeVoice-Realtime-0.5B-4bit | 733 MB | mlx-community/VibeVoice-Realtime-0.5B-4bit | ✅ Excellent |
| VibeVoice-Realtime-0.5B-5bit | 855 MB | mlx-community/VibeVoice-Realtime-0.5B-5bit | ✅ Excellent |
| VibeVoice-Realtime-0.5B-8bit | 1.22 GB | mlx-community/VibeVoice-Realtime-0.5B-8bit | ✅ Excellent |
| VibeVoice-Realtime-0.5B-fp16 | 2.14 GB | mlx-community/VibeVoice-Realtime-0.5B-fp16 | ✅ Good |

**Usage (all variants):**
```bash
pip install -U mlx-audio
python -m mlx_audio.tts.generate --model mlx-community/VibeVoice-Realtime-0.5B-4bit --text "Hello world" --voice en-Emma_woman
```

**Voices available:** en-Emma_woman, en-Carter_man, en-Mike_man, en-Grace_woman, en-Frank_man, en-Davis_man, de-Spk0_man, de-Spk1_woman, fr-Spk0_man, fr-Spk1_woman, it-Spk0_woman, it-Spk1_man, jp-Spk0_man, jp-Spk1_woman, kr-Spk0_woman, kr-Spk1_man, nl-Spk0_man, nl-Spk1_woman, pl-Spk0_man, pl-Spk1_woman, pt-Spk0_woman, pt-Spk1_man, sp-Spk0_woman, sp-Spk1_man, in-Samuel_man

### ASR (7B) — 3 MLX Variants

| Model | Size | Download | 16GB Mac Mini |
|---|---|---|---|
| VibeVoice-ASR-4bit | 5.71 GB | mlx-community/VibeVoice-ASR-4bit | ✅ Comfortable |
| VibeVoice-ASR-5bit | 6.67 GB | mlx-community/VibeVoice-ASR-5bit | ✅ Tight but works |
| VibeVoice-ASR-6bit | 7.62 GB | mlx-community/VibeVoice-ASR-6bit | ⚠️ Risky — may swap |
| VibeVoice-ASR-bf16 | ~16.7 GB | mlx-community/VibeVoice-ASR-bf16 | ❌ Won't fit |

**Usage (all variants):**
```bash
pip install -U mlx-audio

# CLI
python -m mlx_audio.stt.generate --model mlx-community/VibeVoice-ASR-4bit --audio "meeting.wav"

# Python
from mlx_audio.stt.utils import load_model
from mlx_audio.stt.generate import generate_transcription

model = load_model("mlx-community/VibeVoice-ASR-4bit")
transcription = generate_transcription(
    model=model,
    audio_path="meeting.wav",
    output_path="output.txt",
    format="txt",
    verbose=True,
)
print(transcription.text)
```

**Note:** ASR MLX models were converted using `mlx-audio` v0.3.0. The model includes acoustic tokenizer (64-dim) + semantic tokenizer (128-dim) + Qwen2.5-7B backbone — listed as 8B params on HF because tokenizer weights are included in the count.

## GGUF Quantizations (TTS 1.5B only — TTS code was removed from main repo)

### gguf-org/vibevoice-gguf (recommended — uses gguf-connector)

| Quantization | Size | Quality |
|---|---|---|
| IQ4_NL | 3.54 GB | Good |
| Q4_0 | 3.54 GB | Good |
| Q4_K_M | 3.54 GB | Better |
| Q5_0 | 3.70 GB | Better |
| Q5_K_M | 3.70 GB | Better |
| Q6_K | 3.87 GB | Very good |
| Q8_0 | 4.19 GB | Near-original |
| BF16 | 5.42 GB | Original precision |

**Usage:**
```bash
pip install gguf-connector
ggc v6
# Interactive menu to select quantization
```

### wsbagnsv1/VibeVoice-1.5B-gguf (experimental)

| Quantization | Size |
|---|---|
| Q8_0 | 3.0 GB |
| BF16 | 5.42 GB |

**Warning:** Marked as highly experimental, no inference support guaranteed.

### wsbagnsv1/VibeVoice-Large-pt-gguf (Large variant)

| Quantization | Size |
|---|---|
| Q8_0 | 10.1 GB |
| BF16 | 18.7 GB |

This is a different/larger variant — unclear if it's the TTS-1.5B with extra components or a separate model. Only appeared 6 days ago.

## 16GB Mac Mini — What Actually Runs

macOS reserves ~4-5GB. Realistic available memory: ~11-12GB.

### Safe on 16GB Mac Mini

| Model | Quant | Size | Memory at Runtime | Verdict |
|---|---|---|---|---|
| Realtime TTS 0.5B | 4-bit | 733 MB | ~2-3 GB | ✅ Fly — barely uses any memory |
| Realtime TTS 0.5B | 8-bit | 1.22 GB | ~3-4 GB | ✅ Very comfortable |
| Realtime TTS 0.5B | fp16 | 2.14 GB | ~4-5 GB | ✅ Fine, even for long-form |
| ASR 7B | 4-bit | 5.71 GB | ~8-10 GB | ✅ Comfortable for short-medium audio |
| ASR 7B | 5-bit | 6.67 GB | ~9-11 GB | ✅ Works, but close on long audio |

### Borderline / Not Recommended

| Model | Quant | Size | Memory at Runtime | Verdict |
|---|---|---|---|---|
| ASR 7B | 6-bit | 7.62 GB | ~10-13 GB | ⚠️ May swap on 60-min audio |
| ASR 7B | bf16 | ~16.7 GB | 20+ GB | ❌ Impossible |

### Key Considerations for 16GB

1. **ASR 4-bit is the sweet spot** — 5.71 GB leaves ~5-6 GB headroom for KV cache on long audio. The 7.5 Hz tokenization helps — 60 min audio = ~27K tokens, which is manageable.

2. **ASR 5-bit works but be careful with long audio** — 60-minute single-pass will push memory. Consider splitting audio into 20-30 min chunks if you hit swapping.

3. **Realtime TTS is trivially small** — even fp16 fits easily. The 4-bit at 733 MB is overkill but available.

4. **No GGUF for ASR yet** — only the TTS 1.5B model has GGUF quantizations. The ASR 7B only has MLX quantizations from mlx-community.

5. **mlx-audio is the framework to use** — it handles both TTS and ASR via `mlx_audio.tts.generate` and `mlx_audio.stt.generate`. Both are CLI-first with Python API available.

## Quick Start for Mac Mini 16GB

```bash
# Install
pip install -U mlx-audio

# TTS — generate speech (4-bit, 733 MB download)
python -m mlx_audio.tts.generate \
  --model mlx-community/VibeVoice-Realtime-0.5B-4bit \
  --text "Hello from my Mac Mini" \
  --voice en-Carter_man

# ASR — transcribe audio (4-bit, 5.71 GB download)
python -m mlx_audio.stt.generate \
  --model mlx-community/VibeVoice-ASR-4bit \
  --audio "meeting.wav"
```

## Community Apple Silicon Support

## See Also

- [[vibevoice]] — VibeVoice main documentation
- [[vibevoice-architecture-analysis-2026-04-10]] — Architecture deep-dive
- [[vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10]] — Performance comparison with Insanely Fast Whisper


The original VibeVoice repo has MPS (Metal Performance Shaders) support for the TTS models via PyTorch MPS backend. A community fork (github.com/gregory-fanous/VibeVoice) maintained the code after Microsoft removed it. However, **MLX is the preferred path for Apple Silicon** — faster, more memory-efficient, and actively maintained by mlx-community.

For the TTS 1.5B (code removed), users can run it via:
- MPS with PyTorch (community fork) — slower, more memory
- GGUF with gguf-connector — good for CPU/GPU hybrid
- MLX — not available for 1.5B yet (only 0.5B Realtime has MLX)