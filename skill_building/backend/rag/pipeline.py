from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.retrievers import BM25Retriever, EnsembleRetriever
import os
from dotenv import load_dotenv

load_dotenv()

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
        # Get the directory of this script
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

# Initialize components with advanced embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Use lighter, faster embedding model for quicker startup
# You can switch to "FinanceMTEB/FinE5" for finance-specific embeddings (slower first load)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Use HuggingFace with conversational model
llm_endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# Wrap in ChatHuggingFace for better compatibility
llm = ChatHuggingFace(llm=llm_endpoint)

# Build hybrid vector store
def build_hybrid_retriever(docs):
    splits = text_splitter.split_documents(docs)
    
    # Dense retriever (FAISS)
    dense_store = FAISS.from_documents(splits, embeddings)
    dense_retriever = dense_store.as_retriever(search_kwargs={"k": 3})
    
    # Sparse retriever (BM25)
    sparse_retriever = BM25Retriever.from_documents(splits)
    sparse_retriever.k = 3
    
    # Hybrid: Ensemble with weights
    hybrid_retriever = EnsembleRetriever(
        retrievers=[dense_retriever, sparse_retriever],
        weights=[0.7, 0.3]  # Bias towards semantic (dense)
    )
    
    # Save FAISS index
    script_dir = os.path.dirname(os.path.abspath(__file__))
    faiss_path = os.path.join(script_dir, "faiss_index")
    dense_store.save_local(faiss_path)
    print(f"FAISS index saved to {faiss_path}")
    return hybrid_retriever

# RAG query function (now hybrid)
def query_rag(question, hybrid_retriever):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=hybrid_retriever,
        return_source_documents=True
    )
    return qa_chain({"query": question})

# Initialize on startup
try:
    print("Initializing RAG pipeline...")
    docs = load_documents()
    if len(docs) == 0:
        print("WARNING: No documents loaded. RAG system may not work properly.")
        hybrid_retriever = None
    else:
        hybrid_retriever = build_hybrid_retriever(docs)
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