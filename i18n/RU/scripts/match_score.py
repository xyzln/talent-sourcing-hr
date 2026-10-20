#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Калькулятор оценки соответствия кандидатов (русский интерфейс)

Оценивает лиды-кандидатов по измерениям компетенций (на основе доказательств);
выводит взвешенную оценку, grade, сильные стороны, пробелы и флаги жёсткого вето.
Используется на шаге 4 навыка recruit-web-sourcing.

Использование:
    python match_score.py scores.json          # чтение из файла
    echo '<json>' | python match_score.py      # чтение из stdin
    python match_score.py scores.json --json   # машиночитаемый вывод

Формат входа:
{
  "dimensions": [
    {
      "name": "Проектирование высоконагруженных систем",
      "weight": 0.3,
      "level": "must | plus | ref",
      "score": 4,
      "evidence": "Руководил архитектурой системы на 10М+ запросов в сутки"
    }
  ]
}

Правила:
    - сумма весов должна быть 1.0 (иначе автонормализация с предупреждением)
    - score принимает значения 0-5; измерение уровня must с оценкой <=2 даёт жёсткое вето
    - оценка = взвешенное среднее (0-5) x 20; grade A>=85, B>=70, C>=50, D<50
"""

import argparse
import json
import sys

VALID_LEVELS = ("must", "plus", "ref")
LEVEL_NAMES = {"must": "обяз.", "plus": "желат.", "ref": "справ."}


def load_input(path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return json.load(sys.stdin)


def validate(data):
    errors = []
    dims = data.get("dimensions")
    if not isinstance(dims, list) or not dims:
        errors.append("Вход должен содержать непустой массив dimensions")
        return errors, None

    total_weight = 0.0
    for i, d in enumerate(dims, 1):
        name = d.get("name", "").strip()
        if not name:
            errors.append(f"У измерения #{i} отсутствует name")
        weight = d.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"Измерение {name or i}: weight должен быть неотрицательным числом")
        else:
            total_weight += weight
        level = d.get("level")
        if level not in VALID_LEVELS:
            errors.append(f"Измерение {name or i}: level должен быть must/plus/ref, получено {level}")
        score = d.get("score")
        if not isinstance(score, (int, float)) or not (0 <= score <= 5):
            errors.append(f"Измерение {name or i}: score должен быть числом 0-5, получено {score}")
        if not str(d.get("evidence", "")).strip():
            errors.append(f"Измерение {name or i}: отсутствует evidence (нет доказательств — нет оценки)")
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
        grade = "D (ЖЁСТКОЕ ВЕТО)"
    elif total >= 85:
        grade = "A Приоритетный контакт"
    elif total >= 70:
        grade = "B Развиваемый"
    elif total >= 50:
        grade = "C Осторожно"
    else:
        grade = "D Не подходит"

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
    lines.append(f"ОЦЕНКА СООТВЕТСТВИЯ: {result['total']}/100    GRADE: {result['grade']}")
    if result["vetoed"]:
        lines.append("! ЖЁСТКОЕ ВЕТО: обязательное измерение оценено ≤2; по умолчанию grade D, если бизнес явно не сделал исключение")
    if result["weight_normalized"]:
        lines.append("! Веса в сумме не дают 1.0; выполнена автонормализация")
    lines.append("=" * 56)
    lines.append(f"{'ИЗМЕРЕНИЕ':<26}{'ВЕС':>7}  {'УР':<7}{'ОЦ':>4}  ДОКАЗАТЕЛЬСТВО")
    for d in result["details"]:
        lines.append(f"{d['name']:<16}{d['weight']:>6.2f}  {LEVEL_NAMES[d['level']]:<4}{d['score']:>3}  {d['evidence']}")
    lines.append("-" * 56)
    if result["strengths"]:
        lines.append("СИЛЬНЫЕ СТОРОНЫ (≥4): " + ", ".join(d["name"] for d in result["strengths"]))
    else:
        lines.append("СИЛЬНЫЕ СТОРОНЫ (≥4): нет")
    if result["gaps"]:
        lines.append("ПРОБЕЛЫ (<3): " + ", ".join(
            f"{d['name']} ({d['score']})" for d in result["gaps"]))
    else:
        lines.append("ПРОБЕЛЫ (<3): нет")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Калькулятор оценки соответствия кандидатов")
    parser.add_argument("input", nargs="?", help="путь к JSON-файлу с оценками (по умолчанию — stdin)")
    parser.add_argument("--json", action="store_true", help="вывод машиночитаемого JSON")
    args = parser.parse_args()

    try:
        data = load_input(args.input)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Не удалось прочитать входные данные: {e}", file=sys.stderr)
        sys.exit(2)

    errors, total_weight = validate(data)
    if errors:
        for e in errors:
            print(f"Валидация входных данных не пройдена: {e}", file=sys.stderr)
        sys.exit(2)

    result = compute(data, total_weight)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result))


if __name__ == "__main__":
    main()
