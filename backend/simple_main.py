import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uuid
from datetime import datetime
import os
import sys

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Define the data models directly here to avoid import issues
from pydantic import BaseModel, Field

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


class QueryContext(BaseModel):
    query: str
    selected_text: Optional[str] = None
    language: str = "en"  # Default to English, supports "ur" for Urdu
    context_window: Optional[str] = None


class Document(BaseModel):
    id: str
    content: str
    metadata: dict = {}
    embedding: Optional[list] = None


# Create a simple chatbot service
class SimpleChatService:
    def __init__(self):
        # Initialize with some basic knowledge about the textbook
        self.knowledge_base = [
            "Physical AI is the field of AI that functions in the real world and understands physical laws.",
            "ROS 2 is the Robot Operating System used for robot control and communication between nodes.",
            "Gazebo and Unity are used for physics simulation and digital twin creation.",
            "NVIDIA Isaac is a platform for AI-powered robotics with perception and navigation capabilities.",
            "VLA stands for Vision-Language-Action, connecting language models to robot actions.",
            "Humanoid robots are designed to have a human-like form to interact effectively in human environments.",
            "Embodied Intelligence refers to AI systems that exist and operate in physical space rather than digital environments."
        ]
    
    async def query(self, query_context: QueryContext) -> str:
        """
        Simple query processing without vector database
        """
        query = query_context.query.lower()
        
        # If there's selected text, respond based on that
        if query_context.selected_text:
            return f"Based on the selected text: '{query_context.selected_text[:100]}...', I can explain that this content relates to your question about '{query_context.query}'."
        
        # Simple keyword-based response
        if "ros" in query or "robot operating system" in query:
            return "ROS 2 (Robot Operating System 2) is middleware for robot control. It provides services like hardware abstraction, device drivers, libraries, and message-passing between nodes. It's essential for connecting all components of modern robotics systems."
        elif "physical ai" in query or "embodied intelligence" in query:
            return "Physical AI refers to AI systems that function in reality and comprehend physical laws. Embodied Intelligence means AI systems that exist and operate in physical space rather than digital environments. This represents the transition from AI models confined to digital spaces to intelligent agents that operate in the physical world."
        elif "gazebo" in query or "simulation" in query:
            return "Gazebo is a physics simulation environment used for robotics. It allows you to simulate robots in realistic virtual worlds with accurate physics, gravity, and collisions. This is part of creating digital twins for testing robot behaviors before real-world deployment."
        elif "nvidia" in query or "isaac" in query:
            return "NVIDIA Isaac is a comprehensive platform for AI-powered robotics. It includes Isaac Sim for photorealistic simulation and synthetic data generation, and Isaac ROS for hardware-accelerated perception and navigation. It's particularly used for advanced perception systems and training."
        elif "vla" in query or "vision-language-action" in query:
            return "VLA stands for Vision-Language-Action. This represents the convergence of LLMs (Large Language Models) and robotics, where natural language commands are translated into robot actions. It enables robots to understand human language and execute complex tasks based on verbal instructions."
        elif "humanoid" in query or "robot" in query:
            return "Humanoid robots are designed with human-like form factors to operate effectively in human environments. They can be trained using abundant data from human interactions and are optimized for spaces designed for humans."
        else:
            # Generate a generic response with some knowledge
            import random
            base_response = f"Regarding your question about '{query_context.query}', "
            knowledge = random.choice(self.knowledge_base)
            return base_response + knowledge + " For more specific information, please refer to the relevant sections in the textbook or ask more targeted questions about specific topics like ROS 2, Gazebo simulation, NVIDIA Isaac, or Vision-Language-Action systems."


# Create the FastAPI app
app = FastAPI(
    title="Simple RAG Chatbot API",
    description="Simplified API for the RAG Chatbot (no external dependencies)",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the simple chat service
chat_service = SimpleChatService()


@app.post("/api/v1/chat",
          response_model=ChatResponse,
          responses={
              400: {"model": ErrorResponse},
              500: {"model": ErrorResponse}
          })
async def chat_endpoint(chat_request: ChatRequest):
    """
    Main chat endpoint that processes user queries
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

        # Process the query using simple chat service
        response_text = await chat_service.query(query_context)

        # Create and return the response
        response = ChatResponse(
            response=response_text,
            session_id=session_id,
            timestamp=datetime.utcnow().isoformat(),
            sources=["textbook_content"]  # In a real implementation, we would return actual source documents
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat request: {str(e)}"
        )


@app.get("/api/v1/chat/health")
async def chat_health():
    """
    Health check for the chat service
    """
    return {"status": "healthy", "service": "simple_chat"}


@app.get("/")
def read_root():
    return {"message": "Simple RAG Chatbot API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        "simple_main:app",  # Using import string
        host="0.0.0.0",
        port=8000,
        reload=True
    )