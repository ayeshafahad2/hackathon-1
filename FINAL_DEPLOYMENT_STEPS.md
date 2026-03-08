# FINAL DEPLOYMENT GUIDE - HUGGING FACE SPACES

## Quick 3-Step Deployment

### Step 1: Get Your Token (1 minute)

1. Go to: **https://huggingface.co/settings/tokens**
2. Click **"Create new token"**
3. Name: `deploy-physical-ai`
4. Select **"write"** role
5. Click **"Create token"**
6. **Copy the token** (starts with `hf_...`)

---

### Step 2: Run Deployment (2 minutes)

Open Command Prompt in your project folder and run:

```cmd
cd E:\hackathon-1
python deploy_auto.py
```

When prompted, **paste your token** and press Enter.

The script will:
- Create Space: `ayeshafahad2/physical-ai-backend`
- Upload Dockerfile
- Upload backend code
- Upload requirements
- Configure everything

**Wait for "DEPLOYMENT COMPLETE!" message**

---

### Step 3: Add Secrets (2 minutes)

1. Go to: **https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend/settings**
2. Scroll to **"Repository secrets"**
3. Click **"New secret"** 4 times and add:

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

4. Click **Save** on each

---

## Wait for Build (5-10 minutes)

1. Go to: **https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend**
2. Click **"Logs"** tab
3. Watch the Docker build
4. When you see **"Uvicorn running"** - it's ready!

---

## Test Your Backend

Visit: **https://ayeshafahad2-physical-ai-backend.hf.space/health**

Should return:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

---

## Connect to Vercel Frontend

1. Go to: **https://vercel.com/dashboard**
2. Click your project
3. **Settings** -> **Environment Variables**
4. Add:
   - Name: `REACT_APP_BACKEND_URL`
   - Value: `https://ayeshafahad2-physical-ai-backend.hf.space`
   - Environment: **Production**
5. Click **Save**
6. Go to **Deployments** -> Click latest -> **Redeploy**

---

## Test Chatbot!

1. Visit: **https://ayesha-docasaurus-project-1.vercel.app**
2. Click chat button
3. Ask: "What is Physical AI?"
4. It works!

---

## Your URLs

- **Space**: https://huggingface.co/spaces/ayeshafahad2/physical-ai-backend
- **API**: https://ayeshafahad2-physical-ai-backend.hf.space
- **Health**: https://ayeshafahad2-physical-ai-backend.hf.space/health
- **Frontend**: https://ayesha-docasaurus-project-1.vercel.app

---

## Troubleshooting

### Deployment Script Fails

**Error: Token is required**
- Make sure you copied the entire token
- Token starts with `hf_`

**Error: 401 Unauthorized**
- Token is invalid
- Create a new token with "write" role

**Error: 403 Forbidden**
- Token doesn't have "write" permission
- Create new token with correct role

### Space Shows Error

1. Check **Logs** tab
2. Common issues:
   - Missing secrets -> Add all 4 environment variables
   - Build error -> Check Dockerfile paths
   - Port mismatch -> Ensure app_port is 7860

### Chat Not Working

1. **Test backend directly**: Visit health endpoint
2. **Check Vercel env var**: Make sure REACT_APP_BACKEND_URL is set
3. **Clear cache**: Ctrl + Shift + R
4. **Check console**: F12 for errors

---

## Cost: $0

Everything is FREE:
- Hugging Face Spaces: FREE
- Qdrant Cloud: FREE tier
- Vercel: FREE hobby tier

---

## Need Help?

All deployment files are in your project:
- `deploy_auto.py` - Automated deployment script
- `Dockerfile` - Docker configuration
- `HF_DEPLOYMENT_COMPLETE.md` - Detailed guide
- `DEPLOY_HF_NOW.md` - Quick guide
