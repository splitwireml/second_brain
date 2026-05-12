---
source: https://x.com/TheAhmadOsman/status/2048234466519236818
author: "@TheAhmadOsman"
date: 2026-04-26
type: x-article
tweet_id: "2048234466519236818"
---

# @TheAhmadOsman — Kernels Are What You Actually Run

**@TheAhmadOsman** — Sun Apr 26 02:55:25 +0000 2026

---

You don't "run a model"
You run **Kernels**

The model is just a graph

The **Inference Engine** is scheduler / optimizer / executor

But the actual work? That happens in the **Kernels**

- MatMul Kernels
- Attention Kernels
- RMSNorm Kernels
- KV cache Kernels
- Quantized linear Kernels
- Sampling Kernels
- Fused "please don't write this back to memory 9 times" Kernels

**Same model, same GPU, same VRAM**
**Wildly different performance**

Because one stack is using optimized fused Kernels that understand your hardware

And the other stack is playing hot potato with tensors through 47 tiny launches and pretending the GPU is the problem

**Bad Kernels make people say:**
"this model is slow"

**Good Kernels make people say:**
"wait how is this running locally?"

---

This is why Inference Engines and the Kernels implemented within them matter

The model is the recipe
The hardware is the kitchen
The Kernels are the knives, pans, burners, and the chef not cutting onions with a spoon

Most people benchmark models
The real ones benchmark the Kernels underneath

---

Image: ![[HGzKSSraQAElKQ7.jpg]]
