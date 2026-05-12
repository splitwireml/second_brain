---
title: "Akshay Pachaar: Wiki + Graph (FalkorDB)"
created: 2026-04-23
type: raw
source: x/tweet
tweet_id: "2047220248081015110"
author: akshay_pachaar
url: "https://x.com/akshay_pachaar/status/2047220248081015110"
tags: [x-article]
---

**Author:** Akshay 🚀 (@akshay_pachaar)
**Posted:** Thu Apr 23 07:45:17 +0000 2026
**Stats:** 6 replies, 14 retweets, 76 likes

## Raw Content

The next step after Karpathy's wiki idea:

Karpathy's wiki works on knowledge that sits still.

A page on how attention works is just as useful today as it was a year ago.

The LLM reads sources, pulls out ideas, writes clean articles, and keeps them cross-linked.

You never have to rebuild the context from scratch when you want to ask something.

But this breaks the moment you ask a question that spans multiple things at once.

"Which authors moved from Google to Anthropic between 2022 and 2024, and what did they publish after the move?"

A Markdown page can't answer that. The answer lives in the connections between people, companies, papers, and dates.

A wiki can describe that pattern only if someone already wrote an article about it.

A graph lets you ask it directly, ask ten variations of it, and get an answer every time without rebuilding anything.

FalkorDB is an open-source graph database built for exactly this kind of question.

The idea underneath it is simple, and it's what makes the whole thing fast enough to be practical.

Most graph databases store connections as chains of pointers and follow them one by one through memory.

FalkorDB stores the entire graph as a grid of zeros and ones (a sparse matrix) where a 1 means "these two things are connected."

Once your graph is a grid, walking through it becomes math. Two hops is one multiplication. Five hops is five multiplications.

That sounds like a small change, but it lets the CPU do work in parallel and reuse decades of math research that nobody had applied to graph queries before.

In practice, this is the difference between a seven-hop question returning in 350ms and the same question timing out.

The wiki and the graph aren't competing. They sit at different layers.

The wiki stores what something is. The graph stores how everything connects.

Any work where the connections matter as much as the things being connected belongs in a graph.

FalkorDB also comes with vector search built in, which matters for GenAI work.

You can find a relevant part of the graph, search for similar items inside it, and return the answer, all in one query.

Most GraphRAG setups build this by hand across two separate databases. Here you get it in one.

You run it through Docker, query it with Cypher, and connect from Python, JavaScript, Rust, Java, Go, or any Redis client.

Open source and multi-tenant by default, so one instance can host thousands of separate graphs without spinning up thousands of servers.

Repo: https://github.com/FalkorDB/FalkorDB

Karpathy nailed the foundation. The next layer is here.

## Quoted Tweet (Karpathy)

LLM Knowledge Bases — Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. [full quote truncated in API response]
