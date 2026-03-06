# backend/src/translation/routes.py
# Translation API routes

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import Dict, Any

from ..auth.models import User
from ..auth.service import AuthService
from .translator import ProductionUrduTranslator
from ..auth.routes import get_current_user
from ..auth.database import get_db

router = APIRouter()
translator = ProductionUrduTranslator()

@router.post("/translate-urdu")
async def translate_chapter_to_urdu(
    chapter_id: str = Body(...),
    content: str = Body(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Translate chapter content to Urdu
    """
    try:
        # Translate the content to Urdu
        urdu_content = translator.translate_to_urdu(content)
        
        # Award bonus points for using translation feature
        auth_service = AuthService()
        auth_service.award_bonus_points(db, current_user.id, 50)
        
        return {
            "original_content": content,
            "urdu_content": urdu_content,
            "chapter_id": chapter_id,
            "bonus_points_awarded": 50,
            "total_bonus_points": current_user.bonus_points + 50,
            "message": f"Content for chapter {chapter_id} has been translated to Urdu"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating content: {str(e)}")

@router.get("/health")
async def translation_health():
    return {"status": "healthy", "service": "translation"}