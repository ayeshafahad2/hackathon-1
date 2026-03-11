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
      title: 'AI-Powered Personalization',
      description: 'Experience learning tailored to your unique background. Our AI adapts content complexity, examples, and explanations based on your profile.',
      benefits: [
        'Adaptive content complexity',
        'Personalized examples',
        'Background-aware explanations',
        'Learning style matching',
      ],
      bonus: 50,
      gradient: 'linear-gradient(135deg, #6366f1 0%, #0ea5e9 100%)',
      comingSoon: false,
    },
    {
      icon: '🌐',
      title: 'Urdu Translation',
      description: 'Break language barriers with instant Urdu translations. Access complex technical concepts in your native language for better understanding.',
      benefits: [
        'Native language support',
        'Technical term localization',
        'Cultural context adaptation',
        'Bilingual learning',
      ],
      bonus: 50,
      gradient: 'linear-gradient(135deg, #0ea5e9 0%, #22c55e 100%)',
      comingSoon: false,
    },
    {
      icon: '🤖',
      title: 'Smart AI Chatbot',
      description: 'Get instant, context-aware answers 24/7. Our RAG-powered chatbot understands textbook content and provides accurate, cited responses.',
      benefits: [
        'Contextual AI responses',
        'Multi-turn conversations',
        'Source citations',
        'Code explanations',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)',
      comingSoon: false,
    },
    {
      icon: '📊',
      title: 'Progress Analytics',
      description: 'Track your learning journey with detailed analytics. Visualize your progress, identify strengths, and focus on areas for improvement.',
      benefits: [
        'Real-time progress tracking',
        'Performance insights',
        'Achievement milestones',
        'Learning analytics dashboard',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #ec4899 0%, #a855f7 100%)',
      comingSoon: true,
    },
    {
      icon: '📱',
      title: 'Responsive Design',
      description: 'Learn seamlessly across all devices. Our platform delivers a perfect experience on desktop, tablet, and mobile.',
      benefits: [
        'Mobile-first design',
        'Tablet optimization',
        'Desktop experience',
        'Cross-device sync',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)',
      comingSoon: false,
    },
    {
      icon: '🔒',
      title: 'Enterprise Security',
      description: 'Your data is protected with bank-grade security. We use industry-standard encryption and authentication to keep your information safe.',
      benefits: [
        'End-to-end encryption',
        'JWT authentication',
        'Privacy-first architecture',
        'Secure data storage',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%)',
      comingSoon: false,
    },
    {
      icon: '🔍',
      title: 'Smart Search',
      description: 'Find exactly what you need instantly. Our intelligent search understands context and delivers relevant results across all chapters.',
      benefits: [
        'Semantic search',
        'Chapter filtering',
        'Quick navigation',
        'Search history',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #14b8a6 0%, #0ea5e9 100%)',
      comingSoon: false,
    },
    {
      icon: '🎨',
      title: 'Dark & Light Themes',
      description: 'Study comfortably in any environment. Switch between beautiful dark and light themes to reduce eye strain.',
      benefits: [
        'Eye comfort mode',
        'Auto theme detection',
        'Custom color schemes',
        'Accessibility support',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #64748b 0%, #475569 100%)',
      comingSoon: false,
    },
    {
      icon: '🏆',
      title: 'Gamification',
      description: 'Stay motivated with points, badges, and achievements. Turn learning into an engaging game with rewards for your progress.',
      benefits: [
        'Bonus points system',
        'Achievement badges',
        'Learning streaks',
        'Leaderboards',
      ],
      bonus: 0,
      gradient: 'linear-gradient(135deg, #eab308 0%, #f59e0b 100%)',
      comingSoon: true,
    },
  ];

  const steps = [
    {
      number: '01',
      title: 'Create Your Account',
      description: 'Sign up in seconds and tell us about your background, experience level, and learning goals',
      icon: '👤',
      color: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    },
    {
      number: '02',
      title: 'Explore Content',
      description: 'Browse through 13 comprehensive chapters covering Physical AI and Humanoid Robotics',
      icon: '📖',
      color: 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%)',
    },
    {
      number: '03',
      title: 'Personalize Learning',
      description: 'Click "Personalize Content" to adapt material complexity to your knowledge level',
      icon: '⚙️',
      color: 'linear-gradient(135deg, #22c55e 0%, #14b8a6 100%)',
    },
    {
      number: '04',
      title: 'Translate if Needed',
      description: 'Switch to Urdu translation for complex concepts with a single click',
      icon: '🌐',
      color: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)',
    },
    {
      number: '05',
      title: 'Ask AI Assistant',
      description: 'Get instant answers to your questions from our intelligent chatbot',
      icon: '🤖',
      color: 'linear-gradient(135deg, #ec4899 0%, #a855f7 100%)',
    },
    {
      number: '06',
      title: 'Earn Rewards',
      description: 'Collect up to 100 bonus points by using personalization features',
      icon: '🏆',
      color: 'linear-gradient(135deg, #eab308 0%, #f59e0b 100%)',
    },
  ];

  const stats = [
    { value: '13', label: 'Comprehensive Chapters', icon: '📚' },
    { value: '50+', label: 'Topics Covered', icon: '📝' },
    { value: '24/7', label: 'AI Support', icon: '🤖' },
    { value: '100+', label: 'Bonus Points', icon: '🎁' },
  ];

  const testimonials = [
    {
      quote: "The AI chatbot helped me understand complex kinematics concepts in minutes. It's like having a personal tutor!",
      author: 'Student',
      avatar: '👨‍🎓',
    },
    {
      quote: "Urdu translation made it so much easier to grasp difficult topics. This platform is a game-changer!",
      author: 'Learner',
      avatar: '👩‍💻',
    },
    {
      quote: "The personalized content adaptation is incredible. It knows exactly what level to explain things.",
      author: 'Engineer',
      avatar: '👨‍🔬',
    },
  ];

  return (
    <Layout
      title="Features"
      description="Discover the powerful features of our AI-powered learning platform">
      <div className={styles.featuresPage}>
        {/* Hero Section */}
        <section className={styles.featuresHero}>
          <div className={styles.heroGlow}></div>
          <div className={styles.heroContent}>
            <div className={styles.heroBadge}>✨ AI-Powered Learning Platform</div>
            <h1 className={styles.heroTitle}>Everything You Need to Master Physical AI</h1>
            <p className={styles.heroSubtitle}>
              Experience the future of education with our intelligent, personalized learning platform.
              From AI-powered chatbot to Urdu translations – we've got you covered.
            </p>
            <div className={styles.heroCTA}>
              <Link className={clsx('button button--primary button--lg', styles.heroButton)} to="/auth/signup">
                Start Learning Free
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </Link>
              <Link className={clsx('button button--secondary button--lg', styles.heroButtonSecondary)} to="/docs/intro">
                Browse Textbook
              </Link>
            </div>
          </div>
          
          {/* Stats Bar */}
          <div className={styles.statsBar}>
            {stats.map((stat, index) => (
              <div key={index} className={styles.statItem}>
                <div className={styles.statIcon}>{stat.icon}</div>
                <div className={styles.statValue}>{stat.value}</div>
                <div className={styles.statLabel}>{stat.label}</div>
              </div>
            ))}
          </div>
        </section>

        {/* Features Grid */}
        <section className={styles.featuresSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>Powerful Features</h2>
              <p className={styles.sectionSubtitle}>
                Everything you need to succeed in your learning journey
              </p>
            </div>
            
            <div className={styles.featuresGrid}>
              {features.map((feature, index) => (
                <div
                  key={index}
                  className={clsx(styles.featureCard, feature.comingSoon && styles.comingSoon)}
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <div className={styles.featureHeader}>
                    <div
                      className={styles.featureIconWrapper}
                      style={{ background: feature.gradient }}
                    >
                      <span className={styles.featureIcon}>{feature.icon}</span>
                    </div>
                    {feature.comingSoon && (
                      <span className={styles.comingSoonBadge}>Coming Soon</span>
                    )}
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
                Start your learning journey in 6 simple steps
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
                  <div 
                    className={styles.stepIconWrapper}
                    style={{ background: step.color }}
                  >
                    <span className={styles.stepIcon}>{step.icon}</span>
                  </div>
                  <h3 className={styles.stepTitle}>{step.title}</h3>
                  <p className={styles.stepDescription}>{step.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className={styles.testimonialsSection}>
          <div className="container">
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>Loved by Learners</h2>
              <p className={styles.sectionSubtitle}>
                See what our users are saying
              </p>
            </div>
            
            <div className={styles.testimonialsGrid}>
              {testimonials.map((testimonial, index) => (
                <div
                  key={index}
                  className={styles.testimonialCard}
                  style={{ animationDelay: `${index * 0.15}s` }}
                >
                  <div className={styles.testimonialAvatar}>{testimonial.avatar}</div>
                  <div className={styles.testimonialQuote}>"{testimonial.quote}"</div>
                  <div className={styles.testimonialAuthor}>
                    <div className={styles.authorAvatar}>{testimonial.avatar}</div>
                    <div className={styles.authorName}>{testimonial.author}</div>
                  </div>
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

        {/* Final CTA Section */}
        <section className={styles.finalCTASection}>
          <div className="container">
            <div className={styles.finalCTAContent}>
              <div className={styles.finalCTAGlow}></div>
              <h2 className={styles.finalCTATitle}>Ready to Start Learning?</h2>
              <p className={styles.finalCTASubtitle}>
                Join thousands of students mastering Physical AI and Humanoid Robotics
              </p>
              <div className={styles.finalCTAButtons}>
                <Link
                  className={clsx('button button--primary button--lg', styles.finalCTAButton)}
                  to="/auth/signup">
                  Create Free Account
                </Link>
                <Link
                  className={clsx('button button--outline button--lg', styles.finalCTAButtonSecondary)}
                  to="/docs/intro">
                  Explore Textbook
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
