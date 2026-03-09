import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "Physical AI & Humanoid Robotics",
  tagline: "An AI-Native Textbook for the Future",
  favicon: "img/logo.svg",

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
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    function myPlugin() {
      return {
        name: 'auto-scroll-plugin',
        injectHtmlTags() {
          return {
            postBodyTags: [
              `<script>
              (function() {
                function autoScrollSidebar() {
                  const activeLink = document.querySelector('.theme-doc-sidebar-container .menu__link--active');
                  if (activeLink) {
                    const sidebar = document.querySelector('.theme-doc-sidebar-container .thin-scrollbar');
                    if (sidebar) {
                      setTimeout(() => {
                        sidebar.scrollTo({
                          top: activeLink.offsetTop - sidebar.offsetHeight / 2,
                          behavior: 'smooth'
                        });
                      }, 300);
                    }
                  }
                }
                function autoScrollTOC() {
                  const activeLink = document.querySelector('.table-of-contents .table-of-contents__link--active');
                  if (activeLink) {
                    const toc = document.querySelector('.table-of-contents');
                    if (toc) {
                      setTimeout(() => {
                        toc.scrollTo({
                          top: activeLink.offsetTop - toc.offsetHeight / 2,
                          behavior: 'smooth'
                        });
                      }, 300);
                    }
                  }
                }
                setTimeout(() => {
                  autoScrollSidebar();
                  autoScrollTOC();
                }, 500);
                let lastHref = location.href;
                setInterval(() => {
                  if (location.href !== lastHref) {
                    lastHref = location.href;
                    setTimeout(() => {
                      autoScrollSidebar();
                      autoScrollTOC();
                    }, 300);
                  }
                }, 500);
              })();
            </script>`,
            ],
          };
        },
      };
    },
    function backendUrlPlugin() {
      return {
        name: 'backend-url-plugin',
        injectHtmlTags() {
          const backendUrl = process.env.REACT_APP_BACKEND_URL || 'https://Ayeshaaabir-physical-ai-backend.hf.space';
          return {
            headTags: [
              `<script>
                window.BACKEND_URL = '${backendUrl}';
              </script>`,
            ],
          };
        },
      };
    },
  ],

  themeConfig: {
    image: "img/logo.svg",

    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },

    // Announcement bar
    announcementBar: {
      id: 'ai_chatbot',
      content: 'AI Chatbot available - Click the chat icon to ask questions!',
      isCloseable: true,
      backgroundColor: '#6366f1',
      textColor: '#ffffff',
    },

    // Metadata
    metadata: [
      { name: 'theme-color', content: '#6366f1' },
      { name: 'description', content: 'AI-Native Textbook for Physical AI & Humanoid Robotics' },
    ],

    // Navbar
    navbar: {
      title: "Physical AI & Humanoid Robotics",
      logo: {
        alt: "Physical AI & Humanoid Robotics Logo",
        src: "img/logo.svg",
        width: 48,
        height: 48,
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
          to: "/chat",
          label: "AI Chat",
          position: "left",
        },
        {
          type: 'search',
          position: 'right',
        },
        {
          to: "/auth/signin",
          label: "Sign In",
          position: "right",
        },
      ],
    },

    // Footer
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
            {
              label: "AI Assistant",
              to: "/chat",
            },
            {
              label: "Features",
              to: "/features",
            },
          ],
        },
        {
          title: "Resources",
          items: [
            {
              label: "Getting Started",
              to: "/docs/intro",
            },
            {
              label: "Week 1",
              to: "/docs/week-1",
            },
            {
              label: "Capstone",
              to: "/docs/capstone",
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
              label: "X / Twitter",
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
            {
              label: "Hackathon Project",
              href: "https://github.com/ayeshafahad2/hackathon-1",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. Built with modern web technologies.`,
    },

    // Prism
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },

    // Docs sidebar
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
  },
};

export default config;
