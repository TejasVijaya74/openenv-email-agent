# env/models.py
from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    email_text: str
    step_count: int

class Action(BaseModel):
    intent: str
    priority: str
    response: str

class Reward(BaseModel):
    score: float
    feedback: Optional[str]