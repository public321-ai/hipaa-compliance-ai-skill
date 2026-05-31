# HIPAA Agent Architecture

## Components
- **Master Prompt**: Orchestrates all sub-prompts and workflows
- **Sub-Prompts**: Specialized for each HIPAA rule (Privacy, Security, Breach, Enforcement)
- **Schemas**: JSON schemas for structured data validation
- **Tools**: Python scripts for calculations, detection, and scoring
- **Mappings**: Crosswalks to NIST, ISO 27001, HITRUST, CIS

## Data Flow
1. Input (PHI metadata, access logs, policies) -> validated against schemas
2. Master prompt routes to appropriate sub-prompt
3. Sub-prompts invoke tools for calculations
4. Output structured to schemas -> evidence validator
5. Audit trail logged to `access_log.schema.json`

## Security
- No raw PHI in prompts (metadata/classification only)
- All outputs encrypted at rest
- 6-year retention enforced
- Role-based access to agent functions
