// frontend/src/components/Auth/SignupForm.tsx
import React, { useState } from 'react';
import { navigate } from '@docusaurus/router';
import styles from './Auth.module.css';

interface FormData {
  email: string;
  password: string;
  confirmPassword: string;
  softwareExperience: string;
  hardwareExperience: string;
  fieldOfInterest: string;
  educationalAffiliation: string;
}

const SignupForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    email: '',
    password: '',
    confirmPassword: '',
    softwareExperience: 'beginner',
    hardwareExperience: 'none',
    fieldOfInterest: '',
    educationalAffiliation: ''
  });

  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const programmingLanguageOptions = [
    'Python', 'C++', 'MATLAB', 'Java', 'JavaScript', 'C#', 'Rust', 'Go', 'Other'
  ];
  const [selectedLanguages, setSelectedLanguages] = useState<string[]>([]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleLanguageChange = (language: string) => {
    setSelectedLanguages(prev =>
      prev.includes(language)
        ? prev.filter(lang => lang !== language)
        : [...prev, language]
    );
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      // Using Better Auth's register endpoint
      const response = await fetch('/api/auth/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
          profile: {
            softwareExperience: formData.softwareExperience,
            hardwareExperience: formData.hardwareExperience,
            programmingLanguages: selectedLanguages,
            fieldOfInterest: formData.fieldOfInterest,
            educationalAffiliation: formData.educationalAffiliation
          }
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error?.message || 'Registration failed');
      }

      // Redirect to dashboard after successful registration
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.message || 'An error occurred during registration');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.authContainer}>
      <h2>Create Your Account</h2>
      <p className={styles.subtitle}>Tell us about your background to personalize your learning experience</p>

      {error && <div className={styles.error}>{error}</div>}

      <form onSubmit={handleSubmit} className={styles.authForm}>
        <div className={styles.formGroup}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            required
            placeholder="Enter your email"
            disabled={loading}
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
            required
            placeholder="Create a password"
            disabled={loading}
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="confirmPassword">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleInputChange}
            required
            placeholder="Confirm your password"
            disabled={loading}
          />
        </div>

        <div className={styles.formSection}>
          <h3>Software Background</h3>

          <div className={styles.formGroup}>
            <label htmlFor="softwareExperience">Experience Level</label>
            <select
              id="softwareExperience"
              name="softwareExperience"
              value={formData.softwareExperience}
              onChange={handleInputChange}
              disabled={loading}
            >
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="expert">Expert</option>
            </select>
          </div>
        </div>

        <div className={styles.formSection}>
          <h3>Hardware Experience</h3>

          <div className={styles.formGroup}>
            <label htmlFor="hardwareExperience">Experience Level</label>
            <select
              id="hardwareExperience"
              name="hardwareExperience"
              value={formData.hardwareExperience}
              onChange={handleInputChange}
              disabled={loading}
            >
              <option value="none">No Experience</option>
              <option value="basic">Basic</option>
              <option value="advanced">Advanced</option>
              <option value="professional">Professional</option>
            </select>
          </div>
        </div>

        <div className={styles.formSection}>
          <h3>Programming Languages</h3>
          <p>Select all that apply:</p>

          <div className={styles.checkboxGroup}>
            {programmingLanguageOptions.map((language) => (
              <label key={language} className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  checked={selectedLanguages.includes(language)}
                  onChange={() => handleLanguageChange(language)}
                  disabled={loading}
                />
                {language}
              </label>
            ))}
          </div>
        </div>

        <div className={styles.formSection}>
          <h3>Field of Interest</h3>

          <div className={styles.formGroup}>
            <label htmlFor="fieldOfInterest">What area are you most interested in?</label>
            <select
              id="fieldOfInterest"
              name="fieldOfInterest"
              value={formData.fieldOfInterest}
              onChange={handleInputChange}
              disabled={loading}
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
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="educationalAffiliation">Educational/Institutional Affiliation (Optional)</label>
          <input
            type="text"
            id="educationalAffiliation"
            name="educationalAffiliation"
            value={formData.educationalAffiliation}
            onChange={handleInputChange}
            placeholder="University, company, etc."
            disabled={loading}
          />
        </div>

        <button type="submit" className={styles.submitButton} disabled={loading}>
          {loading ? (
            <>
              <span className={styles.loadingSpinner}></span>
              Creating Account...
            </>
          ) : (
            'Sign Up & Personalize'
          )}
        </button>
      </form>

      <div className={styles.formFooter}>
        <p>
          Already have an account? <a href="/auth/signin" className={styles.authLink}>Sign in here</a>
        </p>
      </div>
    </div>
  );
};

export default SignupForm;