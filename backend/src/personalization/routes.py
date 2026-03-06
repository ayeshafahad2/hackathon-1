# backend/src/personalization/routes.py
# Personalization API routes

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import Dict, Any

from ..auth.models import User
from ..auth.service import AuthService
from .engine import PersonalizationEngine
from ..auth.routes import get_current_user  # Assuming this is the function to get user from token
from ..auth.database import get_db

router = APIRouter()

@router.post("/personalize-content")
async def personalize_chapter_content(
    chapter_id: str = Body(...),
    content: str = Body(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Personalize chapter content based on user's background
    """
    try:
        # Use the personalization engine to modify content
        engine = PersonalizationEngine()
        personalized_content = engine.personalize_content(content, current_user)
        
        # Optionally award points for using personalization
        # This would require updating the auth service to award points
        from ..auth.service import AuthService
        auth_service = AuthService()
        auth_service.award_bonus_points(db, current_user.id, 50)
        
        # Update user's profile to indicate personalization was used
        auth_service.update_user_profile(db, current_user.id, personalization_enabled=True)
        
        return {
            "original_content": content,
            "personalized_content": personalized_content,
            "user_profile_used": {
                "software_experience": current_user.software_experience,
                "hardware_experience": current_user.hardware_experience,
                "field_of_interest": current_user.field_of_interest,
                "programming_languages": current_user.programming_languages
            },
            "bonus_points_awarded": 50,
            "message": f"Content for chapter {chapter_id} has been personalized based on your background"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error personalizing content: {str(e)}")

@router.get("/health")
async def personalization_health():
    return {"status": "healthy", "service": "personalization"}