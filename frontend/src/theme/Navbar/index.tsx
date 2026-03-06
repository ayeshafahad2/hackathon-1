// frontend/src/theme/Navbar/index.tsx
import React from 'react';
import OriginalNavbar from '@theme-original/Navbar';
import NavbarLogo from '@site/src/components/NavbarLogo';

export default function Navbar(props) {
  return (
    <OriginalNavbar {...props} />
  );
}