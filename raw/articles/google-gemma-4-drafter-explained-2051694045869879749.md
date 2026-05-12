---
title: "Gemma 4 - Drafter Explained"
author: "Google Gemma"
username: "@googlegemma"
created: "2026-05-05"
source: "https://x.com/googlegemma/status/2051694045869879749"
type: "x_article"
tags: []
---

Gemma 4 - Drafter Explained

[To improve the inference speed of the Gemma 4 models](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/), a new series of autoregressive “drafter” models has been released alongside the main lineup. Instead of solely relying on the primary Gemma 4 models (referred to as the “target” models), the draft model predicts several tokens in the time it takes the target model to process just one. This technique is also known as speculative decoding.

After the drafter has predicted multiple draft tokens, the target model now only has to verify those suggested draft tokens. The verification is done in parallel thereby drastically speeding up inference. It reduces the number of forward passes the target model has to do for each token. Because our drafter generates a sequence of tokens for verification, we refer to it as the Multi-Token Prediction (MTP) head.

The draft models released for the Gemma 4 family are small and introduce several enhancements to improve the quality of drafted tokens and to further speed up inference, like using the target model activations and KV-cache to get better predictions.

These enhancements result in significant decoding speedups while guaranteeing similar quality, making these checkpoints perfect for low-latency and on-device applications.

There is a lot to unpack here, so let’s go through speculative decoding, MTP, and the drafters!

## What is Speculative Decoding?

Gemma 4 models generate text autoregressively and produce one token at a time. Roughly the same amount of compute is needed for each token, regardless of how difficult it is to predict a given token. As such, this can be an unnecessarily slow process when the tokens are quite easy to predict.

Imagine that the larger model is generating text and has already created “Actions speak”. For those that recognize the start of this sentence, it is a common proverb in the English language and extends to “Actions speak louder than words.”. Since it is quite common, smaller models are likely to generate the exact same completion (“louder than words”) as a larger model would. As such, it would be a waste of time and compute for the larger model to predict “louder than words” one token at a time.

With speculative decoding, we can use a smaller draft model to predict several tokens ahead of time. The draft model will receive the same input “Actions speak” and still autoregressively predict a number of tokens, let’s say four tokens. The drafted tokens are generated much faster than the larger model would as the draft model is only a fraction of its size.

## What is Multi-Token Prediction?

However, the drafted tokens are not necessarily correct, otherwise we could just have used the smaller model. Instead, these tokens are given to the target model to verify in parallel. Since the target model can do this in one forward pass, it doesn’t have to do a forward pass for each token. The drafter is what we call the Multi-Token Prediction (MTP) head. Each forward pass of the target model performs regular next-token prediction (NTP) and produces intermediate hidden states. The drafter (MTP Head) uses those hidden states and runs several autoregressive forward passes to general multiple tokens. As such, a single forward pass of the target model results in multiple tokens instead of one. There is one from next-token prediction of the target model and multiple ones from the drafter (MTP head).

If the target model agrees with the suggestions of the draft model, then all tokens are accepted. Instead of having to generate four tokens, the smaller model did that in a fraction of the time. The target model only had to verify them in the time it would have taken the target model to generate one token. Moreover, if all draft tokens were accepted, the target model would still generate one additional token by itself.

If the target model disagrees with only part of the draft tokens, it will accept them until it disagrees. The target model will then replace the rejected token with a token of its own.

This process is actually quite fast considering the model can verify the quality of the drafted tokens all at once instead of having to verify each of the drafted tokens one at a time. Since the draft model is so small, it takes much less time to predict a single token compared to the target model. This means that the target model can verify multiple tokens at almost the same time it takes to generate a single token! Note that the draft model, like most language models, generates those tokens sequentially but can do this much faster due to its small size.

All tokens that the target model deem to be good enough are selected. The first token it rejects and all others that follow are not included are discarded. However, since the target model has done a forward pass it can still perform a next token prediction. So although a token, like “pens”, is rejected the target model would still come with an alternative of the rejected token.

As a result, any number of drafted tokens might be selected by the target model. The full process is quite interesting to visualize considering the draft model performs its processing autoregressively and generates tokens sequence by sequence, the target model can verify all drafted tokens in parallel. The target model is still autoregressive but instead of having to generate those draft tokens one by one, it can now verify them all at once.

## MTP with Gemma 4

The draft models released for the Gemma 4 family are most similar to the dense Gemma 4 models, but much much smaller. In fact, the draft model for the Gemma 4 E2B has only about 76M parameters, four layers, and a smaller input embedding size (256 compared to 1536).

Note how the decoder itself is similar to that of a dense Gemma 4 model. However, there is a lot happening before and after the decoder!

The draft models have various enhancements specifically to make it more efficient and to further speed up inference. Likewise, there are also some interesting techniques used to improve the quality of the drafted tokens and decreases drafter latency. After all, we want the drafted tokens to be as accurate as possible, and to be generated as fast as possible.

These changes can be summarized as follows:

- Target Activations: The draft model uses the activations from the last layer of the target model, concatenates them with the token embeddings, and down-projects them to the drafter model's dimension.

- KV Cache Sharing: The draft model cross-attends to the target model's KV cache rather than building its own.

- Efficient Embedder: The LM Head performs a sparse decoding technique that identifies the most likely clusters of tokens to predict (E2B and E4B only).

Let’s explore each of these in more detail!

Target Activations

To improve the quality of the tokens generated by the draft model, the final activations of the target model (e.g., E2B) are fed to the draft model. These are concatenated with the token embedding of the draft model both having 1,536 values assuming the E2B model. The concatenated embeddings are quite large and for efficiency reasons they are projected down to only 256 values. This is essentially a compression of the processed state of the large draft model and the newly initialized embeddings of the draft model. Why let previous activations go to waste?

These activations are only given to the draft model in the first round of processing. Remember that after the draft starts with an initial round, it may produce several tokens by passing them back to itself autoregressively. As such, in round 2, the activations that the draft model generated in round 1 are used since a new token was generated. Since the intermediate activations of the small draft model are only 256 values, they are projected up to match the dimensions of its input embedding table (namely 1,536 values). Note that to further improve efficiency, the input embedding table is shared between the target model and the draft model.

Then, in round 3, the draft model uses the activations that were generated in round 2, and so on!

KV Cache Sharing

The KV cache can take up quite a bit of space since it contains the key and value representations for every token in the sequence, across every layer. Although Gemma 4 has already taken many steps to reduce this (like setting K=V in the global attention layer), the draft model takes it a step further.

Instead of the draft model needing to process the full prompt and build its own KV cache, it cross-attends to the already-computed KV cache of the target model. For its local attention layers, the draft model simply reuses the last computed local KV cache of the target model. Since the last layer of any Gemma 4 model is always global, that global KV cache is reused for the draft model's global attention layer.

As before, since the target model already did much of the heavy lifting, it would be a waste to throw that away!

The Efficient Embedder

Finally, there is an efficient embedder that reduces the compute needed to generate the drafted tokens from the Language Model Head (LM Head). In traditional models, the LM Head would convert the hidden state generated by the decoders to logits (token probabilities) by multiplying it with a large weights matrix (the same used in the embedding layer, namely the lookup table). For such a small model, this process can be quite expensive!

The question you might ask yourself is whether we really need to calculate the logits for all 262,144 tokens when most of them are likely to be irrelevant?

In the drafter for Gemma 4 E2B and E4B models, this process is made more efficient through a classic technique, namely clustering. All token embeddings have been clustered separately into large groups of tokens that have similar meaning. We then find an embedding representation for each cluster.

This new lookup table is then used in the LM Head where it is multiplied by the hidden state. This results in cluster logits instead of token logits. This means that the cluster logits tell us the clusters that most likely contain the next token. The clusters that are most likely to contain the correct token are selected. Then, all tokens within those clusters are used to calculate the final token logits.

This computation is much easier and instead tells us that the next token is almost certainly in the chosen clusters. This efficient embedder allows for speeding up the draft model even more!