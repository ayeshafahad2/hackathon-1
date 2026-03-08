# -*- coding: utf-8 -*-
import os
from pathlib import Path
from huggingface_hub import HfApi, create_repo, upload_folder

HF_TOKEN = os.environ.get('HF_TOKEN')

print("Deploying to Hugging Face Spaces...")
print()

try:
    api = HfApi(token=HF_TOKEN)
    user_info = api.whoami()
    HF_USERNAME = user_info['name']
    SPACE_NAME = "physical-ai-backend"
    SPACE_ID = f"{HF_USERNAME}/{SPACE_NAME}"
    
    print(f"Logged in as: {HF_USERNAME}")
    print(f"Creating Space: {SPACE_ID}")
    print()
    
    # Create Space
    print("Creating Space...")
    create_repo(
        repo_id=SPACE_ID,
        repo_type="space",
        space_sdk="docker",
        token=HF_TOKEN,
        exist_ok=True
    )
    print("[OK] Space created")
    print()
    
    # Create README
    print("Creating README...")
    readme_content = f"""---
title: Physical AI Backend
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---

# Physical AI Backend API

RAG chatbot backend for Physical AI & Humanoid Robotics textbook.
"""
    with open("temp_readme.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    api.upload_file(
        path_or_fileobj="temp_readme.md",
        path_in_repo="README.md",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    os.remove("temp_readme.md")
    print("[OK] README uploaded")
    print()
    
    # Upload Dockerfile
    print("Uploading Dockerfile...")
    api.upload_file(
        path_or_fileobj="Dockerfile",
        path_in_repo="Dockerfile",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("[OK] Dockerfile uploaded")
    print()
    
    # Upload backend code
    print("Uploading backend code (this may take a moment)...")
    upload_folder(
        folder_path="backend/src",
        path_in_repo="backend/src",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN,
        ignore_patterns=["__pycache__", "*.pyc"]
    )
    print("[OK] Backend code uploaded")
    print()
    
    # Upload requirements
    print("Uploading requirements...")
    api.upload_file(
        path_or_fileobj="backend/requirements-prod.txt",
        path_in_repo="backend/requirements-prod.txt",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("[OK] Requirements uploaded")
    print()
    
    print("=" * 60)
    print("DEPLOYMENT COMPLETE!")
    print("=" * 60)
    print()
    print(f"Space URL: https://huggingface.co/spaces/{SPACE_ID}")
    print(f"API URL: https://{HF_USERNAME}-{SPACE_NAME}.hf.space")
    print(f"Health: https://{HF_USERNAME}-{SPACE_NAME}.hf.space/health")
    print()
    print("IMPORTANT - Add these secrets in Space Settings:")
    print(f"   https://huggingface.co/spaces/{SPACE_ID}/settings")
    print()
    print("GEMINI_API_KEY=AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo")
    print("QDRANT_URL=https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333")
    print("QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzk3OTM2NDY3fQ.9vPv85dVioLnQksZLf02FIFqXFRh102sikVyRoqZSPE")
    print("SECRET_KEY=supersecretkeychangethisinproduction")
    print()
    print("Wait 5-10 minutes for Docker build, then test the health endpoint!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
