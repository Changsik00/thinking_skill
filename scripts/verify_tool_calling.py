import sys
import os
import asyncio
from typing import List, Optional, Any
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.domain.entities import DebateResult
from app.domain.interfaces import ThinkingBrain, MemoryVault
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain

# Mock Imports for testing logic
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.runnables import RunnableLambda

# Mock Memory Vault
class MockVault(MemoryVault):
    def __init__(self):
        self.saved_items = []

    def save(self, result: DebateResult) -> str:
        print(f"MockVault: Saving result about '{result.topic}'")
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
            # 'input_data' is a list of messages
            messages = input_data
            last_msg = messages[-1]
            
            # Check if last msg is ToolMessage -> Return Final Response
            if isinstance(last_msg, ToolMessage):
                return AIMessage(content="I have saved the debate as requested.")
            
            # If HumanMessage or SystemMessage -> Check Content
            # In our graph, input to LLM is [Sys, ... messages, Trigger?]
            # We look for user intent in the prompt or history.
            
            # Simple heuristic: Check if any message contains "save" and "important"
            # In a real scenario, LLM checks context.
            full_text = " ".join([m.content for m in messages if hasattr(m, "content")]).lower()
            
            if "save" in full_text and "important" in full_text:
                print("MockLLM: Generating Tool Call for 'save_debate'")
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
            
        # Bind tools to the mock runnable (for compatibility, though our mock_invoke returns tool calls manually)
        return RunnableLambda(mock_invoke).bind(tools=[self._create_save_tool()])

async def verify():
    load_dotenv()
    print("--- Verifying Selective Archiving (Spec 013) with MOCKED LLM ---")
    
    mock_memory = MockVault()
    # Use the Mock Brain that overrides _get_llm
    brain = MockLangGraphBrain(memory=mock_memory)
    
    # Test 1: Casual conversation (Expect: NO Save)
    print("\n[Test 1] Casual Conversation (Expect: NO Save)")
    topic1 = "What is the capital of France?"
    response1 = brain.think(topic1)
    print(f"Response: {response1}")
    
    if len(mock_memory.saved_items) == 0:
        print("✅ Passed: No save triggered for casual topic.")
    else:
        print(f"❌ Failed: Saved {len(mock_memory.saved_items)} items unexpectedly.")

    # Test 2: Explicit Save Request (Expect: YES Save)
    print("\n[Test 2] Explicit Save Request (Expect: YES Save)")
    topic2 = "Explain Quantum Computing briefly. This is important, please save this debate."
    response2 = brain.think(topic2) 
    print(f"Response: {response2}")
    
    if len(mock_memory.saved_items) == 1:
        print("✅ Passed: Save triggered by user request.")
        saved_item = mock_memory.saved_items[0]
        # In mock, we hardcoded topic="Quantum Computing" in tool args
        print(f"   Saved Topic: {saved_item.topic}")
    else:
        print(f"❌ Failed: Expected 1 saved item, got {len(mock_memory.saved_items)}.")

if __name__ == "__main__":
    asyncio.run(verify())
