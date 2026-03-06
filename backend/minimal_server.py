import uvicorn
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Professional Chatbot")

# Simple models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    selected_text: Optional[str] = None
    language: Optional[str] = "en"

class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: str

# Professional chatbot with greeting support
@app.post("/api/v1/chat")
async def chat_endpoint(
    chat_request: ChatRequest,
    authorization: Optional[str] = Header(None)
):
    message = chat_request.message.lower().strip()
    
    # Handle greetings
    if any(greeting in message for greeting in ["hello", "hi", "hey", "good morning", "good afternoon", "greetings"]):
        response = "Hello! Welcome to the Physical AI & Humanoid Robotics textbook assistant. I'm here to help you understand concepts related to Physical AI and Humanoid Robotics. How can I assist you today?"
    # Handle farewells
    elif any(farewell in message for farewell in ["bye", "goodbye", "see you", "exit", "quit", "thanks", "thank you"]):
        response = "Thank you for visiting the Physical AI & Humanoid Robotics textbook assistant. Feel free to come back anytime with more questions. Have a great day!"
    else:
        # Default response for other queries
        response = f"I received your message: '{chat_request.message}'. To get detailed answers about Physical AI & Humanoid Robotics, please set up your GEMINI_API_KEY in the .env file."
    
    session_id = chat_request.session_id or str(uuid.uuid4())
    
    return {
        "response": response,
        "session_id": session_id,
        "timestamp": datetime.utcnow().isoformat()
    }

# Health check
@app.get("/")
def read_root():
    return {"message": "Professional Chatbot API is running", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Authentication endpoints
@app.post("/api/v1/auth/register")
async def register_user():
    return {"message": "User registration endpoint - full functionality requires database setup"}

@app.post("/api/v1/auth/login")
async def login_user():
    return {"message": "User login endpoint - full functionality requires database setup"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)