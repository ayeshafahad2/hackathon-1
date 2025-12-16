import React, { createContext, useContext, useReducer, ReactNode } from 'react';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

interface ChatState {
  messages: Message[];
  sessionId: string | null;
  isLoading: boolean;
  selectedText: string | null;
}

type ChatAction =
  | { type: 'ADD_MESSAGE'; payload: Message }
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_SESSION_ID'; payload: string }
  | { type: 'SET_SELECTED_TEXT'; payload: string | null }
  | { type: 'CLEAR_MESSAGES' };

interface ChatContextType {
  state: ChatState;
  dispatch: React.Dispatch<ChatAction>;
}

const initialState: ChatState = {
  messages: [],
  sessionId: null,
  isLoading: false,
  selectedText: null,
};

const ChatContext = createContext<ChatContextType | undefined>(undefined);

const chatReducer = (state: ChatState, action: ChatAction): ChatState => {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, action.payload],
      };
    case 'SET_LOADING':
      return {
        ...state,
        isLoading: action.payload,
      };
    case 'SET_SESSION_ID':
      return {
        ...state,
        sessionId: action.payload,
      };
    case 'SET_SELECTED_TEXT':
      return {
        ...state,
        selectedText: action.payload,
      };
    case 'CLEAR_MESSAGES':
      return {
        ...state,
        messages: [],
      };
    default:
      return state;
  }
};

export const ChatProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(chatReducer, initialState);

  return (
    <ChatContext.Provider value={{ state, dispatch }}>
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = (): ChatContextType => {
  const context = useContext(ChatContext);
  if (!context) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
};