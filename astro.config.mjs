import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// GitHub Pages project site: https://tomekdot.github.io/trackmania-galaxy/
// Hybrid: custom galaxy map gallery (src/pages) + Starlight docs (/docs/).
export default defineConfig({
  site: 'https://tomekdot.github.io',
  base: '/trackmania-galaxy',
  output: 'static',
  integrations: [
    starlight({
      title: 'Trackmania Galaxy',
      customCss: ['./src/styles/starlight.css'],
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/tomekdot/trackmania-galaxy' },
      ],
      sidebar: [
        { label: 'Wiki', items: [{ autogenerate: { directory: 'docs' } }] },
      ],
    }),
  ],
});
