# backend/src/auth/service.py
# Authentication and user profile service

from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import jwt
import bcrypt
from sqlalchemy.orm import Session
from .models import User
from ..rag_chatbot.config import settings

# JWT token configuration
SECRET_KEY = settings.secret_key or "fallback-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password"""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Create a JWT access token"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> Optional[Dict[str, Any]]:
        """Verify a JWT token and return the payload"""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.JWTError:
            return None

    def authenticate_user(self, db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate a user by email and password"""
        user = db.query(User).filter(User.email == email).first()
        if not user or not self.verify_password(password, user.hashed_password):
            return None
        return user

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get a user by email"""
        return db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        """Get a user by ID"""
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, email: str, password: str, **profile_data) -> User:
        """Create a new user with profile data"""
        hashed_pwd = self.hash_password(password)
        
        # Map profile data keys to model field names
        profile_fields = {
            'software_experience': profile_data.get('software_experience', 'beginner'),
            'hardware_experience': profile_data.get('hardware_experience', 'none'),
            'programming_languages': profile_data.get('programming_languages', []),
            'field_of_interest': profile_data.get('field_of_interest', ''),
            'educational_affiliation': profile_data.get('educational_affiliation', ''),
            'profile_complete': 'software_experience' in profile_data  # If background questions answered
        }
        
        db_user = User(
            email=email,
            hashed_password=hashed_pwd,
            **profile_fields
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user_profile(self, db: Session, user_id: int, **profile_data) -> User:
        """Update user profile fields"""
        user = self.get_user_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")
        
        # Update profile fields if provided
        for field, value in profile_data.items():
            if hasattr(user, field):
                setattr(user, field, value)
        
        # Mark profile as complete if background questions are answered
        if ('software_experience' in profile_data or 
            'hardware_experience' in profile_data or
            'programming_languages' in profile_data):
            user.profile_complete = True
        
        db.commit()
        db.refresh(user)
        return user

    def award_bonus_points(self, db: Session, user_id: int, points: int) -> User:
        """Award bonus points to a user"""
        user = self.get_user_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")
        
        user.bonus_points += points
        db.commit()
        db.refresh(user)
        return user