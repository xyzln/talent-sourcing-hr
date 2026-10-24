# Agent Design Spec Template

> Used at Step 5 of the `recruit-web-sourcing` skill. Structure every agent design conclusion this way - conclusion first.

---

# "{Agent Name}" Agent Design Spec

- **Requester**: {user/team}
- **Purpose**: {what this agent does}
- **Landing form**: {expert package / standalone skill / sub-agent}
- **Data retrieved**: {YYYY-MM-DD}
- **Designer**: Agent's HR

## 1. Conclusion First (TL;DR)

Answer the user's three biggest questions in 3-5 sentences:

1. **What this agent is**: one-line positioning + the real-world role it corresponds to
2. **Design basis**: which job-design elements the research covered, and source quality
3. **Coverage and landing**: coverage total and grade + recommended landing form and next step

## 2. Job Design Research Summary

| Element | Research finding | Evidence (source + date) |
|---------|-----------------|--------------------------|
| Responsibilities | … | … |
| Requirements | … | … |
| Workflow | … | … |
| Collaboration | … | … |
| KPIs | … | … |
| Toolstack | … | … |

> Elements not found are honestly marked "not found", with the impact on the design explained.

## 3. Agent Design Spec

### 3.1 Frontmatter

```yaml
---
name: {agent-name}
description: {when to activate this agent - purpose + trigger}
displayName:
  zh: {Chinese display name}
  en: {English display name}
profession:
  zh: {profession (zh)}
  en: {profession}
---
```

### 3.2 Persona

{2-4 sentences: who this agent is, what problem it solves, its methodology, how it differs from a generic agent}

### 3.3 Core Capabilities

{3-5 items, each mapping to responsibilities/requirements from the job research, with evidence sources noted}

### 3.4 Workflow

{Step by step, each with explicit actions, inputs, outputs, and checkpoints; mirrors the real job workflow}

### 3.5 Tools and Scripts

{Tools and scripts needed; write "none, pure dialogue flow" if there are none}

### 3.6 Guardrails

{What it won't do, compliance red lines, when it refuses to execute}

### 3.7 Acceptance Criteria

{What "done well" means for this agent - corresponding to the job's KPIs}

## 4. Design Coverage Details

| Design dimension | Weight | Tier | Score | Evidence |
|------------------|--------|------|-------|----------|
| … | … | core | … | … |
| **Weighted total** | 1.0 | — | **XX** | Grade: A/B/C/D |

**Gap items and fix suggestions**: {for every dimension <3, the specific action to add research or design}

## 5. Landing Form

- **Recommended form**: {expert package / standalone skill / sub-agent} + one-line rationale
- **Activation steps**: {which directory to copy to, how to activate, how to verify}

## 6. Risks and Fallbacks

| Risk | Impact | Response |
|------|--------|----------|
| Insufficient job research evidence | Low design coverage | Widen search channels; prioritize L1/L2 first-party materials |
| Job elements span multiple roles | Design sprawl | Converge on core responsibilities; split into multiple agents |
| Wrong landing form | Wrong activation method | Reassess the form by usage frequency and reusability |

## 7. Next Actions (for the user)

1. …
2. …
3. …

---

*This spec is based on publicly available job-design research; retrieval dates are listed at the top. Agent design is for productivity only - never for cheating, fraud, discrimination, or regulatory evasion.*
