# backend/src/auth/routes.py
# Authentication API routes

from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from typing import Optional, List

from .database import get_db
from .models import User
from .service import AuthService
import jwt

router = APIRouter()
security = HTTPBearer()
auth_service = AuthService()

# Pydantic models for request/response
class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str
    software_experience: Optional[str] = "beginner"
    hardware_experience: Optional[str] = "none"
    programming_languages: Optional[List[str]] = []
    field_of_interest: Optional[str] = ""
    educational_affiliation: Optional[str] = ""

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserProfileResponse(BaseModel):
    id: int
    email: str
    software_experience: str
    hardware_experience: str
    programming_languages: List[str]
    field_of_interest: str
    educational_affiliation: str
    personalization_enabled: bool
    bonus_points: int
    profile_complete: bool

class UserProfileUpdateRequest(BaseModel):
    software_experience: Optional[str] = None
    hardware_experience: Optional[str] = None
    programming_languages: Optional[List[str]] = None
    field_of_interest: Optional[str] = None
    educational_affiliation: Optional[str] = None

# Dependency to get current user from token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    token = credentials.credentials
    payload = auth_service.verify_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id: int = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = auth_service.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

# Routes
@router.post("/auth/register", response_model=TokenResponse)
def register_user(
    user_data: UserCreateRequest,
    db: Session = Depends(get_db)
):
    # Check if user already exists
    existing_user = auth_service.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user with profile data
    user = auth_service.create_user(
        db,
        email=user_data.email,
        password=user_data.password,
        software_experience=user_data.software_experience,
        hardware_experience=user_data.hardware_experience,
        programming_languages=user_data.programming_languages,
        field_of_interest=user_data.field_of_interest,
        educational_affiliation=user_data.educational_affiliation
    )
    
    # Create access token
    access_token = auth_service.create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/login", response_model=TokenResponse)
def login_user(
    login_data: UserLoginRequest,
    db: Session = Depends(get_db)
):
    user = auth_service.authenticate_user(
        db, login_data.email, login_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token = auth_service.create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/auth/me", response_model=UserProfileResponse)
def get_current_user_profile(
    current_user: User = Depends(get_current_user)
):
    return UserProfileResponse(
        id=current_user.id,
        email=current_user.email,
        software_experience=current_user.software_experience,
        hardware_experience=current_user.hardware_experience,
        programming_languages=current_user.programming_languages,
        field_of_interest=current_user.field_of_interest,
        educational_affiliation=current_user.educational_affiliation,
        personalization_enabled=current_user.personalization_enabled,
        bonus_points=current_user.bonus_points,
        profile_complete=current_user.profile_complete
    )

@router.put("/auth/profile", response_model=UserProfileResponse)
def update_user_profile(
    profile_update: UserProfileUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated_user = auth_service.update_user_profile(
        db,
        current_user.id,
        software_experience=profile_update.software_experience,
        hardware_experience=profile_update.hardware_experience,
        programming_languages=profile_update.programming_languages,
        field_of_interest=profile_update.field_of_interest,
        educational_affiliation=profile_update.educational_affiliation
    )
    
    return UserProfileResponse(
        id=updated_user.id,
        email=updated_user.email,
        software_experience=updated_user.software_experience,
        hardware_experience=updated_user.hardware_experience,
        programming_languages=updated_user.programming_languages,
        field_of_interest=updated_user.field_of_interest,
        educational_affiliation=updated_user.educational_affiliation,
        personalization_enabled=updated_user.personalization_enabled,
        bonus_points=updated_user.bonus_points,
        profile_complete=updated_user.profile_complete
    )

@router.post("/auth/personalize-content")
def personalize_content_chapter(
    chapter_id: str = Body(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint called when user clicks 'Personalize Content' button
    Awards bonus points and enables personalization
    """
    # Award 50 bonus points for using personalization
    updated_user = auth_service.award_bonus_points(db, current_user.id, 50)
    
    # Enable personalization for this user
    updated_user = auth_service.update_user_profile(
        db, current_user.id, personalization_enabled=True
    )
    
    return {
        "message": f"Content personalization enabled for chapter {chapter_id}",
        "bonus_points_awarded": 50,
        "total_bonus_points": updated_user.bonus_points
    }

@router.post("/auth/translate-urdu")
def translate_chapter_urdu(
    chapter_id: str = Body(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint called when user clicks 'Translate to Urdu' button
    Awards bonus points for using translation feature
    """
    # Award 50 bonus points for using Urdu translation
    updated_user = auth_service.award_bonus_points(db, current_user.id, 50)
    
    return {
        "message": f"Content translated to Urdu for chapter {chapter_id}",
        "bonus_points_awarded": 50,
        "total_bonus_points": updated_user.bonus_points
    }

@router.get("/auth/health")
async def auth_health():
    return {"status": "healthy", "service": "authentication"}