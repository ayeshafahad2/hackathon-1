from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from .routes import chat, content
from .config import settings
from .services.rag_service import get_rag_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    # Startup: Load content
    logger.info("Starting up RAG Chatbot API...")
    rag_service = get_rag_service()
    
    # Load content on startup
    try:
        logger.info("Loading textbook content...")
        result = rag_service.load_content()
        if result.get("success"):
            logger.info(f"Content loaded: {result.get('stats')}")
        else:
            logger.error(f"Failed to load content: {result.get('error')}")
    except Exception as e:
        logger.error(f"Error loading content: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down RAG Chatbot API...")

app = FastAPI(
    title="RAG Chatbot API",
    description="API for the RAG Chatbot integrated with the Physical AI & Humanoid Robotics textbook",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chat.router, tags=["chat"])
app.include_router(content.router, tags=["content"])

@app.get("/")
def read_root():
    return {
        "message": "RAG Chatbot API is running",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/api/v1/chat",
            "health": "/api/v1/health",
            "content_load": "/api/v1/content/load",
            "content_status": "/api/v1/content/status"
        }
    }