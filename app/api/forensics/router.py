from fastapi import APIRouter
from app.api.forensics.cases.router import router as cases_router

router = APIRouter()
router.include_router(cases_router, prefix="", tags=["ForenScope"])

