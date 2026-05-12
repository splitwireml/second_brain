---
updated: 2026-04-11
type: raw
title: Insanely Fast Whisper — Technical Analysis
source: https://github.com/Vaibhavs10/insanely-fast-whisper (cloned)
captured: 2026-04-10
---

# Insanely Fast Whisper — Technical Analysis

## What It Is

An opinionated ~180-line CLI wrapper around HuggingFace's `transformers.pipeline("automatic-speech-recognition")`. No custom inference engine, no custom model — just a convenience layer with Rich progress bars, speaker diarization, and pre-tuned defaults.

**Version:** 0.0.15
**License:** MIT
**Maintainer:** Vaibhav Srivastav (reach_vb), Patrick Arminio
**Community-driven**, not a formal product.

## Default Model

**`openai/whisper-large-v3`** (NOT v3-turbo, NOT v2).

The `--model-name` flag accepts any checkpoint:
- `openai/whisper-large-v3` (default)
- `openai/whisper-large-v3-turbo`
- `openai/whisper-large-v2`
- `distil-whisper/large-v2`
- Any other Whisper-compatible checkpoint

## How Speed is Achieved

Three optimizations layered on top of the standard Transformers pipeline:

1. **Flash Attention 2** (`--flash True`) — ~10x speedup over fp32 baseline. CUDA-only, does NOT work on MPS.
2. **Automatic chunking** — splits audio into 30-second segments (`chunk_length_s=30`)
3. **Batching** — processes 24 chunks in parallel by default (`--batch-size 24`)

### Benchmarks (A100 80GB, 150 min audio)

| Configuration | Time |
|---|---|
| large-v3 fp32 (no optimization) | ~31 min |
| large-v3 fp16 + batching [24] + BetterTransformer | ~5 min |
| **large-v3 fp16 + batching [24] + Flash Attention 2** | **~2 min** |
| distil-large-v2 fp16 + batching + BetterTransformer | ~3 min |
| Faster Whisper large-v2 fp16 + beam_size [1] | ~9 min |

## Architecture

### Core Pipeline (`cli.py`)
```python
pipe = pipeline(
    "automatic-speech-recognition",
    model=args.model_name,
    torch_dtype=torch.float16,
    device="mps" if args.device_id == "mps" else f"cuda:{args.device_id}",
    model_kwargs={"attn_implementation": "flash_attention_2"} if args.flash else {"attn_implementation": "sdpa"},
)

outputs = pipe(
    args.file_name,
    chunk_length_s=30,
    batch_size=args.batch_size,
    generate_kwargs={"task": args.task, "language": language},
    return_timestamps=ts,  # "word" or True (chunk-level)
)
```

### Diarization (`utils/diarization_pipeline.py`)
- Uses `pyannote/speaker-diarization-3.1` (requires HF token)
- Runs AFTER transcription
- Aligns speaker segments to Whisper timestamps using `np.argmin` on end times
- Supports `--num-speakers`, `--min-speakers`, `--max-speakers` constraints

### Output (`utils/result.py`)
JSON with three fields:
- `speakers` — diarization results (empty if no HF token provided)
- `chunks` — Whisper chunk-level timestamps + text
- `text` — full concatenated transcript

## Dependencies

- `transformers` — core ASR pipeline
- `accelerate` — device placement
- `pyannote-audio>=3.1.0` — speaker diarization (optional, requires HF token)
- `rich>=13.7.0` — progress bars
- `setuptools>=68.2.2` — build system

Built with PDM (`pdm-backend`). No PyTorch in dependencies — relies on user's system PyTorch.

## Apple Silicon (MPS) Support

**Works, with significant caveats:**

- `--device-id mps` flag required
- **Flash Attention 2 does NOT work on MPS** — falls back to SDPA (Scaled Dot-Product Attention)
- **Default batch size 24 will OOM** — recommended `--batch-size 4` (~12GB VRAM)
- `torch.mps.empty_cache()` called after pipeline creation
- BetterTransformer path is commented out (`# pipe.model = pipe.model.to_bettertransformer()`)

On a 16GB Mac Mini:
- Batch size 4 → ~12GB VRAM → works
- Batch size 24 → OOM crash
- No FA2 → significantly slower than CUDA equivalent
- SDPA is still faster than raw fp32, but not by the same margin as FA2

## Usage Examples

```bash
# Install
pipx install insanely-fast-whisper==0.0.15 --force

# Zero-install run
pipx run insanely-fast-whisper --file-name audio.mp3

# Mac
insanely-fast-whisper --file-name audio.mp3 --device-id mps --batch-size 4

# With Flash Attention (CUDA only)
insanely-fast-whisper --file-name audio.mp3 --flash True

# With diarization
insanely-fast-whisper --file-name audio.mp3 --hf-token hf_XXXXX

# With custom model (e.g., v3-turbo)
insanely-fast-whisper --file-name audio.mp3 --model-name openai/whisper-large-v3-turbo

# Word-level timestamps
insanely-fast-whisper --file-name audio.mp3 --timestamp word

# Translation mode
insanely-fast-whisper --file-name audio.mp3 --task translate --language en
```

## Pros
- Dead simple — one command, no configuration needed
- Works with any Whisper-compatible checkpoint
- Built-in speaker diarization (pyannote)
- Supports local files, URLs, and `pipx run` for zero-install
- Rich progress bars for UX
- MIT license

## Cons
- Very thin wrapper — replicable in ~10 lines of Python
- No streaming output, no real-time transcription
- No GPU fallback if MPS runs out of memory
- Flash Attention 2 doesn't work on MPS (CUDA only)
- Not actively maintained — version 0.0.15, limited recent commits
- Diarization requires HF token (pyannote is gated)
- No batch inference across multiple files (single file per run)
- Output is JSON only — no SRT, VTT, or TXT export (need `convert_output.py`)

## Verdict

## See Also

- [[insanely-fast-whisper]] — Insanely Fast Whisper project page
- [[vibevoice]] — VibeVoice — alternative ASR with MLX support
- [[vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10]] — Detailed comparison


A convenient CLI for quick Whisper transcriptions, especially on CUDA machines with Flash Attention. On Apple Silicon, it works but loses its main speed advantage (FA2) and requires manual batch-size tuning. Not a production-grade tool — more of a developer convenience utility.