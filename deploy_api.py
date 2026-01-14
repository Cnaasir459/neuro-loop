#!/usr/bin/env python3
"""
GitHub Deploy Script for NeuroLoop Website
"""
import os
import requests
import base64
import sys

GITHUB_USER = "Cnaasir459"
REPO_NAME = "neuroloop-website"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def create_repo():
    """Create GitHub repository"""
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"name": REPO_NAME, "description": "NeuroLoop - Tech & AI Content", "private": False}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Repository '{REPO_NAME}' created!")
        return True
    elif response.status_code == 422:
        print(f"ℹ️  Repository '{REPO_NAME}' already exists")
        return True
    else:
        print(f"❌ Failed to create repo: {response.text}")
        return False

def upload_file(filepath, content):
    """Upload file to GitHub"""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{filepath}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"message": f"Add {filepath}", "content": base64.b64encode(content).decode()}
    
    response = requests.put(url, headers=headers, json=data)
    return response.status_code in [200, 201]

def deploy():
    """Deploy website to GitHub"""
    if not TOKEN:
        print("❌ Error: Set GITHUB_TOKEN environment variable")
        print("   Run: export GITHUB_TOKEN=your_token_here")
        return False
    
    if not create_repo():
        return False
    
    print("📤 Uploading files...")
    base_path = "/home/abdi/my-own-website/neuroloop-website"
    
    files_to_upload = [
        ("README.md", "README.md"),
        (".gitignore", ".gitignore"),
        ("package.json", "package.json"),
        ("astro.config.mjs", "astro.config.mjs"),
        ("tailwind.config.mjs", "tailwind.config.mjs"),
        ("tsconfig.json", "tsconfig.json"),
        (".github/workflows/deploy.yml", ".github/workflows/deploy.yml"),
        ("src/layouts/BaseLayout.astro", "src/layouts/BaseLayout.astro"),
        ("src/pages/index.astro", "src/pages/index.astro"),
        ("src/pages/about.astro", "src/pages/about.astro"),
        ("src/pages/videos/[slug].astro", "src/pages/videos/[slug].astro"),
        ("src/components/Header.astro", "src/components/Header.astro"),
        ("src/components/YouTubeEmbed.astro", "src/components/YouTubeEmbed.astro"),
        ("src/components/VideoCard.astro", "src/components/VideoCard.astro"),
        ("src/components/Search.astro", "src/components/Search.astro"),
        ("src/content/config.ts", "src/content/config.ts"),
        ("src/content/videos/ai-neurostimulation.md", "src/content/videos/ai-neurostimulation.md"),
        ("public/favicon.svg", "public/favicon.svg"),
        ("public/robots.txt", "public/robots.txt"),
    ]
    
    success_count = 0
    for local_path, repo_path in files_to_upload:
        try:
            with open(os.path.join(base_path, local_path), "rb") as f:
                content = f.read()
            if upload_file(repo_path, content):
                print(f"   ✅ {repo_path}")
                success_count += 1
        except Exception as e:
            print(f"   ❌ {repo_path}: {e}")
    
    print(f"\n📤 Uploaded {success_count}/{len(files_to_upload)} files")
    
    # Enable GitHub Pages
    print("\n🔧 Enabling GitHub Pages...")
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/pages"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json", "Content-Length": "0"}
    
    # Try to enable pages via source
    data = {"source": {"branch": "main", "path": "/"}}
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print("✅ GitHub Pages enabled!")
    elif response.status_code == 409:
        print("ℹ️  GitHub Pages already configured")
    else:
        print(f"ℹ️  Pages setup: {response.status_code} - configure manually at:")
        print(f"   https://github.com/{GITHUB_USER}/{REPO_NAME}/settings/pages")
    
    print(f"\n🌐 Your site will be live at:")
    print(f"   https://{GITHUB_USER}.github.io/{REPO_NAME}/")
    print(f"\n⏱️  Wait 1-2 minutes for initial deployment")
    
    return True

if __name__ == "__main__":
    deploy()
