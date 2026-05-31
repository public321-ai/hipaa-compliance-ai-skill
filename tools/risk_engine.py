#!/usr/bin/env python3
# HIPAA Risk Engine - Calculates risk scores based on likelihood and impact.

def calculate_risk_score(likelihood: int, impact: int) -> int:
    if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
        raise ValueError("Likelihood and impact must be between 1 and 5")
    return likelihood * impact

def risk_level(score: int) -> str:
    if score <= 5:
        return "low"
    elif score <= 10:
        return "medium"
    elif score <= 15:
        return "high"
    else:
        return "critical"

def aggregate_risk(assets: list) -> dict:
    scores = []
    for asset in assets:
        for threat in asset.get("threats", []):
            score = calculate_risk_score(threat["likelihood"], threat["impact"])
            scores.append(score)
            threat["risk_score"] = score
            threat["risk_level"] = risk_level(score)
    return {
        "max_score": max(scores) if scores else 0,
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
        "critical_count": sum(1 for s in scores if s > 15),
        "high_count": sum(1 for s in scores if 11 <= s <= 15),
        "assets": assets
    }

if __name__ == "__main__":
    sample = [
        {
            "asset_id": "EHR-01",
            "name": "EHR System",
            "threats": [
                {"likelihood": 4, "impact": 5, "description": "Ransomware"},
                {"likelihood": 3, "impact": 4, "description": "Insider threat"}
            ]
        }
    ]
    print(aggregate_risk(sample))
