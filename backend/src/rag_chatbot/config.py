from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # OpenAI settings
    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"
    embedding_model: str = "text-embedding-ada-002"

    # Qdrant settings
    qdrant_url: str
    qdrant_api_key: Optional[str] = None

    # Postgres settings
    postgres_url: str

    # Application settings
    app_name: str = "RAG Chatbot API"
    debug: bool = False
    max_context_length: int = 4000  # Maximum context length for the model
    response_timeout: int = 30  # Timeout for responses in seconds

    class Config:
        env_file = ".env"


settings = Settings()