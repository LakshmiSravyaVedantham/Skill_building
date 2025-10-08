# 💰 Financial Literacy Skill Building Platform

An AI-powered financial literacy platform that uses RAG (Retrieval-Augmented Generation) technology to provide personalized learning experiences, adaptive quizzes, and real-world financial scenarios.

> **🚀 NEW: Simple Mode Available!** Run the app instantly without any API keys. See [QUICK_START.md](QUICK_START.md) for details.

## 🌟 Features

- **AI-Powered Learning**: Leverages RAG with HuggingFace models for accurate, context-aware financial education
- **Adaptive Quizzes**: Questions tailored to your skill level
- **Real-World Scenarios**: Practice decision-making with realistic financial situations
- **Comprehensive Topics**: Budgeting, investing, emergency funds, debt management, and more
- **Modern UI**: Built with Vue 3 and Tailwind CSS for a beautiful, responsive experience

## 🏗️ Architecture

### Backend
- **FastAPI**: High-performance Python web framework
- **LangChain**: RAG pipeline orchestration
- **HuggingFace**: LLM (Mixtral-8x7B) and embeddings (FinE5)
- **FAISS**: Vector database for semantic search
- **BM25**: Sparse retrieval for keyword matching
- **SQLite**: Lightweight database for user data

### Frontend
- **Vue 3**: Progressive JavaScript framework
- **Vite**: Next-generation frontend tooling
- **Tailwind CSS**: Utility-first CSS framework
- **Vue Router**: Client-side routing
- **Axios**: HTTP client for API calls

## 📋 Prerequisites

- Python 3.9+
- Node.js 18+
- HuggingFace API Token (free at https://huggingface.co/settings/tokens)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/LakshmiSravya123/Skill_building.git
cd Skill_building
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your HuggingFace API token:
# HUGGINGFACEHUB_API_TOKEN=your_token_here
```

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 5. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📁 Project Structure

```
skill_building/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables (not in git)
│   ├── .env.example           # Environment template
│   └── rag/
│       ├── pipeline.py        # RAG implementation
│       └── documents/         # Financial literacy documents
│           ├── budgeting_basics.txt
│           ├── investing_fundamentals.txt
│           └── emergency_fund.txt
├── frontend/
│   ├── package.json           # Node dependencies
│   ├── vite.config.js         # Vite configuration
│   ├── tailwind.config.js     # Tailwind CSS config
│   ├── index.html             # Entry HTML
│   └── src/
│       ├── main.js            # Vue app entry
│       ├── App.vue            # Root component
│       ├── router/
│       │   └── index.js       # Route definitions
│       ├── views/
│       │   ├── Home.vue       # Landing page
│       │   └── Courses.vue    # Course catalog
│       └── components/
│           ├── Quiz.vue       # Adaptive quiz
│           └── Scenario.vue   # Financial scenarios
└── README.md
```

## 🔧 Configuration

### Backend Configuration

Edit `backend/.env`:

```env
# Required: HuggingFace API Token
HUGGINGFACEHUB_API_TOKEN=your_token_here

# Optional: Database (defaults to SQLite)
DATABASE_URL=sqlite:///./skill_building.db

# For PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Frontend Configuration

The frontend is pre-configured to proxy API requests to `http://localhost:8000`. If your backend runs on a different port, edit `frontend/vite.config.js`:

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:YOUR_PORT',
      // ...
    }
  }
}
```

## 📚 API Endpoints

### Health Check
- `GET /` - API status
- `GET /health` - Health check

### Quiz
- `GET /quiz/{course_id}` - Get quiz questions for a course

### Scenarios
- `POST /generate/scenario` - Generate financial scenario
  ```json
  {
    "topic": "Market Crash"
  }
  ```

## 🧪 Testing the RAG Pipeline

Test the RAG system directly:

```bash
cd backend
python -m rag.pipeline
```

This will run a sample query and display results.

## 🐛 Troubleshooting

### Backend Issues

**Issue**: `ModuleNotFoundError: No module named 'langchain'`
- **Solution**: Ensure virtual environment is activated and dependencies are installed:
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**Issue**: `Error loading documents`
- **Solution**: Verify documents exist in `backend/rag/documents/`

**Issue**: `HuggingFace API token not found`
- **Solution**: Add your token to `backend/.env`:
  ```
  HUGGINGFACEHUB_API_TOKEN=your_token_here
  ```

### Frontend Issues

**Issue**: `Cannot find module 'vue'`
- **Solution**: Install dependencies:
  ```bash
  npm install
  ```

**Issue**: API requests fail with CORS error
- **Solution**: Ensure backend is running on port 8000 and CORS is configured in `main.py`

**Issue**: `Failed to resolve import`
- **Solution**: Clear cache and reinstall:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

## 🔒 Security Notes

- Never commit `.env` files to version control
- The `.env` file contains sensitive API tokens
- Use `.env.example` as a template for team members
- For production, use environment variables or secret management services

## 🚀 Deployment

### Backend Deployment
- Use services like Railway, Render, or AWS
- Set environment variables in the platform
- Ensure Python 3.9+ is available
- Install dependencies from `requirements.txt`

### Frontend Deployment
- Build the frontend: `npm run build`
- Deploy the `dist/` folder to Netlify, Vercel, or similar
- Update API proxy configuration for production backend URL

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👥 Authors

- LakshmiSravya123

## 🙏 Acknowledgments

- HuggingFace for LLM and embedding models
- LangChain for RAG framework
- FastAPI for the backend framework
- Vue.js team for the frontend framework

## 📧 Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions

---

**Happy Learning! 💡📚**
