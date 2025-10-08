# 🚀 Quick Setup Guide - Financial Literacy Platform

## ✅ What's Been Fixed and Built

### Issues Resolved
1. ✅ **Missing dependencies** - Created `requirements.txt` with all Python packages
2. ✅ **Documents directory** - Fixed from file to proper directory structure
3. ✅ **Sample documents** - Added 3 comprehensive financial literacy documents + 3 PDFs
4. ✅ **Database config** - Switched from PostgreSQL to SQLite for simplicity
5. ✅ **Frontend structure** - Complete Vue 3 + Vite + Tailwind setup
6. ✅ **CORS issues** - Added CORS middleware for frontend-backend communication
7. ✅ **Environment config** - Created `.env` and `.env.example` files
8. ✅ **Git repository** - Cleaned up and pushed to correct Skill_building repo

### What's Been Built

#### Backend (FastAPI + RAG)
- **FastAPI server** with health endpoints
- **RAG pipeline** using LangChain, HuggingFace, FAISS, and BM25
- **Hybrid retrieval** combining semantic and keyword search
- **Error handling** for robust API responses
- **SQLite database** for user data
- **Sample endpoints**: `/quiz/{id}`, `/generate/scenario`

#### Frontend (Vue 3)
- **Home page** with hero section and feature cards
- **Courses page** with 6 financial literacy courses
- **Quiz component** for adaptive learning
- **Scenario component** for real-world financial situations
- **Responsive design** with Tailwind CSS
- **API integration** with Axios

#### Documentation
- **Comprehensive README** with setup instructions
- **Startup scripts** for easy launch
- **Troubleshooting guide** for common issues

## 🎯 Next Steps to Run the Application

### Step 1: Install Backend Dependencies

```bash
cd /Users/sravyalu/skill_building/backend

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure HuggingFace API Token

1. Get a free token from: https://huggingface.co/settings/tokens
2. Edit `backend/.env`:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_actual_token_here
   ```

### Step 3: Install Frontend Dependencies

```bash
cd /Users/sravyalu/skill_building/frontend

# Install npm packages
npm install
```

This will install:
- Vue 3.5.22
- Vite 7.1.9
- Vue Router 4.3.0
- Axios 1.6.7
- Tailwind CSS 3.4.1
- And all other dependencies

### Step 4: Run the Application

**Terminal 1 - Backend:**
```bash
cd /Users/sravyalu/skill_building/backend
source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd /Users/sravyalu/skill_building/frontend
npm run dev
```

### Step 5: Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🎨 Features You Can Try

1. **Browse Courses** - Click "Courses" to see 6 financial literacy topics
2. **Take Quiz** - Test your knowledge with AI-generated questions
3. **Generate Scenarios** - Enter topics like "Market Crash" or "Emergency Fund" to get personalized scenarios
4. **View Sources** - See which documents the AI used to generate responses

## 🔧 Resolving IDE Warnings

The warnings you're seeing are normal and will disappear after:

1. **Run `npm install`** in the frontend directory
2. **Restart the Vue language server** in your IDE
   - In VS Code/Windsurf: Command Palette → "Vue: Restart Vue server"

The `@apply` warning is expected - Tailwind CSS uses this directive and it's properly configured in `tailwind.config.js`.

## 📦 What's in the Repository

```
skill_building/
├── backend/
│   ├── main.py                    # FastAPI app with CORS, health checks
│   ├── requirements.txt           # Python dependencies (updated)
│   ├── .env                       # Your API tokens (not in git)
│   ├── .env.example              # Template for .env
│   └── rag/
│       ├── pipeline.py           # RAG implementation with hybrid retrieval
│       └── documents/            # Financial literacy content
│           ├── budgeting_basics.txt
│           ├── investing_fundamentals.txt
│           ├── emergency_fund.txt
│           └── *.pdf (3 PDFs)
├── frontend/
│   ├── package.json              # Updated with latest Vue 3.5.22
│   ├── vite.config.js            # Vite config with API proxy
│   ├── tailwind.config.js        # Tailwind CSS config
│   ├── index.html                # Entry point
│   └── src/
│       ├── App.vue               # Main app with navigation
│       ├── main.js               # Vue app initialization
│       ├── router/index.js       # Route definitions
│       ├── views/
│       │   ├── Home.vue          # Landing page
│       │   └── Courses.vue       # Course catalog
│       └── components/
│           ├── Quiz.vue          # Adaptive quiz
│           └── Scenario.vue      # Financial scenarios
├── start_backend.sh              # Easy backend startup
├── start_frontend.sh             # Easy frontend startup
├── README.md                     # Comprehensive documentation
├── SETUP_GUIDE.md               # This file
└── .gitignore                   # Excludes .env, node_modules, etc.
```

## 🎓 How the RAG System Works

1. **Document Loading**: Loads `.txt` and `.pdf` files from `backend/rag/documents/`
2. **Text Splitting**: Chunks documents into 1000-character pieces with 200-char overlap
3. **Embeddings**: Uses FinE5 (finance-specific) model for semantic understanding
4. **Vector Store**: FAISS for fast similarity search
5. **Hybrid Retrieval**: Combines FAISS (70%) + BM25 (30%) for best results
6. **LLM**: Mixtral-8x7B generates responses based on retrieved context
7. **Source Attribution**: Returns source documents for transparency

## 🚨 Important Notes

- **API Token Required**: The backend won't work without a HuggingFace token in `.env`
- **First Run**: RAG pipeline builds FAISS index on first startup (takes 1-2 minutes)
- **Internet Required**: LLM calls go to HuggingFace API
- **Free Tier**: HuggingFace free tier has rate limits

## 🎉 You're All Set!

Your AI-powered financial literacy platform is ready to use. The application provides:
- **Personalized learning** with RAG technology
- **Adaptive quizzes** that adjust to skill level
- **Real-world scenarios** for practical application
- **Source transparency** showing where information comes from

## 📝 Git Status

All changes have been committed to the `ci/add-github-actions` branch and pushed to:
**https://github.com/LakshmiSravya123/Skill_building.git**

Total commits made: 10+
- Backend setup and fixes
- Frontend complete structure
- Documentation
- Sample documents
- Startup scripts
- Repository cleanup

Enjoy building financial literacy! 💰📚
