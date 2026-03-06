// frontend/src/pages/auth/signin.tsx
import React from 'react';
import SigninForm from '../../components/Auth/SigninForm';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

const SigninPage = () => {
  const features = [
    { icon: '🎯', text: 'Personalized learning experience' },
    { icon: '📈', text: 'Track your progress' },
    { icon: '🏆', text: 'Earn bonus points' },
    { icon: '🤖', text: 'AI-powered assistance' },
  ];

  return (
    <Layout title="Sign In" description="Sign in to your account for the Physical AI & Humanoid Robotics textbook">
      <div className="auth-page-wrapper">
        <div className="auth-page-container">
          {/* Left Side - Form */}
          <div className="auth-form-section">
            <div className="auth-back-link">
              <Link to="/" className="back-link">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
                Back to home
              </Link>
            </div>
            <SigninForm />
          </div>

          {/* Right Side - Visual */}
          <div className="auth-visual-section">
            <div className="auth-visual-content">
              <div className="auth-visual-icon">🤖</div>
              <h1 className="auth-visual-title">Welcome Back!</h1>
              <p className="auth-visual-subtitle">
                Continue your journey to master Physical AI & Humanoid Robotics
              </p>
              <div className="auth-features-list">
                {features.map((feature, index) => (
                  <div key={index} className="auth-feature-item">
                    <span className="auth-feature-icon">{feature.icon}</span>
                    <span className="auth-feature-text">{feature.text}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default SigninPage;