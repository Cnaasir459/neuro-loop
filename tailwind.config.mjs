/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: '#FF0000',
        dark: '#0f0f0f',
        darker: '#0a0a0a',
        card: '#1a1a1a',
        text: '#f1f1f1',
        muted: '#aaaaaa',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
