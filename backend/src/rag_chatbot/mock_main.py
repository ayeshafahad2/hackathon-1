from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uuid
from datetime import datetime
from .models.request_models import ChatRequest, ChatResponse, ErrorResponse
from .models.data_models import QueryContext
from .services.mock_rag_service import MockRAGService  # Using mock RAG service


app = FastAPI(
    title="RAG Chatbot API",
    description="API for the RAG Chatbot integrated with the Physical AI & Humanoid Robotics textbook",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize mock RAG service (doesn't require external connections)
rag_service = MockRAGService()


@app.post("/api/v1/chat",
             response_model=ChatResponse,
             responses={
                 400: {"model": ErrorResponse},
                 500: {"model": ErrorResponse}
             })
async def chat_endpoint(chat_request: ChatRequest):
    """
    Main chat endpoint that processes user queries using mocked RAG
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

        # Process the query using mock RAG service
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


@app.post("/api/v1/chat/upload-textbook-content")
async def upload_textbook_content(content: str, title: str = "", section: str = ""):
    """
    Endpoint to upload textbook content for RAG indexing (mock version)
    """
    try:
        from .models.data_models import Document

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

        # Add to mock RAG system
        success = await rag_service.add_document(doc)

        if success:
            return {"message": "Content uploaded successfully (mock)", "doc_id": doc.id}
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to upload content to mock RAG system"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error uploading textbook content: {str(e)}"
        )


@app.get("/api/v1/chat/health")
async def chat_health():
    """
    Health check for the chat service
    """
    return {"status": "healthy", "service": "chat", "type": "mock"}


@app.get("/")
def read_root():
    return {"message": "RAG Chatbot API is running (mock version)"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "connection": "mock"}