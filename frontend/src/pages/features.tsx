// frontend/src/pages/features.tsx
import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './features.module.css';

const FeaturesPage = () => {
  const features = [
    {
      icon: '🎯',
      title: 'Content Personalization',
      description: 'Our system adapts the complexity and examples in each chapter based on your background',
      benefits: [
        'Software experience level',
        'Hardware background',
        'Programming language proficiency',
        'Field of interest',
      ],
      bonus: 50,
      gradient: 'linear-gradient(135deg, #6366f1 0%, #0ea5e9 100%)',
    },
    {
      icon: '🌐',
      title: 'Urdu Translation',
      description: 'Access textbook content in Urdu to enhance your understanding and learning experience',
      benefits: [
        'Native language support',
        'Better comprehension',
        'Cultural context',
        'Inclusive learning',
      ],
      bonus: 50,
      gradient: 'linear-gradient(135deg, #0ea5e9 0%, #22c55e 100%)',
    },
    {
      icon: '📈',
      title: 'Progress Tracking',
      description: 'Track your learning progress and earn bonus points for engaging with personalization features',
      benefits: [
        'Real-time analytics',
        'Achievement badges',
        'Learning streaks',
        'Performance insights',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #ec4899 0%, #a855f7 100%)',
    },
    {
      icon: '🤖',
      title: 'AI-Powered Assistant',
      description: 'Get instant answers to your questions with our intelligent AI chatbot available 24/7',
      benefits: [
        'Contextual responses',
        'Multi-turn conversations',
        'Code explanations',
        'Concept clarification',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)',
    },
    {
      icon: '📱',
      title: 'Responsive Design',
      description: 'Learn on any device with our fully responsive platform optimized for all screen sizes',
      benefits: [
        'Mobile-friendly',
        'Tablet optimized',
        'Desktop experience',
        'Offline access',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)',
    },
    {
      icon: '🔒',
      title: 'Secure Platform',
      description: 'Your data is protected with enterprise-grade security and privacy measures',
      benefits: [
        'End-to-end encryption',
        'Secure authentication',
        'Privacy-first design',
        'Data backup',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%)',
    },
  ];

  const steps = [
    {
      number: '01',
      title: 'Create Account',
      description: 'Sign up and tell us about your background and experience level',
      icon: '👤',
    },
    {
      number: '02',
      title: 'Browse Content',
      description: 'Explore any chapter in the textbook that interests you',
      icon: '📖',
    },
    {
      number: '03',
      title: 'Personalize',
      description: 'Click "Personalize Content" to adapt the material to your level',
      icon: '⚙️',
    },
    {
      number: '04',
      title: 'Translate',
      description: 'Click "Translate to Urdu" for content in your native language',
      icon: '🌐',
    },
    {
      number: '05',
      title: 'Earn Points',
      description: 'Collect bonus points for each feature you use!',
      icon: '🏆',
    },
  ];

  return (
    <Layout 
      title="Features" 
      description="Discover the powerful features of our personalized learning platform">
      <div className={styles.featuresPage}>
        {/* Hero Section */}
        <section className={styles.featuresHero}>
          <div className={styles.heroGlow}></div>
          <div className={styles.heroContent}>
            <div className={styles.heroIcon}>✨</div>
            <h1 className={styles.heroTitle}>Platform Features</h1>
            <p className={styles.heroSubtitle}>
              Discover how our AI-powered platform transforms your learning experience
            </p>
          </div>
        </section>

        {/* Features Grid */}
        <section className={styles.featuresSection}>
          <div className="container">
            <div className={styles.featuresGrid}>
              {features.map((feature, index) => (
                <div 
                  key={index} 
                  className={styles.featureCard}
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <div 
                    className={styles.featureIconWrapper}
                    style={{ background: feature.gradient }}
                  >
                    <span className={styles.featureIcon}>{feature.icon}</span>
                  </div>
                  <h2 className={styles.featureTitle}>{feature.title}</h2>
                  <p className={styles.featureDescription}>{feature.description}</p>
                  {feature.benefits && (
                    <ul className={styles.featureBenefits}>
                      {feature.benefits.map((benefit, idx) => (
                        <li key={idx} className={styles.benefitItem}>
                          <span className={styles.checkIcon}>✓</span>
                          {benefit}
                        </li>
                      ))}
                    </ul>
                  )}
                  {feature.bonus > 0 && (
                    <div className={styles.bonusBadge}>
                      <span className={styles.bonusIcon}>🎁</span>
                      <span className={styles.bonusText}>Earn {feature.bonus} bonus points!</span>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section className={styles.howItWorksSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>How It Works</h2>
              <p className={styles.sectionSubtitle}>
                Get started in 5 simple steps
              </p>
            </div>
            
            <div className={styles.stepsTimeline}>
              {steps.map((step, index) => (
                <div 
                  key={index} 
                  className={styles.stepCard}
                  style={{ animationDelay: `${index * 0.15}s` }}
                >
                  <div className={styles.stepNumber}>{step.number}</div>
                  <div className={styles.stepIcon}>{step.icon}</div>
                  <h3 className={styles.stepTitle}>{step.title}</h3>
                  <p className={styles.stepDescription}>{step.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Bonus Points Section */}
        <section className={styles.bonusSection}>
          <div className="container">
            <div className={styles.bonusContent}>
              <div className={styles.bonusGlow}></div>
              <div className={styles.bonusIconLarge}>🏆</div>
              <h2 className={styles.bonusTitle}>Bonus Points Program</h2>
              <p className={styles.bonusDescription}>
                As a registered user, you can earn up to <strong className={styles.highlight}>100 bonus points</strong> 
                by using our personalization features
              </p>
              
              <div className={styles.pointsShowcase}>
                <div className={styles.pointItem}>
                  <div className={styles.pointValue}>50</div>
                  <div className={styles.pointLabel}>Points</div>
                  <div className={styles.pointDescription}>For personalizing chapter content</div>
                </div>
                <div className={styles.pointDivider}>+</div>
                <div className={styles.pointItem}>
                  <div className={styles.pointValue}>50</div>
                  <div className={styles.pointLabel}>Points</div>
                  <div className={styles.pointDescription}>For translating content to Urdu</div>
                </div>
                <div className={styles.pointDivider}>=</div>
                <div className={styles.pointItemTotal}>
                  <div className={styles.pointValueTotal}>100</div>
                  <div className={styles.pointLabelTotal}>Total Points</div>
                  <div className={styles.pointDescriptionTotal}>Maximum bonus per user!</div>
                </div>
              </div>

              <div className={styles.bonusCta}>
                <Link
                  className={clsx('button button--primary button--lg', styles.bonusButton)}
                  to="/auth/signup">
                  Get Started Now
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </Link>
              </div>
            </div>
          </div>
        </section>
      </div>
    </Layout>
  );
};

export default FeaturesPage;
