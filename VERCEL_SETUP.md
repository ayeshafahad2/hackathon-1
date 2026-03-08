# Vercel Deployment Guide - Complete Setup

## ✅ Backend Status
- **Running**: https://Ayeshaaabir-physical-ai-backend.hf.space
- **Health**: https://Ayeshaaabir-physical-ai-backend.hf.space/health

---

## 🔧 Step 1: Add Environment Variable to Vercel

### Option A: Via Vercel Dashboard (Recommended)

1. Go to: **https://vercel.com/dashboard**
2. Click your project: **ayesha-docasaurus-project-1**
3. Click **Settings** tab
4. Click **Environment Variables**
5. Click **Add New Variable**
6. Add:
   - **Name**: `REACT_APP_BACKEND_URL`
   - **Value**: `https://Ayeshaaabir-physical-ai-backend.hf.space`
   - **Environment**: ✅ Production (check this)
   - **Preview**: ✅ Preview (optional)
   - **Development**: ❌ Development (uncheck)
7. Click **Save**

### Option B: Via Vercel CLI

```bash
cd frontend
vercel env add REACT_APP_BACKEND_URL https://Ayeshaaabir-physical-ai-backend.hf.space
```

---

## 🚀 Step 2: Redeploy Frontend

After adding the environment variable:

1. Go to: **https://vercel.com/dashboard**
2. Click your project
3. Click **Deployments** tab
4. Click the **⋮** (three dots) on the latest deployment
5. Click **Redeploy**
6. Click **Redeploy** again to confirm

OR trigger a new deployment:

```bash
cd frontend
git add .
git commit -m "chore: Update for backend integration"
git push origin main
```

---

## 🧪 Step 3: Test the Integration

### Test 1: Visit Your Site
Go to: **https://ayesha-docasaurus-project-1.vercel.app**

### Test 2: Check Chat Widget
1. Click the 💬 chat button (bottom right)
2. Check the connection status (should show green dot)
3. Ask: "What is Physical AI?"
4. Should get a response!

### Test 3: Check Browser Console
1. Press `F12` to open DevTools
2. Go to **Console** tab
3. Look for any errors
4. Should see no connection errors

---

## 🔍 Troubleshooting

### Chat Shows "Disconnected"

**Check 1**: Verify backend is running
```bash
curl https://Ayeshaaabir-physical-ai-backend.hf.space/health
```

**Check 2**: Verify env var is set in Vercel
- Go to Vercel Dashboard → Settings → Environment Variables
- Make sure `REACT_APP_BACKEND_URL` exists
- Value should be: `https://Ayeshaaabir-physical-ai-backend.hf.space`

**Check 3**: Redeploy frontend
- Vercel only picks up env vars on deploy
- Click Redeploy after adding env var

### CORS Error in Console

The backend should already have CORS configured. If you see CORS errors:

1. Check backend logs on Hugging Face
2. Verify CORS origins include Vercel domain

### 404 on Chat API

Make sure the backend URL is correct:
- ✅ `https://Ayeshaaabir-physical-ai-backend.hf.space`
- ❌ `https://Ayeshaaabir-physical-ai-backend.hf.space/api` (wrong)

---

## 📊 Complete Architecture

```
User Browser
    ↓
https://ayesha-docasaurus-project-1.vercel.app
    ↓ (REACT_APP_BACKEND_URL)
https://Ayeshaaabir-physical-ai-backend.hf.space
    ↓
Qdrant Cloud (Vector DB)
```

---

## ✅ Success Indicators

You'll know it's working when:

1. ✅ Chat widget shows green "Connected" status
2. ✅ Can send messages and get responses
3. ✅ Responses include textbook citations
4. ✅ No errors in browser console
5. ✅ Backend health returns `content_loaded: true`

---

## 🎯 Quick Test Commands

### Test Backend Directly
```bash
curl https://Ayeshaaabir-physical-ai-backend.hf.space/health
```

### Test Chat API
```bash
curl -X POST https://Ayeshaaabir-physical-ai-backend.hf.space/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Physical AI?"}'
```

### Check Vercel Env Vars
```bash
cd frontend
vercel env ls
```

---

## 📝 Environment Variables Summary

| Name | Value | Where |
|------|-------|-------|
| `REACT_APP_BACKEND_URL` | `https://Ayeshaaabir-physical-ai-backend.hf.space` | Vercel |

---

## 🎉 Done!

Your full-stack app is now connected:
- **Frontend**: Vercel
- **Backend**: Hugging Face Spaces
- **Database**: Qdrant Cloud

**Total Cost: $0/month** 🚀
