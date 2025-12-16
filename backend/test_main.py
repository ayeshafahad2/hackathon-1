import uvicorn
import sys
import os


if __name__ == "__main__":
    uvicorn.run(
        "src.rag_chatbot.mock_main:app",  # Using import string
        host="0.0.0.0",
        port=8000,
        reload=True
    )