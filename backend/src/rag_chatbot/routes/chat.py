"""
Chat Routes for RAG Chatbot
API endpoints for chatting with the textbook
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import logging
import uuid

from ..services.rag_service import get_rag_service, RAGService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["chat"])

# Request/Response Models

class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str = Field(..., description="User's message/question")
    session_id: Optional[str] = Field(None, description="Session ID for conversation history")
    selected_text: Optional[str] = Field(None, description="Selected text from the page")
    language: str = Field("en", description="Language preference (en/ur)")


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str = Field(..., description="AI assistant's response")
    sources: List[Dict[str, Any]] = Field(default_factory=list, description="Source citations")
    session_id: str = Field(..., description="Session ID")
    confidence: float = Field(..., description="Confidence score (0-1)")
    language: str = Field("en", description="Response language")
    qwen_available: bool = Field(False, description="Whether Qwen API is configured")


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    service: str
    content_loaded: bool


# In-memory session storage (use Redis in production)
sessions: Dict[str, List[Dict[str, str]]] = {}


@router.get("/health", response_model=HealthResponse)
async def health_check(rag_service: RAGService = Depends(get_rag_service)):
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        service="RAG Chatbot",
        content_loaded=rag_service.content_loaded
    )


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    rag_service: RAGService = Depends(get_rag_service)
):
    """
    Chat with the AI textbook assistant
    
    This endpoint accepts a question about the textbook content and returns
    an answer with citations to the relevant sections.
    """
    try:
        # Generate session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())
        
        # Get chat history for session
        chat_history = sessions.get(session_id, [])
        
        # Add selected text to message if provided
        message = request.message
        if request.selected_text:
            message = f"Context from page: \"{request.selected_text}\"\n\nQuestion: {request.message}"
        
        # Get response from RAG service (async call)
        result = await rag_service.chat(
            message=message,
            session_id=session_id,
            chat_history=chat_history
        )
        
        # Update chat history
        chat_history.append({"role": "user", "content": request.message})
        chat_history.append({"role": "assistant", "content": result["response"]})
        sessions[session_id] = chat_history
        
        # Keep history manageable (last 10 exchanges)
        if len(chat_history) > 20:
            chat_history = chat_history[-20:]
            sessions[session_id] = chat_history
        
        return ChatResponse(
            response=result["response"],
            sources=result["sources"],
            session_id=session_id,
            confidence=result["confidence"],
            language=request.language,
            qwen_available=result.get("qwen_available", False)
        )
        
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )


@router.post("/chat/reset")
async def reset_chat(session_id: str):
    """Reset chat history for a session"""
    if session_id in sessions:
        del sessions[session_id]
    return {"message": "Chat history reset", "session_id": session_id}


@router.get("/sessions")
async def list_sessions():
    """List active sessions (for debugging)"""
    return {
        "active_sessions": len(sessions),
        "session_ids": list(sessions.keys())[:10]  # Limit to first 10
    }
