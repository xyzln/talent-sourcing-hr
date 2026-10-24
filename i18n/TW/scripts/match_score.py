#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agent 設計覆蓋度計算機（繁體中文版）

輸入 agent 設計各維度的評分（基於崗位研究證據），輸出加權覆蓋度、分級、
強覆蓋項、缺口項與一票否決標記。配合 recruit-web-sourcing 技能第 4 步使用。

用法:
    python match_score.py scores.json          # 從檔案讀取
    echo '<json>' | python match_score.py      # 從標準輸入讀取
    python match_score.py scores.json --json   # 機器可讀輸出

輸入格式:
{
  "dimensions": [
    {
      "name": "人格定位清晰",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "崗位角色定義明確：負責用戶行為分析並輸出可執行結論"
    }
  ]
}

規則:
    - weight 之和應為 1.0（不為 1.0 時自動正規化並提示）
    - score 取值 0-5；level 為 must 的維度得分 <=2 觸發一票否決
    - 覆蓋度 = 加權平均分(0-5) x 20；分級 A>=85, B>=70, C>=50, D<50
"""

import argparse
import json
import sys

VALID_LEVELS = ("must", "plus", "ref")
LEVEL_NAMES = {"must": "核心", "plus": "加分", "ref": "參考"}


def load_input(path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate(data):
    errors = []
    dims = data.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errors.append("輸入必須包含非空的 dimensions 陣列")
        return errors, None

    total_weight = 0.0
    for i, d in enumerate(dims, 1):
        name = d.get("name", "").strip()
        if not name:
            errors.append(f"第 {i} 個維度缺少 name")
        weight = d.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"維度 {name or i} 的 weight 必須是非負數字")
        else:
            total_weight += weight
        level = d.get("level")
        if level not in VALID_LEVELS:
            errors.append(f"維度 {name or i} 的 level 必須是 must/plus/ref，得到 {level}")
        score = d.get("score")
        if not isinstance(score, (int, float)) or not (0 <= score <= 5):
            errors.append(f"維度 {name or i} 的 score 必須是 0-5 的數字，得到 {score}")
        if not str(d.get("evidence", "")).strip():
            errors.append(f"維度 {name or i} 缺少 evidence（無證據不評分）")
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
        grade = "D（核心項缺失）"
    elif total >= 85:
        grade = "A 可直接落地"
    elif total >= 70:
        grade = "B 基本可用"
    elif total >= 50:
        grade = "C 有缺口"
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
    lines.append(f"覆蓋度總分: {result['total']}/100    分級: {result['grade']}")
    if result["vetoed"]:
        lines.append("⚠ 觸發一票否決：存在核心設計項得分 ≤2，預設 D 級，除非需求方明確豁免")
    if result["weight_normalized"]:
        lines.append("⚠ 權重之和不為 1.0，已自動正規化")
    lines.append("=" * 56)
    lines.append(f"{'設計維度':<16}{'權重':>6}  {'級':<4}{'分':>3}  證據")
    for d in result["details"]:
        lines.append(f"{d['name']:<16}{d['weight']:>6.2f}  {LEVEL_NAMES[d['level']]:<4}{d['score']:>3}  {d['evidence']}")
    lines.append("-" * 56)
    if result["strengths"]:
        lines.append("強覆蓋項(≥4分): " + ", ".join(d["name"] for d in result["strengths"]))
    else:
        lines.append("強覆蓋項(≥4分): 無")
    if result["gaps"]:
        lines.append("缺口項(<3分): " + ", ".join(
            f"{d['name']}({d['score']}分)" for d in result["gaps"]))
    else:
        lines.append("缺口項(<3分): 無")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Agent 設計覆蓋度計算機")
    parser.add_argument("input", nargs="?", help="評分 JSON 檔案路徑（缺省由標準輸入讀取）")
    parser.add_argument("--json", action="store_true", help="輸出機器可讀 JSON")
    args = parser.parse_args()

    try:
        data = load_input(args.input)
    except (json.JSONDecodeError, OSError) as e:
        print(f"輸入讀取失敗: {e}", file=sys.stderr)
        sys.exit(2)

    errors, total_weight = validate(data)
    if errors:
        for e in errors:
            print(f"輸入驗證失敗: {e}", file=sys.stderr)
        sys.exit(2)

    result = compute(data, total_weight)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result))


if __name__ == "__main__":
    main()
