from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities import DebateResult

class ThinkingBrain(ABC):
    """
    Interface for the 'Brain' that performs the thinking (debate) process.
    """
    @abstractmethod
    def think(self, topic: str, model_name: Optional[str] = None) -> str:
        """
        Executes the thinking process and returns the final conclusion.
        """
        pass

    @abstractmethod
    async def think_stream(self, topic: str, model_name: Optional[str] = None):
        """
        Executes the thinking process and yields text chunks (AsyncIterator).
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

    @abstractmethod
    def list_debates(self, limit: int = 10) -> List[DebateResult]:
        """
        Returns a list of recent debates.
        """
        pass

    @abstractmethod
    def get_debate(self, topic: str) -> Optional[DebateResult]:
        """
        Retrieves a specific debate by topic.
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
