// frontend/src/components/Auth/AuthNavigation.tsx
import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { Link } from '@docusaurus/router';
import styles from './AuthNavigation.module.css';

const AuthNavigation: React.FC = () => {
  const { user, logout } = useAuth();

  return (
    <div className={styles.authNav}>
      {user ? (
        <div className={styles.loggedIn}>
          <span className={styles.welcome}>Welcome, {user.email.split('@')[0]}</span>
          <Link to="/user/profile" className={styles.profileLink}>Profile</Link>
          <button onClick={logout} className={styles.logoutButton}>Logout</button>
        </div>
      ) : (
        <div className={styles.loggedOut}>
          <Link to="/auth/signin" className={styles.signInLink}>Sign In</Link>
          <Link to="/auth/signup" className={styles.signUpLink}>Sign Up</Link>
        </div>
      )}
    </div>
  );
};

export default AuthNavigation;