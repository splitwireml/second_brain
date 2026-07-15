---
source_url: https://x.com/NeoAIForecast/status/2055347680147312810
ingested: 2026-05-19
sha256: a1b2c3d4e5f6
---

# 04 - What a Model Actually Includes

Previous Article - 0[3 - Weights, Parameters, and What the Model Learned](https://x.com/NeoAIForecast/status/2055000311803371740?s=20)

When beginners first download a local LLM, they usually focus on one thing:

The model size.

- 7B.

- 13B.

- 34B.

- 70B.

That number is not the whole model.

A working local model is more like a packaged machine. The weights are the largest and most famous part, but the runtime also needs to know:

- What architecture the weights belong to

- How text becomes tokens

- How many layers and dimensions the model has

- Which special tokens mean "user," "assistant," or "end"

- How chat messages should be formatted

- What license controls usage

- Which file format the runtime can actually load

In this article, we'll unpack what a model actually includes.

Takeaway: A model is not just learned numbers. It is a bundle of design, data, formatting rules, metadata, and legal permissions.

## What you'll learn

By the end, you'll understand:

- Why "model" does not mean one simple thing

- What architecture and weights do

- Why the tokenizer must match the model

- What config files and chat templates control

- Why licenses and file formats matter when running models locally

## Architecture: the model's design

The architecture is the design of the neural network. It defines the shape of the model before any learning happens.

For a local LLM, architecture includes things like:

- Number of layers

- Hidden size

- Attention heads

- Vocabulary size

- Context length support

- Transformer block design

- Activation functions

- Positional encoding method

You can think of architecture as the blueprint.

Two models can have the same parameter count but different architectures. They may behave differently, run differently, and require different runtime support.

For example, a runtime cannot load model weights correctly unless it understands the architecture those weights belong to.

The weights are not floating around independently. They are numbers attached to a specific structure.

Takeaway: Architecture is the shape of the machine. Weights only make sense inside that shape.

## Weights: the learned parameters

The weights are the learned numbers produced by training.

These are what people usually mean when they say:

"This is a 7B model."

A 7B model has roughly 7 billion learned parameters. A 70B model has roughly 70 billion.

Those parameters store statistical patterns learned during training:

- Language patterns

- Code patterns

- Reasoning patterns

- Factual associations

- Style patterns

- Translation patterns

- Instruction-following patterns, if tuned for that

But the weights are not a database.

There is no neat table inside the model that says:

- France = Paris

- Python = programming language

- HTTP 404 = not found

Instead, training adjusts billions of numbers so the model becomes better at predicting the next token across huge amounts of text.

This is why models can generalize, but also why they can hallucinate. They learned patterns. They did not store a perfectly verified fact sheet.

Takeaway: Weights are the learned behavior of the model, not a clean database of facts.

## Tokenizer: the text-to-token map

A model does not directly read text the way you do.

It reads tokens.

The tokenizer is the system that turns text into token IDs before the model sees it.

Example:

```plaintext
Local LLMs are useful.

```

The tokenizer may split that into chunks like:

```plaintext
Local | LL | Ms | are | useful | .

```

Or it may split it differently depending on the tokenizer. Each chunk maps to a number. The model sees those numbers, not the raw text.

This matters because the tokenizer and model are trained together.

If you use the wrong tokenizer, the model receives the wrong token IDs. That can damage quality or break the model completely.

The tokenizer also defines special tokens like:

- Beginning of text

- End of text

- User message marker

- Assistant message marker

- System message marker

- Padding token

- Unknown token, in some tokenizers

These special tokens tell the model where the prompt starts, where a message ends, and what role each piece of text is supposed to play.

Takeaway: The tokenizer is not optional. It is the model's text interface.

## Config: the model's instruction sheet

The config tells the runtime how the model is built.

It usually includes details like:

- Number of layers

- Hidden dimension size

- Attention head count

- Vocabulary size

- Maximum context length

- Tokenizer settings

- Special token IDs

- Architecture type

- Precision or dtype info

- Rope scaling or positional settings, when relevant

Without config, the runtime may not know how to correctly load the weights.

Imagine receiving a box of machine parts with no manual. The parts might all be there, but you still need to know how they fit together.

That is what config does.

It tells the runtime:

"This is the structure these weights belong to."

Takeaway: Config is the runtime's map for assembling and using the model correctly.

## Chat template: the conversation format

This is one of the most overlooked parts of local LLMs.

A chat template tells the runtime how to format messages before sending them to the model.

When you type into a chat app, you may see something simple:

```plaintext
User: Explain tokens.
Assistant:

```

But the model may expect a more specific format internally.

For example, an instruct model might expect messages to be wrapped with special markers like:

```plaintext
<|system|>
You are a helpful assistant.
<|user|>
Explain tokens.
<|assistant|>

```

Another model might expect a completely different format.

This matters because instruction-tuned models are trained on specific message structures.

If you use the wrong chat template, the model may:

- Ignore the system prompt

- Respond in the wrong style

- Continue the user message instead of answering

- Fail to stop properly

- Produce strange role markers

- Act less capable than it really is

This is why the same model can feel much better or worse depending on the runtime and template.

The weights did not change. The prompt formatting changed.

Takeaway: The chat template is the model's conversation grammar. If you format the conversation wrong, the model may behave wrong.

## License: what you are allowed to do

A local model is not just a technical artifact.

It also comes with a license.

The license tells you what you are allowed to do with the model.

Depending on the model, it may define rules around:

- Personal use

- Commercial use

- Redistribution

- Fine-tuning

- Hosting

- Derivative models

- Attribution

- Restricted use cases

This matters more than beginners realize.

Two models may both be downloadable. Both may run locally. Both may be open-weight. But they may not grant the same rights.

"Open-weight" means the weights are available.

It does not always mean "do anything you want."

Some models are permissive. Some are research-only. Some allow commercial use with restrictions. Some have custom licenses with specific terms.

If you are just experimenting locally, this may not matter much at first.

If you are building a product, publishing a fine-tune, or offering a hosted service, it matters a lot.

Takeaway: Local access is technical permission to run the model. The license defines legal permission to use it.

## Formats: how the model is packaged

The same underlying model can appear in different file formats.

Common examples include:

- safetensors

- GGUF

- runtime-specific packages

- framework-specific folders with config, tokenizer, and weight shards

At a high level:

Safetensors is common in the Hugging Face ecosystem. It stores tensors safely and efficiently, often used for training, fine-tuning, and framework-based inference.

GGUF is common for llama.cpp-style local inference. It packages model data and metadata in a format optimized for local runtimes, including quantized versions.

Runtime-specific packaging can bundle the model in the way a particular app expects, such as Ollama model packages or other local inference systems.

The format matters because your runtime needs to support it.

A Python framework might happily load safetensors.

llama.cpp usually wants GGUF.

A desktop app may hide the details but still depends on one of these formats underneath.

Takeaway: Format is the packaging layer. The best format depends on the runtime you plan to use.

## Why model files are often split

Sometimes a model download is not one file.

You may see many files:

```plaintext
config.json
tokenizer.json
tokenizer_config.json
special_tokens_map.json
model-00001-of-00004.safetensors
model-00002-of-00004.safetensors
model-00003-of-00004.safetensors
model-00004-of-00004.safetensors
generation_config.json
README.md
LICENSE

```

This is normal.

Large models are often split into shards because one giant file is harder to upload, download, store, and manage.

The runtime reads the index or config and knows how to assemble those shards into one model.

In GGUF workflows, you may instead download one file like:

```plaintext
model.Q4_K_M.gguf

```

That single file may contain weights, metadata, tokenizer information, and quantization details in one package.

This difference is why model downloads can look confusing at first.

A "model" might be:

- A folder with many files

- A few large weight shards plus configs

- One GGUF file

- A runtime-specific package name

- A hosted repo containing multiple variants

Takeaway: A model can be distributed as one file or many files. What matters is whether your runtime has all the pieces it needs.

## Save-worthy framework: the 7-part model checklist

Before running or choosing a local model, ask:

1. Architecture

- What model family is this?

- Does my runtime support it?

2. Weights

- How many parameters?

- What precision or quantization?

- Can my hardware fit it?

3. Tokenizer

- Is the tokenizer included?

- Does the runtime use the correct one?

4. Config

- Are context length, vocab size, and architecture settings included?

- Does the runtime understand them?

5. Chat template

- Is this a base model or instruct/chat model?

- Is the correct template applied?

6. License

- Can I use it personally?

- Can I use it commercially?

- Can I redistribute or fine-tune it?

7. Format

- Is it safetensors, GGUF, or another package?

- Does my runtime load that format

Takeaway: If a model behaves badly, do not only blame the weights. Check the whole package.

## Common mistakes beginners make

Mistake 1: Thinking the parameter count is the whole model

A 7B model is not just "7 billion numbers." It also needs architecture, tokenizer, config, formatting rules, and runtime support.

Takeaway: Parameter count is one property, not the full identity of the model.

Mistake 2: Ignoring the tokenizer

If the tokenizer is wrong, the model's input is wrong.

Even a powerful model can perform poorly if text is converted into the wrong token IDs.

Takeaway: The tokenizer is part of the model, not a side accessory.

Mistake 3: Using the wrong chat template

Many "bad model" experiences are actually formatting problems.

The model may be capable, but the runtime is not presenting the conversation in the format the model expects.

Takeaway: For instruct models, prompt formatting is part of performance.

Mistake 4: Treating GGUF and safetensors as model quality levels

A format is not the same thing as capability.

GGUF and safetensors are packaging formats. Quality depends on the underlying model, quantization, runtime, prompt formatting, and settings.

Takeaway: File format tells you how the model is packaged, not whether it is smart.

Mistake 5: Assuming open-weight means unrestricted

A downloadable model can still have license restrictions.

Before using a model in a product, check the license.

Takeaway: Local does not automatically mean legally unrestricted.

## Practical next step

Pick one model page on Hugging Face and look for these seven pieces:

- Architecture

- Weights

- Tokenizer

- Config

- Chat template

- License

- Format

Do not install anything yet.

Just inspect the model page like a map.

Look at the file list. Read the model card. Check the license. Notice whether the repo contains config.json, tokenizer files, weight shards, or GGUF files.

This small habit will make local LLMs feel much less mysterious.

Takeaway: Before you run models, learn to read model packages.

## Series bridge

So far, we have covered:

- 00: What local LLMs are

- 01: How inference predicts one token at a time

- 02: How text becomes tokens and context windows work

- 03: What weights and parameters are

- 04: What a complete model package includes

Next up:

05 - Generation, Softmax, Greedy, and Sampling

Now that you know what the model package contains, we can look at what happens during generation.

The model produces raw scores for possible next tokens.

Then decoding settings decide which token actually gets picked.

That is where temperature, top-p, top-k, greedy decoding, and randomness enter the picture.