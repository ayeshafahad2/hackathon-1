import uvicorn
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from src.rag_chatbot.main import app
from src.rag_chatbot.config import settings


if __name__ == "__main__":
    uvicorn.run(
        "src.rag_chatbot.main:app",
        host="0.0.0.0",
        port=8000,
        reload=not settings.debug
    )