from typing import List, Optional
from app.domain.entities import DebateResult
from app.domain.interfaces import MemoryVault

class ListDebatesUseCase:
    def __init__(self, memory_vault: MemoryVault):
        self.memory_vault = memory_vault

    async def execute(self, limit: int = 10) -> List[DebateResult]:
        """
        Retrieves a list of recent debates.
        """
        return self.memory_vault.list_debates(limit=limit)

class GetDebateUseCase:
    def __init__(self, memory_vault: MemoryVault):
        self.memory_vault = memory_vault

    async def execute(self, topic: str) -> Optional[DebateResult]:
        """
        Retrieves details of a specific debate.
        """
        return self.memory_vault.get_debate(topic=topic)
