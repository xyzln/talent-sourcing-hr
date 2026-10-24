# Job → Agent Design Mapping Model

> Used at Steps 3 and 4 of the `recruit-web-sourcing` skill. Goal: translate "job design" into "agent design", and verify design completeness with a reproducible coverage score.

## 1. Job Design Elements → Agent Design Elements

| Job design element | Agent design element | Where it lands |
|--------------------|----------------------|----------------|
| Role positioning (what this role is for) | Agent positioning | frontmatter description + persona opening |
| Responsibilities (what they do) | Skill list and workflow steps | skills array + workflow section |
| Requirements (what makes them competent) | Capability anchors and guardrails | persona core capabilities + iron rules/notes |
| Workflow (how, in what order) | Workflow steps and checkpoints | workflow section (each step has actions and outputs) |
| Collaboration (who they deal with) | Input/output spec and handoff protocol | output spec + trigger/exit conditions |
| KPIs (what "done well" means) | Acceptance criteria and quality bars | the pass line in the output spec |
| Toolstack (what they use) | Tool and script list | scripts/ + reference manuals + tool notes |

**Mapping rules**:
- Elements present in the real job must have a corresponding design in the agent; elements absent from the job must not be invented into the agent
- Every mapping must trace back to job research evidence (source + retrieval date)
- One job element may map to multiple agent elements, but every agent element must have at least one job source

## 2. Agent Design Coverage Anchors (0-5)

Score each agent design dimension against job research evidence:

| Score | Level | Behavioral anchor (generic) |
|-------|-------|----------------------------|
| 5 | Full coverage | All job elements translated, every one backed by evidence; ready to ship |
| 4 | Complete | All major elements covered; details could be polished |
| 3 | Basically covered | Main body covered, but with a clear small gap (missing acceptance criteria / trigger, etc.) |
| 2 | Partially covered | Only about half the elements covered; several filled in by feel |
| 1 | Nominal | The dimension is mentioned but has no executable content |
| 0 | No evidence | No evidence found in the job research to support this design (doesn't mean it shouldn't exist, means it can't be verified) |

**Evidence rule**: no evidence = 0 points, marked "to be verified"; after supplementary searches produce evidence, scores may be updated, keeping the scoring history.

## 3. Common Design Dimensions and Weights

Extract 5-8 design dimensions from the job design research, in three tiers:

| Weight tier | Meaning | Suggested weight | Scoring rule |
|-------------|---------|------------------|--------------|
| Core (hard veto) | Without it the agent doesn't hold up | 0.25-0.35 | Score ≤2 → VETO flag; total still computed but the conclusion must flag it |
| Plus | Significantly improves agent quality | 0.10-0.20 | Counted normally |
| Reference | Affects marginal judgment | 0.05-0.10 | Counted normally |

**Typical dimensions** (tailor to the job; you don't need all):
- Core: persona clarity, responsibility coverage, workflow completeness
- Plus: clear collaboration interface, executable acceptance criteria, complete tooling
- Reference: output format discipline, timestamping mechanism

Weights must sum to 1.0; usually 1-2 core items; more than 2 means the design hasn't converged.

## 4. Coverage Calculation and Grades

Use `scripts/match_score.py`: weighted average (0-5) × 20 = coverage percentage.

| Coverage | Grade | Action |
|----------|-------|--------|
| ≥85 | A Ship it | Build directly as expert package / skill / sub-agent per the spec |
| 70-84 | B Basically usable | Ship while closing gap items (more research or more design) |
| 50-69 | C Has gaps | Finish research or design first, then ship |
| <50 | D Mismatch | Return to step 2 and re-research the role; don't rush to generate |
| Any core item ≤2 | Hard veto | Default D regardless of total, unless the requester explicitly waives |

## 5. Using match_score.py

```bash
# Input JSON (file or stdin), output coverage report
python scripts/match_score.py scores.json
echo '{"dimensions":[{"name":"Persona clarity","weight":0.3,"level":"must","score":4,"evidence":"Role definition is clear: owns user-behavior analysis and outputs actionable conclusions"},{"name":"Responsibility coverage","weight":0.3,"level":"must","score":5,"evidence":"All six responsibilities mapped to workflow steps"},{"name":"Complete tooling","weight":0.2,"level":"plus","score":3,"evidence":"Scoring script exists; report template tool missing"},{"name":"Output format discipline","weight":0.2,"level":"ref","score":2,"evidence":"Only verbal description; no template defined"}]}' | python scripts/match_score.py
```

Input format:

```json
{
  "dimensions": [
    {
      "name": "Persona clarity",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "Role definition is clear: owns user-behavior analysis and outputs actionable conclusions"
    }
  ]
}
```

Output: coverage total, grade, per-dimension details, strong-coverage items (≥4), gap items (<3), and veto flags.

## 6. Usage Discipline

- Scores are based on job research evidence only; no guessing; the evidence field is mandatory
- All design dimensions of the same agent use the same weights for comparability
- When job research updates, change the evidence first, then the scores; no "moving the goalposts"
- Always state confidence alongside the coverage score (evidence sufficient / partially to be verified)
- Low coverage doesn't mean the job research failed - it may just need more search rounds: add research before adding design
