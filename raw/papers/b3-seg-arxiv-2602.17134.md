---
title: B3 Seg Arxiv 2602.17134
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# B³-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG and Beta-Bernoulli Bayesian Updates

**arXiv:** https://arxiv.org/abs/2602.17134
**Authors:** Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma
**Conference:** CVPR 2026
**Topic:** 3D Vision
**Highlighted:** Yes

## Abstract

Interactive 3D Gaussian Splatting (3DGS) segmentation is essential for real-time editing of pre-reconstructed assets in film and game production. However, existing methods rely on predefined camera viewpoints, ground-truth labels, or costly retraining, making them impractical for low-latency use. We propose B³-Seg (Beta-Bernoulli Bayesian Segmentation for 3DGS), a fast and theoretically grounded method for open-vocabulary 3DGS segmentation under camera-free and training-free conditions. Our approach reformulates segmentation as sequential Beta-Bernoulli Bayesian updates and actively selects the next view via analytic Expected Information Gain (EIG). This Bayesian formulation guarantees the adaptive monotonicity and submodularity of EIG, which produces a greedy (1 - 1/e) approximation to the optimal view sampling policy. Experiments on multiple datasets show that B³-Seg achieves competitive results to high-cost supervised methods while operating end-to-end segmentation within a few seconds. The results demonstrate that B³-Seg enables practical, interactive 3DGS segmentation with provable information efficiency.
