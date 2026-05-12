---
title: "Dokploy vs Coolify"
created: 2026-04-16
updated: 2026-04-16
type: comparison
tags: [comparison, platform, self-hosted]
sources: [raw/articles/dokploy-dokploy-2026-04-16.md, raw/articles/coollabsio-coolify-2026-04-15.md]
participants:
  - [[dokploy]]
  - [[coolify]]
---

# Dokploy vs Coolify

Side-by-side comparison of two leading open-source, self-hostable PaaS alternatives to Vercel, Heroku, and Netlify. Both let you deploy full-stack applications, databases, and services on your own servers — but the underlying architecture, ecosystem maturity, and go-to-market differ substantially.

## At a Glance

| | [[dokploy]] | [[coolify]] |
|--|--|--|
| **Stars** | 33,044 | 53,044 |
| **Forks** | 2,349 | 4,064 |
| **License** | Custom (source-available) | Apache-2.0 |
| **Language** | TypeScript (monorepo: `apps/` + `packages/`) | PHP |
| **Created** | April 2024 | January 2021 |
| **Default branch** | `canary` (bleeding edge) | `main` |
| **Install** | `curl -sSL https://dokploy.com/install.sh \| sh` | `curl -fsSL https://cdn.coollabs.io/coolify/install.sh \| bash` |
| **Paid cloud** | app.dokploy.com | app.coolify.io |
| **Community** | Discord (linked from README) | GitHub Sponsors, HN, Product Hunt featured |

## Core Philosophy

**Dokploy** is Docker-native from the ground up. Every application, database, and service runs as a container managed by the Dokploy agent on the target server. The pitch is a free, self-hostable Vercel/Heroku/Netlify with Traefik, Docker Compose, and Docker Swarm built in.

**Coolify** uses SSH-based server management — it connects to registered servers via SSH and writes configuration directly to them. The pitch is "the ease of a cloud with your own servers, no vendor lock-in." All configs persist on the server; removing Coolify doesn't stop running resources.

## Feature-by-Feature Comparison

### Application Deployment

| Dimension | [[dokploy]] | [[coolify]] |
|-----------|------------|-------------|
| Runtimes | Node.js, PHP, Python, Go, Ruby, any Docker image | Any language/runtime via Dockerfile or built-in buildpacks |
| Build options | Docker-based builds | SSH-based builds with buildpack and Dockerfile support |
| Docker Compose | Native first-class support | Supported |
| Pre-built templates | Templates marketplace (Plausible, Pocketbase, Calcom, etc.) | 280+ one-click services |
| SSL/TLS | Traefik auto-provisions via Let's Encrypt | Traefik auto-provisions via Let's Encrypt |
| Rollback | Not explicitly documented | Not explicitly documented |

### Database Support

| Database | [[dokploy]] | [[coolify]] |
|----------|------------|-------------|
| PostgreSQL | Yes | Yes |
| MySQL | Yes | Yes |
| MariaDB | Yes | Yes |
| MongoDB | Yes | Yes |
| Redis | Yes | Yes |
| Automated backups | Yes (to external storage destinations) | Yes |
| One-click provision | Templates | 280+ services catalog |

### Multi-Node and Scaling

| Dimension | [[dokploy]] | [[coolify]] |
|-----------|------------|-------------|
| Architecture | Docker Swarm cluster | Multiple registered servers via SSH |
| Cluster management | Docker Swarm (native) | Independent servers, not a cluster |
| Cross-node networking | Docker overlay network | Per-server, managed independently |
| Load balancing | Traefik (integrated) | Traefik (integrated) |
| Shared storage | Docker volumes | Per-server storage |

**Implication:** Dokploy's Docker Swarm approach means true container orchestration across nodes (service replication, distributed scheduling). Coolify's SSH multi-server approach gives you independent deployment targets — you manually distribute workloads across servers.

### Resource Monitoring

| | [[dokploy]] | [[coolify]] |
|--|--|--|
| CPU monitoring | Per resource, real-time | Per resource, real-time |
| Memory monitoring | Per resource, real-time | Per resource, real-time |
| Storage monitoring | Per resource, real-time | Per resource, real-time |
| Network monitoring | Per resource, real-time | Per resource, real-time |
| Alerting/Notifications | Slack, Discord, Telegram, Email | Slack, Discord, Telegram, Email |

### Developer Experience

| Dimension | [[dokploy]] | [[coolify]] |
|-----------|------------|-------------|
| CLI | Dokploy CLI (dokploy/cli repo) | Coolify CLI |
| REST API | Full REST API | Yes |
| Web dashboard | Yes | Yes |
| Git integration | Yes (GitHub, GitLab, etc.) | Yes |
| Webhooks | Not explicitly documented | Not explicitly documented |
| Team/multi-user | Not explicitly documented | Teams support |

### Installation and Architecture

| | [[dokploy]] | [[coolify]] |
|--|--|--|
| Target server | Docker required | SSH access required |
| Local agent | Docker agent/service on target | None (pure SSH) |
| Management server | Runs as Docker container | Runs on a dedicated "management" server |
| Requirements | Docker on target servers | SSH to target servers |
| Architecture type | Container-native (agent-based) | Configuration-as-code via SSH |

## Ecosystem and Community

### [[coolify]] Ecosystem

Coolify has a massive enterprise sponsor ecosystem — a direct signal of commercial adoption:

- **Huge sponsors:** MVPS (VPS), SerpAPI (Google Search API), ScreenshotOne (screenshots)
- **Infrastructure sponsors:** Hetzner, Hostinger, RunPod, American Cloud, LiquidWeb, Ramnode, VPSDime, GoldenVM, Ubicloud, CubePath, PetroSky Cloud
- **Developer tool sponsors:** Supabase, Tigris, Convex, ByteBase, Logto, Tolgee, Formbricks, Arcjet, Greptile, CodeRabbit
- **Recognitions:** Hacker News front page, Product Hunt featured, Trendshift listed

This sponsor list represents real production deployments at scale.

### [[dokploy]] Ecosystem

Dokploy is younger (April 2024) with a smaller but growing community:
- Discord for help/discussions (linked from README)
- GitHub Sponsors for maintainer funding
- Templates marketplace as a differentiator (curated one-click app configs)
- canary default branch signals active development

## License Implications

| | [[dokploy]] | [[coolify]] |
|--|--|--|
| License type | Custom source-available | Apache-2.0 (OSI-approved) |
| Commercial use | Restricted (read the custom license) | Freely usable in commercial products |
| Modification | Restricted | Permitted |
| Distribution | Restricted | Permitted |
| Attribution | Required | Required |

For enterprise or commercial deployments, the Apache-2.0 license on Coolify removes legal ambiguity. Dokploy's custom license requires review.

## Repository Structure

**Dokploy** (TypeScript monorepo):
```
apps/       # Main application code
packages/   # Shared packages
.github/    # GitHub workflows and assets
```

**Coolify** (PHP, broader structure):
```
app/          # Main application
bootstrap/    # bootstrapping
database/     # DB migrations
docker/       # Docker-related files
lang/         # Localization
routes/       # API/web routes
templates/    # One-click service templates
tests/        # Test suite
```

## When to Choose Which

### Choose [[coolify]] if:
- You need Apache-2.0 licensing for commercial/enterprise use
- You want a more mature project (5 years old, 53K stars)
- You prefer SSH-based management with zero vendor lock-in (configs stay on servers)
- You need the 280+ one-click services catalog
- You want stronger ecosystem signal (major infrastructure sponsors)
- You need teams/multi-user support
- You want enterprise-backed tooling with recognized HN/PH visibility

### Choose [[dokploy]] if:
- Your infrastructure is already Docker-native and you want tight container integration
- You prefer TypeScript for potential customizations or plugin development
- You want Docker Swarm-based clustering (true container orchestration across nodes)
- You're drawn to the templates marketplace for faster initial setup
- You prefer a more modern stack (TypeScript monorepo vs PHP)
- You accept the custom license for the feature set

## Verdict

**[[coolify]] wins on ecosystem maturity, licensing clarity, and breadth of one-click services.** The Apache-2.0 license, enterprise sponsor list (Hetzner, Hostinger, Supabase, etc.), and 5-year development runway make it the safer choice for production commercial deployments.

**[[dokploy]] wins on Docker-first architecture and TypeScript ecosystem fit.** If your stack is container-native and you want true Docker Swarm orchestration, or if you're a TypeScript shop that might extend the platform, Dokploy's opinionated Docker-native design is compelling. The rapid growth to 33K stars in ~2 years signals strong product-market fit.

**Bottom line:** Both are viable self-hosted Vercel/Heroku alternatives. The deciding factor is usually not features but architecture preference: want Docker Swarm containers + TypeScript? Go Dokploy. Want SSH portability + Apache-2.0 + mature ecosystem? Go Coolify.
