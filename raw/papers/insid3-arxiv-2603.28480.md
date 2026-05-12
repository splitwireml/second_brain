---
title: Insid3 Arxiv 2603.28480
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# INSID3: Training-Free In-Context Segmentation with DINOv3

**arXiv:** https://arxiv.org/abs/2603.28480
**Code:** https://github.com/visinf/INSID3
**Authors:** Claudia Cuttano, Gabriele Trivigno, Christoph Reich, Daniel Cremers, Carlo Masone, Stefan Roth
**Conference:** CVPR 2026
**Topic:** Segmentation
**Highlighted:** Yes

## Abstract

In-context segmentation (ICS) aims to segment arbitrary concepts, e.g., objects, parts, or personalized instances, given one annotated visual examples. Existing work relies on (i) fine-tuning vision foundation models (VFMs), which improves in-domain results but harms generalization, or (ii) combines multiple frozen VFMs, which preserves generalization but yields architectural complexity and fixed segmentation granularities. We revisit ICS from a minimalist perspective and ask: Can a single self-supervised backbone support both semantic matching and segmentation, without any supervision or auxiliary models? We show that scaled-up dense self-supervised features from DINOv3 exhibit strong spatial structure and semantic correspondence. We introduce INSID3, a training-free approach that segments concepts at varying granularities only from frozen DINOv3 features, given an in-context example. INSID3 achieves state-of-the-art results across one-shot semantic, part, and personalized segmentation, outperforming previous work by +7.5 % mIoU, while using 3x fewer parameters and without any mask or category-level supervision. Code is available at this https URL.
