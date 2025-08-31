from fastapi import APIRouter
from app.api.threats.scenarios.router import router as scenarios_router

router = APIRouter()
router.include_router(scenarios_router, prefix="", tags=["ThreatSim"])
