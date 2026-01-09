# tests/unit/usecases/test_run_debate.py
import pytest
from app.usecases.run_debate import RunDebateUseCase
from tests.mocks.fake_adapters import FakeBrain, FakeMemory, FakeNerve

def test_run_debate_flow():
    # Given (Arrange)
    expected_topic = "TDD is great"
    expected_content = "Yes, it ensures reliability."
    
    brain = FakeBrain(response=expected_content)
    memory = FakeMemory()
    nerve = FakeNerve()
    
    use_case = RunDebateUseCase(brain=brain, memory=memory, nerve=nerve)
    
    # When (Act)
    result = use_case.execute(expected_topic)
    
    # Then (Assert)
    # 1. Check Result Integrity
    assert result.topic == expected_topic
    assert result.content == expected_content
    
    # 2. Check Brain Interaction
    assert brain.call_count == 1
    assert brain.last_topic == expected_topic
    
    # 3. Check Memory Persistence
    assert len(memory.saved_items) == 1
    saved_item = memory.saved_items[0]
    assert saved_item.topic == expected_topic
    assert saved_item.content == expected_content
    assert result.metadata["saved_path"].startswith("/mock/path/")
    
    # 4. Check Nerve Trigger
    assert nerve.triggered_count == 1
    assert nerve.last_triggered_result == result
