from fastapi import APIRouter
from app.api.location.coords.router import router as coords_router

router = APIRouter()
router.include_router(coords_router, prefix="", tags=["LocationGuard"])
