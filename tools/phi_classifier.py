#!/usr/bin/env python3
# PHI Classifier - Detects PHI identifiers in text or metadata.

PHI_IDENTIFIERS = {
    "name", "address", "dates", "phone", "fax", "email", "ssn", "mrn",
    "health_plan", "account", "certificate", "license", "vehicle",
    "device", "url", "ip", "biometric", "photo", "other_unique"
}

def classify_phi(text: str) -> dict:
    detected = set()
    text_lower = text.lower()
    keywords = {
        "name": ["name", "patient name", "first name", "last name"],
        "ssn": ["ssn", "social security"],
        "mrn": ["mrn", "medical record number", "patient id"],
        "dob": ["dob", "date of birth", "birthdate"],
        "phone": ["phone", "telephone", "mobile"],
        "email": ["email", "e-mail"],
        "address": ["address", "street", "city", "zip"],
        "diagnosis": ["diagnosis", "icd", "condition"],
        "treatment": ["treatment", "procedure", "medication"]
    }
    for identifier, terms in keywords.items():
        if any(term in text_lower for term in terms):
            detected.add(identifier)
    return {
        "contains_phi": len(detected) > 0,
        "identifiers_found": list(detected),
        "phi_types": list(detected),
        "confidence": "high" if len(detected) > 2 else "medium" if detected else "low",
        "recommendation": "encrypt_and_restrict" if detected else "standard_handling"
    }

def deidentify_check(text: str) -> dict:
    found = classify_phi(text)
    safe = len(found["identifiers_found"]) == 0
    return {
        "safe_harbor_compliant": safe,
        "remaining_identifiers": found["identifiers_found"],
        "action": "remove_identifiers" if not safe else "approved"
    }

if __name__ == "__main__":
    sample = "Patient John Doe, SSN 123-45-6789, DOB 01/15/1980"
    print(classify_phi(sample))
    print(deidentify_check(sample))
