---
name: recruit-web-sourcing
description: Enterprise talent sourcing workflow - hand the job to a precisely matched agent temp worker. Use when the user provides role requirements or business needs and asks for web-wide talent search, capability-based matching of candidate leads, or sourcing reports. Covers the full five-step flow: requirement structuring, search strategy design, multi-round web search, capability modeling and scoring, and report output.
slug: recruit-web-sourcing-en
displayName: Talent Sourcing Officer - Web Sourcing & Capability Matching
version: 1.0.0
summary: A precisely matched agent temp worker: web-wide sourcing plus capability matching in five steps
tags: ['web-sourcing', 'capability-matching', 'talent-mapping']
license: MIT
agent_created: true
---
# Web-Wide Recruiting Sourcing & Capability Matching Workflow

## Purpose

Turn a business owner's role or staffing requirements into an executable sourcing action: structure the requirements, design and run web-wide searches, build a capability model and match precisely, then deliver a sourcing report with next actions.

## When to Use

- The user provides a JD or business requirements and asks to find people, search for talent, scan the talent market, or benchmark competitor hiring
- The user asks to filter, match, or rank candidate leads by capability dimensions
- The user asks for a sourcing report, talent map, or hiring-market briefing

## Five-Step Workflow

### Step 1: Clarify and Structure Requirements

Convert business requirements into a structured talent profile; ask when information is missing, never assume. Output four tables:

- **Hard requirements**: seniority / years of experience / education / industry background / location / salary band / start date
- **Capability dimensions**: hard skills, business soft skills, culture-fit items
- **Weighting**: must-haves (hard veto) / plus / reference
- **Search targets**: target companies, target populations, alternative populations

### Step 2: Design the Search Strategy

Build a keyword matrix (role word x skill word x scenario word x channel word) and a target channel list from the talent profile. Method and examples in `references/search-playbook.md`:

- Channel layering: job boards / social and professional communities / competitor moves / industry reports
- Set an explicit goal per round: verify supply density / mine specific leads / check salary and market benchmarks
- Keyword variants: synonyms, abbreviations, EN-ZH mixing (e.g. "backend", "server-side", "Backend")

### Step 3: Run the Web-Wide Search

Execute round by round under the following discipline:

- Log each round: query, channel, hit count, source quality, retrieval date
- Cross-verify: at least two independent sources per conclusion; prefer official and first-party sources
- Timestamp all market and hiring data with the retrieval date
- When a round yields nothing useful, return to Step 2 to broaden keywords or switch channels; never repeat the same query more than twice

### Step 4: Build the Capability Model and Match Precisely

1. Break role requirements into 5-8 scoreable dimensions and build a 0-5 behavioral anchor scale (what is rated, what each level looks like)
2. Score every candidate lead per dimension, based only on evidence found in resumes, profiles, or project descriptions; no evidence, no score
3. Run `scripts/match_score.py` for the weighted match (input: scoring JSON; output: total score, strengths, gaps, veto flags)
4. See `references/capability-matching-model.md` for the scoring model, anchor examples, and grade thresholds

### Step 5: Produce the Sourcing Report

Follow `references/report-template.md`: a conclusion-first report covering talent supply overview, the top-lead table (match score plus evidence), outreach advice, and risks with fallbacks. End with 3 immediately executable next actions for the business owner.

## Iron Rules

- Rate only job-relevant capabilities and evidence; never age, gender, region, marital status, household registration, or any other discriminatory dimension
- Never fabricate sources or candidates; when a search comes up empty, say so and suggest how to widen it
- Public channels only; protect candidate privacy
- Attach a source and retrieval date to every conclusion
