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
            <p className={styles['hero-subtitle']}>مجسم ذہانت کے مستقبل کے لیے آپ کا AI-مقامی گائیڈ</p>
            <div className={styles['hero-buttons']}>
              <Link
                className="button button--primary button--lg"
                to="/docs/intro">
                ابھی سیکھنا شروع کریں →
              </Link>
              <Link
                className="button button--secondary button--lg"
                to="/features">
                خصوصیات دیکھیں
              </Link>
            </div>
          </div>
          <div className={styles['hero-image']}>
            <img
              src="https://loremflickr.com/600/400/robot,purple"
              alt="ہیومنائیڈ روبوٹ"
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
      quote: "یہ ٹیکسٹ بک نے فزیکل اے آئی کی میری تفہیم کو انقلابی انداز میں بدل دیا۔ ROS 2 اور سیمولیشن کے ساتھ عملی نقطہ نظر نے پیچیدہ تصورات کو قابل رسائی بنا دیا۔",
      author: "علی جانسن",
      role: "روبوٹکس انجینئر"
    },
    {
      quote: "AI اور روبوٹکس کے تصورات کا اندراج بے مثال ہے۔ VLA ماڈل صرف پورے کورس کے قابل ہے۔",
      author: "سارة چین",
      role: "AI ریسرچر"
    },
    {
      quote: "بالآخر، ایک ایسے وسیلے کے لیے جو نظریاتی AI اور عملی روبوٹکس کے نفاذ کے درمیان پُل کو پار کرتا ہے۔ سنجیدہ عمل پسندوں کے لیے بے حد تجویز کردہ۔",
      author: "مائیکل روڈریگز",
      role: "پی ایچ ڈی طالب علم"
    }
  ];

  return (
    <section className={styles.testimonials}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>سیکھنے والوں کا کیا کہنا ہے</Heading>
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
            <div className={styles.statLabel}>ہفتوں کا مواد</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>4</div>
            <div className={styles.statLabel}>مرکزی ماڈیولز</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>20+</div>
            <div className={styles.statLabel}>عملی پروجیکٹس</div>
          </div>
          <div className="col col--3 text--center">
            <div className={styles.statNumber}>∞</div>
            <div className={styles.statLabel}>مجسم ذہانت</div>
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
      title={`خوش آمدید ${siteConfig.title}`}
      description="فزیکل اے آئی اور ہیومنائیڈ روبوٹکس سکھانے کے لیے ایک AI-مقامی ٹیکسٹ بک۔">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <StatsSection />
        <TestimonialsSection />
      </main>
    </Layout>
  );
}
