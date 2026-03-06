import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging
import uuid
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Professional RAG Chatbot API",
    description="A professional multilingual chatbot with Gemini AI integration",
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

# Import and mount auth routes
try:
    from src.auth.routes import router as auth_router
    app.include_router(auth_router, prefix="/api/v1")
    logger.info("✓ Authentication routes loaded")
except Exception as e:
    logger.error(f"Authentication routes failed: {e}")

# Import and mount personalization routes
try:
    from src.personalization.routes import router as personalization_router
    app.include_router(personalization_router, prefix="/api/v1/personalization")
    logger.info("✓ Personalization routes loaded")
except Exception as e:
    logger.error(f"Personalization routes failed: {e}")

# Import and mount translation routes
try:
    from src.translation.routes import router as translation_router
    app.include_router(translation_router, prefix="/api/v1/translation")
    logger.info("✓ Translation routes loaded")
except Exception as e:
    logger.error(f"Translation routes failed: {e}")

# Simple chat models for testing
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    selected_text: Optional[str] = None
    language: Optional[str] = "en"

class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: str

# Simple chat endpoint with greeting/farewell handling
@app.post("/api/v1/chat", response_model=ChatResponse)
async def simple_chat_endpoint(chat_request: ChatRequest):
    """Simple chat endpoint that handles greetings and basic questions"""
    message = chat_request.message.lower()
    
    # Handle greetings
    if any(greeting in message for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        response = "Hello! Welcome to the Physical AI & Humanoid Robotics textbook assistant. I'm here to help you understand concepts related to Physical AI and Humanoid Robotics. How can I assist you today?"
    # Handle farewells
    elif any(farewell in message for farewell in ["bye", "goodbye", "see you", "exit", "quit"]):
        response = "Thank you for visiting the Physical AI & Humanoid Robotics textbook assistant. Feel free to come back anytime with more questions. Have a great day!"
    else:
        # For other queries, provide a placeholder response
        response = f"I received your message: '{chat_request.message}'. With Gemini API integration, I would provide detailed answers about Physical AI & Humanoid Robotics. Please set up your GEMINI_API_KEY in the .env file to get full functionality."
    
    session_id = chat_request.session_id or str(uuid.uuid4())
    
    return ChatResponse(
        response=response,
        session_id=session_id,
        timestamp=datetime.utcnow().isoformat()
    )

@app.get("/")
def read_root():
    return {"message": "Professional RAG Chatbot API is running", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "main-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)