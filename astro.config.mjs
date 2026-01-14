import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// For GitHub Pages at cnaasir459/neuroloop-website
//   Public URL: https://cnaasir459.github.io/neuroloop-website
//   Base path: /neuroloop-website
export default defineConfig({
  site: 'https://cnaasir459.github.io/neuroloop-website',
  base: '/neuroloop-website',
  integrations: [tailwind()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
