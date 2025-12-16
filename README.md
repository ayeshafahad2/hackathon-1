# Physical AI & Humanoid Robotics RAG Chatbot

Welcome to the fully functional RAG (Retrieval-Augmented Generation) chatbot for the Physical AI & Humanoid Robotics textbook! This intelligent assistant can answer questions about the textbook content using advanced AI techniques.

## 🚀 Features

- **Smart Question Answering**: Answers questions based on textbook content using RAG technology
- **Text Selection Integration**: Ask questions about specific text selected on the page
- **Multi-language Support**: Currently supports English (with extensibility for Urdu)
- **Real-time Responses**: Fast, contextual answers using OpenAI GPT models
- **Vector Search**: Uses Qdrant vector database for semantic search
- **Modern UI**: Integrated chat widget with smooth user experience

## 🏗️ Architecture

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
- **Frontend**: Docusaurus-based documentation site with integrated React chat widget
- **Backend**: FastAPI server with RAG service integration
- **AI Services**: OpenAI for embeddings and response generation
- **Vector Database**: Qdrant for semantic search and retrieval
- **Content Processing**: Automated textbook content loading

## 🔧 Prerequisites

Before getting started, ensure you have:

- Python 3.8+
- Node.js 16+
- Valid OpenAI API key
- Qdrant Cloud account (or local instance)
- PostgreSQL database (NeonDB recommended)

## 🛠️ Quick Setup

### 1. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

⚠️ **Security Warning**: Never commit API keys or sensitive information to version control!

1. **Copy the example environment files**:
   ```bash
   # Backend environment
   cd backend
   cp .env.example .env

   # Frontend environment (if needed)
   cd ../frontend
   cp .env.example .env
   ```

2. **Edit the `.env` files** with your actual values:
   ```env
   OPENAI_API_KEY=your_actual_openai_api_key_here
   QDRANT_URL=your_actual_qdrant_cluster_url_here
   QDRANT_API_KEY=your_actual_qdrant_api_key_here
   POSTGRES_URL=your_actual_postgresql_connection_string_here
   ```

> **Note**: The `.gitignore` file is configured to exclude all `.env*` files from being committed to the repository.

### 3. Load Textbook Content

```bash
cd backend
python load_textbook_content.py
```

This will:
- Connect to your Qdrant instance
- Process all markdown files in `frontend/docs/`
- Create vector embeddings for semantic search
- Store content for RAG retrieval

### 4. Start the Backend Server

```bash
cd backend
python start_server.py
```

Or for development:

```bash
cd backend
python main.py
```

### 5. Start the Frontend

```bash
cd frontend
npm install
npm start
```

## 💡 Usage Examples

Once deployed, you can:

### Ask General Questions
- "What is Physical AI?"
- "Explain humanoid robotics"
- "How do robots learn?"

### Ask About Selected Text
1. Select any text on the documentation page
2. Ask specific questions about the selected content
3. The chatbot will focus its response on the selected text

### Multi-turn Conversations
The chatbot maintains context for follow-up questions about the same topic.

## 🌐 API Endpoints

The backend provides these REST API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome page |
| GET | `/health` | System health check |
| GET | `/api/v1/chat/health` | Chat service health |
| POST | `/api/v1/chat` | Main chat endpoint |
| POST | `/api/v1/chat/upload-textbook-content` | Upload content programmatically |

### Chat API Example:

```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are the key concepts in Physical AI?",
    "language": "en"
  }'
```

## 🔍 Technical Implementation

### RAG Pipeline:
1. **Query Processing**: User query is received and processed
2. **Embedding Creation**: Query is converted to vector embedding using OpenAI
3. **Vector Search**: Similar content is retrieved from Qdrant database
4. **Context Building**: Relevant textbook content is assembled
5. **Response Generation**: OpenAI generates contextual response
6. **Response Delivery**: Smart, accurate answer is returned

### Content Indexing:
- Textbook markdown files are automatically parsed
- Content is chunked and embedded
- Metadata is preserved for better retrieval
- Vector database is updated in real-time

## 🧪 Testing

Test the complete functionality:

```bash
cd backend
python test_rag_chatbot.py
```

This runs a comprehensive test suite covering:
- API endpoint functionality
- Qdrant connection
- RAG pipeline
- Sample queries

## 🚀 Deployment

### Local Development:
Follow the quick setup steps above.

### Production Deployment:
1. Deploy backend to a cloud service (AWS, GCP, Azure)
2. Deploy frontend to Vercel, Netlify, or similar
3. Ensure secure environment variable management
4. Set up monitoring and logging

## 🔒 Security Considerations

- Keep API keys secure and never commit to version control
- Implement rate limiting for production
- Use HTTPS in production environments
- Validate user inputs to prevent injection attacks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🐛 Troubleshooting

### Common Issues:

**Qdrant Connection Issues:**
- Verify your Qdrant Cloud URL and API key
- Check if your cluster is running
- Ensure proper network connectivity

**API Key Issues:**
- Double-check your OpenAI API key validity
- Ensure sufficient quota remains
- Verify billing information is current

**Content Loading Issues:**
- Check that markdown files exist in `frontend/docs/`
- Verify file permissions
- Look for parsing errors in the logs

**Sensitive Information Accidentally Committed:**
⚠️ **IF YOU ACCIDENTALLY COMMITTED SECRETS:**
- Immediately revoke/regenerate the exposed API keys
- Use `git filter-repo` to remove the sensitive data from history:
  ```bash
  # Install git-filter-repo if not already installed
  pip install git-filter-repo

  # Remove the file from git history (example)
  git filter-repo --path path/to/sensitive/file --invert-paths
  ```
- Follow the detailed steps in SECURITY_GUIDELINES.md

### Debug Mode:
Enable debug mode in your `.env` file:
```env
DEBUG=true
```

## 📚 Resources

- [OpenAI Documentation](https://platform.openai.com/docs/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docusaurus Documentation](https://docusaurus.io/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💬 Ready to Use!

Your RAG Chatbot for the Physical AI & Humanoid Robotics textbook is now fully operational! Start asking questions and exploring the content in a whole new way.