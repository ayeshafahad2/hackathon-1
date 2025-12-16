import React from 'react';
import Layout from '@theme/Layout';
import EnhancedChatComponent from '@site/src/components/Chat/EnhancedChat';
import clsx from 'clsx';
import styles from './chat.module.css';

function ChatPage(): JSX.Element {
  return (
    <Layout
      title="AI Textbook Assistant"
      description="An intelligent chatbot to help you understand textbook content">
      <main className={clsx('container', 'margin-vert--lg')}>
        <div className="row">
          {/* Main content */}
          <div className="col col--8 col--offset-2">
            <div className="text--center padding-horiz--md">
              <h1 className={clsx('hero__title', styles.chatHeroTitle)}>AI Textbook Assistant</h1>
              <p className={clsx('hero__subtitle', styles.chatHeroSubtitle)}>
                Ask questions about the textbook content and get instant, contextual answers powered by AI
              </p>
            </div>

            <div className={styles.chatPageCard}>
              <div className={styles.chatContainer}>
                <EnhancedChatComponent />
              </div>

              <div className={styles.featuresSection}>
                <h2>How it works</h2>
                <div className="row margin-vert--lg">
                  <div className="col col--4">
                    <div className={styles.featureCard}>
                      <div className={styles.featureIcon}>🔍</div>
                      <h3>Select Text</h3>
                      <p>Highlight any text on the page and ask questions about it</p>
                    </div>
                  </div>
                  <div className="col col--4">
                    <div className={styles.featureCard}>
                      <div className={styles.featureIcon}>💬</div>
                      <h3>Ask Questions</h3>
                      <p>Type your question about the content in the chat box</p>
                    </div>
                  </div>
                  <div className="col col--4">
                    <div className={styles.featureCard}>
                      <div className={styles.featureIcon}>🧠</div>
                      <h3>Get Answers</h3>
                      <p>Receive intelligent, contextual answers based on the textbook</p>
                    </div>
                  </div>
                </div>
              </div>

              <div className={styles.benefitsSection}>
                <h2>Benefits</h2>
                <ul>
                  <li>Instant answers to questions about textbook content</li>
                  <li>Contextual understanding of selected text</li>
                  <li>Available 24/7 to assist with learning</li>
                  <li>Supports multiple languages (English and Urdu)</li>
                  <li>Powered by advanced RAG technology for accurate responses</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}

export default ChatPage;