---
title: "03 - Weights, Parameters, and What the Model Learned"
source: "x-bookmarks"
tweet_id: "2055000311803371740"
tweet_url: "https://x.com/NeoAIForecast/status/2055000311803371740"
author_name: "Neo"
author_handle: "@NeoAIForecast"
tweet_date: "Thu May 14 19:00:29 +0000 2026"
bookmark_date: "2026-05-14"
content_type: "x_article"
character_count: 15284
retweet_count: 3
like_count: 22
ingested: 2026-05-19
sha256: ab3f8c3d9e2f4a1b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b
---

# 03 - Weights, Parameters, and What the Model Learned

03 - Weights, Parameters, and What the Model Learned

Previous Article - [02 - Tokens, Tokenizers, and Context Windows](https://x.com/NeoAIForecast/status/2054674887017628012?s=20)

A language model is not a database of facts.

It does not have a neat little table that says:

- Paris = capital of France
- Python = programming language
- llama.cpp = local inference engine

Instead, an LLM is mostly a huge collection of learned numbers.

Those numbers are called parameters.

And if you want to understand why local models need so much memory, why bigger models often feel smarter, and why a model can be impressive but still confidently wrong, you need this mental model:

> A model's weights do not store facts like files. They shape patterns of prediction.

That is what this article explains.

## What you'll learn

By the end, you'll understand:

- What parameters are
- What weights do inside a model
- How training changes those weights
- Why models learn patterns, not clean databases
- Why parameter count matters, but does not guarantee quality
- Why local model size affects memory, speed, and capability

This is the bridge between "the model predicts the next token" and "the model somehow learned language."

Let's demystify it.

## Parameters are learned numbers

When people say a model has 7 billion parameters, they mean the model contains roughly 7 billion learned numerical values.

A parameter is not a word.  It is not a sentence. It is not a fact.

It is a number the model uses while processing tokens.

During inference, your prompt is converted into tokens, those tokens flow through the model, and the parameters help determine what the model predicts next.

A simplified way to think about it:

```plaintext
input tokens
   ↓
model layers
   ↓
learned parameters shape the signal
   ↓
next-token prediction

```

The model's behavior comes from how all these numbers interact.

Not one number.

Not one layer.

Not one "fact cell."

The intelligence is distributed across billions of values.

Takeaway: A parameter is a learned number that helps shape the model's prediction, not a stored fact or memory entry.

## Weights shape how signals flow

You will often hear people use weights and parameters almost interchangeably.

Technically, a weight is a type of parameter. In everyday LLM discussion, "weights" usually means the learned numerical values of the model.

So what do weights do?

They control how strongly one signal influences another.

Imagine the model is processing this sentence:

```plaintext
The capital of France is

```

The model does not look up a row in a database called countries.csv

Instead, the tokens move through many layers of computation. At each stage, weights affect which patterns become stronger and which become weaker.

Signals related to:

- geography
- capitals
- France
- common text patterns
- factual associations
- grammar
- likely completions

All interact.

By the end, the model assigns scores to possible next tokens.

A well-trained model should give a high score to:

```plaintext
Paris

```

But that prediction emerges from patterns in weights, not from a clean lookup table.

Takeaway: Weights are the learned values that guide how token information flows through the model.

## Training adjusts weights through prediction error

So where do these weights come from?

They are learned during training.

At a high level, training works like this:

1. Show the model a sequence of tokens.
2. Ask it to predict the next token.
3. Compare its prediction to the real next token.
4. Measure how wrong it was.
5. Adjust the weights slightly.
6. Repeat this across massive amounts of text.

Example

```plaintext
Training text:
The capital of France is Paris.

Input:
The capital of France is

Correct next token:
Paris

```

Early in training, the model may predict something bad or random.

After many examples, the model gradually adjusts its weights so that better predictions become more likely.

This happens again and again across huge datasets.

The model sees grammar, code, facts, styles, reasoning patterns, formatting patterns, question-answer pairs, and many other structures.

Over time, the weights become a compressed statistical representation of patterns in that data.

Takeaway: Training teaches the model by repeatedly adjusting weights to reduce prediction error.

## The model learns patterns, not a clean fact table

This is one of the most important ideas in the whole series:

> An LLM does not store knowledge the way a database stores knowledge.

A database might store:

```plaintext
country: France
capital: Paris

```

An LLM stores distributed patterns across weights.

That means its "knowledge" is fuzzier.

It can often answer factual questions because the training process shaped its weights around repeated patterns in text.

But it can also:

- mix up similar facts
- invent plausible-sounding answers
- overgeneralize from patterns
- fail on rare details
- answer differently depending on wording
- know something in one format but fail in another

This is why models can feel both brilliant and unreliable.

They are powerful pattern engines, not perfect fact retrieval systems.

If a model saw many examples connecting "France" and "Paris," it may learn that association strongly.

If it saw sparse, contradictory, outdated, or low-quality information, the association may be weaker or distorted.

Takeaway: Model knowledge is statistical and distributed, not a clean collection of verified facts.

## "What the model learned" means "what shaped its predictions"

When we say a model "learned" something, we do not mean it understands in the human sense.

We mean training changed the weights so the model is more likely to produce certain useful outputs in certain contexts.

For example, a model may learn:

- grammar patterns
- code syntax
- common facts
- writing styles
- reasoning templates
- instruction-following behavior
- conversation structure
- mathematical procedures
- associations between concepts

But all of this is reflected in prediction behavior.

The model learned enough about Python syntax if it can complete Python code well.

It learned enough about emails if it can draft plausible emails.

It learned enough about explanations if it can produce coherent teaching sequences.

This is why evaluation matters. You do not inspect a model and ask, "Where is the Python knowledge stored?"

You test behavior:

- Does it write correct code?
- Does it follow instructions?
- Does it reason through a problem?
- Does it stay consistent?
- Does it know when it is uncertain?

Takeaway: A model's learning shows up as behaviour, especially better next-token predictions in useful contexts.

## Bigger parameter counts can help

Parameter count matters because parameters are the model's capacity.

More parameters usually give the model more room to represent patterns.

That can help with:

- broader knowledge
- better instruction following
- stronger reasoning
- more nuanced writing
- better coding ability
- improved multilingual performance
- fewer shallow mistakes

This is why, all else equal, a 70B model often feels more capable than a 7B model.

It has far more learned numerical structure to work with.

But "all else equal" is doing a lot of work.

In the real world, all else is rarely equal.

Takeaway: More parameters can increase model capacity, which often improves capability, but parameter count is only one part of quality.

## Bigger does not always mean better

A larger model is not automatically better for every use case.

Model quality also depends on:

- training data quality
- training data mix
- architecture
- tokenizer
- context length
- post-training
- instruction tuning
- alignment choices
- coding data
- reasoning data
- tool-use data
- domain-specific data

A well-trained 8B model can outperform a weak 13B model.

A specialized coding model can beat a larger general model on coding tasks.

A newer small model can feel better than an older larger model because its training recipe improved.

This is why local LLM users should avoid judging models by parameter count alone. Parameter count tells you size.

It does not fully tell you intelligence, usefulness, style, accuracy, or fit for your task.

Takeaway: Parameter count is a useful signal, not a complete quality score.

## Local model size affects memory

For local LLMs, weights are not abstract. You have to load them into memory.

That memory may be:

- GPU VRAM
- system RAM
- Apple unified memory
- a mix of CPU and GPU memory, depending on your setup

A bigger model has more parameters.

More parameters means more numbers to store.

More numbers means more memory required.

This is why a 70B model is much harder to run locally than a 7B model.

A rough mental model:

```plaintext
more parameters
   ↓
more weights to store
   ↓
more memory required
   ↓
harder to run locally

```

This is also why quantization matters later.

Quantization reduces how much memory each weight needs. But for this article, keep the simple idea:

> Local inference requires loading the model's learned weights somewhere your hardware can access them.

Takeaway: Model size directly affects whether a model fits on your hardware.

## Local model size affects speed

Model size also affects speed.

During inference, the model uses its weights to process the current token sequence and predict the next token.

Bigger models generally require more computation per generated token.

That means:

- slower token generation
- more memory bandwidth pressure
- more heat and power draw
- longer waits for large responses
- greater benefit from strong GPUs or optimized runtimes

This is why local model choice is always a tradeoff.

You are balancing:

- capability
- memory fit
- generation speed
- latency
- context length
- hardware limits

A smaller model may be less capable, but fast enough to feel interactive.

A larger model may answer better, but only if your hardware can run it at an acceptable speed.

Takeaway: Bigger models usually cost more memory and compute per token, which affects local speed.

## The core misconception: "the model contains facts"

Beginners often imagine model weights like a giant compressed encyclopedia.

That is understandable, but incomplete.

A better mental model:

```plaintext
Bad mental model:
Model = database of facts

Better mental model:
Model = learned prediction system shaped by patterns in data

```

This explains several weird behaviors:

Why can a model answer factual questions?

Because training shaped the weights around many factual text patterns.

Why can it hallucinate?

Because it predicts plausible continuations, even when it lacks reliable grounding.

Why can wording change the answer?

Because different prompts activate different learned patterns.

Why can it know old information but miss new information?

Because weights only reflect training and post-training data, not live updates.

Why does local matter?

Because when you run the model locally, you are running those learned weights on your own hardware.

Takeaway: The model is not retrieving perfect truth. It is generating likely continuations from learned patterns.

## Save-worthy framework: The 5-part weights mental model

Use this whenever you see a model name like "Llama 3.3 70B" or "Qwen3.6-27B"

1. Parameters are learned numbers

They are the model's adjustable values.

2. Weights shape computation

They influence how token signals flow through the network.

3. Training changes weights

The model improves by reducing prediction error across huge datasets.

4. Knowledge is distributed

Facts and skills are represented as statistical patterns, not clean database rows.

5. Size creates tradeoffs

More parameters can improve capability, but increase memory and compute needs.

Short version:

```plaintext
parameters = learned numbers
weights = signal-shaping values
training = weight adjustment
knowledge = distributed patterns
local size = memory + speed tradeoff

```

Takeaway: If you understand these five points, parameter counts stop being mysterious marketing numbers.

## Common mistakes beginners make

Mistake 1: Thinking parameters are facts

A 7B model does not contain 7 billion facts. It contains roughly 7 billion learned numerical values. Those values help produce behavior.

Takeaway: Parameters are not facts. They are learned numbers.

Mistake 2: Assuming bigger always means smarter

A bigger model often has more capacity, but quality depends on training. A great small model can beat a mediocre larger model for certain tasks.

Takeaway: Size matters, but training quality and task fit matter too.

Mistake 3: Ignoring memory requirements

Local LLMs must fit on your hardware. If the model is too large, it may not load, or it may run slowly through CPU offloading.

Takeaway: Parameter count is also a hardware requirement signal.

Mistake 4: Treating hallucination as a random bug

Hallucination is deeply connected to how LLMs work. They generate likely text from learned patterns. If they lack grounding, they may still produce confident-sounding answers.

Takeaway: Hallucination is a predictable failure mode of pattern-based generation.

Mistake 5: Confusing learned weights with chat memory

Weights are learned during training.  Chat history is active context.  KV cache helps reuse computation during a session. Long-term memory, if present, is usually an external system.

These are not the same thing.

Takeaway: Learned weights, context, cache, and memory are separate concepts.

## Practical next step

Open the model card for any local model you are interested in.

Look for:

- parameter count, such as 7B, 8B, 14B, 32B, 70B
- architecture family
- context length
- intended use, such as chat, instruct, code, math
- training or post-training notes
- license
- available file formats

Then ask:

```plaintext
What does this model size imply for my hardware?
What was this model trained or tuned to be good at?
Is this parameter count enough for my task?
Is there a smaller model that may be faster and good enough?

```

Do not pick models by size alone.

Pick them by fit.

Takeaway: Parameter count should start your model evaluation, not end it.

## Final thought

Weights are the learned structure inside the model.

They are why the model can write, code, explain, translate, summarize, and reason at all.

But they are not magic.

They are learned numbers shaped by training, compressed into a model file, loaded onto your hardware, and used one token at a time during inference.

Once you understand that, local LLMs become much less mysterious.

You stop asking:

> "Where does the model store the answer?"

And start asking:

> "What patterns did training shape into this model, and can my hardware run them well?"

That is the right mental model.

In the next article, we'll zoom out from weights and ask:

04 - What a Model Actually Includes

Because when you download a local LLM, you are not just downloading "intelligence in a file."

You are dealing with architecture, weights, tokenizer, config, chat templates, licenses, and formats.

That is where local inference starts to become concrete.