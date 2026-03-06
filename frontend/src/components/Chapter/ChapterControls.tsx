// frontend/src/components/Chapter/ChapterControls.tsx
import React, { useState, useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import styles from './ChapterControls.module.css';

interface ChapterControlsProps {
  chapterId: string;
  chapterTitle: string;
  content: string;
  onContentUpdate: (newContent: string) => void;
}

const ChapterControls: React.FC<ChapterControlsProps> = ({ 
  chapterId, 
  chapterTitle, 
  content, 
  onContentUpdate 
}) => {
  const { user, loading, personalizeContent, translateToUrdu } = useAuth();
  const [isPersonalized, setIsPersonalized] = useState(false);
  const [isInUrdu, setIsInUrdu] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [message, setMessage] = useState('');

  // Reset state when chapter changes
  useEffect(() => {
    setIsPersonalized(false);
    setIsInUrdu(false);
    setMessage('');
  }, [chapterId]);

  const handlePersonalizeClick = async () => {
    if (!user) {
      setMessage('Please sign in to use personalization');
      return;
    }

    setIsProcessing(true);
    setMessage('');

    try {
      // In a real implementation, we would call the backend to personalize content
      // For now, we'll just show a message and mark as personalized
      await personalizeContent(chapterId);
      setIsPersonalized(true);
      setMessage('Content has been personalized based on your background!');
      
      // In a real implementation, you'd fetch the personalized content here
      // const response = await fetch(`/api/v1/personalization/personalize-content`, {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //     'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      //   },
      //   body: JSON.stringify({ chapter_id: chapterId, content })
      // });
      // const data = await response.json();
      // onContentUpdate(data.personalized_content);
    } catch (error: any) {
      setMessage(`Error personalizing content: ${error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  const handleTranslateClick = async () => {
    if (!user) {
      setMessage('Please sign in to use translation');
      return;
    }

    setIsProcessing(true);
    setMessage('');

    try {
      // In a real implementation, we would call the backend for translation
      await translateToUrdu(chapterId);
      setIsInUrdu(true);
      setMessage('Content has been translated to Urdu!');
      
      // In a real implementation, you'd fetch the translated content here
      // const response = await fetch(`/api/v1/translation/translate-urdu`, {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //     'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      //   },
      //   body: JSON.stringify({ chapter_id: chapterId, content })
      // });
      // const data = await response.json();
      // onContentUpdate(data.urdu_content);
    } catch (error: any) {
      setMessage(`Error translating content: ${error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  if (loading) {
    return <div className={styles.controls}>Loading...</div>;
  }

  return (
    <div className={styles.controls}>
      <div className={styles.buttons}>
        {!user ? (
          <div className={styles.signinPrompt}>
            <p>Please <a href="/signin">sign in</a> to unlock personalization features and earn bonus points!</p>
          </div>
        ) : (
          <>
            <button
              className={`${styles.controlButton} ${isPersonalized ? styles.active : ''}`}
              onClick={handlePersonalizeClick}
              disabled={isProcessing}
            >
              {isPersonalized ? '✓ Personalized' : 'Personalize Content'}
            </button>
            
            <button
              className={`${styles.controlButton} ${isInUrdu ? styles.active : ''}`}
              onClick={handleTranslateClick}
              disabled={isProcessing}
            >
              {isInUrdu ? '✓ Urdu' : 'Translate to Urdu'}
            </button>
          </>
        )}
      </div>
      
      {message && (
        <div className={styles.message}>
          {message}
        </div>
      )}
      
      {user && (
        <div className={styles.bonusInfo}>
          <p>Earn bonus points: 50 for personalizing, 50 for Urdu translation!</p>
          <p>Your current bonus points: {user.bonusPoints}</p>
        </div>
      )}
    </div>
  );
};

export default ChapterControls;