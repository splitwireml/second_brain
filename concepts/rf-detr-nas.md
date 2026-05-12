---
title: RF-DETR with Neural Architecture Search
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [computer-vision, object-detection, architecture, deep-learning, inference]
sources: [raw/articles/skalskip92-rf-detr-nas-roboflow-2026-04-20.md]
related_entity: [[roboflow]]
---

# RF-DETR with Neural Architecture Search

Fine-tuning approach for [RF-DETR](https://arxiv.org/abs/XXXX) (Roboflow's DETR-based object detection model) using Neural Architecture Search inside the Roboflow platform. As of April 20, 2026.

## How It Works

Roboflow trains approximately 6,000 different model architectures and selects the one that best fits the user's target hardware and required latency. This is architecture search as a service — the user specifies deployment constraints and Roboflow handles theNAS internally.

## Relationship to RF-DETR

RF-DETR is Roboflow's DETR-based object detection model. The NAS integration allows custom architecture selection per-deployment target without the user needing to run NAS themselves.

## Related
- [[roboflow]] — the platform offering this
- [[mixture-of-experts]] — another architecture selection/sparse approach
