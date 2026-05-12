---
title: "Image Restoration"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [computer-vision]
sources: []
---

## Overview

Image restoration is the process of recovering a degraded or damaged image to a higher quality state. Unlike image enhancement which optimizes for subjective quality, image restoration aims to reverse specific degradation processes (blur, noise, scratches, water damage, fading).

## Techniques

- **Deblurring** — removing motion blur, Gaussian blur, or focus blur
- **Denoising** — removing noise while preserving details (BM3D, DnCNN)
- **Scratch removal** — inpainting missing regions in old photographs
- **Colorization** — adding plausible color to grayscale images
- **Super-resolution** — upscaling while recovering fine details (ESRGAN, Real-ESRGAN)
- **Fine-Restoration models** — end-to-end models targeting old/damaged photo recovery

## Related Entities

- [[huggingmodels-fine-restoration-model]] — HuggingFace model for damaged photo restoration
