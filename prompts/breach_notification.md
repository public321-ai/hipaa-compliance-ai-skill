# Breach Notification Rule (45 CFR 164.400-414)

## Definition
Unauthorized acquisition, access, use, or disclosure of PHI that compromises security or privacy.

## Breach Assessment (Risk Assessment)
A breach is presumed unless you demonstrate low probability of compromise via:
1. Nature/extent of PHI involved (identifiers, likelihood of re-identification)
2. Unauthorized person who used PHI or to whom disclosure was made
3. Whether PHI was actually acquired or viewed
4. Extent to which risk has been mitigated

## Notification Timeline
- **Individuals**: Without unreasonable delay, max 60 days from discovery
- **HHS Secretary**: 
  - <500 individuals: annually
  - >=500 individuals: within 60 days
- **Media**: >=500 individuals in a state/jurisdiction: within 60 days

## Notification Content
- Brief description of breach
- Types of PHI involved
- Steps individuals should take
- What you are doing to investigate/mitigate
- Contact procedures

## Workflow
1. Detect anomaly -> log to `access_log.schema.json`
2. Run `breach_detector.py`
3. If breach confirmed -> populate `breach_report.schema.json`
4. Notify affected individuals, HHS, media (if applicable)
5. Document mitigation and lessons learned
