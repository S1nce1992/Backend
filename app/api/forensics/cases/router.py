from fastapi import APIRouter

router = APIRouter()

sample_cases = [
    {"id": 101, "title": "Image EXIF Audit", "status": "open"},
    {"id": 102, "title": "Document Metadata Sweep", "status": "closed"},
    {"id": 103, "title": "Email Header Trace", "status": "in_review"},
]

@router.get("/cases")
def list_cases():
    return {"cases": sample_cases}
