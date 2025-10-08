# 🚀 Quick Start Guide

## Two Ways to Run the Application

### Option 1: Simple Mode (Recommended - No API Key Needed) ⭐

**Perfect for testing and development without any external dependencies!**

```bash
# Terminal 1 - Backend (Simple Mode)
cd backend
source .venv/bin/activate
uvicorn main_simple:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend
cd frontend
npm run dev
```

**Features:**
- ✅ Works immediately, no configuration needed
- ✅ Sample quiz questions for all 6 courses
- ✅ Pre-written financial scenarios
- ✅ No rate limits or API costs
- ❌ Not AI-generated (uses curated content)

### Option 2: Full AI Mode (Requires HuggingFace API)

**For AI-generated content using RAG technology**

```bash
# 1. Get free HuggingFace token
# Visit: https://huggingface.co/settings/tokens

# 2. Add token to backend/.env
echo "HUGGINGFACEHUB_API_TOKEN=your_token_here" > backend/.env

# 3. Start backend with full RAG
cd backend
source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 4. Start frontend
cd frontend
npm run dev
```

**Features:**
- ✅ AI-generated quiz questions
- ✅ Dynamic scenario generation
- ✅ RAG-powered responses from documents
- ⚠️ Subject to HuggingFace rate limits (free tier)
- ⚠️ Requires internet connection

## 🎯 Access the Application

Once both servers are running:

- **Frontend**: http://localhost:5173 or http://localhost:5174
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🆘 Troubleshooting

### "Rate limit" error from HuggingFace
**Solution**: Use Simple Mode (`main_simple.py`) instead of full RAG mode

### Quiz shows "Unable to Load"
**Solution**: Make sure backend is running on port 8000
```bash
curl http://localhost:8000/health
# Should return: {"status":"ok"}
```

### Frontend won't start
**Solution**: Install dependencies first
```bash
cd frontend
npm install
npm run dev
```

### Backend dependencies missing
**Solution**: Install Python packages
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 📊 What's the Difference?

| Feature | Simple Mode | Full AI Mode |
|---------|-------------|--------------|
| Setup Time | Instant | 5-10 minutes |
| API Key Required | ❌ No | ✅ Yes |
| Cost | Free | Free (with limits) |
| Content Quality | Curated | AI-generated |
| Rate Limits | None | Yes (free tier) |
| Internet Required | No | Yes |
| Best For | Testing, Demo | Production, Research |

## 💡 Recommendation

**Start with Simple Mode** to explore the application, then upgrade to Full AI Mode when you:
- Have a HuggingFace API token
- Need dynamic AI-generated content
- Want to experiment with RAG technology

## 🎓 Sample Content in Simple Mode

**Quiz Questions:**
1. Budgeting: "What is the 50/30/20 budgeting rule?"
2. Emergency Fund: "Why is an emergency fund important?"
3. Investing: "What's the difference between stocks and bonds?"
4. Debt: "Strategies to pay off high-interest debt?"
5. Retirement: "Traditional IRA vs Roth IRA?"
6. Taxes: "Common tax deductions for individuals?"

**Scenarios:**
- Market Crash
- Emergency Fund
- Job Loss
- Debt Management

All content is educational and based on financial literacy best practices!

---

**You're ready to go! Start with Simple Mode and enjoy the app! 🎉**
