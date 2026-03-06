# backend/src/auth/models.py
# Database models for user authentication and profile management

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from typing import List, Optional

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Extended profile fields for hardware/software background
    software_experience = Column(String, default="beginner")  # beginner, intermediate, expert
    hardware_experience = Column(String, default="none")     # none, basic, advanced, professional
    programming_languages = Column(ARRAY(String), default=[])  # list of programming languages
    field_of_interest = Column(String, default="")  # robotics, ai, control systems, etc.
    educational_affiliation = Column(String, default="")  # university, company, etc.
    personalization_enabled = Column(Boolean, default=False)
    bonus_points = Column(Integer, default=0)
    profile_complete = Column(Boolean, default=False)  # indicates if background survey is complete