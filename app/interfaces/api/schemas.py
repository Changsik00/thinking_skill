# app/interfaces/api/schemas.py
from typing import Any, Dict

from pydantic import BaseModel


class DebateRequest(BaseModel):
    topic: str


class DebateResponse(BaseModel):
    topic: str
    content: str
    created_at: str
    metadata: Dict[str, Any] = {}
