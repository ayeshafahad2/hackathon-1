#!/usr/bin/env python3
"""
Deploy Physical AI Backend to Hugging Face Spaces
Uses Hugging Face Hub library for automated deployment
"""

import os
import sys
from pathlib import Path
from huggingface_hub import HfApi, create_repo, upload_folder, upload_file
from huggingface_hub.hf_api import SpaceHardware, SpaceStage

# Configuration
HF_USERNAME = "ayeshafahad2"
SPACE_NAME = "physical-ai-backend"
SPACE_ID = f"{HF_USERNAME}/{SPACE_NAME}"

# Get token from environment or command line
HF_TOKEN = os.environ.get("HF_TOKEN") or (sys.argv[1] if len(sys.argv) > 1 else None)

if not HF_TOKEN:
    print("❌ Hugging Face token required!")
    print("\nGet your token from: https://huggingface.co/settings/tokens")
    print("\nUsage:")
    print("  set HF_TOKEN=your_token_here")
    print("  python deploy_to_hf.py")
    print("\nOr:")
    print("  python deploy_to_hf.py your_token_here")
    sys.exit(1)

print("🚀 Deploying Physical AI Backend to Hugging Face Spaces")
print("=" * 60)
print(f"Space: {SPACE_ID}")
print("=" * 60)

try:
    # Initialize API
    api = HfApi(token=HF_TOKEN)
    
    # Get user info to verify token
    user_info = api.whoami()
    print(f"✅ Logged in as: {user_info['name']}")
    
    # Step 1: Create Space
    print("\n📦 Step 1/5: Creating Space...")
    try:
        create_repo(
            repo_id=SPACE_ID,
            repo_type="space",
            space_sdk="docker",
            token=HF_TOKEN,
            exist_ok=True
        )
        print(f"✅ Space created/verified: {SPACE_ID}")
    except Exception as e:
        print(f"❌ Error creating space: {e}")
        sys.exit(1)
    
    # Step 2: Create README.md with proper YAML front matter
    print("\n📝 Step 2/5: Creating README.md...")
    readme_content = """---
title: Physical AI & Humanoid Robotics Backend
emoji: 🤖
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
  - physical-ai
---

# Physical AI & Humanoid Robotics - RAG Chatbot Backend

This Space hosts the backend API for the Physical AI & Humanoid Robotics textbook chatbot.

## Features

- 🤖 RAG-powered chatbot answering questions about Physical AI & Humanoid Robotics
- 📚 Complete textbook content with 13 weeks of material
- 🔍 Semantic search using ChromaDB vector store
- 🌐 RESTful API with CORS support
- ⚡ Fast response times with local embeddings

## API Endpoints

### Health Check
```bash
GET /health
```

### Chat Endpoint
```bash
POST /api/v1/chat
Content-Type: application/json

{
  "message": "What is Physical AI?",
  "session_id": "optional-session-id",
  "language": "en"
}
```

## Environment Variables

Configure these in Space Settings → Repository secrets:

- `GEMINI_API_KEY` - Google Gemini API key
- `QDRANT_URL` - Qdrant Cloud URL
- `QDRANT_API_KEY` - Qdrant API key
- `SECRET_KEY` - Application secret key

## Usage

Your frontend should set `REACT_APP_BACKEND_URL` to this Space's URL.

## License

MIT License
"""
    
    readme_path = Path("temp_readme.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Upload README
    upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    readme_path.unlink()  # Clean up
    print("✅ README.md uploaded")
    
    # Step 3: Upload Dockerfile
    print("\n🐳 Step 3/5: Uploading Dockerfile...")
    dockerfile_path = Path("Dockerfile")
    if not dockerfile_path.exists():
        print("❌ Dockerfile not found!")
        sys.exit(1)
    
    upload_file(
        path_or_fileobj=str(dockerfile_path),
        path_in_repo="Dockerfile",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("✅ Dockerfile uploaded")
    
    # Step 4: Upload backend code
    print("\n📁 Step 4/5: Uploading backend code...")
    
    # Upload backend/src
    src_path = Path("backend/src")
    if not src_path.exists():
        print("❌ backend/src not found!")
        sys.exit(1)
    
    upload_folder(
        folder_path=str(src_path),
        path_in_repo="backend/src",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN,
        ignore_patterns=["__pycache__", "*.pyc", ".git"]
    )
    print("✅ backend/src uploaded")
    
    # Upload requirements
    print("\n📄 Step 5/5: Uploading requirements...")
    req_path = Path("backend/requirements-prod.txt")
    if not req_path.exists():
        print("❌ backend/requirements-prod.txt not found!")
        sys.exit(1)
    
    upload_file(
        path_or_fileobj=str(req_path),
        path_in_repo="backend/requirements-prod.txt",
        repo_id=SPACE_ID,
        repo_type="space",
        token=HF_TOKEN
    )
    print("✅ requirements-prod.txt uploaded")
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ DEPLOYMENT COMPLETE!")
    print("=" * 60)
    print(f"\n🌐 Space URL: https://huggingface.co/spaces/{SPACE_ID}")
    print(f"🔗 Direct API: https://{HF_USERNAME}-{SPACE_NAME}.hf.space")
    print(f"🏥 Health Check: https://{HF_USERNAME}-{SPACE_NAME}.hf.space/health")
    
    print("\n⏳ Next Steps:")
    print("1. Go to Space Settings: https://huggingface.co/spaces/" + SPACE_ID + "/settings")
    print("2. Add Repository secrets:")
    print("   - GEMINI_API_KEY")
    print("   - QDRANT_URL")
    print("   - QDRANT_API_KEY")
    print("   - SECRET_KEY")
    print("3. Wait 5-10 minutes for Docker build")
    print("4. Test health endpoint")
    
    print("\n📊 Monitor build: https://huggingface.co/spaces/" + SPACE_ID + "/logs")
    
except Exception as e:
    print(f"\n❌ Deployment failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
