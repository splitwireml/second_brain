---
source_url: https://x.com/sairahul1/status/2067540315620405543
ingested: 2026-06-22
sha256: cfe80215b103c31fca68bba01a143fcbe953b7506827780100135f488cc77dea
---

# 6 AI Concepts You Must Master to Build Production-Ready AI Systems

6 AI Concepts You Must Master to Build Production-Ready AI Systems

I watched a $200 bill appear on an AWS account overnight.

Not because the system crashed.

An agent ran in a loop for six hours with no stop condition, calling the OpenAI API on every iteration.

Every monitoring dashboard said it was healthy.

Nobody noticed until the invoice hit in the morning.

That is what happens when you build AI systems without understanding how they actually work.

Most people learn AI engineering backwards.

Install a library. Follow a tutorial. Call an API. Get something working. Feel like progress.

Then something breaks in a way that makes no sense.

They change numbers randomly until it stops.

That is not engineering. That's hope with a keyboard.

Here are the 6 concepts that fix this.

---

## The one sentence that explains everything

Every AI system, no matter how complex, is just:

Memory (RAG) + Thinking (LLM + Tokens) + Actions (Agents) + Measurement (Evals)

…assembled through Context Engineering.

That's the whole field.

Everything below is just unpacking what each part actually means.

---

## 1. Tokens and the Context Window

LLMs don't read words. They read chunks called tokens.

"engineering" → 1 token

"unbelievable" → 2 tokens Spaces and punctuation count too.

Every model has a context window — a hard limit on tokens it can hold at once.

→ Claude: 200,000 tokens

→ GPT-5: 400,000 tokens

Think of it like a whiteboard in a meeting room.

The model only works with what's currently on the board.

When the board fills up, old notes get erased to make room.

The model doesn't lose the ability to think.

It loses access to the earlier information.

Why this breaks production systems:

→ Tokens cost money — every API call bills per input and output token

→ Long chat histories fill the window fast

→ When context fills up, earlier instructions get silently dropped

→ What goes into context is an engineering decision, not a default

The failure that proves it:

A team built a customer support agent with full 12-month chat history as context on every request.

Worked beautifully in testing with 5 interactions.

In production, after 50 interactions, the agent started ignoring its own system prompt.

The instructions were still there.

They were buried under 80,000 tokens of conversation history.

The model had effectively stopped attending to them.

The fix wasn't a better model.

It was summarizing older history to keep the window focused.

The uncomfortable truth:

Most "prompt engineering failures" are actually token and context window failures in disguise.

Engineers blame the prompt when the real problem is that the critical instruction is on line 3 of a 500-line context, and the model stopped weighting it.

---

## 2. Embeddings and Vector Search

Embeddings turn meaning into numbers so "similar" can be calculated mathematically.

The problem they solve:

You have 50,000 documents. A user asks a question. You need the 3 most relevant ones — without reading all 50,000 every time.

Keyword search fails here.

If the document says "automobile" and the user asks about "cars," keyword search misses it.

Not because the answer isn't there. Because the words didn't match.

Embeddings solve this differently.

An embedding model converts text into a vector — a list of numbers representing meaning in mathematical space.

Semantically similar text → numerically similar vectors.

"car" and "automobile" → close together

"car" and "photosynthesis" → far apart

How vector search actually works:

1. Every document gets converted to a vector and stored

2. The user's question also becomes a vector

3. The system finds stored vectors closest to the question vector

4. Those are your most relevant documents

This isn't approximate magic. It's geometry.

Similarity is a real mathematical property you can calculate.

Where this shows up in production:

→ Semantic search in any document system

→ Finding similar products, articles, user profiles

→ The retrieval step in RAG (next concept)

→ Memory in AI agents

---

## 3. RAG (Retrieval-Augmented Generation)

Instead of training a model on your data, you retrieve the relevant data at query time and feed it to the model as context.

The problem RAG solves:

LLMs know a lot. They don't know your data.

Your company's internal docs. Your product database. Your customer support history.

None of that was in the training set.

Two options: train a model on your data (expensive, slow, goes stale instantly) or give the model your data exactly when it needs it.

RAG is the second option, done systematically.

The 3-step pipeline:

→ RETRIEVE:

question becomes a vector → vector database finds the most similar stored documents → top 3-5 chunks retrieved

→ AUGMENT:

retrieved documents get added to the model's context → prompt becomes "using this context, answer this question"

→ GENERATE:

model answers grounded in your actual data — not hallucinated

Where RAG breaks down:

→ Bad retrieval = bad answer. The model can only work with what it received

→ Poor chunking splits the answer from its context

→ The model can still hallucinate if retrieval finds nothing useful

A real RAG failure:

A team built an internal knowledge assistant for a 500-page technical manual.

Worked perfectly in demos. In production, answers were vague and sometimes wrong.

The problem: chunk size.

They'd split the manual into 1,000-token chunks by raw character count.

Tables split mid-row. Step-by-step instructions split mid-step.

The retrieval was finding the right general area — but missing the actual answer.

Halving the chunk size and adding overlap fixed 80% of the problems overnight.

The hard opinion:

RAG is overrated when your retrieval is bad.

The LLM cannot fix bad retrieval. It can only hallucinate around it.

If you're seeing wrong answers, stop tweaking your prompt.

Start measuring your retrieval precision.

That's where the answer is.

---

## 4. The Agentic Loop

Agents work by repeatedly choosing an action, executing it, observing the result, and deciding what to do next — until the task is done.

A regular LLM call is stateless. You ask, it answers, done.

An agent is stateful. It acts, observes, decides, repeats.

The loop in plain English:

1. Receive a goal

2. Decide the next action

3. Execute it — search, code, read a file

4. Observe the result

5. Decide the next action based on what was learned

6. Repeat until the goal is complete

7. Return the final answer

Tools are what give agents their power.

Without tools, an LLM only responds with text.

With tools, it can search the web, read files, write code, call APIs, trigger any action you define.

Three things beginners always get wrong:

→ Agents without stop conditions run forever. You must define when to stop — step limit, time limit, or goal condition

→ More tools ≠ better performance. Too many tools confuse the model about which to use

→ Tool errors need explicit handling. A silent failure makes the agent confidently produce garbage

The $200 overnight failure, in detail:

The agent had no maximum step count. Its goal: research a topic and produce a summary.

One of its web search tools returned an empty result.

The agent didn't know how to stop.

It kept searching, retrying, generating intermediate summaries — each one triggering another search.

Six hours later: 847 LLM calls. 2.1 million tokens consumed. A coherent-looking but completely circular summary. A $200 invoice.

The fix was three lines: a max step counter, an explicit handler for empty results, an escalation path when confidence was low.

The same agent now completes in under 12 calls on average.

The opinion you need to hear:

Most agents fail not because the model is bad — but because engineers treat the loop like it's self-managing.

It is not.

Guardrails, stop conditions, error handlers — built in from the start, not added after the first incident.

---

## 5. Evals (Evaluation)

Evals are how you know whether your AI system is actually working — and whether a change made it better or worse.

This is the concept most tutorials skip because it's unglamorous.

It's also what separates engineers who build demos from engineers who build production systems.

The problem without evals:

You change your prompt. Update your retrieval logic. Switch to a newer model.

Did it get better?

You don't know. You could manually check a few examples — but that's a feeling, not evidence.

What evals actually look like:

→ A golden dataset: 25-50 real inputs with known correct outputs, covering main use cases plus 5 known tricky edge cases

→ Binary metrics where possible:

— Did the RAG system retrieve the correct document? Yes/No

— Did the agent complete without error? Yes/No

— Did the response contain the required information? Yes/No

→ Aggregate scores tracked over time:

— Retrieval accuracy: 89% → change made → 84%. Regression found.

— Task completion rate: 76% → new agent version → 81%. Improvement confirmed.

The eval cycle:

Deploy → Measure with evals → Find failures → Add failures to golden dataset → Fix → Run evals again → Compare scores → Ship only if numbers improved

The honest truth:

"Helpfulness: 3.7/5" tells you nothing actionable.

"Retrieved the correct document: 84% of the time" tells you exactly where the problem is and how much a fix improved it.

An AI system without evals is not a product.

It's a demo you cannot confidently change.

---

## 6. Context Engineering

The discipline of deciding exactly what information goes into the model's context window, how it's structured, and what gets left out.

Here's the opinion that makes people uncomfortable:

Context engineering matters more than prompt engineering.

A mediocre prompt in a well-curated context outperforms a brilliant prompt buried in noise — every single time.

Most teams spend 80% of their optimization effort on the prompt and almost none on the context.

The results reflect that.

The naive approach fails:

Include everything. All the history. All the retrieved documents. Every tool description. The system prompt. The user message. All of it.

This fails for a consistent reason: the model gets confused about what matters most.

There's a documented effect called "lost in the middle" — information buried deep in a long context is less likely to be used.

What context engineering actually involves:

→ Selection: which documents, facts, or history does this specific decision need?

→ Compression: can older parts of the conversation be summarized to save tokens?

→ Ordering: critical instructions belong at the beginning and end — not the middle

→ Pruning: what can be removed without affecting output quality?

→ Structure: headers, separators, labeled sections affect how reliably the model uses information

A practical example:

An agent has been running for 45 minutes. It's accumulated 80,000 tokens of conversation history. Its window is 128,000.

You don't want to lose the original goal and constraints, even as history fills the window.

Context engineering: compress older tool outputs, summarize earlier reasoning, keep the task definition prominent throughout the session.

Prompt engineering is writing good instructions.

Context engineering is building the environment in which those instructions are actually followed.

---

## How these 6 concepts form one system

MEMORY → RAG + Embeddings   (what the system knows)

THINKING → LLM + Tokens + Context Window (how it reasons with what it knows)

ACTIONS → Agentic Loop + Tools (what it can do in the world)

MEASUREMENT → Evals (how you know it's working)

GLUE → Context Engineering (what decides what flows between all of the above)

A simple chatbot is just Thinking.

A customer support agent is Memory + Thinking + Actions.

A reliable production system adds Measurement.

The sophistication is in how well the pieces connect.

The flow for any single request:

User question

→ Context Engineering decides what to include

→ Embeddings retrieve relevant Memory (RAG)

→ Tokens determine how much fits in the window

→ LLM reasons over the assembled context

→ Agentic Loop decides if more information is needed

→ Evals measure whether the output was actually correct

---

## Where to start

You don't need to master all six at once.

→ Start with tokens and context windows — they affect everything you build → Add embeddings when you need semantic search or memory

→ Learn RAG when you need to ground a model in your own data

→ Learn the agentic loop when you need automation

→ Add evals before you ship anything to production

→ Apply context engineering as everything else becomes intuitive

That sequence isn't arbitrary.

Each concept makes the next one learnable.

---

## The honest final take

Most teams that struggle with AI in production aren't struggling with the wrong model or the wrong library.

They're struggling because they skipped one of these six concepts.

The agent loops forever because nobody thought about stop conditions.

The RAG answers are wrong because nobody measured retrieval.

The prompt stops working over long sessions because nobody understood how the context window fills up.

These aren't sophisticated problems.

They're basic ones, dressed up in technical vocabulary.

The tools change every six months.

These six concepts are how the tools work.

Learn the concepts, and you'll never be confused by a new tool again.

More importantly — you'll never spend $200 watching an agent loop through the night, wondering what went wrong.

---

If this was useful:

→ Repost to share it with every AI engineer you know

→ Follow @sairahul1 for more systems and breakdowns like this

→ Bookmark this — you'll reference it the next time something breaks in production

I write about AI, building products, and systems that work while you sleep.
