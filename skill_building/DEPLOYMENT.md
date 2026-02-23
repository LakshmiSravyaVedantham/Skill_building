# 🚀 Deployment Guide

## Deploying to Vercel

### Frontend Deployment (Vercel)

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy from the frontend directory**:
```bash
cd frontend
vercel
```

4. **Follow the prompts**:
   - Set up and deploy: Yes
   - Which scope: Your account
   - Link to existing project: No
   - Project name: skill-building-frontend
   - Directory: ./
   - Override settings: No

5. **Set Environment Variables** in Vercel Dashboard:
   - Go to your project settings
   - Add: `VITE_API_URL` = your backend URL

### Backend Deployment Options

#### Option 1: Railway (Recommended for Python)

1. **Go to [Railway.app](https://railway.app)**
2. **Create New Project** → Deploy from GitHub
3. **Select your repository**
4. **Configure**:
   - Root Directory: `backend`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables**:
   - `HUGGINGFACEHUB_API_TOKEN`: Your HuggingFace token
   - `DATABASE_URL`: (Railway provides PostgreSQL)
6. **Deploy!**

#### Option 2: Render

1. **Go to [Render.com](https://render.com)**
2. **New Web Service** → Connect GitHub
3. **Configure**:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Add Environment Variables**
5. **Deploy!**

#### Option 3: Heroku

```bash
# From backend directory
heroku create skill-building-backend
heroku config:set HUGGINGFACEHUB_API_TOKEN=your_token
git push heroku ci/add-github-actions:main
```

### Quick Deploy Commands

**Frontend (Vercel)**:
```bash
cd frontend
npm run build
vercel --prod
```

**Backend (Railway)**:
```bash
# Push to GitHub, Railway auto-deploys
git push origin ci/add-github-actions
```

### Environment Variables Needed

**Frontend (.env.production)**:
```
VITE_API_URL=https://your-backend-url.railway.app
```

**Backend**:
```
HUGGINGFACEHUB_API_TOKEN=your_token_here
DATABASE_URL=your_database_url
```

### Post-Deployment

1. **Update CORS in backend/main.py**:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "https://your-vercel-app.vercel.app"  # Add your Vercel URL
    ],
    ...
)
```

2. **Update API calls in frontend** if needed

3. **Test the deployment**:
   - Visit your Vercel URL
   - Try the Quiz feature
   - Check Scenarios generation

### Troubleshooting

**Frontend not connecting to backend**:
- Check CORS settings in backend
- Verify VITE_API_URL is set correctly
- Check browser console for errors

**Backend not starting**:
- Verify all environment variables are set
- Check logs in Railway/Render dashboard
- Ensure requirements.txt is complete

**HuggingFace API errors**:
- Verify token is valid
- Check rate limits
- Consider using Simple Mode for demos

### Cost Estimates

- **Vercel**: Free tier (perfect for frontend)
- **Railway**: $5/month (includes 500 hours)
- **Render**: Free tier available (spins down after inactivity)
- **HuggingFace**: Free tier with rate limits

### Alternative: Deploy Both on Vercel

Vercel can host both frontend and serverless functions:

1. Create `api/` directory in root
2. Add Python serverless functions
3. Deploy entire project to Vercel

Note: This requires adapting the FastAPI backend to serverless functions.

---

**Recommended Setup**: Frontend on Vercel + Backend on Railway = Fast, reliable, affordable! 🚀
