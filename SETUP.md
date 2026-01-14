#!/bin/bash

echo "🚀 NeuroLoop Website Setup Script"
echo "=================================="

echo ""
echo "Step 1: Creating GitHub repository..."
echo "1. Go to: https://github.com/new"
echo "2. Repository name: neuroloop-website"
echo "3. Make it Public"
echo "4. Don't initialize with README (we already have one)"
echo "5. Click 'Create repository'"
echo ""

read -p "Press Enter after creating the repository..."

echo ""
echo "Step 2: Pushing code to GitHub..."
echo "Run these commands:"
echo ""
echo "cd /home/abdi/my-own-website/neuroloop-website"
echo "git remote set-url origin https://github.com/Cnaasir459/neuroloop-website.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "You'll need to enter your GitHub credentials when prompted."
echo ""

echo "Step 3: Enabling GitHub Pages..."
echo "1. Go to: https://github.com/Cnaasir459/neuroloop-website/settings/pages"
echo "2. Under 'Build and deployment', select 'GitHub Actions'"
echo "3. Click Save"
echo ""

echo "Step 4: Your site will be live at:"
echo "https://cnaasir459.github.io/neuroloop-website/"
echo ""

echo "🎉 Setup complete!"
