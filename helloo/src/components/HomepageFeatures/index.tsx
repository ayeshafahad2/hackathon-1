import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Master the Core of Robotics',
    Svg: () => <img src="https://loremflickr.com/320/240/robot,purple" alt="A sophisticated robot" />,
    description: (
      <>
        Go beyond the basics and delve into the intricate mechanics of humanoid robots. Understand the principles of kinematics, dynamics, and control that underpin modern robotics and build a strong foundation for advanced applications.
      </>
    ),
  },
  {
    title: 'Unlock the Power of AI',
    Svg: () => <img src="https://loremflickr.com/320/240/ai,purple" alt="An AI brain" />,
    description: (
      <>
        Explore the cutting-edge AI that drives intelligent behavior in robots. This textbook covers everything from machine learning and computer vision to natural language processing and reinforcement learning, equipping you with the skills to create truly smart robots.
      </>
    ),
  },
  {
    title: 'Create Real-World Solutions',
    Svg: () => <img src="https://loremflickr.com/320/240/humanoid,purple" alt="A humanoid robot interacting with the world" />,
    description: (
      <>
        Put your knowledge into practice with hands-on projects and real-world case studies. Learn how to design, build, and program humanoid robots to solve complex problems and make a tangible impact on the world.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4', styles.feature)}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3" className={styles['feature-title']}>{title}</Heading>
        <p className={styles['feature-description']}>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
