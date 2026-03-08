# 🚀 Backend Deployment Guide

## ⚠️ Important: Vercel Cannot Host FastAPI Backend

Vercel is designed for:
- ✅ Static sites (HTML, CSS, JS)
- ✅ Serverless functions (Node.js, Python, Go)
- ✅ Frontend frameworks (React, Vue, Next.js)

Vercel **CANNOT** run:
- ❌ Long-running processes (FastAPI, Django, Flask)
- ❌ Databases that need persistence (ChromaDB, PostgreSQL)
- ❌ WebSocket servers
- ❌ Background workers

---

## ✅ Solution: Deploy Backend Separately

You need to deploy your FastAPI backend to a platform that supports:
- Python applications
- Persistent storage (for ChromaDB or Qdrant)
- Long-running processes

---

## 🎯 Recommended: Deploy to Render.com (FREE)

### Step 1: Create Render Account

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"

### Step 2: Connect Your Repository

1. Select your repository: `ayeshafahad2/hackathon-1`
2. Configure the service:

```
Name: physical-ai-backend
Region: Oregon (closest to you)
Branch: main
Root Directory: backend
Runtime: Python
Build Command: pip install -r requirements-prod.txt
Start Command: uvicorn src.rag_chatbot.main:app --host 0.0.0.0 --port $PORT
```

### Step 3: Set Environment Variables

In Render dashboard, add these environment variables:

```
PORT=10000
GEMINI_API_KEY=AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo
QDRANT_URL=https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzk3OTM2NDY3fQ.9vPv85dVioLnQksZLf02FIFqXFRh102sikVyRoqZSPE
SECRET_KEY=supersecretkeychangethisinproduction
```

### Step 4: Deploy

1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Copy your backend URL (e.g., `https://physical-ai-backend-xyz.onrender.com`)

---

## 🔄 Update Frontend to Use Production Backend

### Option 1: Vercel Environment Variables (Recommended)

1. Go to your Vercel dashboard
2. Select your project: `ayesha-docasaurus-project-1`
3. Go to "Settings" → "Environment Variables"
4. Add new variable:

```
Name: REACT_APP_BACKEND_URL
Value: https://your-backend-url.onrender.com
Environment: Production
```

5. Redeploy your frontend (Vercel will auto-redeploy)

### Option 2: Hardcode in .env (Not Recommended)

Create `frontend/.env.production`:

```
REACT_APP_BACKEND_URL=https://your-backend-url.onrender.com
```

---

## 🆓 Alternative Free Hosting Options

### 1. Railway.app (FREE)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
cd backend
railway init
railway up
```

**Pros:**
- Easy deployment
- Free $5 credit/month
- Auto-deploys on git push

**Cons:**
- Requires credit card for verification
- Limited free tier

### 2. Hugging Face Spaces (FREE with GPU)

1. Go to https://huggingface.co/spaces
2. Create new space → Docker SDK
3. Push your backend code
4. Use their free GPU for embeddings

**Pros:**
- Free GPU access
- Good for ML models
- Large storage

**Cons:**
- More complex setup
- Sleeps after inactivity

### 3. Fly.io (FREE tier)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Deploy
cd backend
fly launch
fly deploy
```

**Pros:**
- Free allowance (3 VMs)
- Global edge locations
- Easy CLI deployment

**Cons:**
- Requires credit card
- Limited free resources

---

## 📝 After Backend Deployment

### 1. Test Backend Health

Visit: `https://your-backend-url.com/health`

Expected response:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

### 2. Test Chat Endpoint

```bash
curl -X POST https://your-backend-url.com/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Physical AI?"}'
```

### 3. Update Frontend

Once backend is deployed and working:

1. Set `REACT_APP_BACKEND_URL` in Vercel
2. Redeploy frontend
3. Test chat from your Vercel site

---

## 🔧 Troubleshooting

### Backend Won't Start

**Check logs in Render/Railway dashboard**

Common issues:
- Missing dependencies: Add to `requirements-prod.txt`
- Wrong port: Use `$PORT` environment variable
- Database connection: Check Qdrant credentials

### Chat Still Not Working

1. **Check CORS**: Backend allows your Vercel domain
   ```python
   # In main.py
   allow_origins=["https://your-vercel-app.vercel.app"]
   ```

2. **Check Environment Variables**: Ensure `REACT_APP_BACKEND_URL` is set

3. **Clear Browser Cache**: `Ctrl+Shift+R` to hard reload

### ChromaDB Not Persisting

ChromaDB files are lost on restart in most PaaS. Solutions:

1. **Use Qdrant Cloud** (Already configured!)
2. **Use persistent disk** (Render paid plan)
3. **Rebuild index on startup** (Slow but free)

---

## 📊 Complete Architecture

```
┌─────────────────────┐
│   Vercel Frontend   │
│  (ayesha-docasaurus │
│   -vercel.app)      │
└──────────┬──────────┘
           │
           │ HTTPS
           │ REACT_APP_BACKEND_URL
           │
┌──────────▼──────────┐
│   Render Backend    │
│  (FastAPI on :10000)│
│  - RAG Service      │
│  - Chat API         │
└──────────┬──────────┘
           │
           │ HTTPS
           │
┌──────────▼──────────┐
│   Qdrant Cloud      │
│  (Vector Database)  │
│  - Embeddings       │
│  - Similarity Search│
└─────────────────────┘
```

---

## ✅ Quick Checklist

- [ ] Create Render account
- [ ] Deploy backend to Render
- [ ] Set environment variables
- [ ] Test backend health endpoint
- [ ] Add `REACT_APP_BACKEND_URL` to Vercel
- [ ] Redeploy frontend on Vercel
- [ ] Test chat from production URL
- [ ] Monitor logs for errors

---

## 🎉 Success!

Once deployed, your chatbot will work from your Vercel site:
- Frontend: https://ayesha-docasaurus-project-1.vercel.app
- Backend: https://physical-ai-backend-xyz.onrender.com
- Fully functional RAG chatbot!
