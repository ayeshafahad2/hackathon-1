import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";

const config: Config = {
  title: "Physical AI & Humanoid Robotics",
  tagline: "An AI-Native Textbook",
  favicon: "img/logo.ico",

  future: {
    v4: true,
  },

  url: "https://ayesha-docasaurus-project-1.vercel.app",
  baseUrl: "/",

  organizationName: "ayeshafahad2",
  projectName: "specbook",

  onBrokenLinks: "warn",
i18n: {
  defaultLocale: "en",
  locales: ["en", "ur"],
  localeConfigs: {
    en: { label: "English", direction: "ltr" },
    ur: { label: "اردو", direction: "rtl" },
  },
},


  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.ts"),
          editUrl: "https://github.com/ayeshafahad2/hackathon-1/tree/main/",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],

  themeConfig: {
    image: "img/logo.ico",

    colorMode: {
      respectPrefersColorScheme: true,
    },

    // Add the layout wrapper to include the chat widget globally
    announcementBar: {
      id: 'chat_widget_announcement',
      content: 'AI Chatbot available on all pages - click the chat icon in the bottom-right to ask questions about the textbook!',
      isCloseable: false,
    },

    // Enable theme-direction support for RTL languages
    metadata: [
      { name: 'theme-color', content: '#a855f7' },
    ],

    navbar: {
      title: "Physical AI & Humanoid Robotics",
      logo: {
        alt: "Physical AI & Humanoid Robotics Logo",
        src: "img/logo.ico",
        width: 32,
        height: 32,
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Textbook",
        },
        {
          to: "/features",
          label: "Features",
          position: "left",
        },
        {
          type: "localeDropdown",
          position: "right",
        },
        {
          type: 'search',
          position: 'right',
        },
        {
          href: "https://github.com/ayeshafahad2/specbook",
          label: "GitHub",
          position: "right",
        },
      ],
    },

    footer: {
      style: "dark",
      links: [
        {
          title: "Learning",
          items: [
            {
              label: "Textbook",
              to: "/docs/intro",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Discord",
              href: "https://discordapp.com/invite/docusaurus",
            },
            {
              label: "X",
              href: "https://x.com/docusaurus",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/ayeshafahad2/specbook",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Ayesha. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      // darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
