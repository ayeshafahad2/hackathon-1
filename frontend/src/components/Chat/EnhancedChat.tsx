import React, { useState, useEffect, useRef } from 'react';
import { useColorMode } from '@docusaurus/theme-common';
import { translate } from '@docusaurus/Translate';
import styles from './Chat.module.css';
import { chatWithMockBackend } from './mockService';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

interface EnhancedChatProps {
  compact?: boolean; // For use in sidebar/docked mode
}

const EnhancedChatComponent: React.FC<EnhancedChatProps> = ({ compact = false }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string>('');
  const [isChatOpen, setIsChatOpen] = useState(!compact); // Start open if not compact
  const [backendStatus, setBackendStatus] = useState<'checking' | 'connected' | 'disconnected' | 'error'>('checking');
  const [showScrollToBottom, setShowScrollToBottom] = useState(false);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);
  const messagesContainerRef = useRef<HTMLDivElement>(null);
  const { colorMode } = useColorMode();
  const isDarkTheme = colorMode === 'dark';

  // Function to check backend status
  useEffect(() => {
    const checkBackendStatus = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/chat/health', {
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
  }, [messages]);

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

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Try to call the backend API first
      let response;
      let data;

      try {
        response = await fetch('http://localhost:8000/api/v1/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message: inputValue,
            session_id: sessionId || undefined,
            selected_text: selectedText || undefined,
            language: 'en', // Will be dynamic based on site language
          }),
        });

        if (!response.ok) {
          throw new Error(`API request failed with status ${response.status}`);
        }

        data = await response.json();
        setBackendStatus('connected'); // Backend is working
      } catch (apiError) {
        console.warn('Backend API unavailable, using mock service:', apiError);
        // Use mock service when backend is unavailable
        data = await chatWithMockBackend(inputValue);
        setBackendStatus('disconnected');
      }

      // Add assistant message
      const assistantMessage: Message = {
        id: Date.now().toString(),
        content: data.response,
        role: 'assistant',
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, assistantMessage]);
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
      setMessages(prev => [...prev, errorMessage]);
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

  const startNewChat = () => {
    setMessages([]);
    setSessionId('');
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
              <button onClick={startNewChat} className={styles.newChatButton}>
                New Chat
              </button>
            </div>

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
              {messages.length === 0 ? (
                <div className={styles.welcomeMessage}>
                  <p>{translate({ id: 'chat.welcome', message: 'Welcome! I am your AI assistant for the Physical AI & Humanoid Robotics textbook.' })}</p>
                  <p>{translate({ id: 'chat.instructions', message: 'Select text on the page and ask questions about it, or ask general questions about the content.' })}</p>
                </div>
              ) : (
                messages.map((message) => (
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
        <button
          onClick={startNewChat}
          className={styles.newChatButton}
        >
          New Chat
        </button>
      </div>

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
        {messages.length === 0 ? (
          <div className={styles.welcomeMessage}>
            <p>{translate({ id: 'chat.welcome', message: 'Welcome! I am your AI assistant for the Physical AI & Humanoid Robotics textbook.' })}</p>
            <p>{translate({ id: 'chat.instructions', message: 'Select text on the page and ask questions about it, or ask general questions about the content.' })}</p>
          </div>
        ) : (
          messages.map((message) => (
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