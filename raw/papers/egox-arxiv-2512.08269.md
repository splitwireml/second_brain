---
title: Egox Arxiv 2512.08269
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# EgoX: Egocentric Video Generation from a Single Exocentric Video

**arXiv:** https://arxiv.org/abs/2512.08269
**Code:** https://github.com/DAVIAN-Robotics/EgoX
**Authors:** Taewoong Kang, Kinam Kim, Dohyeon Kim, Minho Park, Junha Hyung, Jaegul Choo
**Conference:** CVPR 2026
**Topic:** Generative Models
**Highlighted:** No

## Abstract

Egocentric perception enables humans to experience and understand the world directly from their own point of view. Translating exocentric (third-person) videos into egocentric (first-person) videos opens up new possibilities for immersive understanding but remains highly challenging due to extreme camera pose variations and minimal view overlap. This task requires faithfully preserving visible content while synthesizing unseen regions in a geometrically consistent manner. To achieve this, we present EgoX, a novel framework for generating egocentric videos from a single exocentric input. EgoX leverages the pretrained spatio-temporal knowledge of large-scale video diffusion models through lightweight LoRA adaptation and introduces a unified conditioning strategy that combines exocentric and egocentric priors via width and channel-wise concatenation. Additionally, a geometry-guided self-attention mechanism selectively attends to spatially relevant regions, ensuring geometric coherence and high visual fidelity. Our approach achieves coherent and realistic egocentric video generation while demonstrating strong scalability and robustness across unseen and in-the-wild videos.
