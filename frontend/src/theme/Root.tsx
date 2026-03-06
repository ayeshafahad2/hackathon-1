import React from 'react';
import { AuthProvider } from '../contexts/AuthContext';
import { ChatProvider } from '../contexts/ChatContext';
import BrowserOnly from '@docusaurus/BrowserOnly';
import SimpleFloatingButton from '../components/SimpleFloatingButton';
import AutoScrollControl from '@site/src/components/AutoScrollControl';

export default function Root({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      <ChatProvider>
        {children}
        <BrowserOnly>
          {() => <SimpleFloatingButton />}
        </BrowserOnly>
        <BrowserOnly>
          {() => <AutoScrollControl />}
        </BrowserOnly>
      </ChatProvider>
    </AuthProvider>
  );
}