---
source_url: https://x.com/h100envy/status/2054877458847903834
ingested: 2026-05-19
tweet_id: "2054877458847903834"
author_name: h100envy
author_handle: "@h100envy"
tweet_date: "Thu May 14 10:52:18 +0000 2026"
sha256: <computed-after-body>
---

# How To Speedrun an AI Engineer Career at Anthropic

How To Speedrun an AI Engineer Career at Anthropic

Inside Anthropic, a single training run for a Claude model uses tens of thousands of GPUs in parallel. Roughly half of the technical staff joined without a formal ML background. The profession is changing faster than ever. And for the first time, the path is open beyond MIT and Stanford graduates.

A speedrun in gaming means completing a game in the minimum possible time by using every legitimate optimization the system allows. Not cheats. Not shortcuts that break the experience. Deep knowledge of the system plus tools that turn dead time into progress.

This article applies the same frame to becoming an AI engineer at Anthropic. The "game" is a hard, traditionally gated profession. The "skips" are AI tools that compress months of solo grinding into days of guided learning. Parts of the route still require the classical foundation. Others have been shortcut by the existence of LLMs that didn't exist three years ago.

# The numbers you need to see first

What Anthropic pays in 2026 (Levels.fyi, May 2026):

- Median total comp for Software Engineer: $710K/year
- Senior SWE: $445K-$575K
- Lead SWE: up to $785K
- Research Scientist median: $746K, top packages to $1.05M
- Highest reported SWE package: $920K
- Glassdoor compensation score: 4.8/5 - highest among all AI companies

What's happening at Anthropic right now:

- Team doubled in 2025, continuing to grow
- 70+ open engineering and research roles
- Offices: SF, NYC, Seattle, London, Dublin, Tokyo, Singapore, Bangalore, Zurich, Sydney
- Visa sponsorship for technical roles - standard
- Hybrid policy: 25% time in office minimum
- Valuation: $61.5B, equity as RSUs with 4-year vest

Speedrun timeline:

- With 3+ years SWE experience: 18-30 months to realistic shot
- From scratch, no degree: 3-4 years

# What roles exist

Anthropic uses a single title for all technical staff - Member of Technical Staff (MTS). But behind this single title sit different functions:

| Role | What they do | Who fits |
|------|--------------|----------|
| Software Engineer (Product) | Claude.ai, API, Claude Code, product features | SWE with 5+ years production experience |
| Software Engineer (Infrastructure) | Inference, GPU clusters, observability | Distributed systems, SRE |
| Research Engineer | Model training, RL infrastructure, evals | At the research/engineering boundary |
| Research Scientist | Interpretability, alignment, scaling laws | PhD or equivalent |
| Applied AI / Forward Deployed | Enterprise Claude deployment | SWE + solutions architecting |
| Safeguards / Trust & Safety | Red-teaming, abuse detection | SWE + security mindset |

The lowest entry barrier without ML background is SWE (Product) and Applied AI. The highest is Research Scientist.

This article focuses on the path to Software Engineer and Research Engineer. The Research Scientist track is covered separately at the end for those with PhD ambitions.

# How AI is changing AI engineering work itself

Most "how to become an AI engineer" content skips the most important thing: in 2026, the profession itself uses AI tools at every step. If you're learning by a 2022 roadmap, you're learning for a role that has already transformed.

AI as code co-pilot - baseline level. Every Anthropic engineer uses Claude daily for first drafts of tests, explaining unfamiliar code, debugging from logs, converting research ideas to pseudocode. Per public Dario Amodei interviews: most new code inside Anthropic is written with Claude assistance.

What this means for you. Your day as an AI engineer in 2026: formulate the task -> AI writes first draft -> you review, edit, test. The idea-to-PR cycle compresses from a day to a couple of hours. But the cost of error has risen - review of shallow code catches fewer bugs than writing it yourself.

What's been added to the skillset in 2026:

- AI-augmented development: working with Claude/Cursor as a coworker
- LLM internals: transformer down to attention patterns
- RL for language models: PPO, DPO, constitutional AI, reward modeling
- Distributed training: data/tensor/pipeline parallelism, FSDP
- Inference optimization: speculative decoding, KV-cache, quantization
- Evaluation methodology: how to measure capabilities when benchmarks saturate within a quarter

This is now baseline expectation at Anthropic interviews.

## The ladder: 7 steps from zero to offer

The main mistake people make is trying a vertical jump. Submit a resume without credentials, get rejected, conclude the path is closed. The path isn't closed. It's a ladder where you can't skip steps.

```
Step 7:    Offer
↑
Step 6:    Interview prep + applications
↑
Step 5:    Anthropic-specific knowledge
↑
Step 4:    Portfolio + open-source
↑
Step 3:    AI/ML core + LLM internals
↑
Step 2:    Production software engineering
↑
Step 1:    Math + CS foundation
```

Step 5 is new in 2026 - it didn't exist in 2022 roadmaps.

# Step 1. Math and CS foundation

The longest step. In an interview, within 10 minutes it becomes clear whether you went through this honestly or jumped past it.

5 layers in strict order:

```
Probability + Information theory    ← entropy, KL-divergence, sampling
                  ↑
Optimization + Calculus             ← gradient descent
                  ↑
Linear algebra                      ← attention, embeddings, SVD
                  ↑
Algorithms                          ← coding interviews
                  ↑
Programming foundations             ← Python, types, OOP, tests
```

## Programming foundations

Python 3.11+ with type hints. async/await (Anthropic explicitly mentions Trio, not asyncio, in job posts). pytest. Git to rebase, cherry-pick, bisect level.

Resources: CS50 from Harvard, "Fluent Python" by Ramalho, "The Missing Semester" from MIT.

## Algorithms

LeetCode medium - not for memorization, for thinking. Anthropic doesn't ask trivial LeetCode, but dynamic programming is the most common point of failure in coding rounds.

## Linear algebra

Heart of deep learning. Attention in a transformer is just matrix multiplication with softmax. The main formula:

Resources: 3Blue1Brown "Essence of Linear Algebra" for intuition, Gilbert Strang MIT 18.06 for rigor.

## Calculus and optimization

Each model weight update is a gradient descent step. Differentiation, chain rule (this is backprop), SGD, Adam, AdamW, learning rate schedules.

## Probability + Information theory

An LLM is just conditional probability P(next_token | context). Distributions, Bayes, entropy, cross-entropy, KL-divergence (all ML loss functions), sampling: temperature, top-k, top-p.

Resources: Harvard Stat 110 (Blitzstein) - best probability course, free on YouTube.

## How AI accelerates this learning

Before: stuck on a Strang proof - lose days alone. Now:

```
I'm stuck on: [textbook excerpt]
My level: I know definitions through chapter X.
Explain three ways:
1. Formally with definitions
2. Geometrically through intuition
3. With a concrete numerical example
Then give me 3 exercises with increasing difficulty.
```

In 5 minutes - an explanation better than the average professor's.

# Step 2. Production software engineering

This step can't be cheated. Anthropic doesn't hire fresh bootcamp grads. A typical SWE job post requires minimum 5 years of commercial experience.

Why: training a frontier model is a distributed system on 30,000+ GPUs. One bug kills a run worth millions of dollars. Idempotency, retry logic, graceful degradation - not from a book, from scars.

Strategy:

1. Get into a product company or serious startup as a junior
2. Grow to Mid/Senior in 2 years
3. Move to a high-impact company (FAANG, unicorn)
4. Try to work with real scale - millions of users, ML in production, GPU loads

What should appear on your resume:

- Distributed systems: CAP, eventual consistency, vector clocks
- Production ML or high-load (one of the two is required)
- Observability: metrics, traces, logs
- On-call experience
- Cross-functional ownership

Tech stack from actual Anthropic 2026 job posts:

- Python + type hints + async (Trio preferred over asyncio)
- PyTorch or JAX - ideally both
- TPU or GPU experience
- Distributed training: FSDP, DeepSpeed, tensor/pipeline parallelism
- CUDA, Triton for low-level work
- Kubernetes, Terraform
- TypeScript + React for product roles
- Rust for performance-critical infrastructure

Main trap with AI use: people get into AI-coding and lose the ability to think. Use AI as leverage, not as a replacement for understanding. Anthropic asks questions in a way that without real understanding, you don't pass.

# Step 3. AI/ML core + LLM internals

Here you transition from "good engineer" to "AI engineer." Without it, you'll get hired at Stripe but not Anthropic.

## Classical ML

Linear/logistic regression, decision trees, gradient boosting, k-means, PCA, cross-validation, bias-variance tradeoff. Needed not because Anthropic uses random forests, but because without classical ML you don't understand the concepts deep learning builds on.

Resource: Andrew Ng Machine Learning Course (Coursera). Old, but foundational.

## Deep Learning fundamentals

- MLP, backprop by hand
- CNN, RNN/LSTM (historical context)
- Transformers - your main focus
- Attention mechanisms in all variations
- Positional encodings (RoPE, ALiBi)
- Normalization (LayerNorm, RMSNorm)

Main resource: Andrej Karpathy "Neural Networks: Zero to Hero" on YouTube - free. Most valuable DL course in existence. Karpathy writes GPT-2 from scratch with his own hands. After it, you understand the transformer at every line of code.

## LLM internals

Anthropic expects you to know:

- Transformer architecture: decoder-only (Claude), encoder vs encoder-decoder
- Pretraining: next-token prediction, scaling laws
- Tokenization: BPE, SentencePiece, Tiktoken
- Context windows: O(n²) problem and solutions (FlashAttention, sliding window, ring attention)
- Inference: KV-cache, speculative decoding, batching
- Post-training: SFT, RLHF, DPO, Constitutional AI
- Mixture of Experts: routing, why Claude and GPT-4 use it

## RL for language models

In 2026 this is the hottest position type at Anthropic. After Claude Sonnet 4.5 and Opus 4.5 they're actively hiring in RL teams.

- Basic RL: MDP, Q-learning, policy gradient
- PPO - the algorithm behind RLHF
- DPO - modern RLHF alternative
- Reward modeling
- Agentic RL: RL for tool use, computer use, long-horizon tasks - frontier work, direct competence of Anthropic's RL team

Resources: Spinning Up in Deep RL (OpenAI), Lilian Weng blog - best RL-for-LLM tutorials.

## How AI accelerates this

Paper implementation: instead of reading for weeks, load PDF into Claude:

```
Attached paper: Constitutional AI.
Background: PyTorch, understand RLHF.
1. Main idea in 3 paragraphs
2. How it differs from standard RLHF
3. What to implement: components
4. Pseudocode for self-supervised critique
5. Main implementation pitfalls
```

You get a working day-plan instead of a month of reading.

# Step 4. Portfolio + open-source

Without GitHub your resume weighs zero. Direct quote from Anthropic careers: they "value direct evidence of ability over credentials."

## Minimum 3 GitHub projects

Project 1: transformer from scratch. Pure PyTorch, no transformers library. From zero to training on a small dataset. If you completed Karpathy - you already have this. Build it out as a production-quality repository with tests, docs, type hints, CI/CD.

Project 2: implementation of a key paper. By increasing difficulty:

- LoRA finetuning - fine-tune LLM with minimal GPU
- Reward model + PPO loop - mini-RLHF
- Mechanistic interpretability circuit - find and describe a specific circuit

Project 3 (the key one for 2026): AI agent or evaluation tool. This is what differentiates you among thousands of applicants:

- Custom Claude Code clone - coding agent on Claude API
- Evaluation harness for some capability
- Interpretability dashboard
- RAG over academic papers - your research assistant

Anthropic hires people who are already building with their API. Show you're on their side of the game.

## Open-source

One merged PR to a significant repo weighs more than ten small projects:

- vLLM, llama.cpp, ollama - inference engines
- HuggingFace transformers
- PyTorch core, DeepSpeed
- Anthropic-related: MCP, SDK, computer-use-demo

## Where to get compute

- Google Colab Pro - $10/mo, T4/A100
- Lambda Labs - $1-2/hr H100/A100
- vast.ai - GPU marketplace, cheapest
- TPU Research Cloud - Google grants free TPUs to independent researchers
- Kaggle notebooks - 30 hours/week free

Train small models (1M-100M parameters) - enough to demonstrate understanding.

# Step 5. Anthropic-specific knowledge

This step is what makes Anthropic unique. They hire not just for technical skill, but for alignment with company mission. This isn't marketing - there's a separate values round at the interview that fails more candidates than technical rounds.

## Read everything Anthropic has published

Not "familiarize with" - actually read with notes. Before the interview.

## Tier 1 - mandatory:

1. Constitutional AI paper (2022) - the company's main technical contribution, laying the RLHF alternative foundation. Without understanding this paper, there's no point going to interview
2. Responsible Scaling Policy (RSP) - foundational document. Anthropic divides AI systems into ASL levels (AI Safety Levels: ASL-1, ASL-2, ASL-3, ASL-4). Recruiters say directly: "candidates who reference RSP naturally do well." Understanding the ASL scale is a prerequisite
3. Core Views on AI Safety - company manifesto on how they view risks. Explains why Anthropic exists and how they differ from OpenAI
4. Recent Model Cards - every model release comes with a detailed technical document. Read the last 2-3

## Tier 2 - strongly recommended:

5. Sleeper Agents (2024) - on deceptive alignment, a critical paper. Shows models can learn to hide behavior
6. Mechanistic Interpretability series - Anthropic is the world leader in reverse-engineering neural networks. Series of 5-7 publications. Read at minimum "Toy Models of Superposition" and "Scaling Monosemanticity"
7. System Prompts publications - Anthropic regularly publishes Claude's system prompts. Rare level of openness. Study the structure - it shows how they think about behavior
8. Tool Use & Computer Use papers - frontier agentic work

## Tier 3 - for deep dive:

9. All scaling laws papers from the team
10. Alignment Faking, Many-shot Jailbreaking - recent safety research
11. Soft prompting and robustness research

Where to find: anthropic.com/research, anthropic.com/news

## Form your own view on AI safety

Don't parrot the Anthropic narrative. They see through it. Show you thought yourself.

Questions you need your own answers to:

- Where do you agree with Anthropic's approach, where do you disagree?
- How do capability research and safety research relate? Do they conflict?
- What is x-risk and do you believe in it?
- Your view on open-source LLMs? Deepfakes? AI in military applications?
- Are you willing to not ship a product if safety team blocks it?
- How do you think about competitive dynamics - should Anthropic slow down if OpenAI accelerates?

Something from this will come up at interview. Don't memorize answers - develop a view. Anthropic values internal consistency more than repeating their own positions back at them.

## Understand the landscape

- How does Anthropic's approach differ from OpenAI's?
- Why does Anthropic exist? (short version: founders left OpenAI in 2021 over safety disagreements)
- Who are Dario Amodei, Daniela Amodei, Chris Olah, Jared Kaplan
- What is the Frontier Model Forum, AISI, and Anthropic's role in them
- AI policy landscape: EU AI Act, Executive Orders, SB 1047

## Use Anthropic products as a professional

Paradox: people apply to Anthropic without using Claude seriously. Before interview:

- Use Claude Code as your daily dev workflow for a few weeks
- Use Claude API to build a non-trivial workflow
- Use Computer Use via MCP
- Play with MCP (Model Context Protocol) - their own open standard
- Read docs.claude.com cover to cover

If you write to Anthropic without deeply knowing their products - it shows in 2 minutes.

# Step 6. Interview

The process takes 4-8 weeks. From public interview reports on Glassdoor, Hello Interview, interviewing.io, Medium.

## Structure (typical SWE loop)

```
1. Recruiter screen          (30 min)
↓
2. Online assessment         (90 min, CodeSignal)
↓
3. Hiring Manager call       (45-60 min)
↓
4. Coding interview          (60 min, pair programming)
↓
5. System design             (60 min)
↓
6. Project deep dive         (60 min)
↓
7. Values interview          (45-60 min) ← most fail here
↓
8. Team matching + references
```

## Recruiter screen

30 minutes. Goal: verify you're not a random applicant, motivation is real, background minimally matches. Prepare:

- 2-minute pitch of your career
- Specific reasons why Anthropic (NOT "you do cool AI")
- Which Anthropic papers you've read and what you took from them
- Understanding of which team you want to join

## Online Assessment

90 minutes on CodeSignal. Not standard LeetCode. You get one large problem in 4 levels. From public reports, concrete examples:

- In-memory key-value store: level 1 - SET/GET/DELETE, level 2 - filters, level 3 - TTL with timestamps, level 4 - file compression
- In-memory cache extension: find a bug -> extend functionality -> add invalidation -> optimize

Main check - code modularity. Can you add functionality without breaking what came before. Tips:

- Write tests at each level before moving on
- Use clean names and subfunctions
- Don't try to write everything at once - incremental progress
- If you didn't get to level 4 - fine. Clean levels 1-3 are better than dirty 1-4

From a public report: "I think I understood what they're looking for wrong. Maybe they're looking for coding speed?" - no, they're looking for production-quality code. Don't trade quality for speed.

## Hiring Manager screen

45-60 minutes with the manager of the team you'd join. No live coding. Goal - engineering judgment:

- "Tell me about the hardest technical decision in your career"
- "Tell me about a time you disagreed with a tech lead. How was it resolved?"
- "How do you approach technical debt?"
- Sometimes review of your code sample or PR

## Coding interview

60 minutes of pair programming. Often on concurrency. From interview reports, a typical task: build a reliable message ingestion component handling unpredictable delays. Edge cases, production-grade thinking, not speed.

What matters:

- Narrate your thinking out loud
- Ask clarifying questions before coding
- Write tests
- Think about failure modes: what if network call drops? What if duplicates arrive?
- Async/await + Trio - refresh in your head

## System Design

Specific to AI infrastructure. Typical questions:

- Design API for serving LLMs at scale: request batching, KV-cache management, multi-tenant isolation, rate limiting per customer
- Design distributed training for a model that doesn't fit on one GPU: data/tensor/pipeline parallelism trade-offs, which to choose when
- Design eval harness: how to measure jailbreak resistance at scale
- Design billing system for token-based pricing: counting tokens during streaming, retries, partial failures

This is not Google-style about news feeds. You need distributed systems foundation plus AI infrastructure understanding.

Answer structure:

1. Clarifying questions (5 min)
2. Functional + non-functional requirements (5 min)
3. High-level architecture (15 min)
4. Deep dive into 1-2 components by interviewer request (20 min)
5. Trade-offs, what would you do differently in v2 (15 min)

## Project deep dive

20 minutes you present your hardest project. 40 minutes defending every decision. This is a design review with the toughest senior staff engineer.

Prepare:

- Slides or whiteboard with architecture diagram
- What was the alternative at each decision and why you chose this way
- What would you do differently with current experience
- Trade-offs in latency, cost, complexity
- Metrics: what you measured, before/after

## Values interview - the main failure point

The technically strongest candidates fail here. This is not "what's your weakness?" questions.

Real question types from public reports:

- "Tell me about a moment you had to slow down a launch over safety concerns. How did you feel?"
- "What specific criticisms of Anthropic do you consider valid?"
- "Describe an ethical conflict at work. How did you resolve it?"
- "If you were leading Anthropic and OpenAI shipped GPT-6 six months early, would you ship Claude faster or not?"
- "Tell me about a time you were wrong about a technical decision. How did you process it emotionally?"

What matters:

1. Use real stories with real ethical weight. Not "once I found a bug and it wasn't prioritized." Something with something actually at stake
2. Be ready to talk about emotions, not just events. Important for Anthropic. Most technical people avoid this. "How did you feel" is not a rhetorical question
3. Don't try to guess the "right" answer. They look for internal consistency, not repeating their position
4. Don't over-engineer your answers. The instinct to structure everything like an engineer works against you here
5. Be ready for emotional follow-ups: "Why specifically that? How do you feel about it now?"

From interviewing.io: "candidates who perform well typically have read Responsible Scaling Policy and can reference it naturally. Familiarity with Constitutional AI signals genuine engagement rather than surface-level interest."

## How to prepare with AI

Mock interviews - infinite supply:

```
Play a senior engineer at Anthropic.
Run a coding round for MTS position.
Problem: distributed system for inference of a frontier model.
Rules:
- Don't give hints without request
- Press on edge cases
- Ask about trade-offs
- At the end give feedback: what's strong, what's weak
Time: 60 minutes.
```

Do this every day for 2-4 weeks. New problem every time. Progress faster than from a dozen human mock interviews.

Values round prep with AI is especially valuable - you need to articulate things you don't normally say out loud. Run-through with Claude helps you hear how answers sound.

# Step 7. Where to apply

## Direct links

- Main: https://www.anthropic.com/careers/jobs - 70+ open positions
- Greenhouse: https://job-boards.greenhouse.io/anthropic
- Research: https://www.anthropic.com/research
- Docs: https://docs.claude.com

## Specific roles for different profiles

- Backend with high-load: Software Engineer Inference, Account Abuse, Cloud Inference
- ML-engineer: Research Engineer (RL Velocity, Pretraining Scaling), ML/Research Engineer Safeguards
- Frontend or fullstack: Software Engineer Claude.ai, Claude Code, Engineering & Design - Product
- Security/abuse: Security Labs Engineer, Account Abuse, Trust & Safety
- Systems engineer / SRE: Cluster Deployment, Infrastructure, GPU Performance

## Channels (strongest to weakest)

1. Referral from a current employee - strongest channel. Where to network: AI conferences (NeurIPS, ICML), SF AI meetups, X/Twitter, open-source PR discussions
2. Direct apply through careers page
3. Recruiter outreach - recruiters find you via LinkedIn or GitHub if profile matches
4. Anthropic STEM Fellow program - for students and recent graduates
5. Open-source visibility - if you made a notable project or MCP server

## Research Scientist Track (for those with PhD ambitions)

This is a different ladder, running in parallel. Research Scientist median TC at Anthropic - $746K, top packages to $1.05M.

## How it differs from Research Engineer

| | Research Engineer | Research Scientist |
|--|-------------------|---------------------|
| What they do | Implement research ideas in code, build infra | Generate research ideas, lead directions |
| Education | Bachelor's enough, MS/PhD a plus | PhD effectively required |
| Publications | Not required | Papers, citations needed |
| Split | 70% engineering / 30% research | 30% engineering / 70% research |
| Entry barrier | Open to experienced SWEs | Very narrow |

## Research directions at Anthropic

Understand which direction to target:

1. Mechanistic Interpretability - reverse-engineering neural networks. Led by Chris Olah. Anthropic is the world leader. If this area lights you up - it's the most "anthropic-y" research
2. Alignment Science - making models do what we want. Includes Constitutional AI, RLHF research, evaluation
3. Scaling and Pretraining - scaling laws, new architectures, efficiency
4. Reinforcement Learning - agentic capabilities, computer use, long-horizon tasks. Very hot direction in 2026
5. Safety and Frontier Red Team - adversarial testing, jailbreak research, alignment stress-testing
6. Societal Impacts - AI economics, policy, societal safety

## Path to Research Scientist

Standard path:

1. Bachelor's in CS/Math/Physics from top university - starting point
2. PhD in ML or adjacent field (4-6 years): MIT, Stanford, Berkeley, CMU, Princeton, Oxford, Cambridge, ETH. Admission itself is competitive
3. Publications at top conferences: NeurIPS, ICML, ICLR. Minimum 3-5 first-author publications for a shot
4. Internship at Anthropic, OpenAI, DeepMind, or FAIR during PhD - common path
5. Apply after PhD or after short postdoc

Non-standard paths (rare but exist):

1. Independent researcher track: write strong papers without formal PhD, make notable research, get invited. Example - some EleutherAI members. Realistic only for people with extraordinary research talent
2. Convert from Research Engineer to Research Scientist inside Anthropic - possible, but requires significant own contribution to research, not just implementation
3. MATS (ML Alignment & Theory Scholars) - 12-week program for people transitioning into AI safety research. https://www.matsprogram.org/. Real pathway
4. Anthropic Fellows program - separate research programs for people outside academia

## What should be in a research scientist candidate's portfolio

- First-author publications at NeurIPS/ICML/ICLR - minimum 2-3
- GitHub with reproduced papers or own research code
- Own research agenda - you must articulate what you want to research and why it matters
- Connection to alignment community - LessWrong, AI Alignment Forum, conferences
- Demonstrated independence - research not as continuation of someone else's agenda, but as your vision

## Alternative entry programs

- Anthropic STEM Fellow - announce on careers page periodically
- Anthropic Research Internship - for PhD students
- MATS - for people transitioning into safety research
- ARENA (Alignment Research Engineer Accelerator) - bootcamp for alignment engineers. https://www.arena.education/
- Constellation Fellowship - for earlier-career safety researchers
- 80,000 Hours - career consulting specific to high-impact AI safety roles

## Interview for Research Scientist

Significantly different from SWE loop:

1. Recruiter screen
2. Research talk - 45-minute presentation of your research, then Q&A. This is the central stage. Not "a project" like for engineers. Full scientific talk
3. Research deep dive - detailed discussion of your agenda
4. Coding round (easier than SWE, but still present)
5. Collaboration round - how you work in a research team
6. Values interview

Main filter - do you have research taste. This is a hard-to-define quality: ability to choose important problems, formulate hypotheses, design experiments that actually test something.

# Main mistakes

1. Skipping math. Visible in 10 minutes at interview. No Cursor saves you when asked to derive attention or explain why gradient vanishing is a mathematical, not engineering problem
2. Technical people without communication. Anthropic is a research-driven company that writes a lot of docs and RFCs. Can't explain your solution five different ways - you don't pass
3. Skipping values round prep. Most common failure point. Prepare like for technical rounds - separately, seriously, in advance
4. Toy GitHub projects. Notebooks with one epoch on MNIST don't count. 2-3 serious projects with production-quality codebase
5. Ignoring open-source. One merged PR to HuggingFace transformers weighs more than all Coursera courses combined
6. Applying "maybe they'll take me" without preparation. After rejection the door opens again in a year, but that's a year lost
7. Over-reliance on AI in learning. AI accelerates everything 5-10x, but you must think yourself. Can't function without Cursor - you don't pass interviews where Cursor is banned
8. Ignoring MCP and Anthropic products. Show you're part of the ecosystem

# Readiness checklist

## Under 70% checked - too early to apply.

Math and theory:

- I can derive backprop by hand
- I understand attention mathematically and can write it in NumPy
- I can explain the difference between cross-entropy and KL-divergence
- I understand scaling laws

Programming:

- Clean Python with type hints, async/await
- PyTorch confidently: wrote and trained a transformer from scratch
- Distributed systems: CAP, consistency models
- LeetCode medium in 25 minutes consistently

ML and LLM:

- Can draw transformer architecture from memory
- Understand differences between pretraining, SFT, RLHF, DPO, Constitutional AI
- Trained a model myself (10M+ parameters)
- Understand inference optimization

Portfolio:

- 3+ serious GitHub projects
- Minimum 1 project with Claude API
- Open-source contribution

Anthropic-specific:

- Read Constitutional AI fully
- Read Responsible Scaling Policy
- Read 5+ Anthropic research posts
- Own view on AI safety
- Used Claude Code and API in real projects

Interview prep:

- 10+ mock interviews
- System design for LLM infrastructure
- Values round: 5+ real stories
- Project deep dive rehearsed

## Where to start tonight

Courses (free):

- Andrej Karpathy "Neural Networks: Zero to Hero" - YouTube
- Harvard Stat 110 - YouTube
- MIT 18.06 Strang - linear algebra
- Fast.ai Practical Deep Learning

Textbooks (open access):

- "Mathematics for Machine Learning" - mml-book.github.io
- "Dive into Deep Learning" - d2l.ai
- "Information Theory, Inference, and Learning Algorithms" - MacKay

Anthropic reading:

- anthropic.com/research
- docs.claude.com
- Constitutional AI paper
- Responsible Scaling Policy

Practical tools:

- Google Colab (free GPUs)
- HuggingFace Spaces
- Kaggle competitions
- Cursor or Claude Code

Communities:

- EleutherAI Discord
- LessWrong and AI Alignment Forum
- Twitter/X - Anthropic engineers are active
- r/MachineLearning

# Final

This is a profession that 5 years ago was accessible only to PhDs from MIT. 3 years ago it opened to strong master's. In 2026 it opens to STEM bachelors with proper preparation. And to self-taught engineers with convincing portfolios.

The bar is higher than ever: you need classical CS stack, production experience, LLM internals, AI safety, and values alignment. Pay reflects this - $710K median total comp.

AI opened the doors. The same AI makes the speedrun viable. An hour with Claude on Strang gives more understanding than a week alone. Mock interviews are available any time. Implementation of an academic paper is an evening instead of a month.

The speedrun doesn't make the profession easy. Math still takes months of work. Distributed systems still need to be understood through scars of production incidents. Values round still filters 50% of technically ready candidates. What AI does - it removes the dead time between effort and feedback. The part of traditional learning where most people gave up.

For the first time in history, the path from zero to Anthropic is technically possible for someone without an MIT diploma. The condition: walk all 7 steps without skipping, and use AI as an acceleration tool rather than a replacement for your own thinking.

# Sources

- Levels.fyi Anthropic (https://www.levels.fyi/companies/anthropic/salaries) - May 2026 data
- Anthropic Careers (https://www.anthropic.com/careers/jobs)
- Greenhouse job board (https://job-boards.greenhouse.io/anthropic)
- Anthropic Research (https://www.anthropic.com/research)
- Constitutional AI paper (Anthropic, 2022)
- Responsible Scaling Policy v3.0
- Hello Interview engineer experiences
- interviewing.io Anthropic guide
- IGotAnOffer Anthropic interview process
- Glassdoor interview reviews
- Actual job descriptions: Research Engineer (RL Velocity, Pretraining Scaling, Discovery)