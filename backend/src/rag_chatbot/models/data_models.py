from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatSession(BaseModel):
    session_id: str
    messages: List[ChatMessage] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Document(BaseModel):
    id: str
    content: str
    metadata: dict = {}
    embedding: Optional[List[float]] = None


class QueryContext(BaseModel):
    query: str
    selected_text: Optional[str] = None
    language: str = "en"  # Default to English, supports "ur" for Urdu
    context_window: Optional[str] = None