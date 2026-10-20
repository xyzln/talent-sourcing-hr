# Search Strategy Playbook

> Used with Steps 2 and 3 of the `recruit-web-sourcing` skill. Goal: cover talent supply information systematically within a limited number of search rounds.

## 1. Channel Layering Matrix

| Layer | Channel type | Typical channels | Primary use | Source quality |
|-------|-------------|------------------|-------------|----------------|
| L1 | Job boards | Boss Zhipin, Zhaopin, Liepin, Lagou, 51job; overseas: LinkedIn, Indeed, Glassdoor | Open roles, salary bands, requirements, talent density | High (first-party JDs) |
| L2 | Social & professional communities | Maimai, Zhihu, GitHub, Stack Overflow, V2EX, Juejin, Behance/Dribbble (design) | Candidate leads, real work, technical influence | Medium-high (self-published) |
| L3 | Competitor & industry moves | Competitor career pages, funding/product news, trade media | Competitor expansion direction, talent flow signals | Medium (needs cross-verification) |
| L4 | Industry reports & data | Compensation surveys, talent market reports, platform white papers | Salary benchmarks, supply/demand trends | Medium (check publication date) |

**Execution order**: L1 first for supply density and salary bands, then L2/L3 to mine specific leads, and L4 last to calibrate market conclusions.

## 2. Building the Keyword Matrix

Cross-combine four word families, using 2-4 combinations per search round:

| Word family | Description | Example (Senior Backend Engineer) |
|-------------|-------------|-----------------------------------|
| Role words | Synonyms and variants of the title | Backend Engineer, Server-side Engineer, Java Developer, Backend Engineer |
| Skill words | Hard skills and toolchain | distributed systems, microservices, high concurrency, Kubernetes, Go, Spring Cloud |
| Scenario words | Business scenarios and industry | e-commerce middle platform, payment systems, SaaS, fintech, ad systems |
| Channel words | Sites and in-site targeting | site:zhipin.com, site:linkedin.com, site:github.com |

**Combination examples**:
- "senior backend engineer microservices high concurrency hiring" -> L1 supply
- "site:github.com high-concurrency Java open source" -> L2 technical leads
- "payment system architect hiring salary" -> salary band

## 3. Search Operator Cheat Sheet

| Operator | Purpose | Example |
|----------|---------|---------|
| `site:` | Restrict to a site | `site:liepin.com algorithm engineer` |
| `intitle:` | Term must appear in title | `intitle:hiring data analyst` |
| `filetype:` | Restrict file type | `filetype:pdf compensation report 2025` |
| `""` | Exact match | `"head of user growth"` |
| `-` | Exclude noise | `hiring -training -security` |
| Time filter | Control freshness | Prefer the last 3-12 months for news/roles |

## 4. Supply Density Assessment (how to judge "is talent easy to find?" in Step 3)

Track four metrics per search round and record them in the sourcing report:

1. **Open role volume**: order of magnitude of open roles on L1 channels (e.g., "~500+ open on Boss Zhipin")
2. **Salary band**: mainstream range and percentiles (P25/P50/P75), timestamped
3. **Talent clusters**: which companies/cities/communities the population concentrates in (competitor list)
4. **Scarcity signals**: long-running postings, rising salaries, relaxed requirements (undersupply) or the opposite

**Conclusion tiers**:
- Ample supply (high role volume, stable salaries) -> raise the bar moderately; focus screening on capability match
- Tight supply (few roles, rising salaries, relaxed requirements) -> start early, widen alternative populations, raise the compensation budget
- Structural scarcity (large pool but few meeting hard requirements) -> tighten veto-item priority, target the "nearest neighbor" population

## 5. Common Role Sourcing Paths (quick reference)

| Role type | Priority channels | Lead-mining tactics |
|-----------|-------------------|---------------------|
| Engineering (frontend/backend/algo) | L1 + GitHub/Juejin | Search open-source contributors and tech blog authors |
| Product | L1 + Maimai/Zhihu | Search product-analysis authors and competitor product news |
| Design | L1 + Behance/Dribbble | Browse portfolios directly; reverse-lookup authors by project type |
| Operations/Marketing | L1 + WeChat accounts/Zhihu | Search bylines of well-known campaigns they ran |
| Sales/BD | L1 + Maimai | Reverse-lookup by target customer segment: "who sold to similar customers" |
| Corporate functions (HR/Finance/Legal) | L1 + vertical communities | Reverse-lookup by industry certifications (CPA, bar exam, etc.) |

## 6. Search Discipline

- Each round validates exactly one hypothesis; no kitchen-sink queries
- Cross-verify every conclusion with at least two independent sources; for salary, prefer first-party open JDs over reports
- Timestamp all market data as "data retrieved: YYYY-MM-DD"
- Two consecutive empty rounds -> switch word families or channels; never repeat the same query more than twice
