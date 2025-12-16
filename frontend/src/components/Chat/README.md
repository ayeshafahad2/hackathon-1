# AI Textbook Assistant Chatbot UI

## Overview

The AI Textbook Assistant is an intelligent chatbot integrated into the Physical AI & Humanoid Robotics textbook. It allows users to ask questions about textbook content and receive contextual answers powered by AI.

## Features

### 1. Contextual Understanding
- Select any text on the page and ask questions about it
- The chatbot receives the selected text as context
- Responses are tailored to the highlighted content

### 2. Conversation Management
- Maintains conversation history within sessions
- Preserves context across multiple exchanges
- Session IDs ensure continuity

### 3. Intuitive UI Components
- Floating chat widget available on all pages
- Expandable/collapsible interface
- Visual indicators for unread messages
- Smooth animations and transitions

### 4. Enhanced User Experience
- Real-time typing indicators
- Message timestamps
- Copy-to-clipboard functionality
- Responsive design for all devices
- Dark/light mode support

## UI Components

### Chat Widget
- **Location**: Bottom-right corner of all pages (by default)
- **Function**: Toggle button to open/close the chat interface
- **Features**: 
  - Animated chat icon (🤖)
  - Unread message indicator (red dot)
  - Hover effects and smooth transitions

### Chat Interface
- **Header**: Chat title and close button
- **Message Area**: Display of conversation history
- **Input Area**: Text area for new messages
- **Action Buttons**: Send message functionality

### Message Display
- **User Messages**: Blue background, right-aligned
- **Assistant Messages**: Light gray background, left-aligned
- **Timestamps**: Time indicators for each message
- **Copy Button**: 📋 icon to copy message content

## API Integration

### Backend Endpoint
- **URL**: `http://localhost:8000/api/v1/chat`
- **Method**: POST
- **Content-Type**: application/json

### Request Payload
```json
{
  "message": "user input text",
  "session_id": "conversation identifier",
  "selected_text": "text highlighted on page",
  "language": "en/ur"
}
```

### Response Format
```json
{
  "response": "AI-generated response",
  "session_id": "updated session identifier",
  "timestamp": "ISO 8601 formatted timestamp",
  "sources": ["array of source documents"]
}
```

## Usage Instructions

### For Textbook Readers
1. **Select Text**: Highlight any text in the textbook
2. **Open Chat**: Click the chat icon (bottom-right corner)
3. **Ask Questions**: Type your question in the input field
4. **Get Answers**: Receive AI-powered responses based on the content

### For Developers
1. **Start Backend**: Run the backend server on port 8000
2. **Start Frontend**: Run the Docusaurus site
3. **Test Connection**: Verify API communication works properly

## Implementation Details

### File Structure
```
src/
├── components/
│   └── Chat/
│       ├── ChatWidget.tsx          # Floating widget component
│       ├── ChatWidget.module.css   # Widget styling
│       ├── index.tsx               # Main chat component
│       ├── Chat.module.css         # Chat interface styling
│       ├── EnhancedChat.tsx        # Enhanced chat version
│       └── TESTING.md              # Testing documentation
├── pages/
│   ├── chat.tsx                    # Dedicated chat page
│   ├── chat.module.css             # Chat page styling
│   └── features.tsx                # Features page with chat demo
└── theme/
    └── Layout/
        └── wrapper.tsx             # Global layout wrapper
```

### Key Technologies
- **Framework**: React with TypeScript
- **UI Library**: Docusaurus components
- **Styling**: CSS Modules
- **API Communication**: Fetch API
- **Text Processing**: DOM selection API

## Customization Options

### Widget Positioning
The chat widget supports different positions:
- `bottom-right` (default)
- `bottom-left`
- `side`

### Styling
- The UI adapts to the site's light/dark mode
- Component styles are contained in CSS modules
- Colors can be customized via CSS custom properties

## Accessibility Features
- ARIA labels for screen readers
- Keyboard navigation support
- Proper color contrast ratios
- Focus management for interactive elements

## Responsive Design
- Desktop: Full-featured chat interface
- Tablet: Optimized message display
- Mobile: Collapsible interface with essential features

## Future Enhancements
- Voice input/output capabilities
- Multi-language support
- Rich media responses
- Advanced conversation management
- Offline capability