---
updated: 2026-04-11
type: raw
title: VibeVoice Architecture and Usage Analysis
source: ~/Documents/Research/vibevoice/sources/VibeVoice/ (cloned repo)
captured: 2026-04-10
---

# VibeVoice — Architecture & Usage Analysis

Research Date: 2026-04-10
Source: https://github.com/microsoft/VibeVoice (cloned to sources/VibeVoice/)

## Answer: It's Models + SDK + Demo Apps + Production Server

Not just models. The repo contains:

### 1. Python SDK (`vibevoice/` package)
- `pip install -e .` — installable Python package
- Full model classes, processors, schedulers
- Designed for both import-as-library AND standalone script usage
- `vibevoice.modular.*` — model definitions (Transformers-compatible)
- `vibevoice.processor.*` — audio/text processors
- `vibevoice.schedule.*` — DPM solver diffusion scheduler
- `vibevoice.scripts.*` — checkpoint conversion utilities

### 2. Three Distinct Models (all in code)
- **VibeVoice-ASR-7B** — speech-to-text (Qwen2.5-7B backbone)
- **VibeVoice-TTS-1.5B** — text-to-speech (Qwen2.5-1.5B backbone) — CODE REMOVED, weights only on HF
- **VibeVoice-Realtime-0.5B** — streaming TTS (Qwen2.5-0.5B backbone) — FULL CODE PRESENT

### 3. Demo Applications (`demo/`)
- **Gradio web UI** for ASR (`demo/vibevoice_asr_gradio_demo.py`) — full browser UI with audio upload, transcription, segment playback, hotwords
- **FastAPI + WebSocket server** for Realtime TTS (`demo/web/app.py` + `demo/web/index.html`) — streaming audio delivery via WebSocket, voice presets, CFG/steps controls
- **CLI batch inference** (`demo/vibevoice_asr_inference_from_file.py`) — transcribe files/directories/HF datasets with batching
- **Colab notebook** (`demo/vibevoice_realtime_colab.ipynb`)
- **Voice presets** (`demo/voices/streaming_model/*.pt`) — 25 pre-built voice profiles (9 languages + 11 English styles)

### 4. Production Server (`vllm_plugin/`)
- **vLLM plugin** — registers VibeVoice ASR as a multimodal model in vLLM
- **OpenAI-compatible API** — `vllm serve` launches a REST server on port 8000
- **Data parallel deployment** — nginx load balancer + multiple vLLM workers for multi-GPU
- **One-click launcher** (`vllm_plugin/scripts/start_server.py`) — installs deps, downloads model, generates tokenizer files, starts server
- **Tensor parallel** support — split 7B model across multiple GPUs
- **API test clients** (`vllm_plugin/tests/test_api.py`)

### 5. Fine-tuning (`finetuning-asr/`)
- LoRA fine-tuning script using PEFT + Transformers Trainer
- Toy dataset included (2 samples)
- Inference script for LoRA-adapted models

## Architecture Deep Dive

### ASR Model (7B) — Speech-to-Text
- **Backbone:** Qwen2.5-7B (language model)
- **Audio encoders:** Acoustic VAE tokenizer (64-dim) + Semantic VAE tokenizer (128-dim)
- **Connector:** SpeechConnector (fc1 -> RMSNorm -> fc2) projects audio features to LM hidden size
- **Pipeline:** Raw audio → VAE tokenizers → connectors → embeddings → Qwen2.5 → text output
- **Output:** Structured transcription with speaker ID, timestamps, content
- **Context:** 64K tokens (60 min audio in single pass)

### TTS/Realtime Model (0.5B/1.5B) — Text-to-Speech
- **Backbone:** Qwen2.5 (0.5B or 1.5B)
- **Architecture:** Two-stage LM — `language_model` (lower layers for text) + `tts_language_model` (upper layers for speech generation)
- **Diffusion head:** VibeVoiceDiffusionHead generates acoustic details from LM hidden states
- **EOS classifier:** BinaryClassifier decides when speech segment ends
- **Tokenizer:** Acoustic tokenizer at 7.5 Hz (ultra-low rate)
- **Scheduler:** DPM-Solver multistep for diffusion sampling
- **Streaming:** AudioStreamer yields audio chunks as they're generated

### vLLM Integration
- Registers as multimodal model via `MULTIMODAL_REGISTRY`
- Patches AudioMediaIO to use FFmpeg for audio loading
- Custom VibeVoiceAudioEncoder with streaming segmentation (60s chunks)
- Supports OpenAI chat completions API with audio input

## How You'd Actually Use It

### As a Library (Python SDK)
```python
# ASR — transcribe audio
from vibevoice.modular.modeling_vibevoice_asr import VibeVoiceASRForConditionalGeneration
from vibevoice.processor.vibevoice_asr_processor import VibeVoiceASRProcessor

processor = VibeVoiceASRProcessor.from_pretrained("microsoft/VibeVoice-ASR")
model = VibeVoiceASRForConditionalGeneration.from_pretrained("microsoft/VibeVoice-ASR")
inputs = processor(audio="meeting.mp3", return_tensors="pt", add_generation_prompt=True)
output = model.generate(**inputs)
text = processor.decode(output[0], skip_special_tokens=True)

# TTS — generate speech (streaming)
from vibevoice import VibeVoiceStreamingForConditionalGenerationInference, VibeVoiceStreamingProcessor

processor = VibeVoiceStreamingProcessor.from_pretrained("microsoft/VibeVoice-Realtime-0.5B")
model = VibeVoiceStreamingForConditionalGenerationInference.from_pretrained("microsoft/VibeVoice-Realtime-0.5B")
# Uses model.generate() with AudioStreamer for chunk-by-chunk audio output
```

### As a Production Server (vLLM)
```bash
# One-click deployment — starts OpenAI-compatible API on port 8000
python vllm_plugin/scripts/start_server.py --model microsoft/VibeVoice-ASR --port 8000

# Multi-GPU: 4 replicas behind nginx
python vllm_plugin/scripts/start_server.py --dp 4

# Then call via OpenAI API
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "vibevoice", "messages": [{"role": "user", "content": [{"type": "audio_url", "audio_url": {"url": "meeting.mp3"}}]}]}'
```

### As a Web App (Demos)
```bash
# Gradio ASR demo — browser UI for transcription
python demo/vibevoice_asr_gradio_demo.py

# FastAPI TTS demo — streaming text-to-speech with WebSockets
python demo/vibevoice_realtime_demo.py --port 3000
# Opens http://localhost:3000 in browser
```

### Fine-tune ASR on Custom Data
```bash
python finetuning-asr/lora_finetune.py --data_dir ./my_dataset --model_path microsoft/VibeVoice-ASR
```

## Dependencies
- PyTorch, Transformers (>=4.51.3), Accelerate, Diffusers
- librosa, scipy, numpy, numba (audio processing)
- FastAPI, uvicorn, aiortc (web/server)
- Gradio (demo UI)
- vLLM (optional, for production serving)
- PEFT (optional, for fine-tuning)

## Key Insight

## See Also

- [[vibevoice]] — VibeVoice main documentation
- [[vibevoice-vs-insanely-fast-whisper-comparison-2026-04-10]] — Comparison with Insanely Fast Whisper
- [[vibevoice-quantizations-mlx-apple-silicon-2026-04-10]] — Quantization details

This is a **research-grade model library with production serving capabilities**. It's not a SaaS or a complete application — it's a toolkit that gives you:
1. The models (downloadable weights + code to run them)
2. A Python SDK (import and use in your own code)
3. Demo apps (Gradio, FastAPI+WebSocket)
4. Production server (vLLM with OpenAI-compatible API)
5. Fine-tuning code (LoRA for ASR)

The TTS code for the 1.5B model was removed due to misuse, but the 0.5B streaming TTS and 7B ASR are fully functional with complete code.