# Physical AI & Humanoid Robotics Textbook - Setup Guide

## Overview
This project contains a Docusaurus-based textbook with an AI assistant for Physical AI & Humanoid Robotics, with both frontend and backend components.

## Prerequisites
- Node.js (v18 or higher)
- Python (v3.8 or higher)
- Access to OpenAI API key (for real AI responses)
- Access to Qdrant cloud account (for vector database)

## Frontend Setup (Docusaurus)

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm start
```
The site will be available at http://localhost:3000

## Backend Setup (FastAPI)

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the `backend` directory with the following:
```env
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=https://your-cluster.your-region.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_api_key_here
POSTGRES_URL=postgresql://username:password@localhost:5432/textbook_db
```

### 3. Start Backend Server
```bash
python main.py
```
The backend API will be available at http://localhost:8000

## AI Assistant Functionality

### With Backend Running (Recommended)
1. Start both the backend and frontend
2. The AI assistant will connect to the backend API
3. All queries will be processed using real AI models with textbook content

### Without Backend (Mock Responses)
1. Start only the frontend
2. The AI assistant will use mock responses based on textbook content
3. The interface will show "🟡 Backend API: Not connected (using mock responses)"

## Key Features

### Textbook Features
- Interactive AI assistant on all pages
- Select text on any page to ask specific questions
- Comprehensive coverage of Physical AI and Humanoid Robotics topics
- Multilingual support (English and Urdu)

### AI Assistant Capabilities
- Contextual understanding of selected text
- Detailed explanations of robotics concepts
- Conversation memory within sessions
- Copy-to-clipboard functionality for responses

## Troubleshooting

### Common Issues
- "Backend API: Not connected" - Backend server isn't running or environment variables aren't set
- CORS errors - Ensure backend is running on localhost:8000
- API key errors - Verify your OpenAI and Qdrant API keys are correct

### Verifying Backend Health
Check if backend is running: `http://localhost:8000/api/v1/chat/health`

## Development
- Frontend: React with TypeScript, Docusaurus framework
- Backend: FastAPI with Python
- AI: OpenAI GPT models with RAG (Retrieval-Augmented Generation)
- Database: Qdrant vector database for context retrieval