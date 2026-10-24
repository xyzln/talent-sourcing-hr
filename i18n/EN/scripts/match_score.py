#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agent design coverage calculator (English UI)

Score agent design dimensions (based on job-design research evidence); outputs
the weighted coverage, grade, strong-coverage items, gaps, and hard-veto flags.
Used at Step 4 of the recruit-web-sourcing skill.

Usage:
    python match_score.py scores.json          # read from file
    echo '<json>' | python match_score.py      # read from stdin
    python match_score.py scores.json --json   # machine-readable output

Input format:
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

Rules:
    - weights should sum to 1.0 (auto-normalized with a warning otherwise)
    - score is 0-5; a must-level dimension scoring <=2 triggers a hard veto
    - coverage = weighted average (0-5) x 20; grades A>=85, B>=70, C>=50, D<50
"""

import argparse
import json
import sys

VALID_LEVELS = ("must", "plus", "ref")
LEVEL_NAMES = {"must": "core", "plus": "plus", "ref": "ref"}


def load_input(path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate(data):
    errors = []
    dims = data.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errors.append("Input must contain a non-empty dimensions array")
        return errors, None

    total_weight = 0.0
    for i, d in enumerate(dims, 1):
        name = d.get("name", "").strip()
        if not name:
            errors.append(f"Dimension #{i} is missing a name")
        weight = d.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"Dimension {name or i}: weight must be a non-negative number")
        else:
            total_weight += weight
        level = d.get("level")
        if level not in VALID_LEVELS:
            errors.append(f"Dimension {name or i}: level must be must/plus/ref, got {level}")
        score = d.get("score")
        if not isinstance(score, (int, float)) or not (0 <= score <= 5):
            errors.append(f"Dimension {name or i}: score must be a number 0-5, got {score}")
        if not str(d.get("evidence", "")).strip():
            errors.append(f"Dimension {name or i}: missing evidence (no evidence, no score)")
    return errors, total_weight


def compute(data, total_weight):
    dims = data["dimensions"]
    if total_weight <= 0:
        total_weight = 1.0
    normalized = abs(total_weight - 1.0) > 0.001

    weighted_sum = 0.0
    vetoed = False
    details = []
    for d in dims:
        w = d["weight"] / total_weight if normalized else d["weight"]
        weighted_sum += w * d["score"]
        if d["level"] == "must" and d["score"] <= 2:
            vetoed = True
        details.append({
            "name": d["name"],
            "weight": round(w, 3),
            "level": d["level"],
            "score": d["score"],
            "evidence": d["evidence"],
        })

    total = round(weighted_sum * 20)
    if vetoed:
        grade = "D (CORE GAP)"
    elif total >= 85:
        grade = "A Ship it"
    elif total >= 70:
        grade = "B Basically usable"
    elif total >= 50:
        grade = "C Has gaps"
    else:
        grade = "D Mismatch"

    strengths = [d for d in details if d["score"] >= 4]
    gaps = [d for d in details if d["score"] < 3]
    return {
        "total": total,
        "grade": grade,
        "vetoed": vetoed,
        "weight_normalized": normalized,
        "details": details,
        "strengths": strengths,
        "gaps": gaps,
    }


def render(result):
    lines = []
    lines.append("=" * 56)
    lines.append(f"COVERAGE: {result['total']}/100    GRADE: {result['grade']}")
    if result["vetoed"]:
        lines.append("! HARD VETO: a core design dimension scored <=2; defaults to grade D unless the requester explicitly waives")
    if result["weight_normalized"]:
        lines.append("! Weights do not sum to 1.0; auto-normalized")
    lines.append("=" * 56)
    lines.append(f"{'DIMENSION':<28}{'WEIGHT':>8}  {'LVL':<6}{'SCR':>4}  EVIDENCE")
    for d in result["details"]:
        lines.append(f"{d['name']:<16}{d['weight']:>6.2f}  {LEVEL_NAMES[d['level']]:<4}{d['score']:>3}  {d['evidence']}")
    lines.append("-" * 56)
    if result["strengths"]:
        lines.append("STRONG COVERAGE (>=4): " + ", ".join(d["name"] for d in result["strengths"]))
    else:
        lines.append("STRONG COVERAGE (>=4): none")
    if result["gaps"]:
        lines.append("GAPS (<3): " + ", ".join(
            f"{d['name']} ({d['score']})" for d in result["gaps"]))
    else:
        lines.append("GAPS (<3): none")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Agent design coverage calculator")
    parser.add_argument("input", nargs="?", help="path to the scoring JSON file (defaults to stdin)")
    parser.add_argument("--json", action="store_true", help="output machine-readable JSON")
    args = parser.parse_args()

    try:
        data = load_input(args.input)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Failed to read input: {e}", file=sys.stderr)
        sys.exit(2)

    errors, total_weight = validate(data)
    if errors:
        for e in errors:
            print(f"Input validation failed: {e}", file=sys.stderr)
        sys.exit(2)

    result = compute(data, total_weight)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result))


if __name__ == "__main__":
    main()
