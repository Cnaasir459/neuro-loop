# 🚀 NeuroLoop Website - Deployment Guide

## Step 1: Create GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "neuroloop-deploy"
4. Select scopes:
   - [x] repo (full control of private/public repositories)
   - [x] workflow (update GitHub Actions workflows)
5. Click "Generate token"
6. **Copy your token** (starts with `ghp_...`)

## Step 2: Run Deployment

Run these commands in your terminal:

```bash
# Set your token
export GITHUB_TOKEN=ghp_your_token_here

# Go to project folder
cd /home/abdi/my-own-website/neuroloop-website

# Run deploy script
python3 deploy_api.py
```

## Step 3: Access Your Website

After deployment completes:
- **URL**: https://cnaasir459.github.io/neuroloop-website/
- **Wait**: 1-2 minutes for initial deployment

## Step 4: Add New Videos

To add a new video, create a file in `src/content/videos/` with this format:

```markdown
---
title: "Your Video Title"
pubDate: 2025-01-14
description: "Brief description"
youtubeId: "VIDEO_ID_HERE"
tags: ["AI", "Tech"]
duration: "MM:SS"
---

Write your show notes here...
```

Then deploy with:
```bash
export GITHUB_TOKEN=ghp_your_token_here
python3 deploy_api.py
```

## Troubleshooting

**"Repository not found"** - The script will create it automatically

**"Pages not enabled"** - Manually enable at:
https://github.com/Cnaasir459/neuroloop-website/settings/pages
→ Select "GitHub Actions" → Save

**Site shows 404** - Wait 2-3 minutes, then refresh

## What Gets Deployed

✅ Homepage with video grid
✅ Video detail pages with YouTube embed
✅ About page
✅ Search functionality
✅ Dark theme styling
✅ Auto-deployment on every push

---
🎉 Your NeuroLoop website is ready!
