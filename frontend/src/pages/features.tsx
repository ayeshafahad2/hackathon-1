import React from 'react';
import Layout from '@theme/Layout';
import { translate } from '@docusaurus/Translate';
import EnhancedChatComponent from '@site/src/components/Chat/EnhancedChat';
import clsx from 'clsx';
import styles from './features.module.css';

export default function Features(): JSX.Element {
  return (
    <Layout
      title={translate({ id: 'features.title', message: 'AI Textbook Features' })}
      description={translate({ id: 'features.description', message: 'Explore the features of our AI-powered textbook assistant' })}>
      <main className={styles.featuresPage}>
        <div className={styles.featuresContainer}>
          <div className={styles.featuresHeader}>
            <h1>{translate({ id: 'features.header', message: 'AI Textbook Features' })}</h1>
            <p>Discover the powerful features that make our AI-powered textbook assistant an essential learning companion.</p>
          </div>

          <div className={styles.featuresContainerAll}>
            <div className={styles.featuresGrid}>
              <div className={clsx(styles.featureSection, styles.chatSection)}>
                <h2>🤖 AI-Powered Chat Assistant</h2>
                <p>
                  Our intelligent chatbot helps you understand complex topics in the textbook through natural conversation.
                  It can answer questions, explain concepts, and provide additional context based on the textbook content.
                </p>

                <div className={styles.chatPreviewContainer}>
                  <h3>Try the AI Assistant</h3>
                  <EnhancedChatComponent />
                </div>

                <div className={styles.featureActions}>
                  <button className={clsx(styles.actionButton, styles.primaryButton)}>
                    Start Chatting
                  </button>
                  <button className={clsx(styles.actionButton, styles.secondaryButton)}>
                    View Demo
                  </button>
                </div>
              </div>

              <div className={clsx(styles.featureSection)}>
                <h2>🔍 Contextual Understanding</h2>
                <p>
                  Select any text in the textbook and ask questions about it. The AI will understand the context of the
                  selected text and provide relevant explanations and answers.
                </p>
                <div className={styles.featureActions}>
                  <button className={clsx(styles.actionButton, styles.primaryButton)}>
                    Learn More
                  </button>
                  <button className={clsx(styles.actionButton, styles.secondaryButton)}>
                    Try It
                  </button>
                </div>
              </div>

              <div className={clsx(styles.featureSection)}>
                <h2>🌐 Multilingual Support</h2>
                <p>
                  The textbook and AI assistant are available in multiple languages, starting with English and Urdu.
                  Switch between languages using the language selector in the navigation bar.
                </p>
                <div className={styles.featureActions}>
                  <button className={clsx(styles.actionButton, styles.primaryButton)}>
                    Explore Languages
                  </button>
                  <button className={clsx(styles.actionButton, styles.secondaryButton)}>
                    View Demo
                  </button>
                </div>
              </div>

              <div className={clsx(styles.featureSection)}>
                <h2>⚡ Advanced Search</h2>
                <p>
                  Search across the entire textbook content to find relevant information quickly. The AI powers the
                  search to understand the meaning behind your queries, not just keyword matching.
                </p>
                <div className={styles.featureActions}>
                  <button className={clsx(styles.actionButton, styles.primaryButton)}>
                    Try Search
                  </button>
                  <button className={clsx(styles.actionButton, styles.secondaryButton)}>
                    See Examples
                  </button>
                </div>
              </div>

              <div className={clsx(styles.featureSection)}>
                <h2>🎯 Interactive Learning</h2>
                <p>
                  Get interactive explanations of complex concepts with examples and analogies that make difficult topics
                  easier to understand. The AI can generate practice questions and provide step-by-step solutions.
                </p>
                <div className={styles.featureActions}>
                  <button className={clsx(styles.actionButton, styles.primaryButton)}>
                    Start Learning
                  </button>
                  <button className={clsx(styles.actionButton, styles.secondaryButton)}>
                    View Examples
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}