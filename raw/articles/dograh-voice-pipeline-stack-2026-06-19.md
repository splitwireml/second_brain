---
source_url: local-research://dograh-voice-pipeline-stack
ingested: 2026-06-19
sha256: 2956b445ac99fe62886974c5ecbf999d86b7a81f8bdf8721969bb3b83aae8b49
---

# Dograh + Split Voice Pipeline on One VM — Research Notes

## Scope
Researching a self-hosted stack that serves Dograh and a custom split voice pipeline from the same VM, with:
- NVIDIA Speech NIM for ASR (Parakeet / Nemotron family)
- SGLang for the text LLM layer using an Unsloth Gemma 12B GGUF checkpoint
- SGLang-Omni for TTS / voice cloning if compatible with the desired Chatterbox checkpoints
- one-run deployment and future LLM checkpoint swap capability

## Key findings

### 1) Dograh is already structurally compatible with a split STT → LLM → TTS architecture
Dograh's live pipeline is built on Pipecat and, in non-realtime mode, it explicitly instantiates separate `create_stt_service`, `create_tts_service`, and `create_llm_service` objects before wiring the run pipeline.^[sources/dograh/api/services/pipecat/run_pipeline.py]

Dograh's own docs also separate three modes at the product level: speech-to-speech realtime, Dograh-managed stack, and BYOK (bring-your-own-key/provider) where LLM, Voice, and Transcriber are configured independently.^[sources/dograh/docs/configurations/inference-providers.mdx]

### 2) Dograh can point at self-hosted OpenAI-compatible backends
Dograh's provider registry exposes OpenAI-compatible base URLs for multiple paths:
- LLM: OpenAI-compatible override and a dedicated `speaches` provider with `base_url` described as "OpenAI-compatible endpoint (Ollama, vLLM, etc.)".^[sources/dograh/api/services/configuration/registry.py]
- TTS: OpenAI-compatible TTS endpoint through `speaches`, described as suitable for self-hosted engines like Kokoro-style APIs.^[sources/dograh/api/services/configuration/registry.py]
- STT: OpenAI-compatible STT endpoint through `speaches` and OpenAI-style base URL overrides.^[sources/dograh/api/services/configuration/registry.py]

This means Dograh does not need to be modified first just to talk to local services, provided those services expose interfaces compatible with the Pipecat integrations Dograh already uses.

### 3) NVIDIA Speech NIM fits the ASR side well, but with hard GPU/VRAM constraints
NVIDIA's ASR NIM is explicitly designed as an independent containerized building block for speech pipelines and supports streaming and offline ASR modes, with the application orchestrating data flow between services.^[https://docs.nvidia.com/nim/speech/latest/about/how-it-works.html]

For ASR, the relevant supported families include Parakeet CTC, Parakeet TDT, Parakeet RNNT Multilingual, and Nemotron ASR Streaming. NVIDIA documents streaming low-latency (`str`), streaming high-throughput (`str-thr`), and offline (`ofl`) profiles, which directly matches the requirement that each stage should be capable of high-throughput inference on its own.^[https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html]

Important constraints:
- Speech NIM requires NVIDIA GPU compute capability >= 8.0.^[https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html]
- This includes Ampere-class RTX 30-series and newer, but memory still matters.
- ASR NIM minimum documented VRAM is 16 GB.^[https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html]
- `Parakeet 1.1b RNNT Multilingual` can consume up to ~50 GB GPU memory when deploying `mode=all`.^[https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html]
- Nemotron ASR Streaming is streaming-only, which is good for realtime use, but loses offline flexibility.^[https://docs.nvidia.com/nim/speech/latest/asr/]

### 4) The requested LLM path is the weakest compatibility point today
SGLang definitely supports GGUF in general and Unsloth documents serving dense GGUF checkpoints with SGLang using `--served-model-name` and `--tokenizer-path`.^[https://docs.unsloth.ai/basics/inference-and-deployment/sglang-guide]

However, current public evidence around Gemma GGUF is mixed and specifically rough for Gemma 3 GGUF:
- historical SGLang issues show Gemma 2 / Gemma 3 GGUF compatibility problems
- one later Gemma 3 GGUF issue still reports `Unknown gguf model_type: gemma3_text`
- another earlier issue shows raw GGUF arch detection failures for Gemma 3 in the SGLang/Transformers stack.^[https://github.com/sgl-project/sglang/issues/2451]^[https://github.com/sgl-project/sglang/issues/4894]^[https://github.com/sgl-project/sglang/issues/8495]

The specific checkpoint family appears to be `unsloth/gemma-3-12b-it-GGUF`, which does offer `Q8_0` and other GGUF variants on Hugging Face.^[https://huggingface.co/unsloth/gemma-3-12b-it-GGUF]

Research verdict: **SGLang + Gemma 12B GGUF is plausible in principle, but the exact Gemma 3 12B GGUF path should be treated as a validation item, not as a guaranteed drop-in production baseline.** If zero-debug deployment is the priority, the safer initial baseline is to use a format and checkpoint combination already well-traveled by SGLang, then introduce Gemma 12B GGUF only after a smoke test passes.

### 5) SGLang-Omni strongly matches the desired architecture pattern, but not the requested Chatterbox model family
SGLang-Omni is explicitly built for multi-stage low-latency pipelines where each stage has its own scheduler and can be placed on processes/GPUs independently. It supports configurable relay backends, stage placement, process colocation/fusion, and streaming edges between stages.^[https://sgl-project.github.io/sglang-omni/]^[https://sgl-project.github.io/sglang-omni/developer_reference/config.html]^[https://sgl-project.github.io/sglang-omni/developer_reference/communication.html]

That architecture is an excellent match for the user's requirement around split-layer processing, independent throughput tuning, and streaming across all layers.

But the current public/model support surface does **not** list Chatterbox. The README and docs list Higgs Audio, Fish Speech S2-Pro, Voxtral TTS, Qwen3-TTS, and MOSS-TTS as the main TTS paths.^[https://github.com/sgl-project/sglang-omni] The cloned source tree also contains no Chatterbox implementation or references in model support.

Research verdict: **SGLang-Omni is the right runtime pattern, but Chatterbox on SGLang-Omni is currently an integration project, not an off-the-shelf supported path.**

### 6) Chatterbox itself is viable, but via its own runtime today
Chatterbox is mature enough as a standalone TTS family:
- Chatterbox-Turbo: 350M, low-compute/low-VRAM, English, optimized for low-latency agents
- Chatterbox-Multilingual V3: 500M, 23+ languages, zero-shot cloning
- original Chatterbox: 500M, English, more creative controls.^[https://github.com/resemble-ai/chatterbox]

Turbo requires a reference clip for cloning in the published usage path, supports paralinguistic tags, and is explicitly framed as the production voice-agent option.^[https://github.com/resemble-ai/chatterbox] The repo targets plain Python usage (`pip install chatterbox-tts`) rather than an existing OpenAI-compatible server runtime.

This means there are two realistic ways to use Chatterbox:
1. run Chatterbox behind a custom small API shim that exposes the TTS contract Dograh can consume
2. contribute a Chatterbox backend to SGLang-Omni

### 7) NVIDIA TTS NIM provides an unexpected alternative, but not the same one requested
NVIDIA's TTS NIM support matrix includes `Chatterbox TTS Multilingual` as a supported model family, but not Chatterbox Turbo.^[https://docs.nvidia.com/nim/speech/26.05.0/reference/support-matrix/tts.html]

This is strategically important:
- if the main requirement is Chatterbox-style multilingual voice cloning under an industrial serving stack, NVIDIA already has a supported route
- but if the requirement is specifically **Turbo and Normal as swappable checkpoints under SGLang-Omni**, NIM does not satisfy that requirement
- and the documented GPU memory for NIM's Chatterbox Multilingual profile is very high (~52.5 GB GPU memory), which makes it unrealistic for many 30-series deployments.^[https://docs.nvidia.com/nim/speech/26.05.0/reference/support-matrix/tts.html]

## Practical architecture decision

### Recommended Phase-1 baseline (lowest risk)
- Dograh: orchestration, UI, workflows, WebRTC / telephony entrypoint
- ASR: NVIDIA Speech NIM (Parakeet CTC English or Nemotron ASR Streaming depending on exact language/feature goals)
- LLM: SGLang with a validated OpenAI-compatible endpoint
- TTS: **temporary pragmatic path**
  - either Chatterbox behind a custom OpenAI-compatible TTS shim
  - or a supported SGLang-Omni TTS family while Chatterbox support is built/validated

This achieves the split-stage architecture immediately, with Dograh consuming all services via provider/base-URL config.

### Recommended Phase-2 target (if SGLang-Omni is mandatory for TTS)
- Keep Dograh + NIM ASR + SGLang LLM
- add a dedicated SGLang-Omni deployment project for TTS
- either:
  - switch to one of the already-supported SGLang-Omni TTS families, or
  - implement and validate a Chatterbox adapter inside SGLang-Omni

## Main risks / blockers
1. **Gemma 12B GGUF on SGLang is not yet a zero-risk production assumption.**
2. **Chatterbox is not a currently supported SGLang-Omni model family.**
3. **NIM imposes a real floor on GPU class and VRAM.** RTX 30-series qualifies architecturally, but not every card is large enough.
4. **One-VM deployment is fine architecturally, but not automatically fine for GPU memory.** Co-locating Dograh, NIM ASR, SGLang LLM, and TTS on a single 24 GB card is a scheduling/memory problem, not just a Docker problem.

## Deployment implication
The system should be designed as a single Compose (or equivalent) project with separate services, healthchecks, and a preflight profile test. "One-run deploy" should mean:
- pinned image tags
- preflight GPU checks
- explicit model/profile env vars
- startup ordering + health gates
- a smoke-test script that exercises STT, LLM, TTS, and Dograh end-to-end

That is achievable, but only after the above compatibility questions are resolved.
