import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: '📋 Introduction',
      collapsed: false,
      items: [
        'intro',
      ],
    },
    {
      type: 'category',
      label: '📚 Weekly Modules',
      collapsed: false,
      items: [
        'week-1',
        'week-2',
      ],
    },
    {
      type: 'category',
      label: '🎓 Capstone Project',
      collapsed: true,
      items: [
        'capstone',
      ],
    },
  ],
};

export default sidebars;
