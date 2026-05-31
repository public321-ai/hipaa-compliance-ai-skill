# Integration Guide

## EHR Systems
- Extract metadata (not PHI) for inventory
- Pull access logs in `access_log.schema.json` format
- Push audit findings to compliance dashboard

## SIEM Tools
- Forward security events to `breach_detector.py`
- Map alerts to HIPAA controls
- Correlate with `access_log.schema.json`

## Cloud Storage
- Verify encryption at rest (AES-256)
- Verify encryption in transit (TLS 1.2+)
- Ensure access logs are collected and forwarded

## Identity Providers
- Sync unique user IDs
- Enforce MFA
- Automate access revocation on termination

## API Endpoints
- `/risk/assess` -> accepts `risk_assessment.schema.json`
- `/phi/inventory` -> accepts `phi_inventory.schema.json`
- `/audit/generate` -> returns audit report
- `/breach/detect` -> accepts access logs, returns incidents
- `/compliance/score` -> returns readiness score
