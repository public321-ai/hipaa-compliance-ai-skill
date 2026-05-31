# Evidence Validator

## Purpose
Validate that compliance evidence meets HIPAA requirements.

## Validation Rules
1. **Timeliness**: Evidence must be within the audit period (typically 12 months)
2. **Completeness**: All required fields populated
3. **Authenticity**: Signed/dated by authorized personnel
4. **Accuracy**: Matches system configurations and actual practices

## Evidence Types
| Type | Required Elements | Validator |
|------|-------------------|-----------|
| Risk Analysis | Scope, methodology, threats, vulnerabilities, scores, remediation | Check schema + date + author |
| Training Records | Date, attendees, topics, completion status | Check roster + content + date |
| BAA | Counterparty, effective date, PHI scope, safeguards, termination clause | Check signature + date + scope |
| Audit Logs | Timestamp, user, action, object, outcome | Check completeness + retention |
| Access Review | System, reviewer, date, findings, actions | Check date + coverage + closure |

## Rejection Criteria
- Missing signature or date
- Outside retention period
- Incomplete fields per schema
- Contradictory data (e.g., training date before hire date)
- Generic/template content without entity-specific customization

## Output
Pass/Fail with specific findings -> `audit_finding.schema.json`
