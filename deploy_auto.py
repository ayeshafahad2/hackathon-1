#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-Click Hugging Face Spaces Deployment
Just run this script and enter your token when prompted
"""

import os
import sys
import io
from pathlib import Path

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("DEPLOYING TO HUGGING FACE SPACES")
print("=" * 60)
print()
print("Get your Hugging Face token:")
print("1. Go to: https://huggingface.co/settings/tokens")
print("2. Create new token with 'write' role")
print("3. Copy the token")
print()

# Get token securely
import getpass
HF_TOKEN = getpass.getpass("Enter HF Token: ").strip()

if not HF_TOKEN:
    print("Token is required!")
    sys.exit(1)

print()
print("Starting deployment...")
print()

# Now import and deploy
from huggingface_hub import HfApi, create_repo, upload_folder, upload_file

HF_USERNAME = "ayeshafahad2"
SPACE_NAME = "physical-ai-backend"
SPACE_ID = f"{HF_USERNAME}/{SPACE_NAME}"

try:
    api = HfApi(token=HF_TOKEN)
    user_info = api.whoami()
    print(f"Logged in as: {user_info['name']}")
    print()
    
    # Step 1: Create Space
    print("Step 1/6: Creating Space...")
    create_repo(
        repo_id=SPACE_ID,
        repo_type="space",
        space_sdk="docker",
        token=HF_TOKEN,
        exist_ok=True
    )
    print(f"Space created: {SPACE_ID}")
    print()
    
    # Step 2: Create and upload README
    print("Step 2/6: Creating README...")
    readme_content = """---
title: Physical AI & Humanoid Robotics Backend
emoji: robot
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
license: mit
tags:
  - fastapi
  - rag
  - chatbot
  - robotics
---

# Physical AI Backend API

RAG-powered chatbot backend for Physical AI & Humanoid Robotics textbook.

## API Endpoints

- GET /health - Health check
- POST /api/v1/chat - Chat endpoint
- POST /api/v1/content/load - Load content
- GET /api/v1/content/status - Content status

## Environment Variables

Set these in Space Settings -> Repository secrets:
- GEMINI_API_KEY
- QDRANT_URL
- QDRANT_API_KEY
- SECRET_KEY

## License

MIT
"""
    
    readme_path = Path("temp_readme_hf.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    readme_path.unlink()
    print("README uploaded")
    print()
    
    # Step 3: Upload Dockerfile
    print("Step 3/6: Uploading Dockerfile...")
    upload_file(
        path_or_fileobj="Dockerfile",
        path_in_repo="Dockerfile",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("Dockerfile uploaded")
    print()
    
    # Step 4: Upload backend/src
    print("Step 4/6: Uploading backend code...")
    upload_folder(
        folder_path="backend/src",
        path_in_repo="backend/src",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN,
        ignore_patterns=["__pycache__", "*.pyc", ".git", "chroma_db"]
    )
    print("Backend code uploaded")
    print()
    
    # Step 5: Upload requirements
    print("Step 5/6: Uploading requirements...")
    upload_file(
        path_or_fileobj="backend/requirements-prod.txt",
        path_in_repo="backend/requirements-prod.txt",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("Requirements uploaded")
    print()
    
    # Complete!
    print()
    print("=" * 60)
    print("DEPLOYMENT COMPLETE!")
    print("=" * 60)
    print()
    print(f"Space URL: https://huggingface.co/spaces/{SPACE_ID}")
    print(f"API URL: https://{HF_USERNAME}-{SPACE_NAME}.hf.space")
    print(f"Health: https://{HF_USERNAME}-{SPACE_NAME}.hf.space/health")
    print()
    print("NEXT STEPS:")
    print()
    print("1. Add Environment Variables:")
    print(f"   Go to: https://huggingface.co/spaces/{SPACE_ID}/settings")
    print("   Scroll to 'Repository secrets'")
    print("   Add these 4 secrets:")
    print()
    print("   GEMINI_API_KEY = AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo")
    print("   QDRANT_URL = https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333")
    print("   QDRANT_API_KEY = [your key]")
    print("   SECRET_KEY = supersecretkeychangethisinproduction")
    print()
    print("2. Wait 5-10 minutes for Docker build")
    print()
    print("3. Monitor: https://huggingface.co/spaces/{SPACE_ID}/logs")
    print()
    print("DONE!")
    
except Exception as e:
    print()
    print(f"Deployment failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
