# Chatbot UI Testing Guide

## Overview
This document describes how to test the chatbot UI and verify its integration with the backend.

## Prerequisites
- Ensure the backend server is running on `http://localhost:8000`
- Ensure the frontend is running on `http://localhost:3000` (or your Docusaurus port)

## Testing Steps

### 1. Backend Server Check
1. Start the backend server:
   ```bash
   cd E:\hackathon-1\backend
   python main.py
   ```
   
2. Verify the backend is running by visiting: `http://localhost:8000/api/v1/chat/health`
3. You should receive a response like:
   ```json
   {"status": "healthy", "service": "chat"}
   ```

### 2. Frontend UI Testing
1. Start the frontend server:
   ```bash
   cd E:\hackathon-1\frontend
   npm start
   ```

2. Open your browser and navigate to the frontend
3. Verify the chat widget appears in the bottom-right corner
4. Click the chat icon to open the chat interface
5. Test the following features:
   - Send a message and verify the response
   - Copy text from the textbook content and see if it appears as context
   - Verify the response is displayed properly
   - Test the copy button functionality

### 3. API Integration Test
To manually test the API integration:

1. Use a tool like Postman or curl to send a test request:
   ```bash
   curl -X POST http://localhost:8000/api/v1/chat \
     -H "Content-Type: application/json" \
     -d '{
       "message": "What is Physical AI?",
       "session_id": "test-session-123",
       "selected_text": "",
       "language": "en"
     }'
   ```

2. Verify you receive a proper JSON response from the backend.

### 4. UI Features Checklist
- [ ] Floating chat widget appears on all pages
- [ ] Chat widget can be opened and closed
- [ ] Message input field works
- [ ] Send button functionality
- [ ] Loading indicators display properly
- [ ] Messages display with proper styling
- [ ] Timestamps show for messages
- [ ] Copy button works for message content
- [ ] Selected text from page appears in chat context
- [ ] Error handling works when backend is unavailable
- [ ] Responsive design works on mobile screens
- [ ] Dark/light mode styling works correctly

## Troubleshooting

### Common Issues:
1. **API Connection Error**: Verify backend server is running on port 8000
2. **CORS Issues**: Ensure backend has proper CORS headers configured
3. **UI Not Loading**: Check browser console for JavaScript errors
4. **Text Selection Not Working**: Test by selecting text on various pages

### Network Requests:
- Frontend makes POST requests to: `http://localhost:8000/api/v1/chat`
- Request format:
  ```json
  {
    "message": "user input",
    "session_id": "session identifier",
    "selected_text": "text selected on page",
    "language": "en/ur"
  }
  ```
- Response format:
  ```json
  {
    "response": "AI response text",
    "session_id": "session identifier",
    "timestamp": "ISO date string",
    "sources": []
  }
  ```