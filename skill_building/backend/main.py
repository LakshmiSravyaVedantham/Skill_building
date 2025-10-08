from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from rag.pipeline import query_rag, hybrid_retriever
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Skill Building API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup - Using SQLite for simplicity
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./skill_building.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    skill_level = Column(Float, default=0.5)

Base.metadata.create_all(bind=engine)

class ScenarioRequest(BaseModel):
    topic: str

# Health Check Endpoint
@app.get("/")
def health_check():
    return {"status": "healthy", "message": "Skill Building API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Updated Quiz Endpoint
@app.get("/quiz/{course_id}")
def get_quiz(course_id: int):
    try:
        # Example: Adapt question based on course/user
        question = "What are key budgeting strategies for beginners?"  # Dynamic in full impl
        result = query_rag(question, hybrid_retriever)
        return {
            "questions": [result["result"]], 
            "sources": [doc.page_content for doc in result["source_documents"]]
        }
    except Exception as e:
        return {"error": str(e), "questions": [], "sources": []}

# Updated Scenario Endpoint
@app.post("/generate/scenario")
def generate_scenario(request: ScenarioRequest):
    try:
        result = query_rag(request.topic, hybrid_retriever)
        return {
            "scenario": result["result"], 
            "sources": [doc.page_content for doc in result["source_documents"]]
        }
    except Exception as e:
        return {"error": str(e), "scenario": "Unable to generate scenario", "sources": []}

# Run: uvicorn main:app --reload --host 0.0.0.0 --port 8000