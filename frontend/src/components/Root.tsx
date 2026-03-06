import React from 'react';
import { ChatProvider } from '../contexts/ChatContext';
import { AuthProvider } from '../contexts/AuthContext';

export default function Root({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      <ChatProvider>{children}</ChatProvider>
    </AuthProvider>
  );
}
