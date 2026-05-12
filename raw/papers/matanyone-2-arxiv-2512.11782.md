---
title: Matanyone 2 Arxiv 2512.11782
created: 2026-04-15
updated: 2026-04-15
type: raw
---
# MatAnyone 2: Scaling Video Matting via a Learned Quality Evaluator

**arXiv:** https://arxiv.org/abs/2512.11782
**Code:** https://github.com/pq-yang/MatAnyone2
**Demo:** https://huggingface.co/spaces/PeiqingYang/MatAnyone
**Authors:** Peiqing Yang, Shangchen Zhou, Kai Hao, Qingyi Tao
**Conference:** CVPR 2026
**Topic:** Segmentation
**Highlighted:** No

## Abstract

Video matting remains limited by the scale and realism of existing datasets. While leveraging segmentation data can enhance semantic stability, the lack of effective boundary supervision often leads to segmentation-like mattes lacking fine details. To this end, we introduce a learned Matting Quality Evaluator (MQE) that assesses semantic and boundary quality of alpha mattes without ground truth. It produces a pixel-wise evaluation map that identifies reliable and erroneous regions, enabling fine-grained quality assessment. The MQE scales up video matting in two ways: (1) as an online matting-quality feedback during training to suppress erroneous regions, providing comprehensive supervision, and (2) as an offline selection module for data curation, improving annotation quality by combining the strengths of leading video and image matting models. This process allows us to build a large-scale real-world video matting dataset, VMReal, containing 28K clips and 2.4M frames. To handle large appearance variations in long videos, we introduce a reference-frame training strategy that incorporates long-range frames beyond the local window for effective training. Our MatAnyone 2 achieves state-of-the-art performance on both synthetic and real-world benchmarks, surpassing prior methods across all metrics.
