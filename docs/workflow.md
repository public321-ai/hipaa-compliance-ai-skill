# HIPAA Lifecycle Workflow

## 1. Discovery
- Inventory PHI systems via `phi_inventory.schema.json`
- Classify data with `phi_classifier.py`

## 2. Risk Assessment
- Run `risk_engine.py` on all assets
- Populate `risk_assessment.schema.json`
- Prioritize critical/high risks

## 3. Controls Implementation
- Map HIPAA to frameworks via `mappings/`
- Implement required + addressable safeguards
- Document evidence

## 4. Audit
- Execute `audit_checklist.md`
- Generate findings via `audit_generator.py`
- Validate evidence with `evidence_validator.md`

## 5. Monitoring
- Continuous access log monitoring
- `breach_detector.py` runs on logs
- Anomalies trigger `breach_notification.md`

## 6. Improvement
- `compliance_scoring.py` measures maturity
- Remediate gaps
- Annual cycle restart
