import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.hero}>
      <div className={styles.heroBackground}>
        <div className={styles.gradientOrb1}></div>
        <div className={styles.gradientOrb2}></div>
      </div>
      
      <div className={styles.heroContent}>
        {/* Hero Image */}
        <div className={styles.heroImageWrapper}>
          <div className={styles.imageGlow}></div>
          <img 
            src="/img/hero-ai-robot.svg" 
            alt="AI Robot"
            className={styles.heroImage}
          />
        </div>

        {/* Title Section */}
        <div className={styles.heroText}>
          <div className={styles.heroBadge}>
            <span className={styles.badgeDot}></span>
            <span>AI-Native Textbook</span>
          </div>
          
          <Heading as="h1" className={styles.title}>
            {siteConfig.title}
          </Heading>
          
          <p className={styles.subtitle}>
            Your AI-Native Guide to the Future of Embodied Intelligence
          </p>
          
          <div className={styles.ctaButtons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro">
              Start Learning
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </Link>
            <Link
              className="button button--secondary button--lg"
              to="/features">
              Explore Features
            </Link>
          </div>

          <div className={styles.heroFooter}>
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
    </header>
  );
}

function FeaturesSection() {
  const features = [
    {
      title: 'Master the Core of Robotics',
      description: 'Go beyond the basics and delve into the intricate mechanics of humanoid robots. Understand the principles of kinematics, dynamics, and control that underpin modern robotics and build a strong foundation for advanced applications.',
      icon: '🦾',
    },
    {
      title: 'Unlock the Power of AI',
      description: 'Explore the cutting-edge AI that drives intelligent behavior in robots. This textbook covers everything from machine learning and computer vision to natural language processing and reinforcement learning, equipping you with the skills to create truly smart robots.',
      icon: '🧠',
    },
    {
      title: 'Create Real-World Solutions',
      description: 'Put knowledge into practice with hands-on projects and real-world case studies. Learn how to design, build, and program humanoid robots to solve complex problems and make a tangible impact on the world.',
      icon: '🚀',
    },
  ];

  return (
    <section className={styles.featuresSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Why This Textbook?</span>
          <Heading as="h2" className={styles.sectionTitle}>
            Everything You Need to Master Physical AI
          </Heading>
          <p className={styles.sectionSubtitle}>
            Your complete guide to mastering Physical AI & Humanoid Robotics
          </p>
        </div>

        <div className={styles.featuresGrid}>
          {features.map((feature, index) => (
            <div key={index} className={styles.featureCard}>
              <div className={styles.featureIconWrapper}>
                <span className={styles.featureIcon}>{feature.icon}</span>
              </div>
              <Heading as="h3" className={styles.featureTitle}>{feature.title}</Heading>
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
          <Heading as="h2" className={styles.sectionTitle}>
            Trusted by Professionals Worldwide
          </Heading>
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
        <Heading as="h2" className={styles.ctaTitle}>Ready to Start Your Journey?</Heading>
        <p className={styles.ctaDescription}>
          Join thousands of learners mastering the future of robotics and AI
        </p>
        <Link
          className="button button--primary button--lg"
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

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="An AI-Native textbook for teaching Physical AI & Humanoid Robotics.">
      <HomepageHeader />
      <main>
        <FeaturesSection />
        <TestimonialsSection />
        <CTASection />
      </main>
    </Layout>
  );
}
