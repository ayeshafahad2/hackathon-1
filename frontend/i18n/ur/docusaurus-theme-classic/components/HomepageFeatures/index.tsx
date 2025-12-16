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
    title: 'روبوٹکس کے مرکز میں مہارت حاصل کریں',
    Svg: () => <img src="https://loremflickr.com/320/240/robot,purple" alt="ایک جدید روبوٹ" />,
    description: (
      <>
        بنیادی باتوں سے آگے بڑھیں اور ہیومنائیڈ روبوٹس کی پیچیدہ میکانکس میں گہرائی میں جائیں۔ کائیمیٹکس، ڈائنامکس، اور کنٹرول کے اصولوں کو سمجھیں جو جدید روبوٹکس کی بنیاد ہیں اور جدید ایپلی کیشنز کے لیے ایک مضبوط بنیاد بنائیں۔
      </>
    ),
  },
  {
    title: 'AI کی طاقت کو غیر مقفل کریں',
    Svg: () => <img src="https://loremflickr.com/320/240/ai,purple" alt="ایک AI دماغ" />,
    description: (
      <>
        روبوٹس میں ذہین رویے کو چلانے والی جدید ترین AI کو دریافت کریں۔ یہ ٹیکسٹ بک مشین لرننگ اور کمپیوٹر وژن سے لے کر نیچرل لینگویج پروسیسنگ اور کمک سیکھنے تک سب کچھ شامل کرتی ہے، جو آپ کو حقیقی معنوں میں سمارٹ روبوٹ بنانے کی مہارتوں سے آراستہ کرتی ہے۔
      </>
    ),
  },
  {
    title: 'حقیقی دنیا کے حل بنائیں',
    Svg: () => <img src="https://loremflickr.com/320/240/humanoid,purple" alt="ایک ہیومنائیڈ روبوٹ دنیا کے ساتھ تعامل کر رہا ہے" />,
    description: (
      <>
        اپنے علم کو عملی جامہ پہنائیں اور حقیقی دنیا کے کیس اسٹڈیز کے ساتھ۔ پیچیدہ مسائل کو حل کرنے اور دنیا پر ٹھوس اثر ڈالنے کے لیے ہیومنائیڈ روبوٹس کو ڈیزائن، تعمیر اور پروگرام کرنا سیکھیں۔
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
