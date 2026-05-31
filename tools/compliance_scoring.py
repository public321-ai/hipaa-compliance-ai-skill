#!/usr/bin/env python3
# Compliance Scoring Engine - Calculates HIPAA readiness score across dimensions.

DIMENSIONS = {
    "governance": 0.20,
    "risk_management": 0.20,
    "technical_controls": 0.20,
    "administrative_controls": 0.20,
    "physical_controls": 0.10,
    "privacy_practices": 0.10
}

def calculate_score(dimension_scores: dict) -> dict:
    total = 0
    breakdown = {}
    for dim, weight in DIMENSIONS.items():
        score = dimension_scores.get(dim, 0)
        weighted = score * weight
        total += weighted
        breakdown[dim] = {
            "raw_score": score,
            "weight": weight,
            "weighted_score": round(weighted, 1)
        }
    overall = round(total)
    if overall >= 91:
        level, label = 5, "Optimized"
    elif overall >= 76:
        level, label = 4, "Managed"
    elif overall >= 51:
        level, label = 3, "Defined"
    elif overall >= 26:
        level, label = 2, "Developing"
    else:
        level, label = 1, "Initial"
    return {
        "overall_score": overall,
        "maturity_level": level,
        "maturity_label": label,
        "dimension_breakdown": breakdown,
        "gaps": [dim for dim, s in dimension_scores.items() if s < 70],
        "priority": "critical" if overall < 50 else "high" if overall < 70 else "medium" if overall < 85 else "low"
    }

if __name__ == "__main__":
    sample = {
        "governance": 85,
        "risk_management": 70,
        "technical_controls": 90,
        "administrative_controls": 65,
        "physical_controls": 80,
        "privacy_practices": 75
    }
    print(calculate_score(sample))
