# Compliance Readiness Scoring

## Maturity Levels
| Level | Description | Score Range |
|-------|-------------|-------------|
| 1 - Initial | Ad hoc, reactive | 0-25 |
| 2 - Developing | Documented, inconsistent | 26-50 |
| 3 - Defined | Standardized, organization-wide | 51-75 |
| 4 - Managed | Measured, monitored, KPIs | 76-90 |
| 5 - Optimized | Continuous improvement, predictive | 91-100 |

## Scoring Dimensions
1. **Governance** (20%): Leadership, roles, policies
2. **Risk Management** (20%): Risk analysis, treatment, monitoring
3. **Technical Controls** (20%): Access, encryption, audit, integrity
4. **Administrative Controls** (20%): Training, BAAs, incident response
5. **Physical Controls** (10%): Facility, workstation, media
6. **Privacy Practices** (10%): NPP, individual rights, minimum necessary

## Calculation
- Run `compliance_scoring.py` with audit findings and evidence
- Weighted average across dimensions
- Round to nearest integer

## Reporting
- Overall score with dimension breakdown
- Gap analysis vs. target level
- Prioritized remediation roadmap
- Timeline to next maturity level
