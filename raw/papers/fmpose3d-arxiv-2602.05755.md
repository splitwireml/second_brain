---
title: Fmpose3D Arxiv 2602.05755
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# FMPose3D: Monocular 3D Pose Estimation via Flow Matching

**arXiv:** https://arxiv.org/abs/2602.05755
**Code:** https://github.com/AdaptiveMotorControlLab/FMPose3D
**Authors:** Ti Wang, Xiaohang Yu, Mackenzie Weygandt Mathis
**Conference:** CVPR 2026
**Topic:** Pose Estimation
**Highlighted:** No

## Abstract

Monocular 3D pose estimation is fundamentally ill-posed due to depth ambiguity and occlusions, thereby motivating probabilistic methods that generate multiple plausible 3D pose hypotheses. In particular, diffusion-based models have recently demonstrated strong performance, but their iterative denoising process typically requires many timesteps for each prediction, making inference computationally expensive. In contrast, we leverage Flow Matching (FM) to learn a velocity field defined by an Ordinary Differential Equation (ODE), enabling efficient generation of 3D pose samples with only a few integration steps. We propose a novel generative pose estimation framework, FMPose3D, that formulates 3D pose estimation as a conditional distribution transport problem. It continuously transports samples from a standard Gaussian prior to the distribution of plausible 3D poses conditioned only on 2D inputs. Although ODE trajectories are deterministic, FMPose3D naturally generates various pose hypotheses by sampling different noise seeds. To obtain a single accurate prediction from those hypotheses, we further introduce a Reprojection-based Posterior Expectation Aggregation (RPEA) module, which approximates the Bayesian posterior expectation over 3D hypotheses. FMPose3D surpasses existing methods on the widely used human pose estimation benchmarks Human3.6M and MPI-INF-3DHP, and further achieves state-of-the-art performance on the 3D animal pose datasets Animal3D and CtrlAni3D, demonstrating strong performance across both 3D pose domains. The code is available at this https URL.
