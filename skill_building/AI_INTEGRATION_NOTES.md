# AI Integration Notes

## Current Status

### ✅ What's Working

**Simple Mode (main_simple.py)**
- Fully functional backend without external AI APIs
- 6 pre-written quiz questions (one per course)
- 4 pre-written financial scenarios
- No rate limits, instant responses
- Perfect for demos and testing

**RAG Pipeline Infrastructure**
- ✅ Document loading (3 TXT + 3 PDF files = 275 chunks)
- ✅ FAISS vector store created successfully
- ✅ Hybrid retrieval (FAISS + BM25) configured
- ✅ Embeddings working (sentence-transformers/all-MiniLM-L6-v2)
- ✅ HuggingFace API token configured

### ⚠️ Known Issues with Full AI Mode

**HuggingFace Inference API Limitations**
- Free tier has strict rate limits
- Many models not available for text-generation task
- Provider compatibility issues with some models
- Tested models:
  - ❌ `mistralai/Mixtral-8x7B-Instruct-v0.1` - Not supported for text-generation
  - ❌ `mistralai/Mistral-7B-Instruct-v0.2` - Provider compatibility issues
  - ❌ `google/flan-t5-large` - StopIteration error

## Solutions & Alternatives

### Option 1: Use Simple Mode (Recommended for Now)
```bash
uvicorn main_simple:app --reload --port 8000
```
- No API dependencies
- Instant startup
- Reliable and fast

### Option 2: Local LLM (Future Enhancement)
Use Ollama or similar for local inference:
```python
from langchain_community.llms import Ollama
llm = Ollama(model="mistral")
```

**Pros:**
- No API costs or rate limits
- Complete privacy
- Works offline

**Cons:**
- Requires powerful hardware (8GB+ RAM)
- Slower inference on CPU
- Need to download models (~4GB each)

### Option 3: OpenAI API (Paid but Reliable)
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
```

**Pros:**
- Very reliable
- Fast responses
- High quality outputs

**Cons:**
- Costs money (~$0.002 per 1K tokens)
- Requires OpenAI API key

### Option 4: Other Free APIs
- **Groq**: Fast inference, free tier available
- **Together AI**: Multiple open-source models
- **Replicate**: Pay-per-use, good for testing

## Technical Details

### RAG Pipeline Components

**Documents Loaded:**
- `budgeting_basics.txt` - 50/30/20 rule, envelope system, zero-based budgeting
- `investing_fundamentals.txt` - Stocks, bonds, ETFs, retirement accounts
- `emergency_fund.txt` - 3-6 months expenses, where to keep it
- 3 PDF files on financial literacy standards

**Embedding Model:**
- `sentence-transformers/all-MiniLM-L6-v2`
- Fast, lightweight (80MB)
- Good general-purpose embeddings

**Vector Store:**
- FAISS index saved to `backend/rag/faiss_index/`
- 275 document chunks
- Hybrid retrieval: 70% semantic (FAISS) + 30% keyword (BM25)

### File Structure
```
backend/
├── main.py              # Full RAG mode (needs working LLM)
├── main_simple.py       # Simple mode (no AI needed) ⭐
├── rag/
│   ├── pipeline.py      # RAG implementation
│   ├── documents/       # Source documents
│   └── faiss_index/     # Vector store (generated)
├── requirements.txt     # Python dependencies
└── .env                 # API tokens
```

## Recommendations

### For Development & Testing
**Use Simple Mode** - It's fast, reliable, and demonstrates all features

### For Production with AI
1. **Best**: Set up local Ollama with Mistral/Llama models
2. **Alternative**: Use OpenAI API (small cost but very reliable)
3. **Budget**: Try Groq or Together AI free tiers

### To Switch to Local LLM (Ollama)

1. Install Ollama:
```bash
# macOS
brew install ollama

# Start Ollama service
ollama serve

# Pull a model
ollama pull mistral
```

2. Update `pipeline.py`:
```python
from langchain_community.llms import Ollama
llm = Ollama(model="mistral", temperature=0.7)
```

3. Restart backend:
```bash
uvicorn main:app --reload --port 8000
```

## What We Built

✅ Complete Vue 3 frontend with beautiful UI
✅ FastAPI backend with CORS configured
✅ RAG pipeline with hybrid retrieval
✅ Document processing (TXT + PDF)
✅ Vector store with FAISS
✅ Simple mode for instant functionality
✅ Error handling and graceful fallbacks
✅ Comprehensive documentation

The infrastructure is solid - we just need a reliable LLM endpoint!

## Next Steps

1. **Short term**: Use Simple Mode for demos
2. **Medium term**: Set up Ollama for local AI
3. **Long term**: Consider paid API for production quality

---

**Bottom Line**: Your app is fully functional in Simple Mode. The RAG infrastructure is ready - we just need a better LLM provider than HuggingFace's free tier.
