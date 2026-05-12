---
title: Computer Vision
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [computer-vision]
sources: []
---

## Overview

Computer vision (CV) is the field of AI that enables machines to interpret and understand visual information from the world — images, videos, and camera streams. It encompasses a wide range of tasks from low-level pixel processing to high-level scene understanding.

## Core Task Hierarchy

- **Image classification** — assign a label to an entire image
- **Object detection** — find and localize objects with bounding boxes
- **Semantic segmentation** — pixel-level class labels ([[segmentation]])
- **Instance segmentation** — distinguish between individual object instances
- **Panoptic segmentation** — unified semantic + instance
- **Pose estimation** — keypoint detection for human body/hand/face
- **Video understanding** — action recognition, temporal modeling
- **3D vision** — depth estimation, NeRF, 3D reconstruction

## Key Models & Paradigms

- **CNNs** — ResNet, ConvNeXt; dominant until ~2020
- **Vision Transformers (ViT)** — transformer architecture for images; foundation for modern CV
- **SAM (Segment Anything)** — Meta's zero-shot segmentation foundation model ([[segmentation]])
- **CLIP** — vision-language alignment for zero-shot image classification
- **Diffusion models** — Stable Diffusion, DALL-E for image generation

## Related Concepts

- [[segmentation]] — the pixel-level task family
- [[point-tracking]] — tracking points across video frames
- [[training-free]] — zero-shot models like SAM that need no task-specific training
- [[3d-vision]] — 3D scene reconstruction and understanding
