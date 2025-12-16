import React from 'react';
import { ChatProvider } from '../contexts/ChatContext';

export default function Root({ children }: { children: React.ReactNode }) {
  return <ChatProvider>{children}</ChatProvider>;
}