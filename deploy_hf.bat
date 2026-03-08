#!/bin/bash
# Hugging Face Spaces Deployment Script
# Automates the deployment of Physical AI Backend to HF Spaces

set -e

echo "🚀 Physical AI Backend - Hugging Face Spaces Deployment"
echo "========================================================"
echo ""

# Configuration
HF_USERNAME="${HF_USERNAME:-ayeshafahad2}"
SPACE_NAME="physical-ai-backend"
FULL_REPO_NAME="$HF_USERNAME/$SPACE_NAME"

echo "📋 Configuration:"
echo "   Username: $HF_USERNAME"
echo "   Space Name: $SPACE_NAME"
echo "   Full Repo: $FULL_REPO_NAME"
echo ""

# Check if huggingface_hub is installed
if ! command -v huggingface-cli &> /dev/null; then
    echo "⚠️  Installing huggingface_hub..."
    pip install huggingface_hub
fi

# Login to Hugging Face
echo "🔐 Logging into Hugging Face..."
huggingface-cli login

# Create Space if it doesn't exist
echo "📦 Creating Space (if not exists)..."
huggingface-cli repo create $SPACE_NAME --type space --space_sdk docker

# Clone the Space repository
echo "📥 Cloning Space repository..."
if [ ! -d "$SPACE_NAME" ]; then
    huggingface-cli download $FULL_REPO_NAME --repo-type space --local-dir $SPACE_NAME
fi

# Copy necessary files to Space
echo "📁 Copying files to Space..."
cp Dockerfile $SPACE_NAME/
cp README_HF.md $SPACE_NAME/README.md
cp -r backend/src $SPACE_NAME/
cp -r backend/data $SPACE_NAME/
cp backend/requirements-prod.txt $SPACE_NAME/
cp backend/.env.example $SPACE_NAME/.env

# Navigate to Space directory
cd $SPACE_NAME

# Git configuration
git config user.name "GitHub Actions"
git config user.email "actions@github.com"

# Add and commit all files
echo "💾 Committing changes..."
git add -A
git commit -m "deploy: Initial deployment of Physical AI Backend" || echo "No changes to commit"

# Push to Hugging Face
echo "⬆️  Pushing to Hugging Face Spaces..."
git push origin main

echo ""
echo "✅ Deployment Complete!"
echo "========================================================"
echo ""
echo "🌐 Your backend will be available at:"
echo "   https://$HF_USERNAME-$SPACE_NAME.hf.space"
echo ""
echo "📊 Check deployment status:"
echo "   https://huggingface.co/spaces/$FULL_REPO_NAME"
echo ""
echo "⚠️  Important Next Steps:"
echo "   1. Go to your Space Settings"
echo "   2. Add environment variables:"
echo "      - GEMINI_API_KEY"
echo "      - QDRANT_URL"
echo "      - QDRANT_API_KEY"
echo "      - SECRET_KEY"
echo "   3. Wait for Docker build to complete (~5-10 minutes)"
echo "   4. Test health endpoint: https://$HF_USERNAME-$SPACE_NAME.hf.space/health"
echo ""
echo "🔄 To redeploy after changes:"
echo "   cd $SPACE_NAME && git push origin main"
echo ""
