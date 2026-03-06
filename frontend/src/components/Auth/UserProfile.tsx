// frontend/src/components/Auth/UserProfile.tsx
import React, { useState, useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { Link } from '@docusaurus/router';
import styles from './Auth.module.css';

const UserProfile: React.FC = () => {
  const { user, loading, updateUserProfile } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    software_experience: '',
    hardware_experience: '',
    programming_languages: [] as string[],
    field_of_interest: '',
    educational_affiliation: ''
  });
  
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (user) {
      setEditData({
        software_experience: user.softwareExperience,
        hardware_experience: user.hardwareExperience,
        programming_languages: user.programmingLanguages,
        field_of_interest: user.fieldOfInterest,
        educational_affiliation: user.educationalAffiliation
      });
    }
  }, [user]);

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleCancelEdit = () => {
    if (user) {
      setEditData({
        software_experience: user.softwareExperience,
        hardware_experience: user.hardwareExperience,
        programming_languages: user.programmingLanguages,
        field_of_interest: user.fieldOfInterest,
        educational_affiliation: user.educationalAffiliation
      });
    }
    setIsEditing(false);
    setMessage('');
  };

  const handleSave = async () => {
    try {
      await updateUserProfile(editData);
      setIsEditing(false);
      setMessage('Profile updated successfully!');
      setTimeout(() => setMessage(''), 3000);
    } catch (error: any) {
      setMessage(`Error updating profile: ${error.message}`);
    }
  };

  if (loading) {
    return <div className={styles.authContainer}>Loading profile...</div>;
  }

  if (!user) {
    return (
      <div className={styles.authContainer}>
        <p>Please <a href="/signin">sign in</a> to view your profile.</p>
      </div>
    );
  }

  return (
    <div className={styles.authContainer}>
      <h2>User Profile</h2>
      
      {message && <div className={styles.message}>{message}</div>}
      
      <div className={styles.profileSection}>
        <h3>Account Information</h3>
        <p><strong>Email:</strong> {user.email}</p>
      </div>
      
      <div className={styles.profileSection}>
        <h3>Background Information</h3>
        
        {isEditing ? (
          <div className={styles.formSection}>
            <div className={styles.formGroup}>
              <label>Software Experience</label>
              <select
                value={editData.software_experience}
                onChange={(e) => setEditData({...editData, software_experience: e.target.value})}
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="expert">Expert</option>
              </select>
            </div>
            
            <div className={styles.formGroup}>
              <label>Hardware Experience</label>
              <select
                value={editData.hardware_experience}
                onChange={(e) => setEditData({...editData, hardware_experience: e.target.value})}
              >
                <option value="none">No Experience</option>
                <option value="basic">Basic</option>
                <option value="advanced">Advanced</option>
                <option value="professional">Professional</option>
              </select>
            </div>
            
            <div className={styles.formGroup}>
              <label>Field of Interest</label>
              <select
                value={editData.field_of_interest}
                onChange={(e) => setEditData({...editData, field_of_interest: e.target.value})}
              >
                <option value="">Select an area</option>
                <option value="robotics">Robotics</option>
                <option value="ai">Artificial Intelligence</option>
                <option value="control_systems">Control Systems</option>
                <option value="embedded_systems">Embedded Systems</option>
                <option value="computer_vision">Computer Vision</option>
                <option value="machine_learning">Machine Learning</option>
                <option value="other">Other</option>
              </select>
            </div>
            
            <div className={styles.formGroup}>
              <label>Educational/Institutional Affiliation</label>
              <input
                type="text"
                value={editData.educational_affiliation}
                onChange={(e) => setEditData({...editData, educational_affiliation: e.target.value})}
              />
            </div>
          </div>
        ) : (
          <div>
            <p><strong>Software Experience:</strong> {user.softwareExperience}</p>
            <p><strong>Hardware Experience:</strong> {user.hardwareExperience}</p>
            <p><strong>Programming Languages:</strong> {user.programmingLanguages.join(', ') || 'None specified'}</p>
            <p><strong>Field of Interest:</strong> {user.fieldOfInterest || 'Not specified'}</p>
            <p><strong>Educational Affiliation:</strong> {user.educationalAffiliation || 'Not specified'}</p>
          </div>
        )}
      </div>
      
      <div className={styles.profileSection}>
        <h3>Bonus Points</h3>
        <p><strong>Total Bonus Points Earned:</strong> {user.bonusPoints}</p>
        <ul>
          <li>50 points for personalizing chapter content</li>
          <li>50 points for translating content to Urdu</li>
        </ul>
        <p><strong>Personalization Enabled:</strong> {user.personalizationEnabled ? 'Yes' : 'No'}</p>
      </div>
      
      <div className={styles.buttonGroup}>
        {isEditing ? (
          <>
            <button className={styles.submitButton} onClick={handleSave}>
              Save Changes
            </button>
            <button 
              className={`${styles.submitButton} ${styles.secondaryButton}`} 
              onClick={handleCancelEdit}
            >
              Cancel
            </button>
          </>
        ) : (
          <button className={styles.submitButton} onClick={handleEditClick}>
            Edit Profile
          </button>
        )}
      </div>
    </div>
  );
};

export default UserProfile;