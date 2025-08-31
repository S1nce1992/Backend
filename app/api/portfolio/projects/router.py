from fastapi import APIRouter

router = APIRouter()

sample_projects = [
    {
        "id": 1,
        "name": "Guardian Net",
        "desc": "Family Safety and Healthy Surveilance of Adult Children",
        "link": "http://localhost:4000"
    },
    {
        "id": 2,
        "name": "Foren Scope",
        "desc": "Forensic analysis for image and document evidence",
        "link": "http://localhost:5000"
    },
    {
        "id": 3,
        "name": "Threat Sim",
        "desc": "Public Cyber Awareness Simulator: Simulates threat scenarios and visualizes response metrics",
        "link": "http://localhost:3000"
    },
    {
        "id": 4,
        "name": "Location Guard",
        "desc": "Control & Transparency on HOW apps use Location Data",
        "link": "http://localhost:4001"
    }
]

@router.get("/projects")
def list_projects():
    return {"projects": sample_projects}




"""# app/api/portfolio/projects/router.py
from fastapi import APIRouter

router = APIRouter()

sample_projects = [
    {"id": 1, "title": "Threat Sim", "description": "Public Cyber Awareness Simulator: Simulates threat scenarios and visualizes response metrics"},
    {"id": 2, "title": "Foren Scope", "description": "Forensic analysis for image and document evidence"},
    {"id": 3, "title": "Portfolio", "description": "My personal portfolio with integrated backend API"},
    {"id": 4, "title": "Location Guard", "description": "Control & Transparency on HOW apps use Location Data"},
    {"id": 5, "title": "Guardian Net", "description": "Family Safety and healthy surveilance of adult children"}
]

@router.get("/projects")
def list_projects():
    return {"projects": sample_projects} """
