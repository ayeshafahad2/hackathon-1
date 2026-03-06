import React from 'react';
import { useLocation } from '@docusaurus/router';
import styles from './SimpleFloatingButton.module.css';

const SimpleFloatingButton: React.FC = () => {
  const location = useLocation();

  // Don't show on the chat page itself to avoid duplication
  const shouldShow = location.pathname !== '/chat';

  if (!shouldShow) {
    return null;
  }

  const handleClick = () => {
    // Navigate to the chat page
    window.location.href = '/chat';
  };

  return (
    <button
      className={styles.floatingButton}
      onClick={handleClick}
      aria-label="Open AI Assistant"
    >
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="3" y="11" width="18" height="10" rx="2" />
        <circle cx="12" cy="5" r="2" />
        <path d="M12 7v4" />
        <line x1="8" y1="16" x2="8" y2="16" />
        <line x1="16" y1="16" x2="16" y2="16" />
      </svg>
    </button>
  );
};

export default SimpleFloatingButton;