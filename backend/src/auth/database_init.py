from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User
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

# Create database engine
DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, 
                      connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables"""
    print(f"Initializing database with URL: {DATABASE_URL}")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()