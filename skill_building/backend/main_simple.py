from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Skill Building API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScenarioRequest(BaseModel):
    topic: str

# Health Check Endpoint
@app.get("/")
def health_check():
    return {"status": "healthy", "message": "Skill Building API is running (Simple Mode - No RAG)"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Sample Quiz Endpoint (without RAG)
@app.get("/quiz/{course_id}")
def get_quiz(course_id: int):
    # Sample questions based on course_id
    questions_map = {
        1: "What is the 50/30/20 budgeting rule and how does it help manage personal finances?",
        2: "Why is an emergency fund important and how many months of expenses should it cover?",
        3: "What is the difference between stocks and bonds in an investment portfolio?",
        4: "What strategies can help you pay off high-interest debt faster?",
        5: "What are the key differences between a Traditional IRA and a Roth IRA?",
        6: "What tax deductions are commonly available for individuals?"
    }
    
    question = questions_map.get(course_id, "What are the basic principles of financial literacy?")
    
    return {
        "questions": [question],
        "sources": [
            "This is sample data. For AI-generated content, configure the HuggingFace API token in backend/.env",
            "Visit https://huggingface.co/settings/tokens to get your free API token"
        ]
    }

# Sample Scenario Endpoint (without RAG)
@app.post("/generate/scenario")
def generate_scenario(request: ScenarioRequest):
    scenarios = {
        "market crash": "Scenario: The stock market has dropped 20% in one week. Your retirement portfolio has lost significant value. What should you do? Consider: 1) Don't panic sell, 2) Review your asset allocation, 3) Consider if you need to rebalance, 4) Remember your long-term goals.",
        "emergency fund": "Scenario: Your car breaks down and needs $1,500 in repairs. You have $2,000 in your emergency fund. How do you handle this? Consider: 1) Use emergency fund for the repair, 2) Get quotes from multiple mechanics, 3) Plan to rebuild the fund, 4) Review your budget to prevent future shortfalls.",
        "job loss": "Scenario: You've been laid off unexpectedly. You have 3 months of expenses saved. What's your action plan? Consider: 1) File for unemployment, 2) Cut non-essential expenses, 3) Update resume and start job search, 4) Consider temporary work, 5) Review health insurance options.",
        "debt": "Scenario: You have $10,000 in credit card debt at 18% APR. How do you tackle this? Consider: 1) Stop using credit cards, 2) Pay more than minimum, 3) Consider debt avalanche or snowball method, 4) Look into balance transfer options, 5) Create a strict budget."
    }
    
    topic_lower = request.topic.lower()
    scenario = scenarios.get(topic_lower, f"Sample scenario for '{request.topic}': This is placeholder content. Configure HuggingFace API for AI-generated scenarios.")
    
    return {
        "scenario": scenario,
        "sources": ["Sample data - Configure HuggingFace API token for AI-generated content"]
    }

# Run: uvicorn main_simple:app --reload --host 0.0.0.0 --port 8000
