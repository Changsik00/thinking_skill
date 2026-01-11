import pytest
from typing import List, Optional, Any
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.runnables import RunnableLambda

from app.domain.entities import DebateResult
from app.domain.interfaces import MemoryVault
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain

# Mock Memory Vault
class MockVault(MemoryVault):
    def __init__(self):
        self.saved_items = []

    def save(self, result: DebateResult) -> str:
        self.saved_items.append(result)
        return f"mock/path/{len(self.saved_items)}"

    def list_debates(self, limit: int = 10) -> List[DebateResult]:
        return []

    def get_debate(self, topic: str) -> Optional[DebateResult]:
        return None

# Mock Brain to bypass API
class MockLangGraphBrain(LangGraphBrain):
    def _get_llm(self, config):
        # Return a Mock Runnable that mimics LLM behavior based on input
        def mock_invoke(input_data: Any, **kwargs):
            messages = input_data
            last_msg = messages[-1]
            
            # Check if last msg is ToolMessage -> Return Final Response
            if isinstance(last_msg, ToolMessage):
                return AIMessage(content="I have saved the debate as requested.")
            
            # Extract content from all messages to find the trigger
            full_text = " ".join([m.content for m in messages if hasattr(m, "content")]).lower()
            
            # Heuristic: Check for "save" and "important"
            if "save" in full_text and "important" in full_text:
                return AIMessage(
                    content="",
                    tool_calls=[{
                        "name": "save_debate",
                        "args": {"topic": "Quantum Computing", "content": "Mocked Content"},
                        "id": "call_123"
                    }]
                )
            
            # Default response
            return AIMessage(content="This is a casual response.")
            
        return RunnableLambda(mock_invoke).bind(tools=[self._create_save_tool()])

@pytest.mark.asyncio
async def test_casual_conversation_no_save():
    """Verify that casual conversation does NOT trigger save."""
    mock_memory = MockVault()
    brain = MockLangGraphBrain(memory=mock_memory)
    
    topic = "What is the capital of France?"
    response = brain.think(topic)
    
    assert "casual response" in response
    assert len(mock_memory.saved_items) == 0

@pytest.mark.asyncio
async def test_explicit_save_request():
    """Verify that explicit save request logic triggers save_debate tool."""
    mock_memory = MockVault()
    brain = MockLangGraphBrain(memory=mock_memory)
    
    topic = "Explain Quantum Computing briefly. This is important, please save this debate."
    response = brain.think(topic)
    
    assert "saved the debate" in response
    assert len(mock_memory.saved_items) == 1
    assert mock_memory.saved_items[0].topic == "Quantum Computing"
