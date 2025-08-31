import sys
from pathlib import Path

# Add the parent of Backend (~/dev) to sys.path so `Shared` can be imported everywhere
sys.path.append(str(Path(__file__).resolve().parents[2]))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multi-App Backend")

# --- CORS setup ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- End CORS setup ---

# Import routers *after* sys.path is fixed
from app.api.crypto.router import router as crypto_router
from app.api.threats.router import router as threats_router
from app.api.forensics.router import router as forensics_router
from app.api.location.router import router as location_router
from app.api.guardian.router import router as guardian_router
from app.api.portfolio.router import router as portfolio_router

# Include routers
app.include_router(crypto_router, prefix="/api/v1/crypto", tags=["Crypto"])
app.include_router(threats_router, prefix="/api/v1/threats", tags=["ThreatSim"])
app.include_router(forensics_router, prefix="/api/v1/forensics", tags=["ForenScope"])
app.include_router(location_router, prefix="/api/v1/location", tags=["LocationGuard"])
app.include_router(guardian_router, prefix="/api/v1/guardian", tags=["GuardianNet"])
app.include_router(portfolio_router, prefix="/api/v1/portfolio", tags=["Portfolio"])

@app.get("/")
def root():
    return {"message": "Backend is Running 🚀"}
