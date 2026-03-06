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
  // Add personalization and translation methods
  personalizeContent: (chapterId: string) => Promise<void>;
  translateToUrdu: (chapterId: string) => Promise<void>;
  getCurrentLanguage: () => string;
  setCurrentLanguage: (lang: string) => void;
  clearChat: () => void;
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
  const [currentLanguage, setCurrentLanguageState] = React.useState<string>('en');

  // Function to personalize content for a chapter
  const personalizeContent = async (chapterId: string) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error('User not authenticated');
    }

    const response = await fetch('http://localhost:8000/api/v1/auth/personalize-content', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ chapter_id: chapterId }),
    });

    if (!response.ok) {
      throw new Error('Failed to personalize content');
    }

    return response.json();
  };

  // Function to translate chapter to Urdu
  const translateToUrdu = async (chapterId: string) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error('User not authenticated');
    }

    const response = await fetch('http://localhost:8000/api/v1/auth/translate-urdu', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ chapter_id: chapterId }),
    });

    if (!response.ok) {
      throw new Error('Failed to translate content');
    }

    return response.json();
  };

  // Get current language
  const getCurrentLanguage = (): string => {
    return currentLanguage;
  };

  // Set current language (exposed version)
  const setLanguage = (lang: string) => {
    setCurrentLanguageState(lang);
  };

  // Clear chat
  const clearChat = () => {
    dispatch({ type: 'CLEAR_MESSAGES' });
  };

  const value: ChatContextType = {
    state,
    dispatch,
    personalizeContent,
    translateToUrdu,
    getCurrentLanguage,
    setCurrentLanguage: setLanguage,
    clearChat
  };

  return (
    <ChatContext.Provider value={value}>
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