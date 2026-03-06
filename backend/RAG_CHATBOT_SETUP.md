# RAG Chatbot Setup Guide

## Overview
This RAG (Retrieval-Augmented Generation) chatbot allows users to ask questions about the Physical AI & Humanoid Robotics textbook and get accurate answers with citations.

## Architecture
```
User Question → Embedding Generation → Vector Search → Context Retrieval → LLM Response → User
```

## Components

### 1. Textbook Content (`data/textbook_content.json`)
- Structured JSON with chapters and sections
- Each section has: id, title, content, tags, metadata

### 2. Embedding Service (`services/embedding_service.py`)
- Uses sentence-transformers (all-MiniLM-L6-v2)
- Generates 384-dimensional embeddings
- Free, local, no API key required

### 3. Vector Store (`services/vector_store.py`)
- Uses ChromaDB for similarity search
- Persistent storage in `./chroma_db`
- Cosine similarity for matching

### 4. RAG Service (`services/rag_service.py`)
- Orchestrates retrieval and generation
- Loads content and generates embeddings
- Retrieves relevant context for queries

### 5. API Routes (`routes/chat.py`, `routes/content.py`)
- `/api/v1/chat` - Main chat endpoint
- `/api/v1/health` - Health check
- `/api/v1/content/load` - Load content
- `/api/v1/content/status` - Content status

## Setup Steps

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
```bash
python main.py
```

The server will:
1. Start on http://localhost:8000
2. Automatically load textbook content
3. Generate embeddings for all sections
4. Store embeddings in ChromaDB

### Step 3: Verify the Setup
Open your browser and check:
- API Root: http://localhost:8000
- Health Check: http://localhost:8000/api/v1/health
- API Docs: http://localhost:8000/docs

### Step 4: Test the Chat Endpoint
```bash
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What are humanoid robots?"}'
```

## API Endpoints

### POST /api/v1/chat
Send a question and get an answer with citations.

**Request:**
```json
{
  "message": "What is ZMP in bipedal walking?",
  "session_id": "optional-session-id",
  "language": "en"
}
```

**Response:**
```json
{
  "response": "Based on the textbook section **Bipedal Locomotion**...",
  "sources": [
    {
      "chapter": "Week 2",
      "section": "Bipedal Locomotion",
      "similarity": 95.3
    }
  ],
  "session_id": "generated-session-id",
  "confidence": 0.953
}
```

### POST /api/v1/content/load
Manually load/reload textbook content.

**Response:**
```json
{
  "success": true,
  "message": "Content loaded successfully",
  "stats": {"total_documents": 24},
  "chapters_processed": 2
}
```

### GET /api/v1/health
Check service health and content status.

**Response:**
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

## Frontend Integration

The chat widget in your frontend is already configured to use this backend.

### Chat Widget Configuration
- Backend URL: `http://localhost:8000/api/v1/chat`
- Health Check: `http://localhost:8000/health`

### Features
1. **Contextual Answers**: Responses based on textbook content
2. **Source Citations**: Shows which chapter/section answers come from
3. **Confidence Scores**: Indicates how relevant the answer is
4. **Session Management**: Maintains conversation context
5. **Selected Text**: Can answer questions about selected text on page

## Adding More Content

### Edit textbook_content.json
Add new chapters following this structure:

```json
{
  "id": "week-3",
  "title": "Chapter Title",
  "order": 3,
  "difficulty": "Intermediate",
  "sections": [
    {
      "id": "week-3-section-1",
      "title": "Section Title",
      "content": "Section content here...",
      "tags": ["tag1", "tag2"],
      "metadata": {
        "keyConcepts": ["Concept 1", "Concept 2"]
      }
    }
  ]
}
```

### Reload Content
After editing, reload the content:
```bash
curl -X POST "http://localhost:8000/api/v1/content/load"
```

Or restart the server.

## Troubleshooting

### Content Not Loading
1. Check that `textbook_content.json` exists
2. Verify JSON is valid (use a JSON validator)
3. Check server logs for errors

### ChromaDB Errors
1. Delete the `chroma_db` folder
2. Restart the server (will recreate database)

### Poor Answer Quality
1. Add more relevant content to the textbook
2. Increase `n_results` in retrieval (default: 3)
3. Improve content structure and tagging

## Performance Optimization

### For Production
1. Use a better embedding model (e.g., `all-mpnet-base-v2`)
2. Add caching for frequent queries
3. Use Redis for session storage
4. Deploy with a proper ASGI server (gunicorn + uvicorn)

### Scaling
1. Use a managed vector database (Pinecone, Weaviate)
2. Add load balancing for multiple instances
3. Implement query caching with Redis

## Next Steps: Qwen LLM Integration

To integrate Qwen for response generation:

1. **Get Qwen API Access**
   - Sign up for Alibaba Cloud
   - Get API key for Qwen

2. **Update rag_service.py**
   - Add Qwen API client
   - Replace mock response with actual LLM call

3. **Configure API Key**
   - Add to `.env` file
   - `QWEN_API_KEY=your-key-here`

## Support

For issues or questions:
1. Check the API logs
2. Review the endpoint documentation at `/docs`
3. Test with curl before frontend integration
