#!/usr/bin/env python3
# HIPAA Audit Generator - Produces structured audit findings from checklist data.

import json
from datetime import datetime

def generate_audit(findings: list, auditor: str, entity: str) -> dict:
    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    open_count = 0
    for f in findings:
        severity_counts[f.get("severity", "low")] += 1
        if f.get("status") == "open":
            open_count += 1
    report = {
        "audit_id": f"AUD-{datetime.now().strftime('%Y%m%d')}-{hash(entity) % 10000}",
        "date": datetime.now().isoformat(),
        "auditor": auditor,
        "entity": entity,
        "summary": {
            "total_findings": len(findings),
            "open_findings": open_count,
            "severity_distribution": severity_counts,
            "compliance_rate": round((len(findings) - open_count) / len(findings) * 100, 1) if findings else 100
        },
        "findings": findings,
        "recommendations": []
    }
    for f in findings:
        if f.get("status") == "open":
            report["recommendations"].append({
                "finding_id": f.get("finding_id"),
                "priority": f.get("severity"),
                "action": f.get("remediation", {}).get("action", "Investigate and remediate"),
                "owner": f.get("remediation", {}).get("owner", "TBD"),
                "due_date": f.get("remediation", {}).get("due_date")
            })
    return report

if __name__ == "__main__":
    sample = [
        {
            "finding_id": "F-001",
            "severity": "high",
            "status": "open",
            "rule": {"cfr_reference": "45 CFR 164.312(a)(1)", "requirement": "Access Control"},
            "remediation": {"action": "Implement unique user IDs", "owner": "IT Security", "due_date": "2025-07-01"}
        }
    ]
    print(json.dumps(generate_audit(sample, "AI Auditor", "Hospital A"), indent=2))
