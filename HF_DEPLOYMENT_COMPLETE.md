# 🚀 Deploy to Hugging Face Spaces - COMPLETE GUIDE

## ✅ Why Hugging Face Spaces?

- ✅ **100% FREE** (unlike Render)
- ✅ **FREE GPU** available
- ✅ **FREE Persistent Storage** options
- ✅ Easy Docker deployment
- ✅ Automatic HTTPS
- ✅ No credit card required

---

## 📋 Prerequisites

1. **Hugging Face Account**: https://huggingface.co/join
2. **Git installed**: `git --version`
3. **Python 3.8+**: `python --version`

---

## 🎯 Method 1: Automated Deployment (RECOMMENDED)

### Step 1: Install Hugging Face Hub

```bash
pip install huggingface_hub
```

### Step 2: Login to Hugging Face

```bash
huggingface-cli login
```

Copy your token from: https://huggingface.co/settings/tokens

### Step 3: Run Deployment Script

```bash
# Set your username
export HF_USERNAME=ayeshafahad2

# Run deployment (Windows)
deploy_hf.bat

# Or on Linux/Mac
bash deploy_hf.sh
```

### Step 4: Add Environment Variables

1. Go to: https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend
2. Click **Settings** → **Repository secrets**
3. Add these secrets:

```
GEMINI_API_KEY=AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo
QDRANT_URL=https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzk3OTM2NDY3fQ.9vPv85dVioLnQksZLf02FIFqXFRh102sikVyRoqZSPE
SECRET_KEY=supersecretkeychangethisinproduction
```

### Step 5: Wait for Build

- Docker build takes **5-10 minutes**
- Watch progress in **Logs** tab
- Status changes: Building → Running → ✅

### Step 6: Test Your Backend

Visit: `https://ayeshafahad2-physical-ai-backend.hf.space/health`

Expected response:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

---

## 🎯 Method 2: Manual Deployment (UI)

### Step 1: Create New Space

1. Go to: https://huggingface.co/new-space
2. **Space name**: `physical-ai-backend`
3. **License**: MIT
4. **SDK**: **Docker** ⚠️ (Important!)
5. Click **Create Space**

### Step 2: Configure README

In your new Space, edit `README.md`:

```yaml
---
title: Physical AI Backend
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---
```

### Step 3: Upload Files

Upload these files to your Space:

1. **Dockerfile** (from project root)
2. **backend/src/** (entire folder)
3. **backend/data/** (entire folder)
4. **backend/requirements-prod.txt**
5. **backend/.env.example**

Click **Files** → **Add file** → **Upload files**

### Step 4: Add Secrets

1. Go to **Settings** tab
2. Scroll to **Repository secrets**
3. Click **New secret**
4. Add all environment variables (see above)

### Step 5: Wait for Deployment

- Docker will automatically build
- Monitor in **Logs** tab
- App runs when status = ✅ Running

---

## 🎯 Method 3: Git Push Deployment

### Clone Your Space

```bash
git clone https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend
cd physical-ai-backend
```

### Copy Files

```bash
# From project root
cp ../../Dockerfile .
cp ../../README_HF.md README.md
cp -r ../../backend/src .
cp -r ../../backend/data .
cp ../../backend/requirements-prod.txt .
```

### Push to Space

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

---

## 🔗 Connect Frontend to HF Backend

### Update Vercel Environment Variable

1. Go to: https://vercel.com/dashboard
2. Select: `ayesha-docasaurus-project-1`
3. **Settings** → **Environment Variables**
4. Add/Edit:

```
Name: REACT_APP_BACKEND_URL
Value: https://ayeshafahad2-physical-ai-backend.hf.space
Environment: Production
```

5. **Redeploy** your frontend

### Test Integration

1. Visit: https://ayesha-docasaurus-project-1.vercel.app
2. Click 💬 chat button
3. Ask: "What is Physical AI?"
4. ✅ Should work!

---

## 📊 Deployment Architecture

```
┌─────────────────────────┐
│   Vercel Frontend       │
│   (ayesha-docasaurus    │
│   -project-1.vercel.app)│
└───────────┬─────────────┘
            │
            │ HTTPS
            │ REACT_APP_BACKEND_URL
            │
┌───────────▼─────────────┐
│   Hugging Face Spaces   │
│   (Docker Container)    │
│   - FastAPI Backend     │
│   - ChromaDB            │
│   - RAG Service         │
│   Port: 7860            │
└───────────┬─────────────┘
            │
            │ HTTPS
            │
┌───────────▼─────────────┐
│   Qdrant Cloud          │
│   (Vector Database)     │
│   - Embeddings          │
│   - Similarity Search   │
└─────────────────────────┘
```

---

## 🔧 Troubleshooting

### Space Shows "Error"

**Check Logs:**
1. Go to your Space
2. Click **Logs** tab
3. Look for error messages

**Common Issues:**
- Missing dependencies → Check `requirements-prod.txt`
- Port mismatch → Ensure Dockerfile uses 7860
- Environment variables → Verify secrets are set

### Build Fails

**Check Docker Build Logs:**
```bash
# View build errors in Logs tab
# Common fixes:
- Ensure COPY uses --chown=user
- Check file paths in Dockerfile
- Verify requirements-prod.txt exists
```

### Chat Not Working After Deployment

1. **Test Backend Directly:**
   ```bash
   curl https://ayeshafahad2-physical-ai-backend.hf.space/health
   ```

2. **Check CORS:**
   - Backend should allow Vercel domain
   - Already configured in `main.py`

3. **Clear Browser Cache:**
   ```
   Ctrl + Shift + R (hard reload)
   ```

4. **Check Browser Console:**
   ```
   F12 → Console → Look for errors
   ```

---

## 📈 Monitoring & Maintenance

### Check Space Status

- **URL**: https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend
- **Status**: Shown at top (Building/Running/Error)
- **Logs**: Click "Logs" tab for real-time output

### Update Backend

```bash
# Make changes to backend code
cd physical-ai-backend
git add .
git commit -m "feat: your changes"
git push origin main
```

Space will automatically rebuild!

### Pause/Resume Space

- **Pause**: Settings → Pause Space (stops billing on paid tiers)
- **Resume**: Click "Resume" button

---

## 💰 Cost Breakdown

| Service | Plan | Cost |
|---------|------|------|
| Hugging Face Spaces | CPU Basic | **FREE** |
| Hugging Face GPU | Optional | $3-30/mo |
| Qdrant Cloud | Free Tier | **FREE** |
| Vercel Frontend | Hobby | **FREE** |
| **TOTAL** | | **$0/mo** |

---

## ✅ Success Checklist

- [ ] Hugging Face account created
- [ ] Space created with Docker SDK
- [ ] All files uploaded
- [ ] Environment variables set
- [ ] Docker build completed (✅ green)
- [ ] Health endpoint responds
- [ ] Vercel REACT_APP_BACKEND_URL set
- [ ] Frontend redeployed
- [ ] Chat working from Vercel site

---

## 🎉 You're Done!

Your complete stack is now deployed:

- **Frontend**: Vercel (FREE)
- **Backend**: Hugging Face Spaces (FREE)
- **Database**: Qdrant Cloud (FREE)

**Live URLs:**
- Frontend: https://ayesha-docasaurus-project-1.vercel.app
- Backend: https://ayeshafahad2-physical-ai-backend.hf.space
- Space: https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend

**Total Monthly Cost: $0** 🎊
