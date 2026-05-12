---
title: Segmentation
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [segmentation, computer-vision]
sources: []
---

## Overview

Segmentation is the computer vision task of assigning a class label to each pixel in an image (semantic segmentation) or to each distinct object instance (instance segmentation). It is a foundational task in computer vision underlying many applied workflows.

## Variants

- **Semantic segmentation** — every pixel gets a class label (person, car, road, sky)
- **Instance segmentation** — distinguishes between separate objects of the same class (each person gets a separate mask)
- **Panoptic segmentation** — combines both: stuff classes (amorphous) + thing classes (countable objects)
- **Interactive/assisted segmentation** — human provides coarse guidance (boxes, points) and the model refines (see [[sam3-ai-box]])

## Key Models

- **SAM (Segment Anything Model)** — Meta's zero-shot segmentation foundation model; SAM3 is the latest version
- **SAM3 AI-Box** — LabelMe v6.1 feature: one bounding box → per-object masks for all objects inside ([[sam3-ai-box]])
- **SegFormer** — transformer-based semantic segmentation
- **Mask2Former** — unified architecture for all segmentation tasks

## Related Concepts

- [[sam3-ai-box]] — the specific bounding-box-to-masks workflow in LabelMe
- [[point-tracking]] — related human-AI collaborative visual task
- [[computer-vision]] — the broader domain
- [[training-free]] — SAM operates without task-specific training (zero-shot)
