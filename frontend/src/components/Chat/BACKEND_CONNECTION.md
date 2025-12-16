# Backend Connection and Mock Service Documentation

## Overview
This documentation explains how the frontend connects to the backend and handles various connection states.

## Backend Connection

### Environment Variables Needed
The backend requires these environment variables in `backend/.env`:
- `OPENAI_API_KEY` - For the OpenAI API
- `QDRANT_URL` - For the vector database
- `QDRANT_API_KEY` - For the vector database
- `POSTGRES_URL` - For the PostgreSQL database

### API Endpoints
- `http://localhost:8000/api/v1/chat` - Main chat endpoint
- `http://localhost:8000/api/v1/chat/health` - Health check endpoint

## Frontend Implementation

### Connection Status Indicators
The chat interface displays the status of the backend connection:
- 🔍 Checking - When initially verifying the connection
- 🟢 Connected - When successfully connected to the backend
- 🟡 Disconnected - When using mock responses
- 🔴 Error - When there's an error connecting

### How It Works
1. On page load, the frontend checks the backend health
2. When a user sends a message, the frontend:
   - First attempts to connect to the backend API
   - If successful, uses the real AI response from the backend
   - If failed, falls back to the mock service with relevant textbook content
3. Connection status is updated in real-time

### Mock Service
The mock service provides detailed responses about Physical AI & Humanoid Robotics topics when the backend is unavailable:
- Contains knowledge about core topics in the textbook
- Provides detailed explanations about robotics concepts
- Maintains a conversational and helpful tone
- Handles common questions about the subject matter

### Starting the Backend
To use the full AI functionality:
1. Ensure all environment variables are set in `backend/.env`
2. Run the backend server: `cd backend && python main.py`
3. The frontend will automatically detect and connect to the backend