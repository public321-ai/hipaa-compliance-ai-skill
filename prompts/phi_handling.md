# PHI Handling Rules

## PHI Definition
Individually identifiable health information (18 identifiers under Safe Harbor):
Names, geographic subdivisions smaller than state, dates (except year), phone/fax, email, SSN, MRN, health plan numbers, account numbers, certificate/license numbers, vehicle identifiers, device identifiers, URLs, IP addresses, biometric identifiers, full-face photos, any other unique identifier.

## Data Classification
- **Restricted**: Full PHI, ePHI
- **Confidential**: De-identified data, aggregated statistics
- **Public**: NPP, general health information

## Handling Rules
- **Storage**: Encrypted at rest, access-controlled, audit-logged
- **Transmission**: Encrypted in transit, minimum necessary
- **Retention**: 6 years minimum (state law may require longer)
- **Disposal**: NIST 800-88 Clear/Purge/Destroy based on media type
- **Access**: Need-to-know, role-based, reviewed quarterly

## De-identification
- **Safe Harbor**: Remove all 18 identifiers
- **Expert Determination**: Statistical method certifying low re-identification risk

## Prohibited
- Storing PHI on unencrypted removable media
- Transmitting PHI via unencrypted email
- Accessing PHI from unsecured public WiFi
- Sharing credentials for PHI access

## Output
Update `phi_inventory.schema.json` for all PHI stores.
