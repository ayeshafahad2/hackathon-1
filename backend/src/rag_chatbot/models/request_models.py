from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    session_id: Optional[str] = None
    selected_text: Optional[str] = None
    language: str = "en"  # Default to English, supports "ur" for Urdu


class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: str
    sources: Optional[list] = []


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None