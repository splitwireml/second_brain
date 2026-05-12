---
title: Roboflow
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [computer-vision, platform, object-detection, deep-learning]
sources: [raw/articles/skalskip92-rf-detr-nas-roboflow-2026-04-20.md]
---

# Roboflow

Computer vision platform providing annotation tools, dataset management, model training, and deployment. Hosts computer vision workflows end-to-end from raw images to deployed inference APIs.

## Notable Integration: RF-DETR with NAS

Roboflow added Neural Architecture Search (NAS) support for training [RF-DETR](https://arxiv.org/abs/XXXX) — their DETR-based object detection model. When training RF-DETR in Roboflow, NAS searches across ~6,000 different model architectures and selects the one that best fits the user's target hardware and latency requirements. Piotr Skalskip reported this on April 20, 2026.

## Related
- [[rf-detr-nas]] — the NAS fine-tuning concept
- [[skalski-p-top-cvpr-2026-papers]] — Skalski's curated CVPR 2026 paper list
