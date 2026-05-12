---
title: Videomt Arxiv 2602.17807
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# VidEoMT: Your ViT is Secretly Also a Video Segmentation Model

**arXiv:** https://arxiv.org/abs/2602.17807
**Code:** https://github.com/tue-mps/videomt
**Authors:** Narges Norouzi, Idil Esen Zulfikar, Niccolò Cavagnero, Tommie Kerssies, Bastian Leibe, Gijs Dubbelman, Daan de Geus
**Conference:** CVPR 2026
**Topic:** Segmentation
**Highlighted:** No

## Abstract

Existing online video segmentation models typically combine a per-frame segmenter with complex specialized tracking modules. While effective, these modules introduce significant architectural complexity and computational overhead. Recent studies suggest that plain Vision Transformer (ViT) encoders, when scaled with sufficient capacity and large-scale pre-training, can conduct accurate image segmentation without requiring specialized modules. Motivated by this observation, we propose the Video Encoder-only Mask Transformer (VidEoMT), a simple encoder-only video segmentation model that eliminates the need for dedicated tracking modules. To enable temporal modeling in an encoder-only ViT, VidEoMT introduces a lightweight query propagation mechanism that carries information across frames by reusing queries from the previous frame. To balance this with adaptability to new content, it employs a query fusion strategy that combines the propagated queries with a set of temporally-agnostic learned queries. As a result, VidEoMT attains the benefits of a tracker without added complexity, achieving competitive accuracy while being 5x-10x faster, running at up to 160 FPS with a ViT-L backbone. Code: this https URL
