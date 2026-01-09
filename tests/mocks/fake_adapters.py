# tests/mocks/fake_adapters.py
from typing import List, Dict
from app.domain.interfaces import ThinkingBrain, MemoryVault, NerveSystem
from app.domain.entities import DebateResult

class FakeBrain(ThinkingBrain):
    def __init__(self, response: str = "Fake Debate Conclusion"):
        self.response = response
        self.call_count = 0
        self.last_topic = ""

    def think(self, topic: str) -> str:
        self.call_count += 1
        self.last_topic = topic
        return self.response

    async def think_stream(self, topic: str):
        self.call_count += 1
        self.last_topic = topic
        yield self.response

class FakeMemory(MemoryVault):
    def __init__(self):
        self.saved_items: List[DebateResult] = []

    def save(self, result: DebateResult) -> str:
        self.saved_items.append(result)
        return f"/mock/path/{len(self.saved_items)}.md"

class FakeNerve(NerveSystem):
    def __init__(self):
        self.triggered_count = 0
        self.last_triggered_result = None

    def trigger(self, result: DebateResult) -> None:
        self.triggered_count += 1
        self.last_triggered_result = result
