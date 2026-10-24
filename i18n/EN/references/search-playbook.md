# Real-World Job Design Research Playbook

> Used at Step 2 of the `recruit-web-sourcing` skill. Goal: systematically understand how a real-world role is designed - responsibilities, requirements, workflow, collaboration, KPIs, toolstack - within a limited number of search rounds.

## 1. Channel Layering Matrix

| Layer | Channel type | Typical channels | Main use | Source quality |
|------|-------------|------------------|---------|----------------|
| L1 | Job boards | Boss Zhipin, Zhaopin, Liepin, Lagou, 51job; overseas: LinkedIn, Indeed, Glassdoor | Role responsibilities, requirements, salary bands, hiring density | High (first-party JDs) |
| L2 | Organizational design materials | Job descriptions, leveling systems, R&R tables, org charts, public company handbooks/wiki | Role positioning, reporting lines, responsibility boundaries | High (first-party, but rarely public) |
| L3 | Practitioner communities | Maimai, Zhihu, V2EX, GitHub, Stack Overflow, Juejin, WeChat official accounts, tech blogs | Real workflows, collaboration styles, daily pain points, toolstack | Medium-high (self-published; watch for individual cases) |
| L4 | Industry reports & methodologies | Consulting role models, HR methodologies, Agile/DevOps/ITIL practice frameworks, salary surveys | Design paradigms, KPIs, market benchmarks | Medium (mind publication dates and applicability) |

**Execution order**: start with L1 for responsibilities and requirements, then L2/L3 for workflow, collaboration, and toolstack, and finally use L4 to calibrate design paradigms and KPIs.

## 2. Keyword Matrix Construction

Cross four word families, 2-4 combinations per round:

| Family | Description | Example (Data Analyst) |
|--------|-------------|------------------------|
| Role words | Synonyms and variants of the job title | Data Analyst, Data Operations, BI Engineer |
| Duty words | What the role does | user behavior analysis, reporting systems, A/B testing, metrics framework |
| Scenario words | Business scenarios and industries | e-commerce, SaaS, fintech, ad delivery |
| Design words | Job-design-related material | job description, responsibilities, requirements, performance review, OKR, leveling |

**Combination examples**:
- "data analyst job responsibilities requirements hiring" -> probe L1 for duties and requirements
- "data analyst day in the life workflow" -> mine L3 for the real daily routine
- "data analyst performance review KPI OKR" -> check KPIs
- 'site:zhihu.com "data analyst" "day in the life"' -> targeted practitioner sharing (on Chinese-language sites, run the query in Chinese)

## 3. Search Operator Cheat Sheet

| Operator | Effect | Example |
|----------|--------|---------|
| `site:` | Restrict to a site | `site:linkedin.com data analyst` |
| `intitle:` | Title must contain | `intitle:job description product manager` |
| `filetype:` | Restrict file type | `filetype:pdf job description finance` |
| `""` | Exact match | `"head of user growth"` |
| `-` | Exclude noise | `data analyst -training -security` |
| Time filter | Control freshness | JD/methodology searches prefer the last 3 years |

## 4. Six-Element Job Design Collection Checklist

Walk this table for every role studied; missing items get follow-up searches:

| Element | What to collect | Primary channels |
|---------|----------------|-------------------|
| Responsibilities | What they actually do, broken into executable actions | L1 JDs, L2 job descriptions |
| Requirements | Knowledge, skills, experience, credentials | L1 JDs |
| Workflow | Work steps, order, cadence, checkpoints | L3 practitioner sharing, L4 methodologies |
| Collaboration | What comes in, what goes out, who they report to | L2 org charts, L3 |
| KPIs | What "done well" means (quality/efficiency/outcome) | L4 methodologies, L1 JD nice-to-haves |
| Toolstack | Tools, systems, templates used | L3, L1 JDs |

## 5. Research Paths by Role Type (Quick Reference)

| Role type | Priority channels | Research tips |
|-----------|-------------------|---------------|
| Engineering (frontend/backend/algo) | L1 + GitHub/Juejin/tech blogs | Read JD skill requirements + engineers' own workflow and collaboration write-ups |
| Product | L1 + Maimai/Zhihu/WeChat official accounts | Search for PMs' PRD process and requirement-review write-ups |
| Design | L1 + Behance/Dribbble/Zcool | Read portfolio notes + designers' collaboration process write-ups |
| Operations/Marketing | L1 + WeChat official accounts/Zhihu | Search for named retrospectives of famous campaigns (name + process) |
| Sales/BD | L1 + Maimai/industry media | Reverse-lookup role design from target customer segments ("served similar clients") |
| Functional (HR/finance/legal) | L1 + vertical communities + L4 | Reverse-lookup by industry credentials (CPA, bar qualification, etc.) |
| Management | L2 + L4 + L3 | Focus on reporting lines, collaboration interfaces, and KPIs |

## 6. Search Discipline

- Each round tests one hypothesis; no "everything in one query"
- Cross-verify every conclusion with at least two independent sources; duties and requirements primarily from L1 live JDs, reports as backup
- Timestamp all research conclusions with "data retrieved: YYYY-MM-DD"
- Two consecutive empty rounds -> switch word family or channel; never repeat the same query more than twice
- For community content, distinguish individual cases from consensus: only treat a pattern as job-design evidence when multiple people describe it independently
