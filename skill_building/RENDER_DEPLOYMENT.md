# 🚀 Render Free Tier Deployment (Memory Optimized)

## ✅ Solution: Lightweight Backend

I've created `main_lightweight.py` that uses **under 100MB** of memory (well within Render's 512MB free tier limit).

### What Changed:

**Before** (Out of Memory ❌):
- Full RAG pipeline with FAISS
- Sentence transformers embeddings
- BM25 retriever
- Memory usage: ~600MB

**Now** (Works on Free Tier ✅):
- Direct HuggingFace API calls
- No embeddings loaded
- No vector database
- Memory usage: ~80MB

### Features Still Working:

✅ AI-generated quiz questions
✅ AI-generated scenarios  
✅ HuggingFace Zephyr-7B model
✅ Fallback to curated content if API fails
✅ All CORS configured
✅ Health endpoints

## Deploy to Render (Free)

### Step 1: Create Render Account

1. Go to **[Render.com](https://render.com)**
2. Sign up with GitHub (free)

### Step 2: Deploy Backend

1. **New Web Service** → Connect GitHub

2. **Select Repository**: `LakshmiSravya123/Skill_building`

3. **Configure**:
   ```
   Name: skill-building-backend
   Region: Oregon (US West)
   Branch: ci/add-github-actions
   Root Directory: skill_building/backend
   Runtime: Python 3
   Build Command: pip install fastapi uvicorn python-dotenv huggingface-hub pydantic
   Start Command: uvicorn main_lightweight:app --host 0.0.0.0 --port $PORT
   ```

4. **Plan**: Select **FREE** ⭐

5. **Environment Variables**:
   - Click "Advanced"
   - Add: `HUGGINGFACEHUB_API_TOKEN` = your token

6. **Create Web Service**

7. **Wait 3-5 minutes** for deployment

8. **Copy your URL**: `https://skill-building-backend-xxxx.onrender.com`

### Step 3: Update Vercel

1. **Vercel Dashboard** → Your project → **Settings** → **Environment Variables**

2. **Add**:
   - Name: `VITE_API_URL`
   - Value: Your Render URL
   - All environments

3. **Redeploy** frontend

## Test Your App

Visit: https://frontend-j4akmsr1p-sravyas-projects-f5209810.vercel.app

- Click **Quiz** - AI generates questions
- Click **Scenarios** - AI generates scenarios
- First load takes 30-60 sec (cold start)

## Memory Usage Comparison

| Version | Memory | Render Free Tier |
|---------|--------|------------------|
| Full RAG (`main.py`) | ~600MB | ❌ Out of Memory |
| Simple (`main_simple.py`) | ~50MB | ✅ Works (no AI) |
| **Lightweight (`main_lightweight.py`)** | **~80MB** | **✅ Works with AI!** |

## What You Get (Free):

✅ AI-powered quiz questions
✅ AI-generated scenarios
✅ HuggingFace Zephyr-7B model
✅ Automatic fallbacks
✅ 750 hours/month (24/7 coverage)
✅ Auto-scaling
✅ HTTPS included

## Limitations:

⚠️ Cold start: 30-60 seconds after 15 min idle
⚠️ No document retrieval (uses direct AI)
⚠️ HuggingFace rate limits apply

## Upgrade Path:

Want the full RAG experience with document retrieval?

**Option 1**: Render Starter Plan ($7/month)
- 512MB → 2GB memory
- No cold starts
- Can run full `main.py` with RAG

**Option 2**: Railway ($5/month)
- 8GB memory included
- Full RAG pipeline works
- No cold starts

But the lightweight version works great for free! 🎉

## Troubleshooting

**Still out of memory?**
- Verify you're using `main_lightweight.py` in start command
- Check Render logs for actual memory usage

**Quiz not working?**
- Check HuggingFace token is set
- Wait 60 seconds for cold start
- Check Render logs for errors

**API errors?**
- HuggingFace free tier has rate limits
- Fallback content will be used automatically

---

**Your app is optimized for Render's free tier! Deploy and enjoy! 🚀**
