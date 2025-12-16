# Physical AI & Humanoid Robotics RAG Chatbot 🤖

Welcome to the **fully functional RAG (Retrieval-Augmented Generation) chatbot** for the Physical AI & Humanoid Robotics textbook! This advanced AI system can answer questions about the textbook content using state-of-the-art retrieval-augmented generation techniques.

## ✅ Complete System Verification

This system has been **fully verified and is ready to use**! All components are implemented and functional:

- ✅ **Backend API** - FastAPI server with RAG integration
- ✅ **Frontend Chat Widget** - React-based interface with Docusaurus integration 
- ✅ **Vector Database** - Qdrant for semantic search and retrieval
- ✅ **AI Services** - OpenAI integration for embeddings and responses
- ✅ **Textbook Content** - 14 content files loaded from `frontend/docs/`
- ✅ **Full RAG Pipeline** - Complete retrieval-augmented generation workflow

## 🚀 Features

- **Intelligent Q&A**: Ask questions about Physical AI & Humanoid Robotics content
- **Contextual Understanding**: Leverages textbook content for accurate responses
- **Text Selection Integration**: Ask about specific text selected on the page
- **Multi-turn Conversations**: Maintains context across multiple interactions
- **Real-time Responses**: Fast, contextual answers using advanced AI
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend     │◄──►│   Backend API    │◄──►│  Vector Store   │
│  (Docusaurus)   │    │   (FastAPI)      │    │   (Qdrant)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
       │                       │                       │
       ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Chat Widget   │    │  RAG Service     │    │ Textbook Docs   │
│  (React)        │    │  (OpenAI+Qdrant) │    │  (Markdown)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Core Components:

**Backend Services:**
- `FastAPI` - REST API framework
- `RAG Service` - Retrieval-Augmented Generation pipeline
- `OpenAI Service` - Embeddings and response generation
- `Qdrant Service` - Vector database operations
- `Embedding Service` - Text vectorization

**Frontend Components:**
- `Docusaurus` - Documentation site framework
- `Chat Widget` - Interactive AI assistant
- `React Components` - Modern UI/UX

## 🛠️ Quick Start

### 1. Install Dependencies

```bash
# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install missing dependencies highlighted by verification
pip install asyncpg python-dotenv
```

### 2. Configure Environment

Ensure your `backend/.env` file contains:

```env
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=https://your-cluster-url.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_api_key_here
POSTGRES_URL=postgresql://your_connection_string
```

### 3. Load Textbook Content

```bash
cd backend
python load_textbook_content.py
```

### 4. Start the System

```bash
# Terminal 1: Start backend
cd backend
python start_server.py

# Terminal 2: Start frontend (in new terminal)
cd frontend
npm install
npm start
```

## 💡 Usage Examples

### Ask Questions About Textbook:
- "What is Physical AI?"
- "Explain humanoid robotics design principles"
- "How do robots learn from human demonstrations?"

### Use Text Selection:
1. Select any text in the documentation
2. The chat widget will detect the selection
3. Ask specific questions about the highlighted content

### Multi-turn Conversations:
- Follow up with related questions
- The system maintains conversation context
- Get deeper insights through iterative questioning

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome page |
| GET | `/health` | System health |
| GET | `/api/v1/chat/health` | Chat service health |
| POST | `/api/v1/chat` | Main chat endpoint |
| POST | `/api/v1/chat/upload-textbook-content` | Upload content |

### Sample API Call:
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are the key concepts in Physical AI?",
    "language": "en"
  }'
```

## 🔍 How It Works

1. **Query Processing**: User question is received and processed
2. **Embedding Creation**: Query is converted to vector embedding
3. **Semantic Search**: Similar content retrieved from vector database
4. **Context Building**: Relevant textbook content assembled
5. **Response Generation**: AI generates contextual answer
6. **Response Delivery**: Smart, accurate answer provided

## 🧪 Testing

Verify full functionality:

```bash
cd backend
python test_rag_chatbot.py
```

## 📚 Content Coverage

The system has loaded 14 textbook content files covering:
- Introduction to Physical AI
- Humanoid Robot Design
- Control Systems for Robotics
- Sensing and Perception
- Robot Learning and Adaptation
- Human-Robot Interaction
- Applications of Physical AI

## 🚀 Deployment

### Development:
```bash
# Backend
cd backend
python start_server.py

# Frontend
cd frontend
npm start
```

### Production:
1. Deploy backend to cloud service
2. Deploy frontend to static hosting
3. Configure environment variables securely
4. Set up monitoring and logging

## 🔒 Security Considerations

- API keys stored securely in environment variables
- Rate limiting for API endpoints
- Input validation for user queries
- Secure HTTPS connections in production

## 📖 Resources

- [OpenAI Documentation](https://platform.openai.com/docs/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docusaurus Documentation](https://docusaurus.io/)

---

## 🎉 Ready to Use!

Your **fully functional RAG Chatbot** for the Physical AI & Humanoid Robotics textbook is ready! Start asking questions and get intelligent, context-aware answers powered by advanced AI technology.

**Start chatting now** and explore the textbook content in a revolutionary new way!