from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import (
    Profile, Experience, Project, Skill,
    ChatMessage, ChatResponse
)
from app.services.resume_service import resume_service
from app.services.chat_service import chat_service

router = APIRouter()


@router.get("/profile", response_model=dict)
async def get_profile():
    """Get profile information"""
    try:
        profile = await resume_service.get_profile()
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/experiences", response_model=List[dict])
async def get_experiences():
    """Get work experiences"""
    try:
        experiences = await resume_service.get_experiences()
        return experiences
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/projects", response_model=List[dict])
async def get_projects():
    """Get projects"""
    try:
        projects = await resume_service.get_projects()
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/skills", response_model=List[dict])
async def get_skills():
    """Get skills"""
    try:
        skills = await resume_service.get_skills()
        return skills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """Send a chat message and get AI response"""
    try:
        response, session_id = await chat_service.get_ai_response(
            message.message,
            message.session_id
        )
        return ChatResponse(response=response, session_id=session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
