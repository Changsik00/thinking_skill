# app/domain/entities.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class DebateResult:
    """
    Represents the final outcome of a debate/discussion.
    """
    topic: str
    content: str  # Final conclusion or summary
    model: str = "macs-agent"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    metadata: dict = field(default_factory=dict)
