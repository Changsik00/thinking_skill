# app/interfaces/api/schemas.py
from pydantic import BaseModel
from typing import Dict, Any

class DebateRequest(BaseModel):
    topic: str

class DebateResponse(BaseModel):
    topic: str
    content: str
    created_at: str
    metadata: Dict[str, Any] = {}
