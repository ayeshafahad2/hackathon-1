#!/usr/bin/env python3
"""
Complete startup script for the RAG Chatbot
This script will:
1. Test Qdrant connection
2. Load textbook content to the vector database
3. Start the FastAPI server
"""

import asyncio
import os
import sys
import subprocess
import threading
import time
from pathlib import Path

# Add the backend src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.rag_chatbot.services.qdrant_service import QdrantService
from src.rag_chatbot.config import settings
from load_textbook_content import test_qdrant_connection, load_textbook_content


def check_dependencies():
    """Check if all required dependencies are installed"""
    print("Checking dependencies...")
    
    required_packages = [
        "fastapi",
        "uvicorn",
        "openai",
        "qdrant-client",
        "pydantic",
        "pydantic-settings",
        "asyncpg",
        "python-dotenv"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True


def validate_env_vars():
    """Validate that required environment variables are set"""
    print("Validating environment variables...")
    
    if not settings.openai_api_key:
        print("❌ OPENAI_API_KEY is not set in .env file")
        return False
        
    if not settings.qdrant_url:
        print("❌ QDRANT_URL is not set in .env file")
        return False
        
    if not settings.qdrant_api_key:
        print("❌ QDRANT_API_KEY is not set in .env file")
        return False
        
    if not settings.postgres_url:
        print("❌ POSTGRES_URL is not set in .env file")
        return False
    
    print("✅ All required environment variables are set")
    return True


def start_fastapi_server():
    """Start the FastAPI server in a separate thread"""
    import uvicorn
    from src.rag_chatbot.main import app
    
    print("🚀 Starting FastAPI server...")
    uvicorn.run(
        "src.rag_chatbot.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False  # Disable reload for production
    )


def main():
    """Main startup sequence"""
    print("=" * 60)
    print("🤖 PHYSICAL AI & HUMANOID ROBOTICS RAG CHATBOT STARTUP")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Validate environment variables
    if not validate_env_vars():
        return False
    
    print("\n🔍 Testing Qdrant Connection...")
    if not test_qdrant_connection():
        print("❌ Qdrant connection failed. Please fix your configuration.")
        return False
    
    print("\n📚 Loading Textbook Content...")
    success = asyncio.run(load_textbook_content())
    if not success:
        print("⚠️  Warning: Could not load textbook content, but server will start anyway")
    
    print("\n✅ Setup completed successfully!")
    print("\n🌐 The RAG Chatbot API is ready at: http://localhost:8000")
    print("\n📋 API Endpoints:")
    print("   GET  /                 - Welcome page")
    print("   GET  /health           - Health check")
    print("   GET  /api/v1/chat/health - Chat service health")
    print("   POST /api/v1/chat      - Chat endpoint")
    print("   POST /api/v1/chat/upload-textbook-content - Upload content")
    
    print("\n📱 To start the frontend:")
    print("   cd frontend")
    print("   npm start")
    
    print("\n🧪 To test the API:")
    print("curl -X POST http://localhost:8000/api/v1/chat \\")
    print("  -H \"Content-Type: application/json\" \\")
    print("  -d '{\"message\": \"What is Physical AI?\"}'")
    
    print("\n" + "=" * 60)
    print("⏳ Starting FastAPI Server... Press Ctrl+C to stop")
    print("=" * 60)
    
    # Start the FastAPI server
    start_fastapi_server()


if __name__ == "__main__":
    main()