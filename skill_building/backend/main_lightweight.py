from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Skill Building API - Lightweight", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
        "https://frontend-j4akmsr1p-sravyas-projects-f5209810.vercel.app",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScenarioRequest(BaseModel):
    topic: str

# Health Check
@app.get("/")
def health_check():
    return {"status": "healthy", "message": "Skill Building API - Lightweight Mode"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Lightweight Quiz - Uses HuggingFace API directly without RAG
@app.get("/quiz/{course_id}")
async def get_quiz(course_id: int):
    from huggingface_hub import InferenceClient
    
    try:
        client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
        
        # Course-specific prompts
        prompts = {
            1: "Generate one concise quiz question about budgeting strategies for beginners, specifically about the 50/30/20 rule.",
            2: "Generate one concise quiz question about emergency funds and why they are important.",
            3: "Generate one concise quiz question about the difference between stocks and bonds.",
            4: "Generate one concise quiz question about strategies to pay off high-interest debt.",
            5: "Generate one concise quiz question about retirement planning and IRA accounts.",
            6: "Generate one concise quiz question about common tax deductions for individuals."
        }
        
        prompt = prompts.get(course_id, "Generate a financial literacy quiz question.")
        
        # Use a lightweight model
        response = client.text_generation(
            prompt,
            model="HuggingFaceH4/zephyr-7b-beta",
            max_new_tokens=150,
            temperature=0.7
        )
        
        return {
            "questions": [response.strip()],
            "sources": ["Generated using HuggingFace Zephyr-7B model"]
        }
    except Exception as e:
        # Fallback to curated questions
        fallback_questions = {
            1: "What is the 50/30/20 budgeting rule and how does it help manage personal finances?",
            2: "Why is an emergency fund important and how many months of expenses should it cover?",
            3: "What is the difference between stocks and bonds in an investment portfolio?",
            4: "What strategies can help you pay off high-interest debt faster?",
            5: "What are the key differences between a Traditional IRA and a Roth IRA?",
            6: "What tax deductions are commonly available for individuals?"
        }
        
        return {
            "questions": [fallback_questions.get(course_id, "What are the basic principles of financial literacy?")],
            "sources": [f"Fallback mode - Error: {str(e)}"]
        }

# Lightweight Scenario Generator
@app.post("/generate/scenario")
async def generate_scenario(request: ScenarioRequest):
    from huggingface_hub import InferenceClient
    
    try:
        client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
        
        prompt = f"Generate a realistic financial scenario about: {request.topic}. Include the situation and 2-3 action steps someone should consider. Keep it under 200 words."
        
        response = client.text_generation(
            prompt,
            model="HuggingFaceH4/zephyr-7b-beta",
            max_new_tokens=250,
            temperature=0.7
        )
        
        return {
            "scenario": response.strip(),
            "sources": ["Generated using HuggingFace Zephyr-7B model"]
        }
    except Exception as e:
        # Fallback scenarios
        scenarios = {
            "market crash": "Scenario: The stock market has dropped 20% in one week. Your retirement portfolio has lost significant value. What should you do? Consider: 1) Don't panic sell, 2) Review your asset allocation, 3) Consider if you need to rebalance, 4) Remember your long-term goals.",
            "emergency fund": "Scenario: Your car breaks down and needs $1,500 in repairs. You have $2,000 in your emergency fund. How do you handle this? Consider: 1) Use emergency fund for the repair, 2) Get quotes from multiple mechanics, 3) Plan to rebuild the fund, 4) Review your budget.",
            "job loss": "Scenario: You've been laid off unexpectedly. You have 3 months of expenses saved. What's your action plan? Consider: 1) File for unemployment, 2) Cut non-essential expenses, 3) Update resume and start job search, 4) Consider temporary work.",
            "debt": "Scenario: You have $10,000 in credit card debt at 18% APR. How do you tackle this? Consider: 1) Stop using credit cards, 2) Pay more than minimum, 3) Consider debt avalanche or snowball method, 4) Look into balance transfer options."
        }
        
        topic_lower = request.topic.lower()
        for key in scenarios:
            if key in topic_lower:
                return {"scenario": scenarios[key], "sources": ["Curated content"]}
        
        return {
            "scenario": f"Sample scenario for '{request.topic}': This is placeholder content. API error: {str(e)}",
            "sources": ["Fallback mode"]
        }

# Run: uvicorn main_lightweight:app --host 0.0.0.0 --port $PORT
