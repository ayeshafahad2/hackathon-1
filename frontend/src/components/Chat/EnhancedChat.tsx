import React, { useState, useEffect, useRef } from 'react';
import { useColorMode } from '@docusaurus/theme-common';
import { translate } from '@docusaurus/Translate';
import { useAuth } from '../../contexts/AuthContext';
import { useChat } from '../../contexts/ChatContext';
import styles from './Chat.module.css';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

interface EnhancedChatProps {
  compact?: boolean; // For use in sidebar/docked mode
  chapterId?: string; // Optional chapter ID for personalization/translation
}

const EnhancedChatComponent: React.FC<EnhancedChatProps> = ({ compact = false, chapterId = 'default' }) => {
  const { state, dispatch, clearChat } = useChat();
  const { user, loading: authLoading } = useAuth();
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string>('');
  const [isChatOpen, setIsChatOpen] = useState(!compact); // Start open if not compact
  const [backendStatus, setBackendStatus] = useState<'checking' | 'connected' | 'disconnected' | 'error'>('checking');
  const [showScrollToBottom, setShowScrollToBottom] = useState(false);
  const [availableLanguages, setAvailableLanguages] = useState([
    { code: 'en', name: 'English' },
    { code: 'ur', name: 'اردو (Urdu)' }
  ]);
  const [currentLanguage, setCurrentLanguage] = useState('en');
  const messagesEndRef = useRef<null | HTMLDivElement>(null);
  const messagesContainerRef = useRef<HTMLDivElement>(null);
  const { colorMode } = useColorMode();
  const isDarkTheme = colorMode === 'dark';

  // Function to check backend status
  useEffect(() => {
    const checkBackendStatus = async () => {
      try {
        // Use environment variable for backend URL in production
        const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
        const response = await fetch(`${backendUrl}/health`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (response.ok) {
          setBackendStatus('connected');
        } else {
          setBackendStatus('error');
        }
      } catch (error) {
        setBackendStatus('disconnected');
      }
    };

    checkBackendStatus();
  }, []);

  // Function to get selected text from the page
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection()?.toString().trim();
      if (selectedText) {
        setSelectedText(selectedText);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  // Scroll to bottom of messages only if user is already near the bottom
  useEffect(() => {
    const messagesContainer = document.querySelector(`.${styles.messagesContainer}`);
    if (messagesContainer) {
      // Check if user is near the bottom before new message arrives
      const isNearBottom = messagesContainer.scrollHeight - messagesContainer.clientHeight <= messagesContainer.scrollTop + 100;
      if (isNearBottom) {
        scrollToBottom();
      }
    }
  }, [state.messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      role: 'user',
      timestamp: new Date(),
    };

    dispatch({ type: 'ADD_MESSAGE', payload: userMessage });
    setInputValue('');
    setIsLoading(true);

    try {
      // Try to call the backend API first
      let response;
      let data;

      try {
        // Get user token if authenticated
        const token = localStorage.getItem('access_token');
        const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

        response = await fetch(`${backendUrl}/api/v1/chat`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(token ? { 'Authorization': `Bearer ${token}` } : {}), // Add auth header if token exists
          },
          body: JSON.stringify({
            message: inputValue,
            session_id: sessionId || undefined,
            selected_text: selectedText || undefined,
            language: currentLanguage, // Use current language setting
          }),
        });

        if (!response.ok) {
          throw new Error(`API request failed with status ${response.status}`);
        }

        data = await response.json();
        setBackendStatus('connected'); // Backend is working
      } catch (apiError) {
        console.warn('Backend API unavailable, using mock service:', apiError);
        // For now, just show an error since we don't have mock service in this context
        throw apiError;
      }

      // Add assistant message
      const assistantMessage: Message = {
        id: Date.now().toString(),
        content: data.response,
        role: 'assistant',
        timestamp: new Date(),
      };

      dispatch({ type: 'ADD_MESSAGE', payload: assistantMessage });
      setSessionId(data.session_id);
      setSelectedText(null); // Clear selected text after use
    } catch (error) {
      console.error('Error sending message:', error);

      // Add error message
      const errorMessage: Message = {
        id: Date.now().toString(),
        content: translate({
          id: 'chat.error',
          message: 'Sorry, I encountered an error. Please try again.',
        }),
        role: 'assistant',
        timestamp: new Date(),
      };
      dispatch({ type: 'ADD_MESSAGE', payload: errorMessage });
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e as any);
    }
  };

  const { personalizeContent, translateToUrdu } = useChat();

  const handlePersonalizeContent = async () => {
    if (!user) {
      alert('Please sign in to use personalization features.');
      return;
    }

    try {
      await personalizeContent(chapterId);
      alert('Content personalization has been applied for this chapter! You\'ve earned 50 bonus points.');
    } catch (error) {
      console.error('Error personalizing content:', error);
      alert('Failed to personalize content. Please try again.');
    }
  };

  const handleTranslateToUrdu = async () => {
    if (!user) {
      alert('Please sign in to use translation features.');
      return;
    }

    try {
      await translateToUrdu(chapterId);
      setCurrentLanguage('ur');
      alert('Content has been translated to Urdu! You\'ve earned 50 bonus points.');
    } catch (error) {
      console.error('Error translating to Urdu:', error);
      alert('Failed to translate content. Please try again.');
    }
  };

  if (compact) {
    return (
      <div className={`${styles.compactChatContainer} ${isDarkTheme ? styles.dark : styles.light}`}>
        <div className={styles.compactHeader}>
          <h3 onClick={() => setIsChatOpen(!isChatOpen)} style={{ cursor: 'pointer' }}>
            {translate({ id: 'chat.title', message: 'AI Assistant' })}
          </h3>
          {!isChatOpen && (
            <button
              onClick={() => setIsChatOpen(true)}
              className={styles.expandButton}
            >
              +
            </button>
          )}
        </div>

        {isChatOpen && (
          <div className={styles.expandedCompactView}>
            <div className={styles.chatControls}>
              <button onClick={clearChat} className={styles.newChatButton}>
                New Chat
              </button>
            </div>

            {/* Bonus Points and Personalization Controls */}
            {user && (
              <div className={styles.bonusControls}>
                <div className={styles.bonusPoints}>
                  <span>Bonus Points: {user.bonusPoints}</span>
                </div>
                <div className={styles.personalizationControls}>
                  <button 
                    className={styles.personalizeButton} 
                    onClick={handlePersonalizeContent}
                    title="Personalize content based on your background"
                  >
                    🎯 Personalize Content
                  </button>
                  <button 
                    className={styles.translateButton} 
                    onClick={handleTranslateToUrdu}
                    title="Translate to Urdu"
                  >
                    🌍 Translate to Urdu
                  </button>
                </div>
              </div>
            )}

            <div
              className={styles.messagesContainer}
              ref={messagesContainerRef}
              onScroll={() => {
                if (messagesContainerRef.current) {
                  const { scrollTop, scrollHeight, clientHeight } = messagesContainerRef.current;
                  // Show scroll to bottom button if user scrolls up more than 100px from bottom
                  const shouldShowButton = scrollHeight - scrollTop > clientHeight + 100;
                  setShowScrollToBottom(shouldShowButton);
                }
              }}
            >
              {state.messages.length === 0 ? (
                <div className={styles.welcomeMessage}>
                  <p>{translate({ id: 'chat.welcome', message: 'Welcome! I am your AI assistant for the Physical AI & Humanoid Robotics textbook.' })}</p>
                  <p>{translate({ id: 'chat.instructions', message: 'Select text on the page and ask questions about it, or ask general questions about the content.' })}</p>
                  {user && (
                    <p>As a registered user, you can earn bonus points by personalizing content and translating to Urdu.</p>
                  )}
                </div>
              ) : (
                state.messages.map((message) => (
                  <div
                    key={message.id}
                    className={`${styles.message} ${styles[message.role]}`}
                  >
                    <div className={styles.messageContent}>
                      {message.content}
                    </div>
                    <div className={styles.messageActions}>
                      <button
                        className={styles.copyButton}
                        onClick={() => navigator.clipboard.writeText(message.content)}
                        title={translate({ id: 'chat.copy', message: 'Copy message' })}
                      >
                        📋
                      </button>
                      <div className={styles.messageTimestamp}>
                        {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </div>
                    </div>
                  </div>
                ))
              )}
              {isLoading && (
                <div className={`${styles.message} ${styles.assistant}`}>
                  <div className={styles.messageContent}>
                    <div className={styles.typingIndicator}>
                      <div></div>
                      <div></div>
                      <div></div>
                    </div>
                  </div>
                  <div className={styles.messageTimestamp}>
                    {new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              )}
              {showScrollToBottom && (
                <button
                  className={styles.scrollToBottomButton}
                  onClick={scrollToBottom}
                  aria-label="Scroll to bottom"
                >
                  ↓
                </button>
              )}
              <div ref={messagesEndRef} />
            </div>

            <form onSubmit={handleSubmit} className={styles.inputForm}>
              <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={translate({ id: 'chat.placeholder', message: 'Ask a question about the textbook...' })}
                className={styles.textInput}
                rows={2}
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={!inputValue.trim() || isLoading}
                className={styles.sendButton}
              >
                {isLoading ? (
                  <span className={styles.loadingSpinner}>●</span>
                ) : (
                  translate({ id: 'chat.send', message: 'Send' })
                )}
              </button>
            </form>

            {selectedText && (
              <div className={styles.selectedTextPreview}>
                <small>{translate({ id: 'chat.selectedText', message: 'Selected text:' })}</small>
                <p>"{selectedText.length > 100 ? selectedText.substring(0, 100) + '...' : selectedText}"</p>
              </div>
            )}

            <div className={styles.compactFooter}>
              <button
                onClick={() => setIsChatOpen(false)}
                className={styles.minimizeButton}
              >
                −
              </button>
            </div>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className={`${styles.chatContainer} ${isDarkTheme ? styles.dark : styles.light}`}>
      <div className={styles.chatHeader}>
        <h3>{translate({ id: 'chat.title', message: 'AI Textbook Assistant' })}</h3>
        <div className={styles.headerActions}>
          <select 
            value={currentLanguage} 
            onChange={(e) => setCurrentLanguage(e.target.value)}
            className={styles.languageSelect}
          >
            {availableLanguages.map(lang => (
              <option key={lang.code} value={lang.code}>{lang.name}</option>
            ))}
          </select>
          <button onClick={clearChat} className={styles.newChatButton}>
            New Chat
          </button>
        </div>
      </div>

      {/* Bonus Points and Personalization Controls */}
      {user && (
        <div className={styles.bonusControls}>
          <div className={styles.bonusPoints}>
            <span>🏆 Bonus Points: {user.bonusPoints}</span>
            <span>👤 Hi, {user.email.split('@')[0]}!</span>
          </div>
          <div className={styles.personalizationControls}>
            <button 
              className={styles.personalizeButton} 
              onClick={handlePersonalizeContent}
              title="Personalize content based on your background"
              disabled={authLoading}
            >
              🎯 Personalize Content
            </button>
            <button 
              className={styles.translateButton} 
              onClick={handleTranslateToUrdu}
              title="Translate to Urdu"
              disabled={authLoading}
            >
              🌍 Translate to Urdu
            </button>
          </div>
        </div>
      )}

      {selectedText && (
        <div className={styles.selectedTextPreview}>
          <small>{translate({ id: 'chat.selectedText', message: 'Selected text:' })}</small>
          <p>"{selectedText.length > 100 ? selectedText.substring(0, 100) + '...' : selectedText}"</p>
        </div>
      )}

      <div
        className={styles.messagesContainer}
        ref={messagesContainerRef}
        onScroll={() => {
          if (messagesContainerRef.current) {
            const { scrollTop, scrollHeight, clientHeight } = messagesContainerRef.current;
            // Show scroll to bottom button if user scrolls up more than 100px from bottom
            const shouldShowButton = scrollHeight - scrollTop > clientHeight + 100;
            setShowScrollToBottom(shouldShowButton);
          }
        }}
      >
        {state.messages.length === 0 ? (
          <div className={styles.welcomeMessage}>
            <p>{translate({ id: 'chat.welcome', message: 'Welcome! I am your AI assistant for the Physical AI & Humanoid Robotics textbook.' })}</p>
            <p>{translate({ id: 'chat.instructions', message: 'Select text on the page and ask questions about it, or ask general questions about the content.' })}</p>
            {user && (
              <div className={styles.bonusInfo}>
                <h4>Bonus Points Opportunity!</h4>
                <ul>
                  <li>🎯 50 points for personalizing content in chapters</li>
                  <li>🌍 50 points for translating content to Urdu</li>
                  <li>Total: {user.bonusPoints} points earned so far</li>
                </ul>
              </div>
            )}
          </div>
        ) : (
          state.messages.map((message) => (
            <div
              key={message.id}
              className={`${styles.message} ${styles[message.role]}`}
            >
              <div className={styles.messageContent}>
                {message.content}
              </div>
              <div className={styles.messageActions}>
                <button
                  className={styles.copyButton}
                  onClick={() => navigator.clipboard.writeText(message.content)}
                  title={translate({ id: 'chat.copy', message: 'Copy message' })}
                >
                  📋
                </button>
                <div className={styles.messageTimestamp}>
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </div>
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className={`${styles.message} ${styles.assistant}`}>
            <div className={styles.messageContent}>
              <div className={styles.typingIndicator}>
                <div></div>
                <div></div>
                <div></div>
              </div>
            </div>
            <div className={styles.messageTimestamp}>
              {new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className={styles.inputForm}>
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={translate({ id: 'chat.placeholder', message: 'Ask a question about the textbook...' })}
          className={styles.textInput}
          rows={2}
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={!inputValue.trim() || isLoading}
          className={styles.sendButton}
        >
          {isLoading ? (
            <span className={styles.loadingSpinner}>●</span>
          ) : (
            translate({ id: 'chat.send', message: 'Send' })
          )}
        </button>
      </form>
    </div>
  );
};

export default EnhancedChatComponent;