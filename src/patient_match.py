from .startup import PATIENTS_DB

async def find_matching_patient(
    match_search_criteria: str,  # "conditions" or "procedures" or "medications"
    code: str
):
    matches = []

    for patient in PATIENTS_DB.values():
        patient_values = patient.get(match_search_criteria, [])
        if any(code in value for value in patient_values):
            # Only return the relevant fields
            matches.append({
                "name": patient.get("name"),
                "dob": patient.get("dob"),
                "address": patient.get("address"),
                "vitals": patient.get("vitals")
            })

    return matches
