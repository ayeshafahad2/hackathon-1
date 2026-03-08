---
title: Physical AI & Humanoid Robotics Backend
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
license: mit
tags:
  - fastapi
  - rag
  - chatbot
  - robotics
  - physical-ai
---

# Physical AI & Humanoid Robotics - RAG Chatbot Backend

This Space hosts the backend API for the Physical AI & Humanoid Robotics textbook chatbot.

## Features

- 🤖 RAG-powered chatbot answering questions about Physical AI & Humanoid Robotics
- 📚 Complete textbook content with 13 weeks of material
- 🔍 Semantic search using ChromaDB vector store
- 🌐 RESTful API with CORS support
- ⚡ Fast response times with local embeddings

## API Endpoints

### Health Check
```bash
GET /health
```

Response:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

### Chat Endpoint
```bash
POST /api/v1/chat
Content-Type: application/json

{
  "message": "What is Physical AI?",
  "session_id": "optional-session-id",
  "language": "en"
}
```

Response:
```json
{
  "response": "Physical AI represents a paradigm shift...",
  "sources": [
    {
      "chapter": "Introduction to Physical AI",
      "section": "Foundations of Physical AI",
      "similarity": 0.95
    }
  ],
  "session_id": "session-id",
  "confidence": 0.95,
  "language": "en"
}
```

### Content Load
```bash
POST /api/v1/content/load
```

### Content Status
```bash
GET /api/v1/content/status
```

## Environment Variables

Configure these in Space Settings → Repository secrets:

- `GEMINI_API_KEY` - Google Gemini API key (optional, for enhanced responses)
- `QDRANT_URL` - Qdrant Cloud URL (optional, for production vector store)
- `QDRANT_API_KEY` - Qdrant API key
- `SECRET_KEY` - Application secret key

## Local Development

```bash
# Build Docker image
docker build -t physical-ai-backend .

# Run container
docker run -p 7860:7860 physical-ai-backend

# Test
curl http://localhost:7860/health
```

## Usage with Frontend

Set `REACT_APP_BACKEND_URL` to this Space's URL in your Vercel frontend:

```
REACT_APP_BACKEND_URL=https://your-username-physical-ai-backend.hf.space
```

## Textbook Coverage

- Week 1-2: Physical AI & Embodied Intelligence
- Week 3-5: ROS 2 Fundamentals & Advanced Topics
- Week 6-7: Gazebo Simulation
- Week 8-10: NVIDIA Isaac Platform & Sim-to-Real
- Week 11-13: Humanoid Kinematics, HRI, VLA Models

## License

MIT License

## Credits

Built with:
- FastAPI
- ChromaDB
- Sentence Transformers
- Hugging Face Spaces
