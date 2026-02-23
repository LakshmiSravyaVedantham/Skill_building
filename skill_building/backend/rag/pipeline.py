import os
from dotenv import load_dotenv

load_dotenv()

# Langchain imports – wrapped so the module loads even when versions conflict
try:
    from langchain_community.document_loaders import PyPDFLoader, TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
    from langchain_core.prompts import PromptTemplate  # noqa: F401
    from langchain.chains import RetrievalQA
    from langchain_community.retrievers import BM25Retriever
    # EnsembleRetriever moved between packages across versions
    try:
        from langchain_community.retrievers import EnsembleRetriever
    except ImportError:
        from langchain.retrievers import EnsembleRetriever
    _LANGCHAIN_AVAILABLE = True
except ImportError as e:
    print(f"WARNING: langchain import error: {e}")
    _LANGCHAIN_AVAILABLE = False

# Check for HuggingFace API token
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not hf_token or hf_token == "your_token_here":
    print("WARNING: HuggingFace API token not set. Please add it to backend/.env")
    print("Get your token from: https://huggingface.co/settings/tokens")
else:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token


# Load and split documents
def load_documents(directory=None):
    if directory is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(script_dir, "documents")

    docs = []
    if not os.path.exists(directory):
        print(f"Warning: Documents directory not found at {directory}")
        return docs

    for file in os.listdir(directory):
        try:
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(directory, file))
                docs.extend(loader.load())
            elif file.endswith(".txt"):
                loader = TextLoader(os.path.join(directory, file))
                docs.extend(loader.load())
        except Exception as e:
            print(f"Error loading {file}: {e}")

    print(f"Loaded {len(docs)} documents from {directory}")
    return docs


def _init_langchain_components():
    """Initialize langchain components. Returns (text_splitter, embeddings, llm) or raises."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="conversational",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    llm = ChatHuggingFace(llm=llm_endpoint)
    return text_splitter, embeddings, llm


def build_hybrid_retriever(docs, text_splitter, embeddings):
    splits = text_splitter.split_documents(docs)

    # Dense retriever (FAISS)
    dense_store = FAISS.from_documents(splits, embeddings)
    dense_retriever = dense_store.as_retriever(search_kwargs={"k": 3})

    # Sparse retriever (BM25)
    sparse_retriever = BM25Retriever.from_documents(splits)
    sparse_retriever.k = 3

    # Hybrid: Ensemble with weights
    hybrid = EnsembleRetriever(
        retrievers=[dense_retriever, sparse_retriever],
        weights=[0.7, 0.3],
    )

    # Save FAISS index
    script_dir = os.path.dirname(os.path.abspath(__file__))
    faiss_path = os.path.join(script_dir, "faiss_index")
    dense_store.save_local(faiss_path)
    print(f"FAISS index saved to {faiss_path}")
    return hybrid


# RAG query function
def query_rag(question, retriever):
    if retriever is None:
        return {"result": "RAG system not available", "source_documents": []}
    qa_chain = RetrievalQA.from_chain_type(
        llm=_llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )
    return qa_chain({"query": question})


# ── Initialize on startup ────────────────────────────────────────────────────
hybrid_retriever = None
_llm = None

try:
    if not _LANGCHAIN_AVAILABLE:
        raise ImportError("langchain packages not fully available")
    print("Initializing RAG pipeline...")
    _text_splitter, _embeddings, _llm = _init_langchain_components()
    docs = load_documents()
    if len(docs) == 0:
        print("WARNING: No documents loaded. RAG system may not work properly.")
    else:
        hybrid_retriever = build_hybrid_retriever(docs, _text_splitter, _embeddings)
        print(f"RAG pipeline initialized successfully with {len(docs)} documents")
except Exception as e:
    print(f"ERROR initializing RAG pipeline: {e}")
    print("The API will still run but RAG features may not work.")
    hybrid_retriever = None

# Example usage
if __name__ == "__main__":
    question = "What are key budgeting strategies for beginners?"
    result = query_rag(question, hybrid_retriever)
    print(result["result"])
