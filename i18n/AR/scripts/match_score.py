#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""حاسبة درجة مطابقة المرشحين (واجهة عربية)

تقيّم فرص المرشحين على أبعاد المهارات (بناءً على الأدلة)؛ وتُخرج درجة المطابقة
المرجّحة والتصنيف ونقاط القوة والفجوات وأعلام النقض القاطع. تُستخدم في الخطوة 4
من مهارة recruit-web-sourcing.

الاستخدام:
    python match_score.py scores.json          # القراءة من ملف
    echo '<json>' | python match_score.py      # القراءة من الإدخال القياسي
    python match_score.py scores.json --json   # مخرجات قابلة للقراءة آليًا

صيغة المُدخل:
{
  "dimensions": [
    {
      "name": "تصميم الأنظمة عالية التزامن",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "قاد تصميم نظام يخدم أكثر من 10 ملايين طلب يوميًا"
    }
  ]
}

القواعد:
    - يجب أن يكون مجموع الأوزان 1.0 (وإلا يتم التطبيع تلقائيًا مع تحذير)
    - الدرجة بين 0-5؛ والبُعد ذو المستوى must الذي يحصل على ≤2 يؤدي إلى نقض قاطع
    - درجة المطابقة = المتوسط المرجّح (0-5) × 20؛ التصنيف A≥85 وB≥70 وC≥50 وD<50
"""

import argparse
import json
import sys

VALID_LEVELS = ("must", "plus", "ref")
LEVEL_NAMES = {"must": "أساسي", "plus": "مرغوب", "ref": "مرجعي"}


def load_input(path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate(data):
    errors = []
    dims = data.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errors.append("يجب أن يحتوي المُدخل على مصفوفة dimensions غير فارغة")
        return errors, None

    total_weight = 0.0
    for i, d in enumerate(dims, 1):
        name = d.get("name", "").strip()
        if not name:
            errors.append(f"البُعد رقم {i} يفتقد إلى name")
        weight = d.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"البُعد {name or i}: يجب أن يكون الوزن رقمًا غير سالب")
        else:
            total_weight += weight
        level = d.get("level")
        if level not in VALID_LEVELS:
            errors.append(f"البُعد {name or i}: يجب أن يكون المستوى must/plus/ref، والقيمة {level}")
        score = d.get("score")
        if not isinstance(score, (int, float)) or not (0 <= score <= 5):
            errors.append(f"البُعد {name or i}: يجب أن تكون الدرجة رقمًا بين 0-5، والقيمة {score}")
        if not str(d.get("evidence", "")).strip():
            errors.append(f"البُعد {name or i}: يفتقد إلى evidence (لا دليل لا تقييم)")
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
        grade = "D (نقض قاطع)"
    elif total >= 85:
        grade = "A تواصل فوري"
    elif total >= 70:
        grade = "B قابل للتطوير"
    elif total >= 50:
        grade = "C بحذر"
    else:
        grade = "D غير مطابق"

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
    lines.append(f"درجة المطابقة: {result['total']}/100    التصنيف: {result['grade']}")
    if result["vetoed"]:
        lines.append("! نقض قاطع: بُعد أساسي حصل على ≤2؛ يُصنّف D افتراضيًا ما لم يُعفَ صراحة من صاحب العمل")
    if result["weight_normalized"]:
        lines.append("! مجموع الأوزان لا يساوي 1.0؛ تم التطبيع تلقائيًا")
    lines.append("=" * 56)
    lines.append(f"{'البُعد':<22}{'الوزن':>7}  {'المستوى':<8}{'الدرجة':>5}  الدليل")
    for d in result["details"]:
        lines.append(f"{d['name']:<16}{d['weight']:>6.2f}  {LEVEL_NAMES[d['level']]:<4}{d['score']:>3}  {d['evidence']}")
    lines.append("-" * 56)
    if result["strengths"]:
        lines.append("نقاط القوة (≥4): " + ", ".join(d["name"] for d in result["strengths"]))
    else:
        lines.append("نقاط القوة (≥4): لا شيء")
    if result["gaps"]:
        lines.append("الفجوات (<3): " + ", ".join(
            f"{d['name']} ({d['score']})" for d in result["gaps"]))
    else:
        lines.append("الفجوات (<3): لا شيء")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="حاسبة درجة مطابقة المرشحين")
    parser.add_argument("input", nargs="?", help="مسار ملف JSON للتقييمات (افتراضيًا من الإدخال القياسي)")
    parser.add_argument("--json", action="store_true", help="إخراج JSON قابل للقراءة آليًا")
    args = parser.parse_args()

    try:
        data = load_input(args.input)
    except (json.JSONDecodeError, OSError) as e:
        print(f"فشل قراءة المُدخل: {e}", file=sys.stderr)
        sys.exit(2)

    errors, total_weight = validate(data)
    if errors:
        for e in errors:
            print(f"فشل التحقق من المُدخل: {e}", file=sys.stderr)
        sys.exit(2)

    result = compute(data, total_weight)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result))


if __name__ == "__main__":
    main()
