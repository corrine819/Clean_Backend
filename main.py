from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class PlanRequest(BaseModel):
    goal: str
    energy_level: int
    days_per_week: int
    equipment: str
    fitness_level: str
    injuries: str

# Routes
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/generate_multi_day_plan")
def generate_multi_day_plan(request: PlanRequest) -> Dict:
    # Placeholder logic
    plan = {
        "days": [
            {"day": 1, "workout": "Full Body Workout", "nutrition": "High Protein Meals"},
            {"day": 2, "workout": "Cardio & Core", "nutrition": "Balanced Meals"},
            {"day": 3, "workout": "Upper Body Strength", "nutrition": "Low Carb Meals"},
        ]
    }
    return {"plan": plan}