from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ProfileBase(BaseModel):
    """Base profile information"""
    name: str
    title: str
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    website: Optional[str] = None


class Profile(ProfileBase):
    """Profile with ID and timestamps"""
    id: str
    created_at: datetime


class ExperienceBase(BaseModel):
    """Base work experience"""
    company: str
    position: str
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = []


class Experience(ExperienceBase):
    """Experience with ID"""
    id: str
    profile_id: str
    created_at: datetime


class ProjectBase(BaseModel):
    """Base project information"""
    title: str
    description: Optional[str] = None
    technologies: List[str] = []
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None


class Project(ProjectBase):
    """Project with ID"""
    id: str
    profile_id: str
    created_at: datetime


class SkillBase(BaseModel):
    """Base skill information"""
    category: str
    name: str
    proficiency: Optional[str] = None


class Skill(SkillBase):
    """Skill with ID"""
    id: str
    profile_id: str
    created_at: datetime


class ChatMessage(BaseModel):
    """Chat message request"""
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response"""
    response: str
    session_id: str
