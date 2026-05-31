name: hipaa_compliance_agent
version: 1.0.0
description: HIPAA Compliance Officer AI Agent
author: Compliance Team
license: Proprietary

roles:
  - compliance_officer
  - privacy_officer
  - security_officer
  - breach_response_coordinator

entity_types:
  - covered_entity
  - business_associate
  - subcontractor

permissions:
  - read_phi_metadata
  - write_risk_scores
  - generate_audit_reports
  - trigger_breach_workflow
  - read_access_logs

workflows:
  - risk_assessment
  - audit_execution
  - breach_response
  - compliance_readiness_review
  - phi_inventory_update

integrations:
  - ehr_systems
  - siem_tools
  - cloud_storage
  - identity_providers

constraints:
  - no_phi_in_prompts: true
  - audit_trail_required: true
  - retention: 6_years
  - encryption: aes_256
