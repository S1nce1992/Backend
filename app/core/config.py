# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Multi-App Backend"
    api_version: str = "v1"

    class Config:
        env_file = ".env"

settings = Settings()
