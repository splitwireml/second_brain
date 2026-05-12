---
title: Lightricks Ltx 2 3 2026 04 16
updated: 2026-04-16
type: raw
source: https://huggingface.co/Lightricks/LTX-2.3
retrieved: 2026-04-16
---

# LTX-2.3 Model Card

**Source:** https://huggingface.co/Lightricks/LTX-2.3

## Metadata
- **Developed by:** Lightricks
- **Model type:** DiT-based audio-video foundation model (diffusion)
- **License:** LTX-2 Community License Agreement (non-commercial + restrictions; see LICENSE)
- **Repository:** https://github.com/Lightricks/LTX-2
- **Paper:** arXiv:2601.03233
- **Pipeline tags:** image-to-video, text-to-video, video-to-video, image-text-to-video, audio-to-video, text-to-audio, video-to-audio, audio-to-audio, text-to-audio-video, image-to-audio-video, image-text-to-audio-video
- **Languages:** en, de, es, fr, ja, ko, zh, it, pt
- **Library:** Diffusers
- **Demo:** https://app.ltx.studio/ltx-2-playground/i2v
- **API Playground:** https://console.ltx.video/playground/

## Model Checkpoints

| Name | Notes |
|------|-------|
| ltx-2.3-22b-dev | Full model, flexible and trainable in bf16 |
| ltx-2.3-22b-distilled | Distilled version, 8 steps, CFG=1 |
| ltx-2.3-22b-distilled-1.1 | Distilled v1.1 — different aesthetic, improved audio vs v1.0 |
| ltx-2.3-22b-distilled-lora-384 | LoRA applicable to full model (384-res) |
| ltx-2.3-22b-distilled-lora-384-1.1 | LoRA for v1.1 distilled model |
| ltx-2.3-spatial-upscaler-x2-1.1 | x2 spatial upscaler for latents |
| ltx-2.3-spatial-upscaler-x1.5-1.0 | x1.5 spatial upscaler for latents |
| ltx-2.3-temporal-upscaler-x2-1.0 | x2 temporal upscaler (higher FPS) |

## Requirements
- Python >= 3.12
- CUDA version > 12.7
- PyTorch ~= 2.7

## Technical Constraints
- Width & height must be divisible by 32
- Frame count must be divisible by 8 + 1 (i.e., 9, 17, 25, 33...)
- If not divisible: pad input with -1, then crop to desired resolution/frames

## Limitations
- Not intended for or able to provide factual information
- May amplify societal biases
- Prompt following is heavily influenced by prompting-style
- May generate inappropriate or offensive content
- Audio without speech may be lower quality

## Training
The base (dev) model is fully trainable. LoRAs and IC-LoRAs can be reproduced following the LTX-2 Trainer Readme. Training for motion, style, or likeness can take less than an hour in many settings.

## BibTeX
@article{hacohen2025ltx2,
  title={LTX-2: Efficient Joint Audio-Visual Foundation Model},
  author={HaCohen, Yoav and Brazowski, Benny and Chiprut, Nisan and Bitterman, Yaki and Kvochko, Andrew and Berkowitz, Avishai and Shalem, Daniel and Lifschitz, Daphna and Moshe, Dudu and Porat, Eitan and Richardson, Eitan and Guy Shiran and Itay Chachy and Jonathan Chetboun and Michael Finkelson and Michael Kupchick and Nir Zabari and Nitzan Guetta and Noa Kotler and Ofir Bibi and Ori Gordon and Poriya Panet and Roi Benita and Shahar Armon and Victor Kulikov and Yaron Inger and Yonatan Shiftan and Zeev Melumian and Zeev Farbman},
  journal={arXiv preprint arXiv:2601.03233},
  year={2025}
}