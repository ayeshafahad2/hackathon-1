import React, { useEffect } from 'react';
import { useIsBrowser } from '@docusaurus/router';

const ClientChatWidget: React.FC = () => {
  const isBrowser = useIsBrowser();

  useEffect(() => {
    if (!isBrowser) return;

    const ChatWidget = require('./Chat/ChatWidget').default;
    if (typeof window !== 'undefined' && window.document) {
      // Create a container for the chat widget
      let container = document.getElementById('chat-widget-container');
      if (!container) {
        container = document.createElement('div');
        container.id = 'chat-widget-container';
        document.body.appendChild(container);
      }

      // Render the chat widget using React DOM
      const React = require('react');
      const ReactDOM = require('react-dom/client');
      
      const root = ReactDOM.createRoot(container);
      root.render(<ChatWidget position="bottom-right" defaultOpen={false} />);
      
      return () => {
        // Cleanup - unmount the component when the component unmounts
        root.unmount();
      };
    }
  }, [isBrowser]);

  // This component doesn't render anything itself,
  // the actual chat widget is rendered in a portal-like fashion
  return null;
};

export default ClientChatWidget;