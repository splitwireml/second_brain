---
updated: 2026-04-17
title: UpWork Job Monitor — Project Specification
source: https://www.upwork.com/api/graphql/v1?alias=mostRecentJobsFeed`
type: article
---

# UpWork Job Monitor — Project Specification

> Source: User-provided project spec (pasted content, 2026-01-11)

## Recent Projects Feed API

**Endpoint:** `https://www.upwork.com/api/graphql/v1?alias=mostRecentJobsFeed`

**GraphQL Query:**
```graphql
query($limit: Int, $toTime: String) {
  mostRecentJobsFeed(limit: $limit, toTime: $toTime) {
    results {
      id, uid: id, title, ciphertext, description, type, recno,
      freelancersToHire, duration, engagement,
      amount { amount },
      createdOn: createdDateTime,
      publishedOn: publishedDateTime,
      prefFreelancerLocationMandatory,
      connectPrice,
      client {
        totalHires, totalSpent, paymentVerificationStatus,
        location { country },
        totalReviews, totalFeedback, hasFinancialPrivacy
      },
      tierText, tier, tierLabel, proposalsTier,
      enterpriseJob, premium,
      jobTs: jobTime,
      attrs: skills {
        id, uid: id, prettyName: prefLabel, prefLabel
      },
      hourlyBudget { type, min, max },
      isApplied
    },
    paging {
      total, count,
      resultSetTs: minTime, maxTime
    }
  }
}
```

**Variables:** `{"limit": 10}`

## Job Detail API

**Endpoint:** `https://www.upwork.com/api/graphql/v1?alias=gql-query-jobauthdetails`

**Purpose:** Get detailed info per job — proposals count, invited count, qualifications, budget breakdown, client stats.

**Variables:** `{"id": "~021878008129465158590"}` (job UID)

## Authentication

- **Bearer token:** `oauth2v2_96ac365aa037df4c29925917a22ceae4`
- **Cookies:** Large cookie jar including `visitor_id`, `master_access_token`, `user_uid`, `oauth2_global_js_token`, `XSRF-TOKEN`, `cf_clearance`, etc.

---

## Planned Core Features

1. **Polling Script** — Call mostRecentJobsFeed every 15 minutes
2. **Initial Filtering** — Filter out jobs that:
   - Were present in previous search (deduplication)
   - Have unverified clients
   - Have low-rated clients
   - Are from new clients
   - Have low spend/threshold amount
   - Have low hire rate
   - Have high number of invites
   - Have positive "interviewing" count
   - Have location restrictions
3. **AI Analysis** — Use AI to generate tags for job description:
   - Base project domain (e.g., "chatbot development")
   - Deeper project domain (e.g., "SQL-connected chatbot with visualizations")
   - Project requirements
   - Estimated time to completion
   - Technologies required
   - From scratch vs. integration
   - Mentioned timeline
   - Detailed description
4. **Smart Filtering** — Match generated tags against user preferences
5. **Sample Proposal Generation** — Using knowledge base + settings to generate a proposal
6. **Discord Notifications** — Send selected jobs to Discord

---

## Notes

- The API uses Bearer auth + extensive cookie jar
- Cookie values in spec are likely expired (from ~Jan 2025)
- GraphQL aliased queries (`alias=mostRecentJobsFeed`) may indicate Upwork API versioning