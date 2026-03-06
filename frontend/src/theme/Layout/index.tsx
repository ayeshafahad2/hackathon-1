// frontend/src/theme/Layout/index.tsx
import React from 'react';
import OriginalLayout from '@theme-original/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';

type Props = {
  children?: React.ReactNode;
};

export default function Layout(props: Props) {
  return (
    <>
      <OriginalLayout {...props}>
        {props.children}
      </OriginalLayout>

      {/* Add any global auth-aware components here if needed */}
      <BrowserOnly>
        {() => null}
      </BrowserOnly>
    </>
  );
}