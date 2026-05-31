# HIPAA Compliance AI Agent

AI-powered compliance officer for healthcare organizations. Automates Privacy Rule, Security Rule, Breach Notification, and Enforcement Rule workflows.

## Capabilities
- PHI detection & classification
- Risk assessment & scoring
- Audit generation & evidence validation
- Breach detection & reporting
- Compliance readiness scoring
- Cross-framework mapping (NIST, ISO 27001, HITRUST, CIS)

## Quick Start
1. Configure `skill.yaml` with your entity type (CE, BA, BA subcontractor)
2. Load PHI inventory via `schemas/phi_inventory.schema.json`
3. Run `risk_engine.py` to baseline risk posture
4. Execute `audit_generator.py` for gap analysis

## Architecture
- Master prompt orchestrates sub-prompts
- Schemas enforce structured data exchange
- Tools perform calculations and classifications
- Mappings align HIPAA with external frameworks
