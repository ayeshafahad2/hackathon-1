# ⚡ DEPLOY BACKEND TO HUGGING FACE - 5 MINUTE GUIDE

## 🎯 Follow These Exact Steps

### Step 1: Create Hugging Face Account (1 min)

1. Go to: **https://huggingface.co/join**
2. Sign up with GitHub (fastest)
3. Verify email

---

### Step 2: Create Space (1 min)

1. Go to: **https://huggingface.co/new-space**
2. Fill in:
   - **Space name**: `physical-ai-backend`
   - **License**: MIT
   - **SDK**: **Docker** ⚠️ (MUST select Docker!)
3. Click **Create Space**

---

### Step 3: Configure README (1 min)

1. In your new Space, click **Files**
2. Click on `README.md`
3. Click **Edit**
4. Replace ENTIRE content with:

```yaml
---
title: Physical AI Backend
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
---

# Physical AI & Humanoid Robotics Backend

Deploying RAG chatbot backend...
```

5. Click **Commit changes to main**

---

### Step 4: Upload Files (2 min)

1. Click **Files** tab
2. Click **Add file** → **Upload files**
3. Upload these files from your project:

**Upload these 5 items:**
- `Dockerfile` (from project root)
- `README_HF.md` → rename to `README.md` when uploading
- `backend/src/` (entire folder)
- `backend/data/` (entire folder)  
- `backend/requirements-prod.txt`

4. Click **Commit changes to main**

---

### Step 5: Add Secrets (CRITICAL!)

1. In your Space, click **Settings** tab
2. Scroll to **Repository secrets**
3. Click **New secret** 4 times, add these:

```
Name: GEMINI_API_KEY
Value: AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo
```

```
Name: QDRANT_URL
Value: https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333
```

```
Name: QDRANT_API_KEY
Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzk3OTM2NDY3fQ.9vPv85dVioLnQksZLf02FIFqXFRh102sikVyRoqZSPE
```

```
Name: SECRET_KEY
Value: supersecretkeychangethisinproduction
```

---

### Step 6: Wait for Build (5-10 min)

1. Click **Logs** tab
2. Watch Docker build
3. Status will change: `Building` → `Running` → ✅
4. When you see `Uvicorn running on http://0.0.0.0:7860` → **DONE!**

---

### Step 7: Test Backend

1. Visit: `https://ayeshafahad2-physical-ai-backend.hf.space/health`
2. Should see:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

---

### Step 8: Connect to Vercel Frontend

1. Go to: **https://vercel.com/dashboard**
2. Click your project: `ayesha-docasaurus-project-1`
3. Click **Settings** → **Environment Variables**
4. Click **Add New Variable**:
   - **Name**: `REACT_APP_BACKEND_URL`
   - **Value**: `https://ayeshafahad2-physical-ai-backend.hf.space`
   - **Environment**: Production ✅
5. Click **Save**
6. Go to **Deployments** → Click latest → **Redeploy**

---

### Step 9: Test Chatbot! 🎉

1. Visit: **https://ayesha-docasaurus-project-1.vercel.app**
2. Click 💬 chat button
3. Ask: "What is Physical AI?"
4. **IT SHOULD WORK!** ✅

---

## 🔗 Your URLs

- **Space**: https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend
- **Backend API**: https://ayeshafahad2-physical-ai-backend.hf.space
- **Frontend**: https://ayesha-docasaurus-project-1.vercel.app

---

## 🆘 If Something Goes Wrong

### Backend Shows Error

1. Check **Logs** tab in Space
2. Look for error messages
3. Common fix: Ensure all secrets are set correctly

### Chat Still Not Working

1. **Hard refresh**: `Ctrl + Shift + R`
2. **Check console**: F12 → Console
3. **Verify URL**: Make sure `REACT_APP_BACKEND_URL` is set in Vercel

### Need Help?

- Check `HF_DEPLOYMENT_COMPLETE.md` for detailed troubleshooting
- All docs are in your project folder

---

## ✅ Success Indicators

You'll know it's working when:
- ✅ Space status = "Running" (green)
- ✅ `/health` returns `content_loaded: true`
- ✅ Chat responds with textbook answers
- ✅ Answers include source citations

---

**Total Time**: 10-15 minutes
**Total Cost**: $0 (100% FREE!)
