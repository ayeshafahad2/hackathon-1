# 🤖 RAG Chatbot - Complete Implementation Guide

## Overview

This is a complete RAG (Retrieval-Augmented Generation) chatbot for the Physical AI & Humanoid Robotics textbook. The chatbot can answer questions about the textbook content with accurate citations.

## ✨ Features

- **Smart Retrieval**: Finds relevant textbook sections using semantic search
- **Source Citations**: Every answer includes references to specific chapters/sections
- **Confidence Scoring**: Shows how relevant the answer is to the question
- **Session Management**: Maintains conversation context
- **Multi-language Support**: Can respond in English or Urdu
- **Selected Text Context**: Can answer questions about selected text on the page
- **Free & Local**: Uses local embeddings (no API key required for basic functionality)
- **Qwen Ready**: Optional Qwen LLM integration for AI-powered responses

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User asks question                     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Frontend (React/Docusaurus)                                │
│  - Chat Widget                                              │
│  - Sends question to backend                                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Backend (FastAPI)                                          │
│  - /api/v1/chat endpoint                                    │
│  - Receives question                                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  RAG Service                                                │
│  1. Generate embedding for question                         │
│  2. Search vector database                                  │
│  3. Retrieve relevant context                               │
│  4. Generate response with LLM                              │
└─────────────────────────────────────────────────────────────┘
                            │
                    ┌───────┴───────┐
                    ▼               ▼
        ┌───────────────┐   ┌───────────────┐
        │  Embedding    │   │  Vector Store │
        │  Service      │   │  (ChromaDB)   │
        │  (sentence-   │   │  - Textbook   │
        │   transformers)│  │  - Embeddings │
        └───────────────┘   └───────────────┘
                    │               │
                    └───────┬───────┘
                            ▼
                ┌───────────────────────┐
                │   Qwen LLM (Optional) │
                │   - AI Response       │
                │   - Natural Language  │
                └───────────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Response with       │
                │   Sources & Confidence│
                └───────────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Display to User     │
                └───────────────────────┘
```

## 📁 Project Structure

```
backend/
├── src/
│   └── rag_chatbot/
│       ├── data/
│       │   └── textbook_content.json    # Textbook content
│       ├── services/
│       │   ├── embedding_service.py     # Embedding generation
│       │   ├── vector_store.py          # ChromaDB operations
│       │   ├── rag_service.py           # RAG orchestration
│       │   └── qwen_service.py          # Qwen LLM integration
│       ├── routes/
│       │   ├── chat.py                  # Chat API endpoints
│       │   └── content.py               # Content management
│       ├── main.py                      # FastAPI app
│       └── config.py                    # Configuration
├── requirements.txt                      # Python dependencies
├── .env.example                          # Environment template
├── start_rag_backend.bat                 # Quick start script
└── RAG_CHATBOT_SETUP.md                  # Detailed setup guide

frontend/
├── src/
│   ├── components/
│   │   └── Chat/
│   │       ├── ChatWidget.tsx           # Main chat component
│   │       ├── ChatWidget.module.css    # Chat styles
│   │       └── EnhancedChat.tsx         # Enhanced chat UI
│   └── pages/
│       └── chat.tsx                     # Chat page
└── ...
```

## 🚀 Quick Start

### Step 1: Start the Backend

**Option A: Using the batch script (Windows)**
```bash
cd backend
start_rag_backend.bat
```

**Option B: Manual start**
```bash
cd backend
pip install -r requirements.txt
python main.py
```

The backend will:
1. Start on `http://localhost:8000`
2. Load textbook content automatically
3. Generate embeddings for all sections
4. Store embeddings in ChromaDB

### Step 2: Verify Backend is Running

Open your browser and check:
- **API Root**: http://localhost:8000
- **Health Check**: http://localhost:8000/api/v1/health
- **API Docs**: http://localhost:8000/docs

You should see:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

### Step 3: Start the Frontend

```bash
cd frontend
npm start
```

The frontend will start on `http://localhost:3000`

### Step 4: Test the Chatbot

1. Go to `http://localhost:3000`
2. Click the chat icon (bottom-right corner)
3. Ask a question like: "What are humanoid robots?"
4. You'll get an answer with textbook citations!

## 📚 Textbook Content

### Current Content (Week 1-2)

**Week 1: Introduction to Humanoid Robotics**
- What are Humanoid Robots?
- History and Evolution of Humanoid Robots
- Key Components of a Humanoid Robot
- Introduction to Physical AI

**Week 2: Robot Kinematics and Motion**
- Introduction to Kinematics
- Forward Kinematics
- Inverse Kinematics
- Bipedal Locomotion

### Adding More Content

Edit `backend/src/rag_chatbot/data/textbook_content.json`:

```json
{
  "chapters": [
    {
      "id": "week-3",
      "title": "Robot Dynamics and Control",
      "order": 3,
      "difficulty": "Intermediate",
      "sections": [
        {
          "id": "week-3-section-1",
          "title": "Introduction to Dynamics",
          "content": "Your content here...",
          "tags": ["dynamics", "forces", "control"],
          "metadata": {
            "keyConcepts": ["Forces", "Torques", "Equations of Motion"]
          }
        }
      ]
    }
  ]
}
```

Then reload:
```bash
curl -X POST "http://localhost:8000/api/v1/content/load"
```

## 🔧 Configuration

### Basic Setup (No API Key Required)

The chatbot works out of the box with:
- ✅ Semantic search
- ✅ Source citations
- ✅ Confidence scoring
- ✅ Context-aware responses

### Advanced Setup (With Qwen API)

For AI-powered natural language responses:

1. **Get Qwen API Key**
   - Sign up at: https://dashscope.console.aliyun.com/
   - Create an API key

2. **Configure Environment**
   Edit `backend/.env`:
   ```env
   QWEN_API_KEY=your-api-key-here
   QWEN_MODEL=qwen-turbo
   ```

3. **Restart Backend**
   ```bash
   python main.py
   ```

## 📖 API Endpoints

### POST /api/v1/chat
Chat with the AI assistant.

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
  "response": "📚 **From the textbook:**\n\nBased on **Bipedal Locomotion** from **Week 2**:\n\n_Zero Moment Point (ZMP) is the point where the net moment of inertial and gravitational forces is zero. It must stay within the support polygon for stability._\n\n**Related sections:** Introduction to Kinematics",
  "sources": [
    {
      "chapter": "Week 2",
      "section": "Bipedal Locomotion",
      "similarity": 95.3
    }
  ],
  "session_id": "abc123",
  "confidence": 0.953,
  "qwen_available": false
}
```

### GET /api/v1/health
Check service health.

### POST /api/v1/content/load
Load textbook content into vector store.

### GET /api/v1/content/status
Get content loading status.

## 🎯 Example Questions

Try asking:
- "What are humanoid robots?"
- "Explain ZMP in walking"
- "What is forward kinematics?"
- "What sensors do humanoid robots use?"
- "How does Physical AI differ from traditional AI?"
- "What is the history of humanoid robots?"
- "Explain degrees of freedom in robotics"

## 🛠️ Troubleshooting

### Backend Won't Start

**Issue**: Module not found error
**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

### Content Not Loading

**Issue**: content_loaded: false
**Solution**:
1. Check that `textbook_content.json` exists
2. Validate JSON: https://jsonlint.com/
3. Check backend logs for errors

### ChromaDB Errors

**Issue**: Database errors
**Solution**:
```bash
# Delete ChromaDB and restart
rm -rf chroma_db
python main.py
```

### Frontend Can't Connect

**Issue**: Backend not responding
**Solution**:
1. Verify backend is running on port 8000
2. Check CORS settings in backend
3. Check browser console for errors

## 📊 Performance

### Response Times
- **Without Qwen**: < 1 second (retrieval only)
- **With Qwen**: 2-5 seconds (includes LLM generation)

### Accuracy
- Depends on content quality and coverage
- Confidence score indicates relevance
- Higher similarity = more relevant answer

## 🔐 Security Notes

- API key stored in environment variables
- CORS configured for localhost only (production: update allowed origins)
- Session data stored in memory (production: use Redis)

## 📈 Next Steps

1. **Add More Content**: Expand the textbook with more chapters
2. **Configure Qwen**: Get API key for better responses
3. **Deploy**: Host on cloud (AWS, GCP, Azure)
4. **Analytics**: Track popular questions
5. **Feedback**: Add thumbs up/down for responses

## 🤝 Support

For issues or questions:
1. Check API logs
2. Review `/docs` endpoint
3. Test with curl first

## 📝 License

Part of the Physical AI & Humanoid Robotics textbook project.

---

**Ready to start chatting!** 🚀

Visit http://localhost:3000 and click the chat icon!
