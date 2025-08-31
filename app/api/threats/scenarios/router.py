from fastapi import APIRouter

router = APIRouter()

sample_scenarios = [
    {"id": 1, "name": "Phishing Campaign", "severity": "medium"},
    {"id": 2, "name": "Ransomware Outbreak", "severity": "high"},
    {"id": 3, "name": "DDoS Spike", "severity": "low"},
]

@router.get("/scenarios")
def list_scenarios():
    return {"scenarios": sample_scenarios}
