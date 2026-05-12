---
title: Interior Design SaaS Project Management Tool
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [idea, saas, product, opportunity]
sources: []
related_entity: [[waleed]]
---

## End Goal

Build a lightweight SaaS tool that replaces WhatsApp for job site communication in interior design companies. Two interfaces: manager (full oversight) and worker (task-focused). Position at a low price point to capture small operations in Bangalore and beyond.

## How Monetizable

- SaaS subscription: Rs 999–2,999/month per company (manager seat + up to 5 worker seats)
- Free tier: 1 project, 3 workers — for trials and small operators
- Upsell: additional projects, additional seats, advanced reporting, custom branding
- One competitor exists in Bangalore market with hidden pricing and likely higher cost; price-to-win

## Vector

SaaS (primary), mobile apps (secondary — mobile-first)

## Target Market

- Primary: Small to medium interior design and finishing companies in Bangalore
- Target size: 2–20 employees, 1 manager + multiple workers per site
- Secondary: Expand to other Indian cities with high interior design market density
- Tertiary: Construction and renovation companies globally (future)

## SRS: Product Requirements

### Multi-User Architecture

- [ ] Manager role: full project visibility, can create/edit projects, assign rooms, approve items
- [ ] Worker role: limited to assigned projects and rooms, can post updates, photos, audio
- [ ] Admin panel: user management, subscription management, project overview
- [ ] Per-seat pricing with seat count enforcement

### Project & Room Management

- [ ] Create project: name, client, address, start date, target completion
- [ ] Named rooms/sections per project (e.g., "Master Bedroom", "Modular Kitchen")
- [ ] Room status: not started / in progress / completed / on hold
- [ ] Per-room photo gallery (chronological, newest first)
- [ ] Project-level progress % (auto-calculated from room statuses)

### Communication Threads

- [ ] Photo threads per room: worker posts photo → adds caption + tags → manager sees thread
- [ ] Audio messages: worker records + posts audio note in a thread (voice update)
- [ ] Text comments on any thread item
- [ ] @mention workers or manager in any comment
- [ ] No WhatsApp number required — all communication stays in-app

### Document Management

- [ ] Upload plan PDFs per project (floor plan, electrical plan, etc.)
- [ ] View documents in-app (PDF viewer)
- [ ] Label and categorize documents (plan, invoice, reference, etc.)
- [ ] Document version history

### Item Lists & Supply Tracking

- [ ] Create item lists per project or per room
- [ ] Item: name, quantity, unit, rate, status (pending / ordered / delivered)
- [ ] Mark items as complete; track pending vs delivered
- [ ] Item list summary per project

### Notifications

- [ ] Push notification on new photo/audio/comment in subscribed threads
- [ ] Email digest option for manager (daily summary)

### Reporting

- [ ] Project status dashboard per manager
- [ ] Completion timeline per project (actual vs target)
- [ ] Activity log per project (who posted what, when)
- [ ] Export project report as PDF

### Mobile Requirements

- [ ] Native mobile app (React Native or Flutter — TBD based on dev speed)
- [ ] Offline-first: photos and audio queue when offline, sync when connected
- [ ] Camera integration for on-site photo/audio capture
- [ ] Fast upload (compressed images, background sync)

## Validation

*[To be filled after validation session]*

## See also

- [[waleed]] — primary user and first customer for the project management tool
- [[alventra-marketing]] — parallel local SEO agency use case for the same target market
