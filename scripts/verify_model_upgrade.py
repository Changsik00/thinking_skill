import asyncio
import os
import sys

from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.infrastructure.llm.langgraph_adapter import LangGraphBrain


async def verify():
    load_dotenv()

    print("--- 1. Checking Configuration ---")
    brain = LangGraphBrain()
    print(f"Default Model (from env): {brain.default_model_name}")

    expected_model = os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash-001")
    if brain.default_model_name == expected_model:
        print("✅ Default model matches .env")
    else:
        print(f"❌ Mismatch: Expected {expected_model}, got {brain.default_model_name}")

    print("\n--- 2. Checking Factory Method (Mocking Config) ---")
    # We can't easily mock the internal _get_llm call without invoking the graph,
    # but we can inspect the graph or run a mock invocation.

    # Let's run a dry invocation if possible, or just instantiate LLM manually using the logic in brain.
    # Actually, let's trust the integration test.

    # But we can try to inspect the LLM object created by _get_llm
    config = {"configurable": {"model_name": "gemini-1.5-flash"}}
    llm = brain._get_llm(config)
    print(f"Requested 'gemini-1.5-flash'. LLM Model: {llm.model}")

    if llm.model == "gemini-1.5-flash":
        print("✅ Dynamic Model Selection works (Factory level)")
    else:
        print(f"❌ Failed: Got {llm.model}")


if __name__ == "__main__":
    asyncio.run(verify())
