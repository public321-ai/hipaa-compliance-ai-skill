# PHI Threat Model

## Threat Actors
- **External**: Hackers, ransomware groups, nation-states
- **Internal**: Malicious insiders, negligent employees
- **Third Party**: Business associates, vendors, subcontractors

## Threat Vectors
1. **Network**: Unencrypted transmission, phishing, malware
2. **Endpoint**: Lost/stolen devices, unauthorized software
3. **Physical**: Tailgating, unsecured workstations, improper disposal
4. **Application**: SQL injection, broken access control, insecure APIs
5. **Human**: Social engineering, credential sharing, misdelivery

## PHI-Specific Risks
- **Re-identification**: De-identified data combined with external datasets
- **Secondary Use**: PHI used for marketing or research without authorization
- **Cloud Exposure**: Misconfigured S3 buckets, database exposure
- **Ransomware**: ePHI encryption + exfiltration

## Mitigations
- Encrypt ePHI at rest and in transit
- Implement MFA and least privilege
- Monitor access logs with anomaly detection
- Train workforce on phishing and social engineering
- Maintain offline backups for ransomware recovery
- Execute and monitor BAAs with third parties
