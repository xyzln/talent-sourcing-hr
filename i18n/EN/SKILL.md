---
name: recruit-web-sourcing
description: Agent design workflow - hand the agent-building job to Agent's HR. Use when the user doesn't know how to create an agent or generate sub-agents: first research how the corresponding real-world role is designed (responsibilities, requirements, workflow, collaboration, KPIs), then translate the job design into agent persona, skills, tools, workflow, and guardrails, and generate a shippable agent spec. Covers the full five-step flow: clarify needs, study job design, map job to agent, score design coverage, and generate the spec.
slug: recruit-web-sourcing-en
displayName: Agent's HR - Job-Design Research & Agent Generation
version: 1.1.0
summary: Agent's HR: study how the real-world role is designed, then generate the matching agent
tags: ['agent-design', 'job-design-research', 'sub-agent-generation']
license: MIT
agent_created: true
---
# Job-Design Research & Agent Generation Workflow

## Purpose

Turn "I want to build an agent but don't know how to design it" into a shippable agent spec: first research how the corresponding real-world role is designed, then translate the job design item by item into an agent design, and finally verify design completeness with a coverage score.

## When to Use

- The user says "I don't know how to make an agent / sub-agent / skill", or asks "how should this agent be designed"
- The user describes what the agent should do but can't produce a structured design
- The user wants to turn a real-world role into an agent
- The user needs a design spec for an expert package, standalone skill, or sub-agent

## Five-Step Workflow

### Step 1: Clarify Needs

Confirm four things; ask when information is missing, never assume:

- **Purpose**: what will this agent do, for whom, used by whom?
- **Scenario**: typical tasks and inputs/outputs?
- **Form**: expert package / standalone skill / sub-agent (determines the spec format and activation method)
- **Boundaries**: what it explicitly does not do, and the red lines

### Step 2: Study the Real-World Job Design

Research web-wide how the corresponding role is designed, collecting six elements. Method and channels in `references/search-playbook.md`:

- **Responsibilities**: what the person in this role actually does (broken into executable actions)
- **Requirements**: what makes them competent (knowledge, skills, experience, credentials)
- **Workflow**: real work steps, order, and checkpoints
- **Collaboration**: who they deal with, what gets handed over, who receives the output
- **KPIs**: what "done well" means (quality, efficiency, outcome standards)
- **Toolstack**: tools, systems, and methods used

Search discipline: log query, channel, hit count, source quality, and retrieval date each round; cross-verify every conclusion with at least two independent sources; when nothing is found, say so and suggest how to widen the search; never fabricate.

### Step 3: Map Job to Agent

Translate job design elements into agent design elements; mapping rules in `references/capability-matching-model.md`:

| Job element | Agent design element |
|-------------|---------------------|
| Role positioning | frontmatter description + persona section |
| Responsibilities | skill list + workflow steps |
| Requirements | capability anchors + guardrails |
| Workflow | workflow steps and checkpoints |
| Collaboration | input/output spec and handoff protocol |
| KPIs | acceptance criteria and quality bars |
| Toolstack | tool and script list |

Every mapping must trace back to the job research evidence from Step 2; elements absent from the real job must not appear in the agent.

### Step 4: Score Design Coverage

1. Break the agent design into 5-8 scoreable dimensions (persona clarity, responsibility coverage, workflow completeness, collaboration interface, acceptance criteria, tooling, boundary clarity, etc.)
2. Score each dimension against job research evidence on the 0-5 anchor scale; no evidence, no score
3. Run `scripts/match_score.py` for the weighted coverage (input: scoring JSON; output: total, grade, strong-coverage items, gap items, veto flags)
4. See `references/capability-matching-model.md` for the scoring model, anchor examples, and grade thresholds
5. For gapped dimensions, return to Step 3 to add design or Step 2 to add research, then rescore

### Step 5: Generate the Agent Spec

Follow `references/report-template.md` for the full spec: conclusion first (what this agent is, its job-design basis, coverage grade), job design research summary (six elements + sources), agent design spec (frontmatter, persona, skills, workflow, tools, guardrails, acceptance criteria), coverage details with gap-fix suggestions, and the landing form (expert package / skill / sub-agent) with activation steps. End with 3 immediately executable next actions for the user.

## Iron Rules

- Job-design research uses publicly available sources only (JDs, organizational design materials, industry reports, practitioner sharing); every conclusion carries its source and retrieval date; nothing is fabricated
- Every agent design element must come from job research evidence; no invented capabilities
- Never design agents for cheating, fraud, discrimination, regulatory evasion, or privacy violations
- Coverage scores are evidence-based only; no evidence = 0 points, marked "to be verified"
- Ask first when needs are unclear; never generate a design on wrong assumptions
