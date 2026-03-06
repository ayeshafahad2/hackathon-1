import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <header className={styles.hero}>
      <div className={styles.heroBackground}>
        <div className={styles.gradientOrb1}></div>
        <div className={styles.gradientOrb2}></div>
        <div className={styles.gradientOrb3}></div>
      </div>

      <div className={styles.heroContent}>
        {/* Hero Image */}
        <div className={`${styles.heroImageWrapper} ${isVisible ? styles.animateIn : ''}`}>
          <div className={styles.imageGlow}></div>
          <img
            src="/img/hero-ai-robot.svg"
            alt="AI Robot"
            className={styles.heroImage}
          />
          <div className={styles.floatingElements}>
            <div className={styles.floatingElement1}>🤖</div>
            <div className={styles.floatingElement2}>🧠</div>
            <div className={styles.floatingElement3}>⚡</div>
          </div>
        </div>

        {/* Title Section */}
        <div className={styles.heroText}>
          <div className={`${styles.heroBadge} ${isVisible ? styles.fadeInDown : ''}`}>
            <span className={styles.badgeDot}></span>
            <span>AI-Native Textbook</span>
            <span className={styles.badgeNew}>NEW</span>
          </div>

          <h1 className={`${styles.title} ${isVisible ? styles.fadeInUp : ''}`}>
            {siteConfig.title}
          </h1>

          <p className={`${styles.subtitle} ${isVisible ? styles.fadeInUp : ''}`}>
            Your AI-Native Guide to the Future of Embodied Intelligence
          </p>

          <div className={`${styles.ctaButtons} ${isVisible ? styles.fadeInUp : ''}`}>
            <Link
              className={clsx('button button--primary button--lg', styles.ctaButton)}
              to="/docs/intro">
              <span>Start Learning</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </Link>
            <Link
              className={clsx('button button--secondary button--lg', styles.ctaButtonSecondary)}
              to="/features">
              Explore Features
            </Link>
          </div>

          <div className={`${styles.heroFooter} ${isVisible ? styles.fadeInUp : ''}`}>
            <div className={styles.heroFeature}>
              <span className={styles.checkmark}>✓</span>
              <span>Comprehensive curriculum</span>
            </div>
            <div className={styles.heroFeature}>
              <span className={styles.checkmark}>✓</span>
              <span>Hands-on projects</span>
            </div>
            <div className={styles.heroFeature}>
              <span className={styles.checkmark}>✓</span>
              <span>AI-powered assistance</span>
            </div>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className={styles.scrollIndicator}>
        <div className={styles.mouse}>
          <div className={styles.wheel}></div>
        </div>
        <span>Scroll to explore</span>
      </div>
    </header>
  );
}

function FeaturesSection() {
  const features = [
    {
      title: 'Master the Core of Robotics',
      description: 'Go beyond the basics and delve into the intricate mechanics of humanoid robots. Understand the principles of kinematics, dynamics, and control that underpin modern robotics and build a strong foundation for advanced applications.',
      icon: '🦾',
      color: 'linear-gradient(135deg, #6366f1 0%, #0ea5e9 100%)',
    },
    {
      title: 'Unlock the Power of AI',
      description: 'Explore the cutting-edge AI that drives intelligent behavior in robots. This textbook covers everything from machine learning and computer vision to natural language processing and reinforcement learning, equipping you with the skills to create truly smart robots.',
      icon: '🧠',
      color: 'linear-gradient(135deg, #ec4899 0%, #a855f7 100%)',
    },
    {
      title: 'Create Real-World Solutions',
      description: 'Put knowledge into practice with hands-on projects and real-world case studies. Learn how to design, build, and program humanoid robots to solve complex problems and make a tangible impact on the world.',
      icon: '🚀',
      color: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)',
    },
  ];

  return (
    <section className={styles.featuresSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Why This Textbook?</span>
          <h2 className={styles.sectionTitle}>
            Everything You Need to Master Physical AI
          </h2>
          <p className={styles.sectionSubtitle}>
            Your complete guide to mastering Physical AI & Humanoid Robotics
          </p>
        </div>

        <div className={styles.featuresGrid}>
          {features.map((feature, index) => (
            <div key={index} className={styles.featureCard}>
              <div className={styles.featureIconWrapper} style={{ background: feature.color }}>
                <span className={styles.featureIcon}>{feature.icon}</span>
              </div>
              <h3 className={styles.featureTitle}>{feature.title}</h3>
              <p className={styles.featureDescription}>{feature.description}</p>
              <Link to="/docs/intro" className={styles.featureLink}>
                Learn more
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </Link>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function StatsSection() {
  const stats = [
    { value: '12+', label: 'Comprehensive Chapters', suffix: '' },
    { value: '50', label: 'Hours of Content', suffix: '+' },
    { value: '100', label: 'Bonus Points Available', suffix: '' },
    { value: '24/7', label: 'AI Assistant Support', suffix: '' },
  ];

  return (
    <section className={styles.statsSection}>
      <div className="container">
        <div className={styles.statsGrid}>
          {stats.map((stat, index) => (
            <div key={index} className={styles.statCard}>
              <div className={styles.statValue}>
                {stat.value}<span className={styles.statSuffix}>{stat.suffix}</span>
              </div>
              <div className={styles.statLabel}>{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function TopicsPreviewSection() {
  const topics = [
    {
      icon: '🤖',
      title: 'Introduction to Humanoid Robotics',
      description: 'Understand the fundamentals of humanoid robot design and applications',
      chapters: 3,
      difficulty: 'Beginner',
    },
    {
      icon: '⚙️',
      title: 'Kinematics & Dynamics',
      description: 'Master the mathematical foundations of robot motion and forces',
      chapters: 4,
      difficulty: 'Intermediate',
    },
    {
      icon: '🧠',
      title: 'Vision-Language-Action Models',
      description: 'Learn cutting-edge AI models that enable robots to perceive and act',
      chapters: 3,
      difficulty: 'Advanced',
    },
    {
      icon: '🎮',
      title: 'Simulation with Isaac Sim',
      description: 'Build and test robots in photorealistic virtual environments',
      chapters: 2,
      difficulty: 'Intermediate',
    },
  ];

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'Beginner': return '#22c55e';
      case 'Intermediate': return '#f59e0b';
      case 'Advanced': return '#ef4444';
      default: return '#6366f1';
    }
  };

  return (
    <section className={styles.topicsSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Curriculum Preview</span>
          <h2 className={styles.sectionTitle}>
            What You'll Learn
          </h2>
          <p className={styles.sectionSubtitle}>
            A comprehensive curriculum designed by industry experts
          </p>
        </div>

        <div className={styles.topicsGrid}>
          {topics.map((topic, index) => (
            <div key={index} className={styles.topicCard}>
              <div className={styles.topicHeader}>
                <span className={styles.topicIcon}>{topic.icon}</span>
                <span 
                  className={styles.difficultyBadge}
                  style={{ background: `${getDifficultyColor(topic.difficulty)}20`, color: getDifficultyColor(topic.difficulty) }}
                >
                  {topic.difficulty}
                </span>
              </div>
              <h3 className={styles.topicTitle}>{topic.title}</h3>
              <p className={styles.topicDescription}>{topic.description}</p>
              <div className={styles.topicMeta}>
                <span className={styles.topicChapters}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                  </svg>
                  {topic.chapters} Chapters
                </span>
              </div>
            </div>
          ))}
        </div>

        <div className={styles.viewAllWrapper}>
          <Link
            className={clsx('button button--secondary button--lg', styles.viewAllButton)}
            to="/docs/intro">
            View Full Curriculum
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </Link>
        </div>
      </div>
    </section>
  );
}

function TestimonialsSection() {
  const testimonials = [
    {
      quote: "This textbook revolutionized my understanding of Physical AI. The hands-on approach with ROS 2 and simulation made complex concepts accessible.",
      author: "Alex Johnson",
      role: "Robotics Engineer",
      company: "Boston Dynamics"
    },
    {
      quote: "The integration of AI and robotics concepts is unparalleled. The VLA module alone is worth the entire course.",
      author: "Sarah Chen",
      role: "AI Researcher",
      company: "OpenAI"
    },
    {
      quote: "Finally, a resource that bridges the gap between theoretical AI and practical robotics implementation. Highly recommended for serious practitioners.",
      author: "Michael Rodriguez",
      role: "PhD Student",
      company: "MIT Robotics"
    }
  ];

  return (
    <section className={styles.testimonialsSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Testimonials</span>
          <h2 className={styles.sectionTitle}>
            Trusted by Professionals Worldwide
          </h2>
        </div>
        
        <div className={styles.testimonialsGrid}>
          {testimonials.map((testimonial, index) => (
            <div key={index} className={styles.testimonialCard}>
              <div className={styles.quoteIcon}>"</div>
              <p className={styles.testimonialQuote}>{testimonial.quote}</p>
              <div className={styles.testimonialAuthor}>
                <div className={styles.authorInfo}>
                  <div className={styles.authorName}>{testimonial.author}</div>
                  <div className={styles.authorRole}>{testimonial.role}</div>
                  <div className={styles.authorCompany}>{testimonial.company}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section className={styles.ctaSection}>
      <div className={styles.ctaContent}>
        <h2 className={styles.ctaTitle}>Ready to Start Your Journey?</h2>
        <p className={styles.ctaDescription}>
          Join thousands of learners mastering the future of robotics and AI
        </p>
        <Link
          className={clsx('button button--primary button--lg', styles.ctaButton)}
          to="/docs/intro">
          Get Started Free
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
            <path d="M5 12h14M12 5l7 7-7 7"/>
          </svg>
        </Link>
      </div>
    </section>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="An AI-Native textbook for Physical AI & Humanoid Robotics">
      <HomepageHeader />
      <main>
        <StatsSection />
        <FeaturesSection />
        <TopicsPreviewSection />
        <TestimonialsSection />
        <CTASection />
      </main>
    </Layout>
  );
}
