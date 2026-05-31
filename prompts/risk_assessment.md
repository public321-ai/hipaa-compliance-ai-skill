# Risk Assessment Prompt

## Objective
Identify threats and vulnerabilities to PHI, assess likelihood and impact, assign risk scores.

## Methodology
1. **Asset Inventory**: Identify systems storing, processing, or transmitting PHI
2. **Threat Identification**: Natural, human (malicious/non-malicious), environmental
3. **Vulnerability Assessment**: Technical, administrative, physical gaps
4. **Likelihood Scoring**: 1-5 scale (1=rare, 5=almost certain)
5. **Impact Scoring**: 1-5 scale (1=negligible, 5=catastrophic)
6. **Risk Score**: Likelihood x Impact

## Risk Matrix
| Likelihood \ Impact | 1-Low | 2-Med | 3-High | 4-Crit | 5-Catastrophic |
|---------------------|-------|-------|--------|--------|----------------|
| 5-Almost Certain    | 5     | 10    | 15     | 20     | 25             |
| 4-Likely            | 4     | 8     | 12     | 16     | 20             |
| 3-Possible          | 3     | 6     | 9      | 12     | 15             |
| 2-Unlikely          | 2     | 4     | 6      | 8      | 10             |
| 1-Rare              | 1     | 2     | 3      | 4      | 5              |

## Risk Thresholds
- 1-5: Low (accept/monitor)
- 6-10: Medium (mitigate within 90 days)
- 11-15: High (mitigate within 30 days)
- 16-25: Critical (mitigate immediately, escalate to leadership)

## Output
Populate `risk_assessment.schema.json` and trigger `risk_engine.py` for calculation.
