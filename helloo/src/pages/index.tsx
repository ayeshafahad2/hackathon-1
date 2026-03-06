import type { ReactNode } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";
import Heading from "@theme/Heading";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroContent}>
          
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>

          <p className={styles.heroSubtitle}>
            Your AI-Native Guide to the Future of 
            <span className={styles.highlight}> Embodied Intelligence</span>
          </p>

          <p className={styles.heroDescription}>
            A modern textbook designed for developers, researchers, and students
            to master the foundations of Physical AI, humanoid robotics, and the
            next generation of intelligent machines.
          </p>

          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro"
            >
              Start Learning
            </Link>

            <Link
              className="button button--outline button--lg"
              to="/docs/intro"
            >
              Explore Documentation
            </Link>
          </div>

        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="An AI-Native textbook for teaching Physical AI & Humanoid Robotics."
    >
      <HomepageHeader />

      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}