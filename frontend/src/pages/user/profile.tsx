// frontend/src/pages/user/profile.tsx
import React from 'react';
import UserProfile from '../../components/Auth/UserProfile';
import Layout from '@theme/Layout';

const ProfilePage = () => {
  return (
    <Layout title="User Profile" description="Manage your profile and background information">
      <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
        <UserProfile />
      </div>
    </Layout>
  );
};

export default ProfilePage;