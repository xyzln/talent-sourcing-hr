# Capability Modeling & Precision Matching Model

> Used with Step 4 of the `recruit-web-sourcing` skill. Goal: turn "is this a fit?" from a gut call into a reproducible score.

## 1. Decomposing Capability Dimensions

Extract 5-8 capability dimensions from the JD and business requirements, grouped into three categories:

| Category | Meaning | Examples |
|----------|---------|----------|
| Hard skills | The craft of doing the job | distributed architecture design, SQL optimization, campaign strategy |
| Business soft skills | The craft of getting things done | cross-functional driving, client negotiation, team mentoring |
| Culture fit | The baseline that matches the org | startup-pace adaptability, data-driven decisions, open collaboration |

**Decomposition rules**:
- Every dimension must be observable, askable, and verifiable; reject vague words like "has potential" or "feels right"
- A dimension belongs to one category only; if the business owner stressed it verbally but it is missing from the JD, record it and note the source
- Keep 5-8 dimensions: fewer than 5 risks misses; more than 8 dilutes weights

## 2. The 0-5 Behavioral Anchor Scale

Define each dimension in five levels of "what it looks like"; score by matching evidence to the anchor:

| Score | Level | Behavioral anchor (generic wording) |
|-------|-------|------------------------------------|
| 5 | Expert | Verifiable benchmark output (led same-scale/same-difficulty projects; results recognized by industry or company) |
| 4 | Proficient | Independently delivered similar work end-to-end; stable quality; little guidance needed |
| 3 | Competent | Completed similar work under guidance; handles routine scenarios |
| 2 | Beginner | Exposure without independent delivery, or training/course-level experience only |
| 1 | Aware | Conceptual knowledge only; no practice |
| 0 | No evidence | No evidence found in public information (not "cannot do" - means "cannot verify") |

**Anchor example ("high-concurrency system design")**:
- 5: Led architecture design for a system serving 10M+ requests/day; public talk or verifiable case
- 4: Independently owned core modules of a million-request system
- 3: Participated in high-concurrency development, owning several modules
- 2: Learning/practice projects only; never in production
- 1: Course-level or conceptual knowledge
- 0: No relevant information

**Evidence rule**: no evidence = 0 and flagged "to verify"; evidence obtained later via interview/reference check can update the score - keep the score history.

## 3. Weighting

| Weight level | Meaning | Suggested weight | Scoring rule |
|--------------|---------|------------------|--------------|
| Must-have (hard veto) | Failing it means overall mismatch | 0.25-0.35 | Score <=2 -> flag VETO; total still computed but the conclusion must call it out |
| Plus | Significant exceeders get priority | 0.10-0.20 | Counted normally |
| Reference | Influences marginal judgment | 0.05-0.10 | Counted normally |

Weights must sum to 1.0; set 1-2 must-haves - more than 2 means the profile has not converged.

## 4. Match Score Computation and Grading

Use `scripts/match_score.py`: weighted average (0-5) x 20 = match score (0-100).

| Score | Grade | Recommended action |
|-------|-------|--------------------|
| >=85 | A Priority outreach | Reach out immediately with tailored messaging |
| 70-84 | B Developable | Reach out while sizing the cost and timeline of closing gaps |
| 50-69 | C Caution | Fallback option only when supply is tight; state the gaps explicitly |
| <50 | D No match | Keep off the sourcing list |
| Any must-have <=2 | Hard veto | Defaults to D regardless of total, unless the business owner explicitly waives |

## 5. Using match_score.py

```bash
# Input JSON (file or stdin), outputs the match report
python scripts/match_score.py scores.json
echo '{"dimensions":[{"name":"High-concurrency system design","weight":0.3,"level":"must","score":4,"evidence":"Led architecture for a 10M+ requests/day system"},{"name":"Team mentoring","weight":0.2,"level":"plus","score":3,"evidence":"Led a team of 5"}]}' | python scripts/match_score.py
```

Input format:

```json
{
  "dimensions": [
    {
      "name": "High-concurrency system design",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "Led architecture for a 10M+ requests/day system"
    }
  ]
}
```

Output: total match score, grade, per-dimension breakdown, strengths (>=4), gaps (<3), and hard-veto flags.

## 6. Usage Discipline

- Score on public-channel evidence only; no guessing; the evidence field is mandatory
- All candidate leads for the same role use the same dimensions and weights to stay comparable
- When business requirements change, update the profile and weights first, then re-score - no moving goalposts
- Always report match score together with a confidence note (evidence sufficient / partially pending)
