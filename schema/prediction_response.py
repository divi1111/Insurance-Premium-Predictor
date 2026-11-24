from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str=(Field(...,description="The predicted insurance premium category", example="High"))

    confidence : float= Field(..., description="Model's confident score for the predicted class ranges from 0 to 1")
    class_probabilties : Dict[str, float]=Field(...,description="Probabilties distribution across all possible classes", example={"Low":0.15,"Medium": 0.01,"High":0.84})