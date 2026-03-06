// frontend/src/pages/auth/signup.tsx
import React from 'react';
import SignupForm from '../../components/Auth/SignupForm';
import Layout from '@theme/Layout';

const SignupPage = () => {
  return (
    <Layout title="Sign Up" description="Create your account for the Physical AI & Humanoid Robotics textbook">
      <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
        <SignupForm />
      </div>
    </Layout>
  );
};

export default SignupPage;