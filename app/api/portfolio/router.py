from fastapi import APIRouter
from app.api.portfolio.projects.router import router as projects_router

router = APIRouter()

# Mount the /projects route(s) here so they become part of /portfolio
router.include_router(projects_router, prefix="", tags=["Portfolio"])
