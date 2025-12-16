import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './features.module.css';

function FeatureSection({title, description, icon, link, color}: {title: string, description: string, icon: string, link?: string, color: string}) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureCardInner} style={{borderLeft: `5px solid ${color}`}}>
        <div className={styles.featureIcon}>{icon}</div>
        <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
        <p className={styles.featureDescription}>{description}</p>
        {link && (
          <Link to={link} className={styles.featureLink}>
            مزید جانیں →
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
      title={`خصوصیات | ${siteConfig.title}`}
      description="فزیکل اے آئی اور ہیومنائیڈ روبوٹکس ٹیکسٹ بک کی جامع خصوصیات کا جائزہ لیں">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <Heading as="h1" className="hero__title">
            جامع سیکھنے کی خصوصیات
          </Heading>
          <p className="hero__subtitle">
            وہ جدید ماڈیولز دریافت کریں جو ہماری فزیکل اے آئی اور ہیومنائیڈ روبوٹکس ٹیکسٹ بک کو نمایاں تعلیمی وسائل کا درجہ دیتے ہیں
          </p>
        </div>
      </header>
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <FeatureSection
                title="ROS 2 فنڈامینٹلز"
                description="ماڈرن روبوٹکس سسٹم کے تمام جزوؤں کو جوڑنے والے مڈل ویئر کو ماسٹر کریں۔ نوڈز، ٹاپکس، سروسز، اور ایکشنز کے بارے میں جانیں۔"
                icon="🔌"
                link="/docs/week-1"
                color="#FF4081"
              />
              <FeatureSection
                title="فزکس سیمولیشن"
                description="حقیقی فزکس سیمولیشنز تیار کرنے کے لیے گیزیبو اور یونٹی میں گہرائی سے جاؤ۔ ریجڈ باڈی ڈائنامکس، کولیشنز، اور ماحولیاتی تعاملات کو سمجھیں۔"
                icon="🎮"
                link="/docs/week-3"
                color="#2196F3"
              />
              <FeatureSection
                title="AI ادراک"
                description="ایڈوانسڈ ادراک سسٹم کے لیے NVIDIA Isaac کا استعمال کریں۔ انٹیلیجنٹ روبوٹ نیویگیشن کے لیے VSLAM، کمپیوٹر وژن، اور سینسر فیوژن سیکھیں۔"
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
                title="ویژن-لینگویج-ایکشن"
                description="LLMs اور روبوٹکس کی طاقت کو جوڑیں۔ VLA ماڈلز کا استعمال کرتے ہوئے قدرتی زبان کے حکم کو روبوٹ کے اعمال میں تبدیل کرنا سیکھیں۔"
                icon="🗣️"
                link="/docs/week-7"
                color="#FFC107"
              />
              <FeatureSection
                title="ہیومنائیڈ کنٹرول"
                description="ہیومنائیڈ روبوٹس کی میکانکات کو سمجھیں، بشمول کنیمیٹکس، ڈائنامکس، اور بائی پیڈل لوکوموشن کے لیے توازن کنٹرول۔"
                icon="🦾"
                link="/docs/week-9"
                color="#9C27B0"
              />
              <FeatureSection
                title="ریل ورلڈ ڈیپلومنٹ"
                description="سمولیشن اور حقیقت کے درمیان فاصلہ پُٹ کریں۔ ہارڈ ویئر کے احتیاط، سینسر انٹیگریشن، اور ایج کمپیوٹنگ کے بارے میں جانیں۔"
                icon="🏭"
                link="/docs/week-11"
                color="#795548"
              />
            </div>
          </div>
        </section>

        <section className={clsx(styles.resources, 'margin-vert--xl')}>
          <div className="container padding-horiz--md text--center">
            <Heading as="h2">اضافی سیکھنے کے وسائل</Heading>
            <p className="padding-horiz--md">
              ہمارے اضافی مواد اور کمیونٹی وسائل کے ساتھ اپنے سیکھنے کے تجربے کو بہتر بنائیں
            </p>
            <div className="row margin-vert--lg">
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/intro">
                  شروع کریں
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-1/intro-to-ros">
                  ROS 2 ٹیوٹوریلز
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-6/computer-vision">
                  کمپیوٹر وژن لیبز
                </Link>
              </div>
              <div className="col col--3">
                <Link className={styles.resourceLink} to="/docs/week-13/capstone">
                  کیپسٹون پروجیکٹ
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}