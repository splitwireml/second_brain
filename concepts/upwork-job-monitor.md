---
title: UpWork Job Monitor
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [automation, agent, project]
sources: [raw/articles/upwork-job-monitor-project-spec.md]
related_entity: [[career-ops]]
---

# UpWork Job Monitor

An autonomous job monitoring agent that polls UpWork's GraphQL API every 15 minutes for new project postings, filters them through a multi-stage pipeline (rule-based + AI tag analysis), and pushes matching jobs to Discord.

## Architecture

### Data Flow

```
UpWork GraphQL API (mostRecentJobsFeed)
    → 15-min polling loop
    → Stage 1: Rule-based deduplication + client quality filters
    → Stage 2: AI tag generation (domain, tech stack, timeline, requirements)
    → Stage 3: Preference matching against generated tags
    → Discord webhook notification
```

### Stage 1 — Rule-Based Filtering

Filters applied to every incoming job:

| Filter | Logic |
|---|---|
| Deduplication | Track seen job IDs across polls |
| Client verification | Reject if `paymentVerificationStatus` is false |
| Client rating | Reject if `totalFeedback` < threshold or `totalHires` = 0 |
| New client | Reject if `totalSpent` below threshold |
| Budget | Reject if `amount.amount` below minimum |
| Hire rate | Reject if `totalHires / totalSpent` ratio too low |
| Invite overload | Reject if `proposalsTier` signals high competition |
| Interviewing | Reject if positive interviewing count |
| Location restrictions | Reject if `prefFreelancerLocationMandatory` is set |

### Stage 2 — AI Tag Generation

Jobs passing Stage 1 are sent to an LLM (e.g., Claude) with the full `description` + `attrs.skills` to generate structured tags:

- **Base domain** — e.g., "chatbot development"
- **Sub-domain** — e.g., "SQL-connected chatbot with visualizations"
- **Technologies** — explicit list from description + skills
- **From scratch vs. integration** — binary determination
- **Timeline** — extracted from description if mentioned
- **Estimated effort** — rough time-box (hours/days/weeks)
- **Requirements depth** — brief, medium, or detailed

### Stage 3 — Preference Matching

User-defined preference tags are compared against AI-generated tags using cosine similarity or keyword overlap. Jobs scoring above a threshold are queued for notification.

### Notification

Selected jobs are formatted as a Discord embed and sent via webhook. Embed contains: title, budget, client summary, key tags, and a direct link.

## UpWork API

### Recent Jobs Feed

**Endpoint:** `https://www.upwork.com/api/graphql/v1?alias=mostRecentJobsFeed`

```graphql
query($limit: Int, $toTime: String) {
  mostRecentJobsFeed(limit: $limit, toTime: $toTime) {
    results {
      id, title, ciphertext, description, type, recno,
      freelancersToHire, duration, engagement,
      amount { amount },
      createdOn, publishedOn,
      prefFreelancerLocationMandatory, connectPrice,
      client { totalHires, totalSpent, paymentVerificationStatus,
               location { country }, totalReviews, totalFeedback,
               hasFinancialPrivacy },
      tierText, tier, tierLabel, proposalsTier, enterpriseJob, premium,
      attrs: skills { id, uid, prettyName, prefLabel },
      hourlyBudget { type, min, max }, isApplied
    }
  }
}
```

### Job Detail (per-job)

**Endpoint:** `https://www.upwork.com/api/graphql/v1?alias=gql-query-jobauthdetails`

Returns: full budget, `totalApplicants`, `totalInvitedToInterview`, `qualifications`, `clientActivity`, `applicantsBidsStats`.

### Auth

Requires `Authorization: Bearer <oauth_token>` header + full cookie jar (`master_access_token`, `user_uid`, `XSRF-TOKEN`, `cf_clearance`, etc.).

## Related Concepts

- [[ai-job-search-automation]] — the broader pattern; this is a specific implementation targeting UpWork
- [[autoresearch]] — the autonomous propose→score→evolve→decide loop applied to marketing copy; same evaluation paradigm
- [[paperclip-orchestrator]] — agent orchestration with human-in-the-loop approval; relevant for multi-stage filtering architecture
- [[ai-freelancer-200-hour-guide]] — the monetization context for why this tool exists (earning income via AI freelancing)
