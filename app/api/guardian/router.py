from fastapi import APIRouter
from app.api.guardian.incidents.router import router as incidents_router

router = APIRouter()
router.include_router(incidents_router, prefix="", tags=["GuardianNet"])

