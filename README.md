# NeuroLoop Website

Official website for the NeuroLoop YouTube channel (@neuroloop98). Built with [Astro](https://astro.build) and deployed on GitHub Pages.

## Features

- 📹 YouTube video embeds
- 📝 Detailed show notes for each video
- 🔍 Full-text search
- 🎨 Dark mode design
- ⚡ Fast performance with static generation
- 📱 Fully responsive

## Tech Stack

- **Framework**: [Astro](https://astro.build)
- **Styling**: [Tailwind CSS](https://tailwindcss.com)
- **Search**: [Pagefind](https://pagefind.app)
- **Hosting**: GitHub Pages
- **Content**: Markdown with frontmatter

## Getting Started

### Prerequisites

- Node.js 18+
- npm or pnpm

### Installation

```bash
# Clone the repository
git clone https://github.com/Cnaasir459/neuroloop-website.git
cd neuroloop-website

# Install dependencies
npm install

# Start development server
npm run dev
```

### Build for Production

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Adding New Videos

1. Create a new Markdown file in `src/content/videos/`
2. Add the required frontmatter:

```markdown
---
title: "Your Video Title"
pubDate: 2025-01-14
description: "Brief description of the video"
youtubeId: "your-youtube-video-id"
tags: ["Tag1", "Tag2"]
duration: "MM:SS"
---

Write your show notes here using Markdown...

## Section Heading

Your content...
```

3. Commit and push to GitHub
4. The site will auto-deploy

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## License

MIT
