---
title: SAM3 AI-Box Mode
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [computer-vision, segmentation]
sources: [raw/articles/labelme-v6.1-release-2026-04-16.md]
related_entity: [[labelme]]
---

# SAM3 AI-Box Mode

A segmentation workflow in [LabelMe v6.1](https://labelme.io/blog/labelme-v6.1) where the user drags a single bounding box and SAM3 (Segment Anything Model 3) automatically segments every distinct object inside the box.

## How it works

1. User draws one rectangular box around a region of interest
2. SAM3 identifies all discrete objects within that region
3. Each object is returned as a separate polygon or mask shape
4. User can toggle between polygon and mask output

## Use cases

- **Crowds**: One box over a group of people → individual person masks
- **Shelves**: Retail shelf with many products → per-product segmentation
- **Piled objects**: Items in a heap or stack → separated instances

## Relationship to other concepts

- [[sam3-ai-box]] is a specific workflow built on top of the more general [[segmentation]] task type
- It represents a human-AI collaboration pattern: human provides coarse bounding box, AI handles fine-grained instance separation
- This is similar in spirit to [[point-tracking]] where human guidance directs the model, though SAM3 AI-Box operates on boxes rather than individual points
- Part of the broader trend of [[training-free]] segmentation assistance where pre-trained models reduce annotation labor
