from fastapi import APIRouter, HTTPException
from typing import Optional
import uuid
from datetime import datetime
from ..models.request_models import ChatRequest, ChatResponse, ErrorResponse
from ..models.data_models import QueryContext
from ..services.rag_service import RAGService


router = APIRouter()
rag_service = RAGService()


@router.post("/chat",
             response_model=ChatResponse,
             responses={
                 400: {"model": ErrorResponse},
                 500: {"model": ErrorResponse}
             })
async def chat_endpoint(chat_request: ChatRequest):
    """
    Main chat endpoint that processes user queries using RAG
    """
    try:
        # Generate a session ID if not provided
        session_id = chat_request.session_id or str(uuid.uuid4())

        # Create query context from the request
        query_context = QueryContext(
            query=chat_request.message,
            selected_text=chat_request.selected_text,
            language=chat_request.language
        )

        # Process the query using RAG service
        response_text = await rag_service.query(query_context)

        # Create and return the response
        response = ChatResponse(
            response=response_text,
            session_id=session_id,
            timestamp=datetime.utcnow().isoformat(),
            sources=[]  # In a more advanced implementation, we would return source documents
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat request: {str(e)}"
        )


@router.post("/chat/upload-textbook-content")
async def upload_textbook_content(content: str, title: str = "", section: str = ""):
    """
    Endpoint to upload textbook content for RAG indexing
    """
    try:
        from ..models.data_models import Document

        # Create a document from the content
        doc = Document(
            id=str(uuid.uuid4()),
            content=content,
            metadata={
                "title": title,
                "section": section,
                "created_at": datetime.utcnow().isoformat()
            }
        )

        # Add to RAG system
        success = await rag_service.add_document(doc)

        if success:
            return {"message": "Content uploaded successfully", "doc_id": doc.id}
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to upload content to RAG system"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error uploading textbook content: {str(e)}"
        )


@router.get("/chat/health")
async def chat_health():
    """
    Health check for the chat service
    """
    return {"status": "healthy", "service": "chat"}