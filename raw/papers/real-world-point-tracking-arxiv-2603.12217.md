---
title: Real World Point Tracking Arxiv 2603.12217
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# Real-World Point Tracking with Verifier-Guided Pseudo-Labeling

**arXiv:** https://arxiv.org/abs/2603.12217
**Code:** https://github.com/gorkaydemir/track_on_r
**Project Page:** https://kuis-ai.github.io/track_on_r
**Authors:** Görkay Aydemir, Fatma Güney, Weidi Xie
**Conference:** CVPR 2026
**Topic:** Object Tracking
**Highlighted:** Yes

## Abstract

Models for long-term point tracking are typically trained on large synthetic datasets. The performance of these models degrades in real-world videos due to different characteristics and the absence of dense ground-truth annotations. Self-training on unlabeled videos has been explored as a practical solution, but the quality of pseudo-labels strongly depends on the reliability of teacher models, which vary across frames and scenes. In this paper, we address the problem of real-world fine-tuning and introduce verifier, a meta-model that learns to assess the reliability of tracker predictions and guide pseudo-label generation. Given candidate trajectories from multiple pretrained trackers, the verifier evaluates them per frame and selects the most trustworthy predictions, resulting in high-quality pseudo-label trajectories. When applied for fine-tuning, verifier-guided pseudo-labeling substantially improves the quality of supervision and enables data-efficient adaptation to unlabeled videos. Extensive experiments on four real-world benchmarks demonstrate that our approach achieves state-of-the-art results while requiring less data than prior self-training methods.
