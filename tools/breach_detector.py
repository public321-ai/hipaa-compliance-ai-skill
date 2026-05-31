#!/usr/bin/env python3
# Breach Detector - Analyzes access logs for potential PHI breaches.

from datetime import datetime

def detect_breach(access_logs: list, threshold: int = 100) -> list:
    incidents = []
    user_access = {}
    for log in access_logs:
        uid = log.get("user_id")
        user_access.setdefault(uid, []).append(log)
    for user, logs in user_access.items():
        if len(logs) > threshold:
            incidents.append({
                "type": "bulk_access",
                "user": user,
                "count": len(logs),
                "severity": "high",
                "reason": f"User accessed {len(logs)} records in period"
            })
        after_hours = [l for l in logs if is_after_hours(l.get("timestamp"))]
        if len(after_hours) > 10:
            incidents.append({
                "type": "after_hours",
                "user": user,
                "count": len(after_hours),
                "severity": "medium",
                "reason": "Unusual after-hours access pattern"
            })
        denied_then_success = detect_denied_then_success(logs)
        if denied_then_success:
            incidents.append({
                "type": "unauthorized_access_attempt",
                "user": user,
                "severity": "critical",
                "reason": "Denied access followed by successful access"
            })
    return incidents

def is_after_hours(timestamp_str: str) -> bool:
    try:
        dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        hour = dt.hour
        return hour >= 18 or hour < 6
    except:
        return False

def detect_denied_then_success(logs: list) -> bool:
    sorted_logs = sorted(logs, key=lambda x: x.get("timestamp", ""))
    for i in range(len(sorted_logs) - 1):
        if sorted_logs[i].get("outcome") == "denied" and sorted_logs[i+1].get("outcome") == "success":
            return True
    return False

if __name__ == "__main__":
    sample_logs = [
        {"user_id": "U001", "timestamp": "2025-06-01T22:00:00Z", "outcome": "success", "action": "read"},
        {"user_id": "U001", "timestamp": "2025-06-01T22:01:00Z", "outcome": "success", "action": "read"},
        {"user_id": "U002", "timestamp": "2025-06-01T14:00:00Z", "outcome": "denied", "action": "read"},
        {"user_id": "U002", "timestamp": "2025-06-01T14:01:00Z", "outcome": "success", "action": "read"},
    ]
    print(detect_breach(sample_logs, threshold=1))
