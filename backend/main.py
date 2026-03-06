import uvicorn
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from src.rag_chatbot.main import app
from src.rag_chatbot.config import settings

# Initialize database tables
from src.auth.database import init_db
init_db()

# Import and mount auth routes
from src.auth.routes import router as auth_router
app.include_router(auth_router, prefix="/api/v1")

# Import and mount personalization routes
from src.personalization.routes import router as personalization_router
app.include_router(personalization_router, prefix="/api/v1/personalization")

# Import and mount translation routes
from src.translation.routes import router as translation_router
app.include_router(translation_router, prefix="/api/v1/translation")

# Import and mount RAG chat routes
from src.rag_chatbot.routes.chat import router as chat_router
app.include_router(chat_router)

# Import and mount content management routes
from src.rag_chatbot.routes.content import router as content_router
app.include_router(content_router)


if __name__ == "__main__":
    uvicorn.run(
        "src.rag_chatbot.main:app",
        host="0.0.0.0",
        port=8000,
        reload=not settings.debug
    )