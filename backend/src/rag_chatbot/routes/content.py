"""
Content Management Routes
Endpoints for managing textbook content
"""

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Any
import logging

from ..services.rag_service import get_rag_service, RAGService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/content", tags=["content"])


class ContentLoadResponse(BaseModel):
    """Response for content loading"""
    success: bool
    message: str
    stats: Dict[str, Any]
    chapters_processed: int


@router.post("/load", response_model=ContentLoadResponse)
async def load_content(
    background_tasks: BackgroundTasks,
    rag_service: RAGService = Depends(get_rag_service)
):
    """
    Load textbook content into the vector store
    
    This endpoint loads the textbook content from the JSON file,
    generates embeddings, and stores them in the vector database.
    
    This should be called once when the service starts or when
    content is updated.
    """
    try:
        logger.info("Loading textbook content...")
        result = rag_service.load_content()
        
        if result.get("success"):
            return ContentLoadResponse(
                success=True,
                message=result.get("message", "Content loaded successfully"),
                stats=result.get("stats", {}),
                chapters_processed=result.get("chapters_processed", 0)
            )
        else:
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to load content")
            )
            
    except Exception as e:
        logger.error(f"Error loading content: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error loading content: {str(e)}"
        )


@router.get("/status")
async def content_status(rag_service: RAGService = Depends(get_rag_service)):
    """Get content loading status"""
    stats = rag_service.vector_store.get_collection_stats()
    return {
        "content_loaded": rag_service.content_loaded,
        "stats": stats,
        "content_path": rag_service.content_path
    }


@router.post("/reset")
async def reset_content(rag_service: RAGService = Depends(get_rag_service)):
    """Reset the vector store (delete all content)"""
    try:
        rag_service.vector_store.reset()
        rag_service.content_loaded = False
        return {
            "success": True,
            "message": "Vector store reset successfully"
        }
    except Exception as e:
        logger.error(f"Error resetting content: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error resetting content: {str(e)}"
        )
