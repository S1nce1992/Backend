from fastapi import APIRouter

router = APIRouter()

sample_incidents = [
    {"id": 9001, "type": "Intrusion", "status": "open"},
    {"id": 9002, "type": "Malware Detected", "status": "mitigated"},
    {"id": 9003, "type": "Policy Violation", "status": "under_investigation"},
]

@router.get("/incidents")
def list_incidents():
    return {"incidents": sample_incidents}
