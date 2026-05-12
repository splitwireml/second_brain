---
updated: 2026-04-11
type: raw
title: Microsoft VibeVoice - Open-Source Frontier Voice AI
source_url: https://github.com/microsoft/VibeVoice
captured: 2026-04-10
---

# Microsoft VibeVoice — Open-Source Frontier Voice AI

**Repo:** https://github.com/microsoft/VibeVoice
**Project Page:** https://microsoft.github.io/VibeVoice/
**License:** MIT
**Stars:** 38,114 | **Forks:** 4,395
**Primary Language:** Python
**Top Contributors:** YaoyaoChang, MSLDCherryPick, pengzhiliang, Damon-Salvetore, wenhui0924

---

## Overview

VibeVoice is a **family of open-source frontier voice AI models** that includes both Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) models.

**Core innovation:** Uses continuous speech tokenizers (Acoustic and Semantic) operating at an ultra-low frame rate of **7.5 Hz**. These tokenizers efficiently preserve audio fidelity while significantly boosting computational efficiency for processing long sequences. VibeVoice employs a **next-token diffusion framework**, leveraging an LLM to understand textual context and dialogue flow, and a diffusion head to generate high-fidelity acoustic details.

## Models

| Model | Size | Purpose | Links |
|---|---|---|---|
| VibeVoice-ASR-7B | 7B | Long-form speech recognition | HF, Playground |
| VibeVoice-TTS-1.5B | 1.5B | Long-form multi-speaker TTS | HF (code removed) |
| VibeVoice-Realtime-0.5B | 0.5B | Real-time streaming TTS | HF, Colab |

### VibeVoice-ASR (7B) — Long-form Speech Recognition

- Handles **60-minute long-form audio** in a single pass (up to 64K token length)
- Generates structured transcriptions: **Who** (Speaker), **When** (Timestamps), **What** (Content)
- **Customized Hotwords** — user-provided names/terms to improve accuracy
- **Natively multilingual** — 50+ languages supported
- **Finetuning code available**
- **vLLM inference supported** for faster inference
- Part of Hugging Face Transformers release (March 2026)

### VibeVoice-TTS (1.5B) — Long-form Multi-speaker TTS

- Synthesizes speech up to **90 minutes long** with up to **4 distinct speakers**
- Accepted as an **Oral at ICLR 2026**
- ⚠️ **Code removed from repo** (Sept 2025) due to misuse — weights still available on HF

### VibeVoice-Realtime (0.5B) — Real-time Streaming TTS

- Supports streaming text input
- Robust long-form speech generation
- **Experimental speakers** added (Dec 2025): multilingual voices in 9 languages (DE, FR, IT, JP, KR, NL, PL, PT, ES) + 11 English style voices

## Timeline

- **2025-08-25:** VibeVoice-TTS open-sourced (accepted as Oral at ICLR 2026)
- **2025-09-05:** TTS code removed due to misuse concerns
- **2025-12-03:** VibeVoice-Realtime-0.5B open-sourced
- **2025-12-16:** Experimental multilingual speakers added to Realtime
- **2026-01-21:** VibeVoice-ASR open-sourced; finetuning code released
- **2026-03-06:** ASR integrated into Hugging Face Transformers
- Community: Vibing voice input method (macOS/Windows) powered by VibeVoice-ASR

## Key Architecture Details

## See Also

- [[vibevoice]] — VibeVoice main page
- [[vibevoice-architecture-analysis-2026-04-10]] — Architecture analysis
- [[omnivoice]] — OmniVoice — alternative voice AI paper


- **Continuous speech tokenizers** (Acoustic + Semantic) at 7.5 Hz
- **Next-token diffusion framework**: LLM for context + diffusion head for acoustic generation
- Ultra-low frame rate enables efficient long-sequence processing
- Single-pass 60-min audio processing (vs. chunked approach of conventional ASR)