---
title: Pixal3D
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [model, 3d, 3d-vision, computer-vision, image, open-source]
sources: [raw/articles/tencentarc-pixal3d-huggingface-2026-06-04.md]
---

# Pixal3D

Pixal3D is a single-image 3D generation system from [[tencentarc]] that aims for near-reconstruction-level fidelity by explicitly lifting image pixels into 3D through back-projection rather than only injecting image features through attention. The public model card positions it as a high-fidelity path from one image to detailed geometry plus PBR textures on [[huggingface]].

## Confirmed From The Model Card

- **Task**: generate a GLB mesh from a single image.
- **Core claim**: explicit pixel-to-3D correspondences via back-projection improve fidelity over looser attention-based image conditioning.
- **Output quality target**: detailed geometry plus PBR textures.
- **Paper status**: accepted to SIGGRAPH 2026 in April 2026.
- **Release cadence**: inference code, demo, improved Trellis.2-based version, and training/data toolkit were all released in April–May 2026.
- **Deployment surface**: Hugging Face model repo plus a public Gradio demo.

## Architecture And Training Notes

The README describes Pixal3D as a three-stage cascade:

1. **Sparse Structure** — 32 → 64 resolution.
2. **Shape** — 256 → 512 → 1024 resolution.
3. **Texture** — 256 → 512 → 1024 resolution.

All stages use pixel-aligned projection conditioning and view-aligned latents, with 2 views by default. The `main` branch is described as an improved implementation on the Trellis.2 backbone, while the `paper` branch preserves the SIGGRAPH paper version built on Direct3D-S2.

## Operational Notes

- **Standard inference**: `python inference.py --image ... --output ./output.glb`
- **Low-VRAM mode**: `--low_vram` reduces peak memory by loading models on demand.
- **Default resolution**: 1536 in standard mode, 1024 in low-VRAM mode, both overrideable with `--resolution`.
- **Environment setup**: base install follows Trellis.2, then adds `requirements.txt`, `natten==0.21.0`, and a `utils3d` wheel.
- **Attention fallback**: if `flash_attn` is unavailable, the README suggests PyTorch SDPA via `ATTN_BACKEND=sdpa`.

## Evidence Layers

### Confirmed

The model card explicitly confirms single-image 3D generation, GLB export, low-VRAM inference, a public web demo, and a full three-stage training pipeline.

### Likely

The install instructions strongly suggest a CUDA-first deployment path because `natten` is installed with `NATTEN_CUDA_ARCH=...` and `flash_attn` is treated as the default fast-attention path. The README does not explicitly claim broader hardware portability, so that remains likely rather than confirmed.

## Positioning

Relative to the broader [[3d-vision]] landscape, Pixal3D is notable for emphasizing direct pixel alignment instead of weaker cross-attention injection. It sits near other image-to-3D systems such as [[lyra-2-0]], but this source does not provide a benchmark comparison, so any quality ranking beyond the authors' claims would be speculative.

## Related

- [[tencentarc]]
- [[tencent]]
- [[huggingface]]
- [[computer-vision]]
- [[3d-vision]]
- [[lyra-2-0]]
