# Full System Startup Guide

This guide will walk you through the complete setup and startup of the Physical AI & Humanoid Robotics RAG Chatbot system.

## Step 1: Verify Dependencies

Make sure you have Python 3.8+ and Node.js 16+ installed:

```bash
python --version
node --version
```

## Step 2: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Step 3: Set Up Environment Variables

Create a `.env` file in the `backend/` directory with your credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=your_qdrant_cloud_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
POSTGRES_URL=your_postgres_connection_string_here
```

## Step 4: Load Textbook Content

First load your textbook content into the vector database:

```bash
cd backend
python load_textbook_content.py
```

This will connect to your Qdrant instance and load the content from the `frontend/docs/` directory.

## Step 5: Start Backend Server

```bash
cd backend
python start_server.py
```

The server will be available at `http://localhost:8000`

## Step 6: Install and Start Frontend

Open a new terminal, navigate to the frontend directory and start the development server:

```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000`

## Step 7: Verify Everything Works

1. Visit the frontend at `http://localhost:3000`
2. Check that the chat widget appears on the page
3. Navigate to the dedicated chat page at `/chat`
4. Test asking questions about the textbook content

## Troubleshooting

### Backend Issues:
- If the server fails to start, check the `.env` file
- If Qdrant connection fails, verify your URL and API key
- Make sure all required packages are installed

### Frontend Issues:
- If the chat widget doesn't load, check browser console for errors
- Make sure the backend server is running at `http://localhost:8000`
- Verify CORS settings if running on different ports

### Chat Functionality:
- If responses seem generic, make sure content was loaded to Qdrant
- Check that OpenAI API key is valid and has sufficient quota
- Verify that the backend can reach both OpenAI and Qdrant services

## Testing the API Directly

You can test the API endpoints directly using curl:

```bash
# Health check
curl http://localhost:8000/health

# Chat endpoint
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Physical AI?", "language": "en"}'
```

## Shutting Down

To shut down the system:
1. Stop the frontend server (Ctrl+C in the frontend terminal)
2. Stop the backend server (Ctrl+C in the backend terminal)

## Development Tips

- Use `python test_rag_chatbot.py` to run the comprehensive test suite
- Monitor the backend logs for any errors or warnings
- The chat history is maintained per session in the browser
- Selected text integration allows asking specific questions about highlighted content