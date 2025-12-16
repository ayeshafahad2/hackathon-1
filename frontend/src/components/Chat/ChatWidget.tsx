import React, { useState, useEffect } from 'react';
import EnhancedChatComponent from './EnhancedChat';
import styles from './ChatWidget.module.css';

interface ChatWidgetProps {
  position?: 'bottom-right' | 'bottom-left' | 'side';
  defaultOpen?: boolean;
}

const ChatWidget: React.FC<ChatWidgetProps> = ({
  position = 'bottom-right',
  defaultOpen = false
}) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);
  const [hasUnread, setHasUnread] = useState(false);

  // Show unread indicator when new messages arrive
  useEffect(() => {
    // This would be connected to the actual chat state in a full implementation
    const handleNewMessage = () => {
      if (!isOpen) {
        setHasUnread(true);
      }
    };

    // Cleanup function
    return () => {
      // Cleanup listeners if any
    };
  }, [isOpen]);

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (isOpen) {
      setHasUnread(false); // Clear unread when opening
    }
  };

  return (
    <div className={`${styles.chatWidget} ${styles[position]}`}>
      {isOpen ? (
        <div className={styles.chatExpanded}>
          <div className={styles.chatHeader}>
            <h4>AI Textbook Assistant</h4>
            <button
              onClick={toggleChat}
              className={styles.closeButton}
              aria-label="Close chat"
            >
              ×
            </button>
          </div>
          <div className={styles.chatBody}>
            <EnhancedChatComponent compact={false} />
          </div>
        </div>
      ) : (
        <button
          className={`${styles.chatToggle} ${hasUnread ? styles.unread : ''}`}
          onClick={toggleChat}
          aria-label="Open chat"
        >
          <span className={styles.chatIcon}>🤖</span>
          {hasUnread && <span className={styles.unreadIndicator}></span>}
        </button>
      )}
    </div>
  );
};

export default ChatWidget;