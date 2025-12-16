import React, { useState } from 'react';
import { useLocation } from '@docusaurus/router';
import styles from './SimpleFloatingButton.module.css';

const SimpleFloatingButton: React.FC = () => {
  const [isVisible, setIsVisible] = useState(true);
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
      🤖
    </button>
  );
};

export default SimpleFloatingButton;