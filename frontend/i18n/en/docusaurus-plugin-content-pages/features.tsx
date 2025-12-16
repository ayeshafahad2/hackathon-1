import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from '@site/src/pages/features.module.css';

function FeatureSection({title, description, icon, link, color}: {title: string, description: string, icon: string, link?: string, color: string}) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureCardInner} style={{borderLeft: `5px solid ${color}`}}>
        <div className={styles.featureIcon}>{icon}</div>
        <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
        <p className={styles.featureDescription}>{description}</p>
        {link && (
          <Link to={link} className={styles.featureLink}>
            Learn More →
          </Link>
        )}
      </div>
    </div>
  );
}

export default function FeaturesPage(): React.ReactElement {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Features | ${siteConfig.title}`}
      description="Explore the comprehensive features of our Physical AI & Humanoid Robotics textbook">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <Heading as="h1" className="hero__title">
            Comprehensive Learning Features
          </Heading>
          <p className="hero__subtitle">
            Discover the cutting-edge modules that make our Physical AI & Humanoid Robotics textbook the premier educational resource
          </p>
        </div>
      </header>
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <FeatureSection
                title="ROS 2 Fundamentals"
                description="Master the Robot Operating System 2, the middleware that connects all components of modern robotics systems. Learn about nodes, topics, services, and actions."
                icon="🔌"
                link="/docs/week-1"
                color="#FF4081"
              />
              <FeatureSection
                title="Physics Simulation"
                description="Dive deep into Gazebo and Unity for creating realistic physics simulations. Understand rigid body dynamics, collisions, and environmental interactions."
                icon="🎮"
                link="/docs/week-3"
                color="#2196F3"
              />
              <FeatureSection
                title="AI Perception"
                description="Explore NVIDIA Isaac for advanced perception systems. Learn VSLAM, computer vision, and sensor fusion for intelligent robot navigation."
                icon="👁️"
                link="/docs/week-5"
                color="#4CAF50"
              />
            </div>
          </div>
        </section>

        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <FeatureSection
                title="Vision-Language-Action"
                description="Combine the power of LLMs with robotics. Learn how to translate natural language commands into robot actions using VLA models."
                icon="🗣️"
                link="/docs/week-7"
                color="#FFC107"
              />
              <FeatureSection
                title="Humanoid Control"
                description="Understand the mechanics of humanoid robots, including kinematics, dynamics, and balance control for bipedal locomotion."
                icon="🦾"
                link="/docs/week-9"
                color="#9C27B0"
              />
              <FeatureSection
                title="Real-World Deployment"
                description="Bridge the gap between simulation and reality. Learn about hardware constraints, sensor integration, and edge computing."
                icon="🏭"
                link="/docs/week-11"
                color="#795548"
              />
            </div>
          </div>
        </section>

        <section className={clsx(styles.resources, 'margin-vert--xl')}>
          <div className="container padding-horiz--md text--center">
            <Heading as="h2">Additional Learning Resources</Heading>
            <p className="padding-horiz--md">
              Enhance your learning experience with our supplementary materials and community resources
            </p>
            <div className="row margin-vert--lg">
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/intro">
                  Getting Started
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-1/intro-to-ros">
                  ROS 2 Tutorials
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-6/computer-vision">
                  Computer Vision Labs
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-13/capstone">
                  Capstone Project
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}