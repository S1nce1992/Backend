from fastapi import APIRouter

router = APIRouter()

sample_coords = [
    {"id": 1, "lat": 45.4215, "lon": -75.6972, "label": "Ottawa"},
    {"id": 2, "lat": 43.6532, "lon": -79.3832, "label": "Toronto"},
    {"id": 3, "lat": 45.5019, "lon": -73.5674, "label": "Montreal"},
]

@router.get("/coords")
def list_coords():
    return {"coords": sample_coords}
