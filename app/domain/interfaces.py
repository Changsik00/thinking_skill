# app/domain/interfaces.py
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities import DebateResult

class ThinkingBrain(ABC):
    """
    Interface for the 'Brain' that performs the thinking (debate) process.
    """
    @abstractmethod
    def think(self, topic: str) -> str:
        """
        Executes the thinking process and returns the final conclusion.
        """
        pass

class MemoryVault(ABC):
    """
    Interface for 'Memory' storage.
    """
    @abstractmethod
    def save(self, result: DebateResult) -> str:
        """
        Saves the debate result and returns a location identifier (e.g., file path or ID).
        """
        pass

class NerveSystem(ABC):
    """
    Interface for 'Nerve' system (automation triggers).
    """
    @abstractmethod
    def trigger(self, result: DebateResult) -> None:
        """
        Triggers external actions based on the result.
        """
        pass
