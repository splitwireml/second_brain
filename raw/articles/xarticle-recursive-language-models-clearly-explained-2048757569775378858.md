---
title: "Recursive Language Models, clearly explained"
source: "x-bookmarks"
tweet_id: "2048757569775378858"
tweet_url: "https://x.com/akshay_pachaar/status/2048757569775378858"
author_name: "Akshay 🚀"
author_handle: "@akshay_pachaar"
tweet_date: "Mon Apr 27 13:34:03 +0000 2026"
bookmark_date: "2026-04-27"
content_type: "x_article"
character_count: 5140
retweet_count: 39
like_count: 223
external_urls:
  - "https://arxiv.org/abs/2512.24601v1)"
  - "https://github.com/alexzhang13/rlm)"
---

# Recursive Language Models, clearly explained

Recursive Language Models, clearly explained

Researchers from MIT recently proposed a clever solution to one of the biggest limitations of modern LLMs: context rot.

Here's what context rot looks like:

You paste a 200-page document into ChatGPT. You ask a simple question. The answer comes back wrong, even though the information is right there on page 53.

You didn't exceed the context window. The model just got worse at reasoning because there was too much to process at once.

The elegant fix they proposed is called Recursive Language Models. The results are striking, and the core idea is surprisingly intuitive.

Let's understand it step-by-step.

# The Problem: Context Rot Is a Reasoning Failure, Not a Window Failure

A model that advertises a 1M-token window can still produce garbage on a 50K-token document, and the reason has nothing to do with how much text fits.

Frontier models ace the needle-in-a-haystack benchmark. You hide one weird sentence in a pile of filler text, ask about that sentence, and the model finds it.

That test measures retrieval against a blob of tokens. It does not measure reasoning across those tokens.

Frontier models ace needle-in-a-haystack tests. But ask them to count, classify, or reason over thousands of buried entries, and performance collapses.

You've probably noticed this yourself:

- Long Claude Code sessions get sluggish

- Extended ChatGPT conversations require more repetition

The model isn't hallucinating, it's just getting dumber as context grows

# The Fix: Recursive Language Models (RLMs)

The core idea is simple:

Instead of forcing the model to process everything at once, let it break context into smaller pieces and handle them recursively.

The key shift is context-centric decomposition:

- Agents decompose tasks based on human-designed steps

- RLMs let the model decompose the context itself

The model becomes a programmer analyzing a dataset, not a student cramming for an exam.

# How RLMs Work

## 1. Separate query from context

In a normal LLM call, the query and the full context ride together inside one prompt. Everything you want the model to see has to fit in that single prompt window before generation starts.

RLMs break that assumption. The context lives outside the prompt, in a runtime memory slot, while the root model sees only the question and a set of tools.

Think of a Jupyter notebook. You load a dataframe into a variable called df, and from then on every cell references df without re-uploading the CSV.

RLMs borrow that exact mental model. The 200-page document becomes a variable, let's call it ctx, that sits in a REPL environment the model can interact with through tool calls.

## 2. The model gets tools

The root model cannot read ctx directly, so the whole design lives or dies on the tools it uses to probe that variable. The paper gives the model four, and together they cover every access pattern a data analyst would reach for.

- Peek at context (view first 2,000 chars to understand structure)

- Grep using regex to filter relevant lines

- Partition into smaller chunks

- Call itself recursively on those chunks

## 3. Strategy emerges from the task

Agent frameworks traditionally hardcode the decomposition. A human picks the steps, the order, and the fallback policy up front, and the model plays a part the human already scripted.

RLMs do the opposite. The root model decides how to break the problem down based on what it finds as it looks.

It might grep first, then partition. Or peek, then summarize. It figures this out on its own rather than following a human-designed workflow.

# A Concrete Example

Say you have 5,000 customer support tickets and you ask: "Among users 12345, 67890, and 11111, how many questions are about billing?"

A normal LLM receives all 5,000 tickets, tries to scan everything, and makes counting errors.

An RLM handles it differently:

1. Peeks at structure: "Each line has Date, User ID, Question"

2. Greps for target users, reducing 5,000 lines to 50

3. Spawns a recursive call: "Classify each as billing or other"

4. Returns: Final Result

The root model's context stayed small throughout. No rot.

# Why It Matters

- No context rot: Accuracy holds regardless of document size

- Unlimited context: 10M tokens? Just partition more

- Interpretable: See exactly what the model did

- Cost-efficient: Smaller calls beat one massive API call

- Future-proof: As LLMs improve, RLMs improve automatically

RLMs treat context as data to be programmatically explored.

The model combines code execution and language reasoning. It's not summarization. It's not a rigid agent. It decides how to decompose the problem based on what it discovers.

To read more about this, I am sharing the research paper and a startup code on RLMs that you can build on top of.

- [Paper →](https://arxiv.org/abs/2512.24601v1)

- [GitHub →](https://github.com/alexzhang13/rlm)

---

Thanks for reading!

If you found it insightful, reshare with your network.

Find me →[@akshay_pachaar](https://x.com/@akshay_pachaar) ✔️

For more insights and tutorials on LLMs, AI Agents, and Machine Learning!
