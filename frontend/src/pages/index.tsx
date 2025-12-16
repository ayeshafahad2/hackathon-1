import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles['hero-banner'])}>
      <div className="container">
        <div className={styles['hero-content']}>
          <div className={styles['hero-text']}>
            <Heading as="h1" className={styles['hero-title']}>
              {siteConfig.title}
            </Heading>
            <p className={styles['hero-subtitle']}>Your AI-Native Guide to the Future of Embodied Intelligence</p>
            <div className={styles['hero-buttons']}>
              <Link
                className="button button--primary button--lg"
                to="/docs/intro">
                Start Learning Now →
              </Link>
              <Link
                className="button button--secondary button--lg"
                to="/chat">
                Try AI Assistant
              </Link>
            </div>
          </div>
          <div className={styles['hero-image']}>
            <img
              src="https://loremflickr.com/600/400/robot,purple"
              alt="Humanoid Robot"
              className={styles['hero-img']}
            />
          </div>
        </div>
      </div>
    </header>
  );
}

function TestimonialsSection() {
  const testimonials = [
    {
      quote: "This textbook revolutionized my understanding of Physical AI. The hands-on approach with ROS 2 and simulation made complex concepts accessible.",
      author: "Alex Johnson",
      role: "Robotics Engineer"
    },
    {
      quote: "The integration of AI and robotics concepts is unparalleled. The VLA module alone is worth the entire course.",
      author: "Sarah Chen",
      role: "AI Researcher"
    },
    {
      quote: "Finally, a resource that bridges the gap between theoretical AI and practical robotics implementation. Highly recommended for serious practitioners.",
      author: "Michael Rodriguez",
      role: "PhD Student"
    }
  ];

  return (
    <section className={styles.testimonials}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>What Learners Are Saying</Heading>
        <div className="row">
          {testimonials.map((testimonial, index) => (
            <div className="col col--4" key={index}>
              <div className={styles.testimonialCard}>
                <div className={styles.quoteIcon}>❝</div>
                <p className={styles.testimonialText}>{testimonial.quote}</p>
                <div className={styles.testimonialAuthor}>
                  <strong>{testimonial.author}</strong>
                  <span className={styles.testimonialRole}>{testimonial.role}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function StatsSection() {
  return (
    <section className={styles.stats}>
      <div className="container">
        <div className="row">
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>13</div>
            <div className={styles.statLabel}>Weeks of Content</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>4</div>
            <div className={styles.statLabel}>Core Modules</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>20+</div>
            <div className={styles.statLabel}>Hands-on Projects</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>∞</div>
            <div className={styles.statLabel}>Embodied Intelligence</div>
          </div>
        </div>
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
        <HomepageFeatures />
        <StatsSection />
        <TestimonialsSection />
      </main>
    </Layout>
  );
}
