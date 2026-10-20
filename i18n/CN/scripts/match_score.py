#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""match_score.py — 人才匹配度计算器

输入候选线索在各能力维度上的评分（基于证据），输出加权匹配度、分级、
优势项、缺口项与一票否决标记。配合 recruit-web-sourcing 技能第 4 步使用。

用法:
    python match_score.py scores.json          # 从文件读取
    echo '<json>' | python match_score.py      # 从标准输入读取
    python match_score.py scores.json --json   # 机器可读输出

输入格式:
{
  "dimensions": [
    {
      "name": "高并发系统设计",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "主导过日均千万级请求系统架构"
    }
  ]
}

规则:
    - weight 之和应为 1.0（不为 1.0 时自动归一化并提示）
    - score 取值 0-5；level 为 must 的维度得分 <=2 触发一票否决
    - 匹配度 = 加权平均分(0-5) x 20；分级 A>=85, B>=70, C>=50, D<50
"""

import argparse
import json
import sys

VALID_LEVELS = ("must", "plus", "ref")
LEVEL_NAMES = {"must": "必备", "plus": "加分", "ref": "参考"}


def load_input(path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate(data):
    errors = []
    dims = data.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errors.append("输入必须包含非空的 dimensions 数组")
        return errors, None

    total_weight = 0.0
    for i, d in enumerate(dims, 1):
        name = d.get("name", "").strip()
        if not name:
            errors.append(f"第 {i} 个维度缺少 name")
        weight = d.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"维度 '{name or i}' 的 weight 必须是非负数字")
        else:
            total_weight += weight
        level = d.get("level")
        if level not in VALID_LEVELS:
            errors.append(f"维度 '{name or i}' 的 level 必须是 must/plus/ref，得到 '{level}'")
        score = d.get("score")
        if not isinstance(score, (int, float)) or not (0 <= score <= 5):
            errors.append(f"维度 '{name or i}' 的 score 必须是 0-5 的数字，得到 '{score}'")
        if not str(d.get("evidence", "")).strip():
            errors.append(f"维度 '{name or i}' 缺少 evidence（无证据不评分）")
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
        grade = "D（一票否决）"
    elif total >= 85:
        grade = "A 优先寻访"
    elif total >= 70:
        grade = "B 可培养"
    elif total >= 50:
        grade = "C 谨慎"
    else:
        grade = "D 不匹配"

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
    lines.append(f"匹配度总分: {result['total']}/100    分级: {result['grade']}")
    if result["vetoed"]:
        lines.append("⚠ 触发一票否决：存在必备项得分 ≤2，默认 D 级，除非业务方明确豁免")
    if result["weight_normalized"]:
        lines.append("⚠ 权重之和不为 1.0，已自动归一化")
    lines.append("=" * 56)
    lines.append(f"{'能力维度':<16}{'权重':>6}  {'级':<4}{'分':>3}  证据")
    for d in result["details"]:
        lines.append(f"{d['name']:<16}{d['weight']:>6.2f}  {LEVEL_NAMES[d['level']]:<4}{d['score']:>3}  {d['evidence']}")
    lines.append("-" * 56)
    if result["strengths"]:
        lines.append("优势项(≥4分): " + "、".join(d["name"] for d in result["strengths"]))
    else:
        lines.append("优势项(≥4分): 无")
    if result["gaps"]:
        lines.append("缺口项(<3分): " + "、".join(
            f"{d['name']}({d['score']}分)" for d in result["gaps"]))
    else:
        lines.append("缺口项(<3分): 无")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="人才匹配度计算器")
    parser.add_argument("input", nargs="?", help="评分 JSON 文件路径（缺省从标准输入读取）")
    parser.add_argument("--json", action="store_true", help="输出机器可读 JSON")
    args = parser.parse_args()

    try:
        data = load_input(args.input)
    except (json.JSONDecodeError, OSError) as e:
        print(f"输入读取失败: {e}", file=sys.stderr)
        sys.exit(2)

    errors, total_weight = validate(data)
    if errors:
        for e in errors:
            print(f"输入校验失败: {e}", file=sys.stderr)
        sys.exit(2)

    result = compute(data, total_weight)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result))


if __name__ == "__main__":
    main()
