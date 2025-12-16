from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat
from .config import settings

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

# Include chat routes
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])

@app.get("/")
def read_root():
    return {"message": "RAG Chatbot API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}