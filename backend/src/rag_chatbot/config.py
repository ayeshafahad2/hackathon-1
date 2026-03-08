from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # OpenAI settings
    openai_api_key: Optional[str] = None  # Optional since we're switching to Gemini
    openai_model: str = "gpt-3.5-turbo"
    embedding_model: str = "text-embedding-ada-002"

    # Google Gemini settings
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-pro"

    # Qdrant settings (optional for deployment)
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None

    # Postgres settings
    postgres_url: Optional[str] = None

    # NeonDB settings
    neondb_api_key: Optional[str] = None

    # Application settings
    app_name: str = "RAG Chatbot API"
    debug: bool = False
    log_level: str = "info"
    max_context_length: int = 4000  # Maximum context length for the model
    response_timeout: int = 30  # Timeout for responses in seconds

    # Authentication settings
    secret_key: Optional[str] = "fallback-secret-key-change-in-production"
    better_auth_secret: Optional[str] = "fallback-better-auth-secret-change-in-production"
    better_auth_url: Optional[str] = "http://localhost:3000"
    database_url: Optional[str] = "postgresql://user:password@localhost/dbname"
    base_url: Optional[str] = "http://localhost:8000"

    class Config:
        env_file = ".env"


settings = Settings()