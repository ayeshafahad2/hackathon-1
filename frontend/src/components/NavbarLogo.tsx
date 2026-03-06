import React from 'react';

const NavbarLogo = ({ style }) => (
  <svg
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    style={style}
  >
    {/* Robot head */}
    <rect x="8" y="4" width="8" height="8" rx="2" fill="currentColor" />

    {/* Robot eyes */}
    <circle cx="10" cy="7" r="1" fill="white" />
    <circle cx="14" cy="7" r="1" fill="white" />

    {/* Robot body */}
    <rect x="9" y="12" width="6" height="6" rx="1" fill="currentColor" />

    {/* Circuit lines */}
    <path d="M6 10 L7 10" stroke="white" strokeWidth="0.5" />
    <path d="M17 10 L18 10" stroke="white" strokeWidth="0.5" />
    <path d="M10 16 L11 16" stroke="white" strokeWidth="0.5" />
    <path d="M13 16 L14 16" stroke="white" strokeWidth="0.5" />

    {/* AI neural network dots */}
    <circle cx="4" cy="6" r="1" fill="currentColor" />
    <circle cx="5" cy="8" r="0.8" fill="currentColor" />
    <circle cx="3" cy="9" r="0.8" fill="currentColor" />
    <circle cx="20" cy="6" r="1" fill="currentColor" />
    <circle cx="19" cy="8" r="0.8" fill="currentColor" />
    <circle cx="21" cy="9" r="0.8" fill="currentColor" />
  </svg>
);

export default NavbarLogo;