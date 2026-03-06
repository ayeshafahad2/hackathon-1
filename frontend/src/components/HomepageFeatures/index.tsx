import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Master the Core of Robotics',
    description: (
      <>
        Go beyond the basics and delve into the intricate mechanics of humanoid robots. Understand the principles of kinematics, dynamics, and control that underpin modern robotics and build a strong foundation for advanced applications.
      </>
    ),
  },
  {
    title: 'Unlock the Power of AI',
    description: (
      <>
        Explore the cutting-edge AI that drives intelligent behavior in robots. This textbook covers everything from machine learning and computer vision to natural language processing and reinforcement learning, equipping you with the skills to create truly smart robots.
      </>
    ),
  },
  {
    title: 'Create Real-World Solutions',
    description: (
      <>
        Put knowledge into practice with hands-on projects and real-world case studies. Learn how to design, build, and program humanoid robots to solve complex problems and make a tangible impact on the world.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4', styles.feature)}>
      <div className={styles.featureContent}>
        <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
        <p className={styles.featureDescription}>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.featuresHeader}>
          <Heading as="h2" className={styles.featuresTitle}>Why This Textbook?</Heading>
          <p className={styles.featuresSubtitle}>
            Your complete guide to mastering Physical AI & Humanoid Robotics
          </p>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
