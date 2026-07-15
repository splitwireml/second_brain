---
source_url: https://x.com/cyrilXBT/status/2068135133618540931
ingested: 2026-06-22
sha256: 0eddff19bf3cc5920682e24ca4c8336ca77b8fee45a9e8001b4c35367c6b09e6
---

---
title: "How to Build a Multi-Agent System That Actually Finishes the Job - Full Course"
source: "x-bookmarks"
tweet_id: "2068135133618540931"
tweet_url: "https://x.com/cyrilXBT/status/2068135133618540931"
author_name: "CyrilXBT"
author_handle: "@cyrilXBT"
tweet_date: "Sat Jun 20 00:53:34 +0000 2026"
bookmark_date: "2026-06-20"
content_type: "x_article"
character_count: 24781
retweet_count: 79
like_count: 412
---

# How to Build a Multi-Agent System That Actually Finishes the Job - Full Course

How to Build a Multi-Agent System That Actually Finishes the Job - Full Course

Most multi-agent systems fail in a specific, predictable way.

They start strong. The researcher agent pulls good information. The writer agent produces a solid draft. Everything looks promising for the first two steps. Then somewhere around step three or four, the system stalls. An agent waits for input that never arrives. Another agent declares success on a half-finished task. A third agent loops on the same correction five times without ever resolving it. You come back an hour later to find a system that did a lot of work and finished nothing.

This isn't a multi-agent problem. It's a finishing problem. And finishing is the one thing most multi-agent guides never actually teach, because finishing isn't about adding more agents or smarter prompts. It's about architecture decisions that determine whether a system converges on a result or just generates activity forever.

This course builds a multi-agent system designed around one single principle: every component exists to move the system toward a defined finish line, and nothing in the system is allowed to declare victory without proving it.

By the end you'll have a working four-agent system with explicit success criteria, a verification loop that can't be faked, and a manager that knows the difference between "an agent said it's done" and "the task is actually done."

## Why Multi-Agent Systems Stall

Before building anything, understand the four failure modes that kill most multi-agent setups. Every architecture decision in this course exists specifically to prevent one of these.

Failure mode 1: Undefined done. The system has no explicit definition of what "finished" means. Each agent decides for itself when its part is complete, and those individual definitions never add up to a coherent finished product. The writer thinks a draft is done. The reviewer thinks review is done after one pass. Nobody agreed in advance on what the finished deliverable actually looks like, so the system can run forever without anyone noticing it never actually finished.

Failure mode 2: No verification, just self-report. An agent says "task completed successfully" and the system believes it. This is the single most common failure in production multi-agent systems. An agent that fabricates 14% of its output while reporting full success is worse than an agent that fails loudly, because the failure is invisible until a human discovers it downstream.

Failure mode 3: Unbounded loops. An agent gets stuck correcting the same issue repeatedly because nothing tells it when to stop trying and escalate instead. Five retries of the same failed fix isn't progress. It's the system pretending to work while actually being stuck.

Failure mode 4: No handoff protocol. Agent A finishes its piece and Agent B has no clear instruction for what to do with it, what format to expect, or what to do if the input is malformed. The system breaks at the seams between agents, not inside any individual agent.

Every piece of architecture in this course maps directly to fixing one of these four failures.

## The Four-Agent Architecture

This system uses four specialized agents instead of one generalist, because specialization is what makes verification possible. A single agent verifying its own work is checking its own homework. Four agents with distinct roles and a manager that enforces handoffs between them creates actual accountability.

The Researcher. Gathers information, only information. Does not draft, does not analyze beyond organizing what it found. Its only job is producing a structured research brief that the next agent can use without re-researching anything.

The Builder. Takes the research brief and produces the actual deliverable, whether that's a written piece, a piece of code, a plan, or a design. Does not verify its own output. Does not decide when it's done. It builds, then hands off.

The Judge. Verifies the Builder's output against explicit, predefined success criteria. Rejects work that doesn't meet the bar, and specifically states why, not just that it failed. Never rewrites the work itself. Its only job is grading and providing specific correction feedback.

The Manager. Owns the entire process. Defines the success criteria before anything starts, enforces the sequence between agents, decides when a rejected piece of work goes back for revision versus when it needs escalation to a human, and is the only agent allowed to declare the overall task finished.

This separation is the actual unlock. The Builder cannot grade itself. The Judge cannot fix what it rejects. The Manager cannot build or judge. Each agent is structurally prevented from cutting corners because the next agent in the chain has no incentive to let bad work through.

## Step 1: Define Done Before You Write a Single Prompt

This is the step almost everyone skips, and it's the reason almost everyone's multi-agent system never converges.

Before building any agent, write the actual definition of finished for your specific task. Not a vague goal. A checklist specific enough that a stranger could look at the output and the checklist and determine pass or fail without asking you anything.

# Definition of Done — [TASK NAME]

## The Deliverable
[Exactly what gets produced. Not "a good article."
A 1,500-word article with three sourced statistics,
a clear thesis stated in the first 100 words, and
a call to action in the final paragraph.]

## Required Properties
- [ ] Property 1, stated as a testable condition
- [ ] Property 2, stated as a testable condition
- [ ] Property 3, stated as a testable condition

## Disqualifying Conditions
[Things that automatically fail regardless of
anything else being correct. Example: any
unsourced statistical claim. Example: any
section under 100 words.]

## Success Threshold
[What percentage or count of required properties
must pass for the Judge to approve. Be explicit.
"Most of the requirements" is not a threshold.
"All required properties plus zero disqualifying
conditions" is a threshold.]

Here's a worked example for a real task, building a technical blog post:

# Definition of Done — Technical Blog Post on RAG Optimization

## The Deliverable
A 2,500 to 3,000 word technical article explaining
four specific memory optimization techniques for
RAG systems, with working code for each technique.

## Required Properties
- [ ] Contains working, syntactically valid Python
      code for all four techniques
- [ ] Each technique includes a stated expected
      memory reduction percentage
- [ ] Includes a benchmark or measurement section
      readers can run themselves
- [ ] Written in active voice, no AI cliché phrases
- [ ] Every technical claim is either demonstrated
      in code or explicitly marked as a general guideline

## Disqualifying Conditions
- Any code block that would raise a syntax error
- Any memory reduction claim with no supporting
  explanation of why it works
- Word count under 2,200 or over 3,500

## Success Threshold
All required properties must pass.
Zero disqualifying conditions present.
No partial credit on code correctness.

This document is not optional setup work. It is the spine of the entire system. The Judge will use this exact document to grade. The Manager will use it to decide whether to approve or escalate. Without it, "done" is a feeling instead of a fact, and feelings are exactly what cause multi-agent systems to drift forever without finishing.

## Step 2: Build the Researcher

The Researcher's entire job is producing one structured artifact: a research brief the Builder can use without doing any additional research of its own.

# researcher-agent

## Role
You gather information only. You do not draft,
analyze beyond organization, or make recommendations
about what the final deliverable should say.

## Input
A task description and the Definition of Done document.

## Process

1. Identify every factual claim, statistic, or piece
   of external information the Definition of Done
   implies will be needed.

2. Search for and verify each one against credible
   sources. Note the source for everything.

3. Identify gaps: information the task needs that
   you could not find or verify. Flag these explicitly
   rather than guessing or fabricating to fill them.

4. Organize findings into the structured brief below.
   Do not write prose for the final deliverable.
   Only organize raw material.

## Output Format

---
# Research Brief — [TASK]

## Verified Facts
1. [Fact] — Source: [citation]
2. [Fact] — Source: [citation]

## Relevant Context
[Background information the Builder needs but that
isn't a discrete citable fact]

## Gaps Identified
[Anything the Definition of Done requires that
could not be verified. Be explicit. The Builder
needs to know what it cannot claim with confidence.]

## Confidence Assessment
[Overall: how solid is this research foundation?
HIGH / MEDIUM / LOW, with one sentence justifying it.]
---

## Hard Rule
Never pass unverified information to the Builder
as if it were verified. An unflagged gap here becomes
a fabricated claim downstream, and that failure is
much harder to catch later than it is to flag now.

The "Gaps Identified" section is the single most important part of this entire agent. Most multi-agent failures around fabrication trace back to a Researcher that quietly filled a gap instead of flagging it. Forcing explicit gap identification means the Builder either finds the missing information itself, asks for help, or clearly marks the resulting content as a general statement rather than a verified fact. None of those outcomes are fabrication. Silent gap-filling is.

## Step 3: Build the Builder

The Builder produces the actual deliverable from the research brief. Its only job is building, never verifying.

# builder-agent

## Role
You produce the deliverable described in the
Definition of Done, using only the Research Brief
as your factual foundation. You do not grade your
own output. You do not decide when you're finished
beyond producing a complete first attempt.

## Input
The Definition of Done document.
The Research Brief from the Researcher agent.
If this is a revision: the Judge's specific
rejection feedback from the previous round.

## Process

1. Read the Definition of Done fully before
   producing anything.

2. Read the Research Brief. Note any flagged gaps.
   For each gap, either omit any claim that depends
   on it, or explicitly mark the relevant content
   as general guidance rather than a verified fact.

3. Produce the complete deliverable, addressing
   every Required Property in the Definition of Done.

4. If this is a revision cycle: address every single
   point in the Judge's rejection feedback specifically.
   Do not regenerate from scratch unless the feedback
   says the entire approach was wrong. Targeted fixes
   only, to avoid introducing new problems while
   fixing old ones.

5. Before handing off, self-check against the
   Required Properties list as a final pass.
   This is not verification. This is just making
   sure you didn't forget to attempt something.

## Output Format
The complete deliverable, plus:

---
## Builder Notes
- Gaps from research that affected this draft: [list]
- Required Properties I'm confident are met: [list]
- Required Properties I'm uncertain about: [list]
---

## Hard Rule
The "uncertain about" section must be honest.
An agent that always claims full confidence is
giving the Judge no useful signal. Flag genuine
uncertainty. That's not a weakness in your output,
it's information the Judge needs.

The Builder Notes section matters because it gives the Judge a starting point instead of grading from zero every time. An honest "I'm uncertain about the code's edge case handling" from the Builder tells the Judge exactly where to look first.

## Step 4: Build the Judge

The Judge is the agent that prevents the entire system from declaring false victories. This is the component most multi-agent tutorials skip entirely, and it's exactly why those tutorials produce systems that don't finish reliably.

# judge-agent

## Role
You verify the Builder's output against the
Definition of Done. You do not rewrite or fix
anything. You grade, and you provide specific,
actionable feedback when rejecting.

## Input
The Definition of Done document.
The Builder's complete output and Builder Notes.

## Process

1. Go through every Required Property in the
   Definition of Done one at a time. For each one,
   determine pass or fail with specific evidence
   from the actual output, not a general impression.

2. Check every Disqualifying Condition explicitly.
   A single disqualifying condition present means
   automatic rejection regardless of how good
   everything else is.

3. For code: actually trace through the logic.
   Don't assume code is correct because it looks
   plausible. If you cannot fully verify correctness,
   say so explicitly rather than approving on faith.

4. For factual claims: cross-reference against the
   Research Brief. Any claim not traceable to a
   verified fact or explicitly marked as general
   guidance is a fabrication and an automatic
   rejection regardless of how reasonable it sounds.

5. Compare the Builder's self-reported confidence
   against your own findings. A mismatch where the
   Builder claimed confidence on something you find
   actually wrong is worth flagging separately,
   since it suggests a pattern worth correcting.

## Output Format

---
# Judge Verdict — [TASK]

## Verdict: PASS / REJECT

## Required Properties Checklist
- [Property]: PASS / FAIL — [specific evidence]
- [Property]: PASS / FAIL — [specific evidence]

## Disqualifying Conditions Check
- [Condition]: PRESENT / NOT PRESENT — [evidence]

## If REJECTED: Specific Correction Instructions
[Not "make it better." Exact, actionable fixes.
"The second code block raises a KeyError on empty
input, add input validation before the dictionary
lookup on line 14" — that level of specificity.]

## Confidence Mismatch Flag
[Did the Builder claim confidence on something
that's actually wrong? Note it if so.]
---

## Hard Rule
Never approve based on overall impression.
Every single Required Property gets individually
checked against evidence. "Looks good overall"
is not a verdict, it's the exact failure mode
this agent exists to prevent.

This level of specificity in the rejection feedback is what prevents the unbounded loop failure mode. A Builder that receives "the second code block raises a KeyError on empty input, add validation on line 14" can fix exactly that. A Builder that receives "needs more polish" will guess, possibly introduce new problems, and the system loops without converging.

## Step 5: Build the Manager

The Manager is the only agent that owns the full lifecycle and the only agent permitted to declare the overall task finished or escalate it to a human.

# manager-agent

## Role
You own the entire process from task receipt to
final delivery. You do not build or judge anything
yourself. You sequence the other agents, enforce
the Definition of Done, and make the call on
revision versus escalation.

## Input
The original task request.

## Process

1. If a Definition of Done doesn't already exist
   for this task type, create one before doing
   anything else. Do not proceed without it.

2. Dispatch to Researcher. Receive Research Brief.
   If the Confidence Assessment is LOW, decide
   whether to proceed with explicit gap flags or
   escalate for human input on the missing pieces
   before continuing.

3. Dispatch to Builder with the Research Brief
   and Definition of Done.

4. Dispatch Builder's output to Judge.

5. On Judge PASS: deliver the final output.
   The task is finished. State explicitly that
   it is finished and why, citing the passed checklist.

6. On Judge REJECT: send the specific correction
   instructions back to Builder for a revision cycle.

7. Track revision cycles. This is the critical
   anti-loop mechanism:

   - Cycle 1-2 rejected: normal revision flow,
     dispatch back to Builder
   - Cycle 3 rejected: the Judge's feedback
     pattern gets re-examined. Is the same
     property failing repeatedly? If so, the
     Definition of Done itself may be unclear
     or unrealistic, not the Builder's execution.
   - Cycle 4 rejected: stop. Escalate to a human
     with the full history: original task,
     Definition of Done, all four Builder attempts,
     and all four Judge verdicts. Do not attempt
     a fifth cycle automatically.

8. Maintain a log of every cycle, every verdict,
   and every decision point for the final report.

## Output Format

---
# Task Status Report — [TASK]

## Status: COMPLETE / ESCALATED

## If COMPLETE
[The final deliverable, plus a summary of which
cycle it passed on and confirmation against the
full Required Properties checklist.]

## If ESCALATED
[Full history of all attempts, the specific
property or condition that kept failing, and
a recommendation for what a human should look
at first.]
---

## Hard Rule
Never declare COMPLETE without a PASS verdict
from the Judge against the actual Definition of Done.
Never run a fifth revision cycle automatically.
Four failed attempts at the same task is a strong
signal that something structural is wrong, either
with the Definition of Done or the Researcher's
input, and more automated retries won't fix
a structural problem.

The four-cycle cap with mandatory escalation is the direct fix for the unbounded loop failure mode. It converts "the system might run forever" into "the system either finishes or tells you exactly why it can't, within a bounded number of attempts."

## Step 6: Wire the Handoffs Explicitly

The fourth failure mode, broken handoffs, gets fixed by making every handoff between agents a structured data object instead of a loose conversational message.

# handoff_schema.py

class ResearchBrief:
    def __init__(self, verified_facts, context, gaps, confidence):
        self.verified_facts = verified_facts  # list of (fact, source)
        self.context = context                # string
        self.gaps = gaps                       # list of strings
        self.confidence = confidence           # "HIGH" / "MEDIUM" / "LOW"

class BuilderOutput:
    def __init__(self, deliverable, gaps_affecting_draft, 
                 confident_properties, uncertain_properties):
        self.deliverable = deliverable
        self.gaps_affecting_draft = gaps_affecting_draft
        self.confident_properties = confident_properties
        self.uncertain_properties = uncertain_properties

class JudgeVerdict:
    def __init__(self, verdict, property_results, 
                 disqualifying_conditions, correction_instructions):
        self.verdict = verdict  # "PASS" / "REJECT"
        self.property_results = property_results  # dict
        self.disqualifying_conditions = disqualifying_conditions
        self.correction_instructions = correction_instructions

class TaskCycle:
    def __init__(self, cycle_number, builder_output, judge_verdict):
        self.cycle_number = cycle_number
        self.builder_output = builder_output
        self.judge_verdict = judge_verdict


def run_multi_agent_task(task_description, definition_of_done):
    """
    Orchestration function implementing the Manager's
    sequencing logic with the hard four-cycle cap.
    """
    research_brief = call_researcher_agent(
        task_description, definition_of_done
    )

    if research_brief.confidence == "LOW":
        escalate_for_human_input(research_brief)
        return

    cycles = []
    max_cycles = 4
    correction_feedback = None

    for cycle_number in range(1, max_cycles + 1):
        builder_output = call_builder_agent(
            definition_of_done, 
            research_brief, 
            correction_feedback
        )

        judge_verdict = call_judge_agent(
            definition_of_done, 
            builder_output
        )

        cycles.append(TaskCycle(cycle_number, builder_output, judge_verdict))

        if judge_verdict.verdict == "PASS":
            return deliver_complete_task(builder_output, cycles)

        correction_feedback = judge_verdict.correction_instructions

        if cycle_number == 3:
            check_for_structural_failure(cycles)

    return escalate_to_human(task_description, definition_of_done, cycles)


def check_for_structural_failure(cycles):
    """
    After cycle 3, check if the same property has 
    failed across multiple attempts. Repeated identical
    failures suggest the Definition of Done itself
    needs revision, not another Builder attempt.
    """
    failed_properties_by_cycle = [
        {k for k, v in c.judge_verdict.property_results.items() if v == "FAIL"}
        for c in cycles
    ]
    
    persistent_failures = set.intersection(*failed_properties_by_cycle)
    
    if persistent_failures:
        print(
            f"Warning: properties {persistent_failures} have "
            f"failed across all attempts so far. This may "
            f"indicate an unclear or unrealistic Definition "
            f"of Done rather than a Builder execution problem."
        )

This schema does two things that loose conversational handoffs can't. It forces every agent to produce exactly the fields the next agent needs, eliminating ambiguity about what was actually communicated. And it makes the entire cycle history inspectable as data, which is what lets the structural failure check at cycle three actually work, since you can programmatically compare property failures across cycles instead of relying on an agent to remember and notice a pattern in conversation.

## Step 7: Test the System Against Its Own Failure Modes

Before trusting this system on a real task, deliberately test each of the four failure modes you built it to prevent.

Test undefined done: Run the system with a deliberately vague Definition of Done, missing the Required Properties section entirely. Confirm the Manager refuses to proceed rather than guessing at what "done" means.

Test fabrication: Feed the Builder a Research Brief with an explicit gap flagged, then check whether the resulting deliverable either omits the gapped claim or marks it clearly as general guidance rather than presenting it as fact. If the Builder fabricates to fill the gap anyway, the Judge should catch it on the cross-reference check and reject.

Test the unbounded loop: Deliberately write a Definition of Done with one impossible-to-satisfy Required Property. Confirm the system escalates at cycle four instead of running a fifth cycle, and confirm the structural failure warning fires at cycle three.

Test broken handoffs: Manually corrupt one field in a handoff object, like an empty verified_facts list, and confirm the receiving agent flags the problem rather than silently proceeding with missing information.

A system that passes all four of these tests has actually been built to finish jobs, not just to demonstrate impressive-looking output on a clean happy-path run.

## What Changes When the System Actually Finishes

Once this architecture is running, the difference from a typical multi-agent setup shows up immediately on the first real task. Instead of returning after an hour to an ambiguous pile of partial outputs, you get one of exactly two things: a completed deliverable that passed every Required Property against an explicit checklist, or an escalation report telling you precisely which property kept failing and across how many attempts.

That binary outcome is the entire point. A multi-agent system that can produce ambiguous results isn't actually multi-agent engineering. It's multiple uncoordinated single-agent sessions running in the same conversation. The Definition of Done, the role separation between Builder and Judge, the structured handoffs, and the hard cycle cap are what convert a collection of capable agents into a system that converges on an answer instead of generating activity indefinitely.

Build the Definition of Done for your specific task first, before writing a single agent prompt. Build the four agents in the order in this course, Researcher, Builder, Judge, Manager, testing each one's handoff format before moving to the next. Run the four failure-mode tests before trusting it on anything real.

The system that finishes the job isn't the one with the smartest individual agents.

It's the one where no agent is allowed to declare victory without proving it, and no failure is allowed to loop forever without surfacing to a human who can actually fix it.

Follow @cyrilXBT for every multi-agent architecture, loop engineering build, and autonomous system design that makes your AI workflows actually finish what they start.
