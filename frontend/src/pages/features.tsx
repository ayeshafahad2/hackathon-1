// frontend/src/pages/features.tsx
import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './features.module.css';

const FeaturesPage = () => {
  const features = [
    {
      title: 'AI-Powered Personalization',
      description: 'Experience learning tailored to your unique background. Our AI adapts content complexity, examples, and explanations based on your profile.',
      benefits: [
        'Adaptive content complexity',
        'Personalized examples',
        'Background-aware explanations',
        'Learning style matching',
      ],
      bonus: 50,
      comingSoon: false,
    },
    {
      title: 'Urdu Translation',
      description: 'Break language barriers with instant Urdu translations. Access complex technical concepts in your native language for better understanding.',
      benefits: [
        'Native language support',
        'Technical term localization',
        'Cultural context adaptation',
        'Bilingual learning',
      ],
      bonus: 50,
      comingSoon: false,
    },
    {
      title: 'Smart AI Chatbot',
      description: 'Get instant, context-aware answers 24/7. Our RAG-powered chatbot understands textbook content and provides accurate, cited responses.',
      benefits: [
        'Contextual AI responses',
        'Multi-turn conversations',
        'Source citations',
        'Code explanations',
      ],
      bonus: 0,
      comingSoon: false,
    },
    {
      title: 'Progress Analytics',
      description: 'Track your learning journey with detailed analytics. Visualize your progress, identify strengths, and focus on areas for improvement.',
      benefits: [
        'Real-time progress tracking',
        'Performance insights',
        'Achievement milestones',
        'Learning analytics dashboard',
      ],
      bonus: 0,
      comingSoon: true,
    },
    {
      title: 'Responsive Design',
      description: 'Learn seamlessly across all devices. Our platform delivers a perfect experience on desktop, tablet, and mobile.',
      benefits: [
        'Mobile-first design',
        'Tablet optimization',
        'Desktop experience',
        'Cross-device sync',
      ],
      bonus: 0,
      comingSoon: false,
    },
    {
      title: 'Enterprise Security',
      description: 'Your data is protected with bank-grade security. We use industry-standard encryption and authentication to keep your information safe.',
      benefits: [
        'End-to-end encryption',
        'JWT authentication',
        'Privacy-first architecture',
        'Secure data storage',
      ],
      bonus: 0,
      comingSoon: false,
    },
    {
      title: 'Smart Search',
      description: 'Find exactly what you need instantly. Our intelligent search understands context and delivers relevant results across all chapters.',
      benefits: [
        'Semantic search',
        'Chapter filtering',
        'Quick navigation',
        'Search history',
      ],
      bonus: 0,
      comingSoon: false,
    },
    {
      title: 'Dark & Light Themes',
      description: 'Study comfortably in any environment. Switch between beautiful dark and light themes to reduce eye strain.',
      benefits: [
        'Eye comfort mode',
        'Auto theme detection',
        'Custom color schemes',
        'Accessibility support',
      ],
      bonus: 0,
      comingSoon: false,
    },
    {
      title: 'Gamification',
      description: 'Stay motivated with points, badges, and achievements. Turn learning into an engaging game with rewards for your progress.',
      benefits: [
        'Bonus points system',
        'Achievement badges',
        'Learning streaks',
        'Leaderboards',
      ],
      bonus: 0,
      comingSoon: true,
    },
  ];

  const steps = [
    {
      number: '01',
      title: 'Create Account',
      description: 'Sign up and tell us about your background',
    },
    {
      number: '02',
      title: 'Browse Content',
      description: 'Explore chapters that interest you',
    },
    {
      number: '03',
      title: 'Personalize',
      description: 'Adapt material to your knowledge level',
    },
    {
      number: '04',
      title: 'Translate',
      description: 'Get content in your native language',
    },
    {
      number: '05',
      title: 'Ask Questions',
      description: 'Get instant answers from AI chatbot',
    },
    {
      number: '06',
      title: 'Earn Points',
      description: 'Collect bonus points for using features',
    },
  ];

  return (
    <Layout
      title="Features"
      description="Discover the powerful features of our AI-powered learning platform">
      <div className={styles.featuresPage}>
        {/* Hero Section */}
        <section className={styles.featuresHero}>
          <div className={styles.heroBackground}>
            <div className={styles.gradientOrb1}></div>
            <div className={styles.gradientOrb2}></div>
            <div className={styles.gradientOrb3}></div>
          </div>
          
          <div className={styles.heroContent}>
            <div className={styles.heroBadge}>
              <span className={styles.badgeDot}></span>
              <span>Platform Features</span>
            </div>
            
            <h1 className={styles.heroTitle}>Everything You Need to Succeed</h1>
            
            <p className={styles.heroSubtitle}>
              A comprehensive platform designed to help you master Physical AI and Humanoid Robotics
            </p>
            
            <div className={styles.heroCTA}>
              <Link className={clsx('button button--primary button--lg', styles.heroButton)} to="/auth/signup">
                <span>Get Started Free</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </Link>
              <Link className={clsx('button button--secondary button--lg', styles.heroButtonSecondary)} to="/docs/intro">
                View Documentation
              </Link>
            </div>
          </div>
        </section>

        {/* Features Grid */}
        <section className={styles.featuresSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <span className={styles.sectionLabel}>Platform Features</span>
              <h2 className={styles.sectionTitle}>Powerful Tools for Modern Learning</h2>
              <p className={styles.sectionSubtitle}>
                Built with cutting-edge technology to enhance your educational experience
              </p>
            </div>
            
            <div className={styles.featuresGrid}>
              {features.map((feature, index) => (
                <div
                  key={index}
                  className={clsx(styles.featureCard, feature.comingSoon && styles.comingSoon)}
                >
                  <div className={styles.featureContent}>
                    <h3 className={styles.featureTitle}>{feature.title}</h3>
                    <p className={styles.featureDescription}>{feature.description}</p>
                    {feature.benefits && (
                      <ul className={styles.featureBenefits}>
                        {feature.benefits.map((benefit, idx) => (
                          <li key={idx} className={styles.benefitItem}>
                            <span className={styles.checkIcon}>✓</span>
                            <span>{benefit}</span>
                          </li>
                        ))}
                      </ul>
                    )}
                    {feature.bonus > 0 && (
                      <div className={styles.bonusBadge}>
                        Earn {feature.bonus} bonus points
                      </div>
                    )}
                    {feature.comingSoon && (
                      <div className={styles.comingSoonBadge}>Coming Soon</div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section className={styles.howItWorksSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <span className={styles.sectionLabel}>How It Works</span>
              <h2 className={styles.sectionTitle}>Start Learning in Minutes</h2>
              <p className={styles.sectionSubtitle}>
                Get up and running with our platform in six simple steps
              </p>
            </div>

            <div className={styles.stepsGrid}>
              {steps.map((step, index) => (
                <div key={index} className={styles.stepCard}>
                  <div className={styles.stepNumber}>{step.number}</div>
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
              <span className={styles.bonusLabel}>Rewards Program</span>
              <h2 className={styles.bonusTitle}>Earn Bonus Points</h2>
              <p className={styles.bonusDescription}>
                Get rewarded for engaging with the platform. Earn up to <strong>100 points</strong> by using personalization features.
              </p>

              <div className={styles.pointsShowcase}>
                <div className={styles.pointItem}>
                  <div className={styles.pointValue}>50</div>
                  <div className={styles.pointLabel}>Personalize Content</div>
                </div>
                <div className={styles.pointDivider}>+</div>
                <div className={styles.pointItem}>
                  <div className={styles.pointValue}>50</div>
                  <div className={styles.pointLabel}>Translate to Urdu</div>
                </div>
                <div className={styles.pointDivider}>=</div>
                <div className={styles.pointItemTotal}>
                  <div className={styles.pointValueTotal}>100</div>
                  <div className={styles.pointLabelTotal}>Total Points</div>
                </div>
              </div>

              <div className={styles.bonusCta}>
                <Link
                  className={clsx('button button--primary button--lg', styles.bonusButton)}
                  to="/auth/signup">
                  Start Earning Points
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* Final CTA Section */}
        <section className={styles.finalCTASection}>
          <div className="container">
            <div className={styles.finalCTAContent}>
              <h2 className={styles.finalCTATitle}>Ready to Get Started?</h2>
              <p className={styles.finalCTASubtitle}>
                Join students learning Physical AI and Humanoid Robotics today
              </p>
              <div className={styles.finalCTAButtons}>
                <Link
                  className={clsx('button button--primary button--lg', styles.finalCTAButton)}
                  to="/auth/signup">
                  Create Account
                </Link>
                <Link
                  className={clsx('button button--outline button--lg', styles.finalCTAButtonSecondary)}
                  to="/docs/intro">
                  Browse Textbook
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
