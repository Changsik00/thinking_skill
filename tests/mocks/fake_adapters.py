# tests/mocks/fake_adapters.py
from typing import List, Optional

from app.domain.entities import DebateResult
from app.domain.interfaces import MemoryVault, NerveSystem, ThinkingBrain


class FakeBrain(ThinkingBrain):
    def __init__(self, response: str = "Fake Debate Conclusion"):
        self.response = response
        self.call_count = 0
        self.last_topic = ""

    def think(self, topic: str, model_name: Optional[str] = None) -> str:
        self.call_count += 1
        self.last_topic = topic
        return self.response

    async def think_stream(self, topic: str, model_name: Optional[str] = None):
        self.call_count += 1
        self.last_topic = topic
        yield self.response


class FakeMemory(MemoryVault):
    def __init__(self):
        self.saved_items: List[DebateResult] = []

    def save(self, result: DebateResult) -> str:
        self.saved_items.append(result)
        return f"/mock/path/{len(self.saved_items)}.md"

    def list_debates(self, limit: int = 10) -> List[DebateResult]:
        return self.saved_items[:limit]

    def get_debate(self, topic: str) -> Optional[DebateResult]:
        for item in self.saved_items:
            if item.topic == topic:
                return item
        return None


class FakeNerve(NerveSystem):
    def __init__(self):
        self.triggered_count = 0
        self.last_triggered_result = None

    def trigger(self, result: DebateResult) -> None:
        self.triggered_count += 1
        self.last_triggered_result = result
