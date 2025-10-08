# 🆓 100% Free Deployment Guide

## Your App is Already Deployed!

✅ **Frontend**: Live on Vercel (Free Forever)
- URL: https://frontend-j4akmsr1p-sravyas-projects-f5209810.vercel.app
- Cost: $0/month

Now let's deploy the backend for FREE!

## Deploy Backend to Render (Free Tier)

### Step 1: Sign Up for Render

1. Go to **[Render.com](https://render.com)**
2. Click **"Get Started for Free"**
3. Sign up with your **GitHub account**

### Step 2: Deploy Backend

1. Once logged in, click **"New +"** → **"Web Service"**

2. **Connect your GitHub repository**:
   - Click "Connect account" if needed
   - Find and select: `LakshmiSravya123/Skill_building`

3. **Configure the service**:
   - **Name**: `skill-building-backend`
   - **Region**: Oregon (US West) - closest to you
   - **Branch**: `ci/add-github-actions`
   - **Root Directory**: `skill_building/backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Select Free Plan**:
   - Choose **"Free"** (not Starter)
   - Free tier includes:
     - 750 hours/month (enough for 24/7)
     - Spins down after 15 min of inactivity
     - Spins up automatically when accessed

5. **Add Environment Variables**:
   - Click **"Advanced"**
   - Add environment variable:
     - **Key**: `HUGGINGFACEHUB_API_TOKEN`
     - **Value**: (paste your HuggingFace token)

6. **Click "Create Web Service"**

7. **Wait for deployment** (3-5 minutes)
   - You'll see logs as it builds
   - When you see "Your service is live 🎉" - it's ready!

8. **Copy your Render URL**:
   - It will be something like: `https://skill-building-backend.onrender.com`

### Step 3: Update Vercel with Backend URL

1. Go to **[Vercel Dashboard](https://vercel.com/sravyas-projects-f5209810/frontend)**

2. Click on your project → **Settings** → **Environment Variables**

3. **Add new variable**:
   - **Name**: `VITE_API_URL`
   - **Value**: Your Render URL (e.g., `https://skill-building-backend.onrender.com`)
   - **Environment**: Production, Preview, Development (select all)

4. Click **"Save"**

5. Go to **Deployments** tab

6. Click the **3 dots** on the latest deployment → **"Redeploy"**

### Step 4: Test Your App!

Visit your Vercel URL and try the Quiz - it should work now! 🎉

**Note**: First request might take 30-60 seconds as Render spins up the free tier service.

## Free Tier Limitations & Solutions

### Render Free Tier:
- ✅ 750 hours/month (plenty for 24/7)
- ⚠️ Spins down after 15 min inactivity
- ⚠️ Cold start takes 30-60 seconds

**Solution**: The app will "wake up" automatically when someone visits. Just be patient on first load!

### Vercel Free Tier:
- ✅ Unlimited bandwidth
- ✅ 100 GB-hours compute
- ✅ Perfect for frontend

### HuggingFace Free Tier:
- ✅ Free API access
- ⚠️ Rate limits (30 requests/hour for some models)
- **Solution**: Use Simple Mode (`main_simple.py`) if you hit limits

## Alternative: Keep Backend Local

If you want to avoid cold starts, you can:

1. Keep backend running locally
2. Use **ngrok** to expose it:
   ```bash
   # Install ngrok
   brew install ngrok
   
   # Run your backend
   cd backend
   uvicorn main:app --port 8000
   
   # In another terminal, expose it
   ngrok http 8000
   ```

3. Copy the ngrok URL to Vercel's `VITE_API_URL`

**Note**: ngrok free tier gives you a new URL each time you restart.

## Cost Breakdown

| Service | Cost | What You Get |
|---------|------|--------------|
| Vercel (Frontend) | $0 | Unlimited deployments, global CDN |
| Render (Backend) | $0 | 750 hours/month, auto-scaling |
| HuggingFace API | $0 | AI model access with rate limits |
| **Total** | **$0/month** | Full-stack AI app! |

## Upgrade Paths (Optional)

If you want to remove cold starts later:

- **Render Starter**: $7/month (no spin down)
- **Railway**: $5/month (500 hours)
- **Fly.io**: $5/month (shared CPU)

But the free tier works great for portfolios and demos! 🎓

## Troubleshooting

**Quiz shows error**:
- Check Render logs for errors
- Verify HuggingFace token is set
- Wait 60 seconds for cold start

**Backend won't deploy**:
- Check `requirements.txt` is in `skill_building/backend/`
- Verify Python version in render.yaml
- Check Render build logs

**CORS errors**:
- Already fixed! Your Vercel URL is in the CORS settings

---

## 🎉 You're Done!

Your AI-powered financial literacy platform is now:
- ✅ Deployed globally
- ✅ 100% free
- ✅ Using real AI
- ✅ Accessible to anyone with the link

**Share your app**: https://frontend-j4akmsr1p-sravyas-projects-f5209810.vercel.app

Congratulations! 🚀🎓💰
