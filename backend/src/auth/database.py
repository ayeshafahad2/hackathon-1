# backend/src/auth/database.py
# Database setup for the authentication system

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..rag_chatbot.config import settings
import os

def get_database_url():
    """Get database URL from settings, with fallback to SQLite for development"""
    # Use PostgreSQL if configured, otherwise fallback to SQLite
    if settings.postgres_url:
        return settings.postgres_url
    elif settings.database_url and 'sqlite' in settings.database_url.lower():
        return settings.database_url
    else:
        # Default to SQLite for development
        return "sqlite:///./users.db"

# Create database URL
DATABASE_URL = get_database_url()

# For SQLite, we need a different approach than PostgreSQL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize the database and create tables"""
    Base.metadata.create_all(bind=engine)