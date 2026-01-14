#!/bin/bash
# Deploy script - run this in your terminal

echo "🚀 Deploying NeuroLoop Website to GitHub Pages..."
echo ""

# Check if git is configured
if ! git config user.email > /dev/null 2>&1; then
    echo "Configuring git..."
    git config user.email "cnaasir459@github.com"
    git config user.name "Cnaasir459"
fi

# Add remote with token
echo "Adding remote..."
git remote set-url origin https://Cnaasir459:$GITHUB_TOKEN@github.com/Cnaasir459/neuroloop-website.git 2>/dev/null || true

# Push
echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Code pushed! Now enable GitHub Pages:"
echo "1. Go to: https://github.com/Cnaasir459/neuroloop-website/settings/pages"
echo "2. Select 'GitHub Actions' under Build and deployment"
echo "3. Wait 1-2 minutes for deployment"
echo ""
echo "🌐 Your site: https://cnaasir459.github.io/neuroloop-website/"
