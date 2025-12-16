import React, { useState, useEffect, useRef } from 'react';
import { useLocation } from '@docusaurus/router';
import clsx from 'clsx';
import styles from './AutoScrollControl.module.css';

const AutoScrollControl: React.FC = () => {
  const [speed, setSpeed] = useState(50); // pixels per second
  const [isPlaying, setIsPlaying] = useState(false);
  const intervalRef = useRef<NodeJS.Timeout | null>(null);
  const lastScrollTime = useRef<number>(0);
  const location = useLocation();

  // Check if we're on a textbook page (in the docs directory)
  const isTextbookPage = location.pathname.includes('/docs/');

  const toggleAutoScroll = () => {
    if (isPlaying) {
      // Pause auto-scrolling
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
      setIsPlaying(false);
    } else {
      // Start auto-scrolling
      setIsPlaying(true);
      lastScrollTime.current = performance.now();

      intervalRef.current = setInterval(() => {
        try {
          // Check if document is loaded and has scrollable content
          if (typeof window !== 'undefined' && window.document) {
            const now = performance.now();
            const deltaTime = (now - lastScrollTime.current) / 1000; // Convert to seconds
            lastScrollTime.current = now;

            const scrollAmount = speed * deltaTime;

            // Scroll by the calculated amount
            window.scrollBy(0, scrollAmount);

            // Check if we've reached the bottom
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const windowHeight = window.innerHeight;
            const documentHeight = Math.max(
              document.body.scrollHeight,
              document.body.offsetHeight,
              document.documentElement.clientHeight
            );

            if (scrollTop + windowHeight >= documentHeight - 100) { // Stop 100px before bottom
              setIsPlaying(false);
              if (intervalRef.current) {
                clearInterval(intervalRef.current);
                intervalRef.current = null;
              }
            }
          }
        } catch (error) {
          console.error('AutoScrollControl error:', error);
          if (intervalRef.current) {
            clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          setIsPlaying(false);
        }
      }, 16); // ~60fps
    }
  };

  const handleSpeedChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newSpeed = parseInt(e.target.value, 10);
    setSpeed(newSpeed);

    // If currently auto-scrolling, restart with new speed
    if (isPlaying) {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
      setIsPlaying(false);
      setTimeout(() => {
        if (typeof window !== 'undefined' && window.document) {
          setIsPlaying(true);
          lastScrollTime.current = performance.now();

          intervalRef.current = setInterval(() => {
            try {
              if (typeof window !== 'undefined' && window.document) {
                const now = performance.now();
                const deltaTime = (now - lastScrollTime.current) / 1000;
                lastScrollTime.current = now;

                const scrollAmount = newSpeed * deltaTime;

                window.scrollBy(0, scrollAmount);

                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const windowHeight = window.innerHeight;
                const documentHeight = Math.max(
                  document.body.scrollHeight,
                  document.body.offsetHeight,
                  document.documentElement.clientHeight
                );

                if (scrollTop + windowHeight >= documentHeight - 100) {
                  setIsPlaying(false);
                  if (intervalRef.current) {
                    clearInterval(intervalRef.current);
                    intervalRef.current = null;
                  }
                }
              }
            } catch (error) {
              console.error('AutoScrollControl speed change error:', error);
              if (intervalRef.current) {
                clearInterval(intervalRef.current);
                intervalRef.current = null;
              }
              setIsPlaying(false);
            }
          }, 16);
        }
      }, 0);
    }
  };

  const resetScroll = () => {
    try {
      if (typeof window !== 'undefined' && window.document) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        if (isPlaying) {
          if (intervalRef.current) {
            clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          setIsPlaying(false);
        }
      }
    } catch (error) {
      console.error('AutoScrollControl reset error:', error);
    }
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, []);

  return (
    <>
      {isTextbookPage && (
        <div className={clsx(styles.autoScrollControl, styles.floating)}>
          <div className={styles.controlPanel}>
            <div className={styles.speedControl}>
              <input
                id="scrollSpeed"
                type="range"
                min="1"
                max="200"
                value={speed}
                onChange={handleSpeedChange}
                className={styles.speedSlider}
                title={`Speed: ${speed}px/sec`}
              />
              <span className={styles.speedValue}>{speed}</span>
            </div>
            <div className={styles.buttons}>
              <button
                onClick={toggleAutoScroll}
                className={clsx(styles.controlButton, {
                  [styles.active]: isPlaying
                })}
                aria-label={isPlaying ? "Pause auto-scroll" : "Start auto-scroll"}
              >
                {isPlaying ? "⏸️" : "▶️"}
              </button>
              <button
                onClick={resetScroll}
                className={styles.controlButton}
                aria-label="Reset scroll position"
              >
                🔄
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default AutoScrollControl;