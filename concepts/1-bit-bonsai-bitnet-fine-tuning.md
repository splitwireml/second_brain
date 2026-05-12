---
title: 1-bit Bonsai & BitNet b1.58 Fine-Tuning on RTX 40 Series
created: 2026-04-01
updated: 2026-04-01
type: concept
tags: [model, training, quantization]
sources: [raw/articles/x-bookmarks-2026.md]
---

     1|# 1-bit Bonsai & BitNet b1.58 Fine-Tuning on RTX 40 Series — Research Report
     2|
     3|> **Date:** 2026-04-01
     4|> **Tags:** #research #1-bit-LLM #BitNet #Bonsai #fine-tuning #RTX-40-series #quantization #CUDA
     7|---
     8|
     9|## Overview
    10|
    11|This report covers the landscape of fine-tuning 1-bit large language models — specifically the **BitNet b1.58** architecture (ternary weights: {-1, 0, +1}) and the **PrismML Bonsai** models — on consumer NVIDIA RTX 40 series GPUs (RTX 4090, RTX 4080, RTX 4070 Ti, etc.) running Linux with CUDA. It covers the two distinct model families, their memory requirements, available frameworks, step-by-step pipelines, benchmarks, and current limitations.
    12|
    13|---
    14|
    15|## Research Questions
    16|
    17|1. What are 1-bit bonsai/BitNet b1.58 models, and how does the architecture work?
    18|2. What are the VRAM/VRAM requirements for fine-tuning on RTX 40xx GPUs?
    19|3. What tools and frameworks support fine-tuning 1-bit models on consumer GPUs?
    20|4. What does the end-to-end fine-tuning pipeline look like on Linux + CUDA?
    21|5. What are the current limitations, gotchas, and open questions?
    22|
    23|---
    24|
    25|## 1. The Two 1-bit Model Families
    26|
    27|There are two distinct approaches to 1-bit LLMs currently in circulation:
    28|
    29|### A. Microsoft BitNet b1.58
    30|
    31|- **Architecture:** Standard Transformer with `BitLinear` layers replacing `nn.Linear`
    32|- **Weight scheme:** Ternary / 1.58 bits per weight — values constrained to {-1, 0, +1}
    33|- **Quantization method:** Quantization-Aware Training (QAT) — trained from scratch with 1-bit weights, not post-trained
    34|- **How it works:** Weights are quantized via `absmax` scaling then rounded to nearest integer in {-1, 0, +1}. Activations use 8-bit quantization. Matrix multiplication becomes **integer addition** (no floating-point multiplication on weights), giving massive efficiency gains
    35|- **Key property:** Full-precision shadow weights are maintained during training for gradient updates; only the forward pass uses ternary weights (Straight-Through Estimator for backward pass)
    36|- **Inference:** Custom CUDA kernels (BitNet team) or `bitnet.cpp` (CPU). CuBLAS does not natively support W1.58A8 mixed-precision matmul, so custom kernels are needed
    37|- **Pre-quantized checkpoints:** Microsoft and TII-UAE Falcon-Edge have released pre-quantized BitNet-compatible checkpoints on Hugging Face (e.g., `tiiuae/Falcon-E-1B-Base` at revision `prequantized`)
    38|
    39|### B. PrismML Bonsai
    40|
    41|- **Architecture:** Based on Qwen3-8B dense architecture — GQA (32 query / 8 KV heads), SwiGLU MLP, RoPE, RMSNorm
    42|- **Weight scheme:** Pure binary (1-bit), not ternary — weights are {0, 1} mapped to {-scale, +scale} with group size 128 (g128). Effectively ~1 bit per weight
    43|- **Quantization method:** Proprietary Caltech IP — not fully open-sourced; claims end-to-end 1-bit across embeddings, attention projections, MLP projections, and LM head
    44|- **Released sizes:** 0.2B, 0.4B, 1.7B, 4B, 8B (8.19B total / ~6.95B non-embedding parameters)
    45|- **Memory footprint:** 1.15 GB for 8B model (vs 16.38 GB FP16) — 14x smaller
    46|- **Inference speed on RTX 4090:** 440 tokens/sec (token generation) via llama.cpp CUDA fork — **6.2x faster** than FP16 Qwen3-8B on the same GPU
    47|- **Energy efficiency:** 0.276 mWh/tok vs 1.134 mWh/tok FP16 — 4.1x lower on RTX 4090 CUDA
    48|- **License:** Apache 2.0
    49|- **Training:** Google v4 TPUs for pretraining; no fine-tuning pipeline released by PrismML yet
    50|
    51|### Key Distinction
    52|
    53|| Property | BitNet b1.58 | Bonsai (PrismML) |
    54||---|---|---|
    55|| Bits per weight | 1.58 (ternary: -1, 0, +1) | 1.0 (binary: 0 or 1) |
    56|| Architecture origin | Custom BitNet (Microsoft) | Qwen3-8B (dense Transformer) |
    57|| Training method | QAT from scratch | Proprietary compression |
    58|| Open-source | Mostly open (checkpoints) | Weights open, method closed |
    59|| Inference stack | bitnet.cpp, llama.cpp (TQ1_0/TQ2_0 formats) | llama.cpp fork, MLX fork |
    60|| Fine-tuning support | Yes (via `onebitllms`, QVAC Fabric) | Limited / not yet released |
    61|| Fine-tuneable today | Yes | Partially (architectural details unclear) |
    62|
    63|---
    64|
    65|## 2. VRAM Requirements for Fine-tuning on RTX 40 Series
    66|
    67|### Memory Breakdown by Model Family
    68|
    69|**BitNet b1.58 (TII-UAE Falcon-Edge 1B example):**
    70|| Format | VRAM for 1B model | Notes |
    71||---|---|---|
    72|| BF16 (full) | ~7 GB | Not practical |
    73|| TQ2_0 (~2 bits) | ~1.9 GB | llama.cpp format |
    74|| TQ1_0 (~1.6 bits) | ~1.0 GB | Most compressed |
    75|
    76|**PrismML Bonsai 8B:**
    77|| Format | Memory Footprint | Fits in RTX 4090? |
    78||---|---|---|
    79|| FP16 (16-bit) | 16.38 GB | Yes (24GB total) |
    80|| Bonsai 1-bit | 1.15 GB | Yes — trivially small |
    81|
    82|**RTX 40 Series VRAM Landscape:**
    83|| GPU | VRAM |适合的任务 |
    84||---|---|---|
    85|| RTX 4090 | 24 GB GDDR6X | Best consumer option — fits 8B at FP16 or Bonsai 8B + fine-tuning |
    86|| RTX 4080 Super | 16 GB GDDR6X | Bonsai 8B fine-tuning OK; 8B FP16 tight |
    87|| RTX 4070 Ti | 12 GB GDDR6X | Bonsai 8B fine-tuning OK; 8B FP16 OOM |
    88|| RTX 4080 | 12 GB GDDR6X | Same as 4070 Ti |
    89|| RTX 4070 | 12 GB GDDR6X | Bonsai 4B comfortable, 8B tight |
    90|| RTX 4060 Ti 16GB | 16 GB | Bonsai 8B OK; QLoRA 7B possible |
    91|
    92|### Fine-tuning Method Comparison (7B class models)
    93|
    94|| Method | VRAM Needed | RTX 4090 Feasible? |
    95||---|---|---|
    96|| Full FP16 fine-tuning | 60–120 GB | No |
    97|| LoRA (BF16) | 16–28 GB | Yes (24GB, tight) |
    98|| QLoRA (4-bit NF4) | 6–10 GB | Yes — comfortable |
    99|| BitNet b1.58 fine-tuning | ~1–3 GB (1B–3B) | Yes — very comfortable |
   100|| Bonsai 1-bit fine-tuning | ~1.5–3 GB (est.) | Yes — very comfortable |
   101|
   102|### Key Insight on BitNet Memory Efficiency
   103|
   104|BitNet b1.58 uses ~4x less VRAM than FP16 equivalents because:
   105|1. Ternary weights are packed 16 weights per byte
   106|2. Activations use 8-bit quantization (INT8)
   107|3. Forward pass = integer addition only (no FP multiply)
   108|4. Gradient computation still happens on shadow weights (BF16), but these are small overhead
   109|
   110|---
   111|
   112|## 3. Available Frameworks & Tools for Fine-tuning
   113|
   114|### A. `onebitllms` (TII-UAE / Falcon-Edge)
   115|
   116|The primary open-source tool for fine-tuning BitNet b1.58 models.
   117|
   118|**What it does:**
   119|- Converts pre-quantized BitNet checkpoints to training format
   120|- Replaces `nn.Linear` with `BitNetLinear` custom layers
   121|- Post-training quantization to 1-bit
   122|- Optional conversion back to BF16 for validation
   123|
   124|**Installation:**
   125|```bash
   126|pip install onebitllms
   127|# or from source:
   128|pip install git+https://github.com/tiiuae/onebitllms.git
   129|```
   130|
   131|**Requirements:**
   132|- NVIDIA CUDA-compiled GPU
   133|- `trl` library (Hugging Face's training wrapper)
   134|- Pre-quantized checkpoint (e.g., `tiiuae/Falcon-E-1B-Base` revision `prequantized`)
   135|- Triton for optimized quantization kernels
   136|
   137|**Limitations:**
   138|- Only full fine-tuning supported at present (no PEFT/LoRA built-in as of late 2025)
   139|- Falcon-Edge team notes LoRA support for BitNet is an "open question" for upcoming releases
   140|
   141|**Fine-tuning example:**
   142|```python
   143|import torch
   144|from transformers import AutoModelForCausalLM, AutoTokenizer
   145|from trl import SFTTrainer
   146|from onebitllms import replace_linear_with_bitnet_linear, quantize_to_1bit
   147|
   148|model_id = "tiiuae/Falcon-E-1B-Base"
   149|model = AutoModelForCausalLM.from_pretrained(
   150|    model_id,
   151|    torch_dtype=torch.bfloat16,
   152|    revision="prequantized"
   153|)
   154|model = replace_linear_with_bitnet_linear(model)
   155|
   156|trainer = SFTTrainer(
   157|    model=model,
   158|    train_dataset=train_dataset,
   159|    args=TrainingArguments(
   160|        per_device_train_batch_size=1,
   161|        learning_rate=1e-4,
   162|        output_dir="./output",
   163|        gradient_accumulation_steps=16,
   164|    ),
   165|)
   166|trainer.train()
   167|
   168|# Quantize to 1-bit for deployment
   169|quantize_to_1bit("./output", "./output-1bit")
   170|```
   171|
   172|**Training hardware reported:** 8xA10G 23GB instance (~8.5 hours for Falcon-1B Capybara fine-tune)
   173|
   174|---
   175|
   176|### B. QVAC Fabric (Tether) — LoRA for BitNet b1.58
   177|
   178|**Released March 2026** — first cross-platform LoRA fine-tuning for BitNet b1.58 on heterogeneous GPUs.
   179|
   180|**What it does:**
   181|- Builds on llama.cpp with custom Vulkan backend for GPU inference + fine-tuning
   182|- Supports **LoRA adapters** on top of frozen BitNet base weights
   183|- Multi-platform: NVIDIA (CUDA/Vulkan), AMD, Apple Silicon, mobile GPUs (Adreno, Mali, Apple Bionic)
   184|- llama.cpp fork with TQ1_0 and TQ2_0 BitNet weight formats
   185|- Fine-tuning on **Samsung S25 (Adreno GPU), iPhone 16 (Apple Bionic), Pixel 9 (Mali GPU)**
   186|
   187|**Memory benchmarks (BitNet-1B TQ1_0):**
   188|- 77.8% less VRAM than Gemma-3-1B FP16
   189|- 65.6% less VRAM than Qwen3-0.6B FP16
   190|- 125M parameter model fine-tunes in ~10 minutes on Samsung S25
   191|
   192|**VRAM for LoRA fine-tuning BitNet 1B on consumer GPUs (TQ1_0 format):**
   193|- Estimated: **~600–800 MB** — extremely low
   194|
   195|**Multi-platform binaries:** Released on Hugging Face — search `qvac` org for `fabric-llm-bitnet` repositories.
   196|
   197|---
   198|
   199|### C. BitLoRA (Academic — ScienceDirect 2026)
   200|
   201|**"BitLoRA: Quantization-Compatible Adapter Tuning for 1.58-bit LLM in Federated On-Device AI-Agent"** — published May 2026 in Expert Systems with Applications.
   202|
   203|- Novel PEFT framework designed specifically for 1.58-bit BitLinear layers
   204|- Adapts LoRA architecture to be quantization-compatible (standard LoRA is incompatible with BitNet because LoRA uses FP16 computations while BitNet uses INT8)
   205|- Integrates into Hugging Face PEFT
   206|- Cuts GPU memory by **>85%** vs standard fine-tuning while maintaining accuracy
   207|- Designed for federated on-device learning scenarios
   208|
   209|---
   210|
   211|### D. PrismML Bonsai Fine-tuning
   212|
   213|As of April 2026, **no dedicated fine-tuning pipeline has been released by PrismML**. However:
   214|
   215|- The model architecture (Qwen3-8B) is a standard dense Transformer — standard LoRA/QLoRA applies to the **FP16 base** before 1-bit compression
   216|- Fine-tuning would happen **before** the proprietary 1-bit compression step
   217|- The community is awaiting the release of the compression pipeline or pre-compression checkpoints
   218|- For inference and deployment: use the PrismML llama.cpp fork with CUDA support
   219|
   220|**Build and run Bonsai 8B on RTX 4090 (llama.cpp CUDA):**
   221|```bash
   222|git clone https://github.com/prism-ml/llama.cpp  # PrismML fork
   223|cd llama.cpp
   224|cmake -B build -DGGML_CUDA=ON
   225|cmake --build build -j
   226|
   227|# Download model
   228|huggingface-cli download prism-ml/Bonsai-8B-gguf \
   229|  --local-dir models/bonsai-8b
   230|
   231|# Run inference
   232|./build/bin/llama-cli \
   233|  -m models/bonsai-8b/Bonsai-8B-Q1_0_g128.gguf \
   234|  -p "You are a helpful assistant" \
   235|  -cnv
   236|```
   237|
   238|**Build with CUDA optimizations for RTX 40 series (Ada Lovelace, sm_89):**
   239|```bash
   240|cmake -B build \
   241|  -DGGML_CUDA=ON \
   242|  -DGGML_CUDA_F16=ON \
   243|  -DCMAKE_CUDA_ARCHITECTURES=89 \
   244|  -DLLAMA_CURL=ON
   245|cmake --build build -j$(nproc)
   246|```
   247|
   248|RTX 4090 = Ada Lovelace architecture → CUDA compute capability **8.9 (sm_89)**
   249|RTX 4070 Ti = Ada Lovelace → **sm_89**
   250|
   251|---
   252|
   253|### E. Standard QLoRA (for comparison / if BitNet not available)
   254|
   255|If fine-tuning a standard 8B model on RTX 4090:
   256|
   257|```bash
   258|pip install unsloth  # Recommended for RTX 40 series — 2x faster, 30% less VRAM
   259|```
   260|
   261|```python
   262|from unsloth import FastLanguageModel
   263|
   264|model, tokenizer = FastLanguageModel.from_pretrained(
   265|    model_name="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
   266|    max_seq_length=4096,
   267|    dtype=None,
   268|    load_in_4bit=True,
   269|)
   270|
   271|model = FastLanguageModel.get_peft_model(
   272|    model,
   273|    r=16,
   274|    lora_alpha=32,
   275|    lora_dropout=0.05,
   276|    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
   277|                    "gate_proj", "up_proj", "down_proj"],
   278|)
   279|
   280|# Train with standard Hugging Face trainer
   281|```
   282|
   283|**RTX 4090 VRAM usage with Unsloth QLoRA:** ~6–8 GB for 7B model
   284|
   285|---
   286|
   287|## 4. End-to-End Fine-tuning Pipeline on Linux + RTX 40 Series
   288|
   289|### Pipeline A: BitNet b1.58 via `onebitllms` + `trl`
   290|
   291|**Prerequisites:**
   292|```bash
   293|# Environment setup
   294|conda create -n bitnet python=3.10
   295|conda activate bitnet
   296|pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   297|pip install transformers trl peft datasets accelerate
   298|pip install onebitllms
   299|pip install bitsandbytes  # For related quantization work
   300|```
   301|
   302|**Step 1 — Get pre-quantized checkpoint:**
   303|```bash
   304|huggingface-cli download tiiuae/Falcon-E-1B-Base \
   305|  --local-dir ./models/Falcon-E-1B-Base \
   306|  --revision prequantized
   307|```
   308|
   309|**Step 2 — Prepare dataset:**
   310|```python
   311|from datasets import load_dataset
   312|
   313|dataset = load_dataset("trl-lib/Capybara", split="train")
   314|# Format for causal LM:
   315|def format_prompt(example):
   316|    return {"text": f"### User:\n{example['conversations'][0]['content']}\n\n### Assistant:\n{example['conversations'][1]['content']}"}
   317|
   318|dataset = dataset.map(format_prompt)
   319|```
   320|
   321|**Step 3 — Replace linear layers with BitNetLinear:**
   322|```python
   323|from onebitllms import replace_linear_with_bitnet_linear
   324|model = replace_linear_with_bitnet_linear(model)
   325|```
   326|
   327|**Step 4 — Configure and run training:**
   328|```python
   329|from trl import SFTTrainer
   330|from transformers import TrainingArguments
   331|
   332|trainer = SFTTrainer(
   333|    model=model,
   334|    train_dataset=dataset,
   335|    dataset_text_field="text",
   336|    args=TrainingArguments(
   337|        output_dir="./falcon-bitnet-output",
   338|        per_device_train_batch_size=1,
   339|        gradient_accumulation_steps=16,
   340|        learning_rate=1e-4,
   341|        num_train_epochs=3,
   342|        logging_steps=1,
   343|        save_strategy="steps",
   344|        save_steps=100,
   345|        bf16=True,
   346|    ),
   347|)
   348|trainer.train()
   349|```
   350|
   351|**Step 5 — Quantize for inference:**
   352|```python
   353|from onebitllms import quantize_to_1bit
   354|quantize_to_1bit("./falcon-bitnet-output", "./falcon-bitnet-1bit")
   355|```
   356|
   357|**Step 6 — Deploy with bitnet.cpp:**
   358|```bash
   359|# Build bitnet.cpp
   360|git clone --recursive https://github.com/microsoft/BitNet.git
   361|cd BitNet
   362|mkdir build && cd build
   363|cmake .. -DCMAKE_BUILD_TYPE=Release
   364|cmake --build .
   365|
   366|# Run inference
   367|python run_inference.py \
   368|  -m ./falcon-bitnet-1bit/ggml-model-i2_s.gguf \
   369|  -p "Explain quantum computing" \
   370|  -cnv
   371|```
   372|
   373|---
   374|
   375|### Pipeline B: Bonsai 8B — Standard LoRA Before Proprietary Compression
   376|
   377|**Note: This is the current workaround since PrismML hasn't released a dedicated fine-tuning tool.**
   378|
   379|**Step 1 — Install Unsloth:**
   380|```bash
   381|pip install unsloth
   382|```
   383|
   384|**Step 2 — Load base model (Qwen3-8B) for LoRA fine-tuning:**
   385|```python
   386|from unsloth import FastLanguageModel
   387|
   388|model, tokenizer = FastLanguageModel.from_pretrained(
   389|    model_name="unsloth/Qwen3-8B-bnb-4bit",  # Qwen3 8B base in 4-bit
   390|    max_seq_length=4096,
   391|    load_in_4bit=True,
   392|)
   393|
   394|model = FastLanguageModel.get_peft_model(model, r=16, lora_alpha=32)
   395|```
   396|
   397|**Step 3 — Fine-tune:**
   398|```python
   399|from trl import SFTTrainer
   400|
   401|trainer = SFTTrainer(
   402|    model=model,
   403|    train_dataset=formatted_dataset,
   404|    dataset_text_field="text",
   405|    args=TrainingArguments(
   406|        output_dir="./bonsai-lora-output",
   407|        per_device_train_batch_size=4,
   408|        learning_rate=2e-4,
   409|        num_train_epochs=3,
   410|        bf16=True,
   411|    ),
   412|)
   413|trainer.train()
   414|
   415|model.save_pretrained("./bonsai-lora-adapter")
   416|```
   417|
   418|**Step 4 — Wait for PrismML's compression tool** (not yet released) or use the LoRA adapter with standard inference.
   419|
   420|---
   421|
   422|### RTX 40 Series CUDA Configuration
   423|
   424|**CUDA architecture flag:**
   425|```bash
   426|# RTX 40 series = Ada Lovelace = sm_89
   427|-DCMAKE_CUDA_ARCHITECTURES=89
   428|```
   429|
   430|**For CUDA 12.x + PyTorch:**
   431|```bash
   432|pip install torch torchvision torchaudio \
   433|  --index-url https://download.pytorch.org/whl/cu121
   434|```
   435|
   436|**Verify CUDA:**
   437|```python
   438|import torch
   439|print(f"CUDA available: {torch.cuda.is_available()}")
   440|print(f"GPU: {torch.cuda.get_device_name(0)}")
   441|print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
   442|```
   443|
   444|---
   445|
   446|## 5. Performance Benchmarks
   447|
   448|### Bonsai 8B Throughput (RTX 4090, llama.cpp CUDA)
   449|
   450|| Format | Token Gen Speed | FP16 Baseline | Speedup |
   451||---|---|---|---|
   452|| Bonsai 1-bit (Q1_0_g128) | 368 tok/s | — | — |
   453|| FP16 Qwen3-8B | 59 tok/s | 59 tok/s | 1.0x |
   454|| Bonsai 1-bit (TG128) | 368 tok/s | 59 tok/s | **6.2x** |
   455|| Bonsai 1-bit (PP512) | 11,809 tok/s | 10,453 tok/s | 1.13x |
   456|
   457|*TG = token generation (single token), PP512 = prompt processing 512 tokens*
   458|
   459|### Bonsai 8B vs Full-Precision 8B Benchmarks (EvalScope on H100)
   460|
   461|| Model | Avg Score | MMLU-R | GSM8K | HumanEval+ | IFEval |
   462||---|---|---|---|---|---|
   463|| Qwen 3 8B (FP16, 16 GB) | 79.3 | 83 | 93 | 82.3 | 84.2 |
   464|| RNJ 8B (FP16, 16 GB) | 73.1 | 75.5 | 93.7 | 84.2 | 73.8 |
   465|| Mistral3 8B (FP16, 16 GB) | 71.0 | 73.9 | 87.2 | 67.4 | 75.4 |
   466|| **Bonsai 8B (1-bit, 1.15 GB)** | **70.5** | **65.7** | **88** | **73.8** | **79.8** |
   467|
   468|Bonsai 8B (1.15 GB) performs comparably to full-precision 8B models (16 GB) at **14x smaller size**, matching or exceeding on GSM8K and IFEval.
   469|
   470|### BitNet b1.58 VRAM vs FP16 Comparisons
   471|
   472|| Model | BitNet-1B (TQ1_0) | Gemma-3-1B (FP16) | Savings |
   473||---|---|---|---|
   474|| VRAM | ~614 MB | ~1,536 MB | **77.8% less** |
   475|
   476|| Model | BitNet-13B (TQ1_0) | Qwen3-4B (Q4) | Comparison |
   477||---|---|---|---|
   478|| Parameters | 13B | 4B | 3x larger model |
   479|| VRAM | 2,789 MB | ~4,000 MB (Q4 est.) | **29% less memory** |
   480|
   481|### Energy Efficiency (RTX 4090 CUDA)
   482|
   483|| Model | Energy per Token | vs FP16 Baseline |
   484||---|---|---|
   485|| Bonsai 8B | 0.276 mWh/tok | 4.1x lower |
   486|| FP16 Qwen3-8B | 1.134 mWh/tok | baseline |
   487|
   488|---
   489|
   490|## 6. Architecture Deep Dive: How BitLinear Works
   491|
   492|The `BitLinear` layer is the core building block of BitNet b1.58:
## Key References

See [[llm-server-throughput-optimization]] for inference optimization context, and [[vibe-kanban-agent-spawning]] for how BitNet-quantized models can run on consumer hardware in agent workflows.

