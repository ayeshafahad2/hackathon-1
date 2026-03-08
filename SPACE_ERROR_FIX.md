## 🚨 Space Error - Troubleshooting

Your Hugging Face Space is showing an error. Here's what to do:

### Step 1: Check the Error

Go to: **https://huggingface.co/spaces/Ayeshaaabir/physical-ai-backend**

Click on the **"Logs"** tab to see the error message.

### Common Issues & Fixes:

#### Issue 1: Dockerfile Path Error
**Error**: `failed to solve: no build stage`
**Fix**: ✅ Already fixed - new Dockerfile uploaded

#### Issue 2: Missing Files
**Error**: `FileNotFoundError: backend/src`
**Fix**: The files need to be in the correct structure

#### Issue 3: Environment Variables Missing
**Error**: `Qdrant URL not configured`
**Fix**: Add the 4 secrets in Space Settings

---

### Step 2: Monitor the Rebuild

The simplified Dockerfile has been uploaded. Watch the logs:

**https://huggingface.co/spaces/Ayeshaaabir/physical-ai-backend/logs**

You should see:
1. `FROM python:3.11-slim` - pulling image
2. `pip install` - installing dependencies
3. `COPY backend/src` - copying files
4. `Uvicorn running` - server started ✅

---

### Step 3: Add Environment Variables (CRITICAL!)

Go to: **https://huggingface.co/spaces/Ayeshaaabir/physical-ai-backend/settings**

Scroll to **"Repository secrets"**

Add these 4 secrets:

1. Click "New secret"
   - Name: `GEMINI_API_KEY`
   - Value: `AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo`
   - Click Save

2. Click "New secret"
   - Name: `QDRANT_URL`
   - Value: `https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333`
   - Click Save

3. Click "New secret"
   - Name: `QDRANT_API_KEY`
   - Value: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzk3OTM2NDY3fQ.9vPv85dVioLnQksZLf02FIFqXFRh102sikVyRoqZSPE`
   - Click Save

4. Click "New secret"
   - Name: `SECRET_KEY`
   - Value: `supersecretkeychangethisinproduction`
   - Click Save

---

### Step 4: Restart the Space

After adding secrets:

1. Go to: **https://huggingface.co/spaces/Ayeshaaabir/physical-ai-backend**
2. Click **"Factory reboot"** button (top right)
3. Confirm reboot
4. Wait for rebuild

---

### Step 5: Test Health

Once status shows "Running":

Visit: **https://Ayeshaaabir-physical-ai-backend.hf.space/health**

Should return:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot",
  "content_loaded": true
}
```

---

## 🆘 Still Having Issues?

### Share the Error Log

Copy the error from the Logs tab and I'll fix it.

Common errors:
- `ModuleNotFoundError` → Missing dependency
- `FileNotFoundError` → Wrong file path
- `ConnectionError` → Qdrant credentials wrong
- `Port in use` → Wrong port configuration

---

**Current Status**: Dockerfile simplified and uploaded. Waiting for rebuild and environment variables to be added.
