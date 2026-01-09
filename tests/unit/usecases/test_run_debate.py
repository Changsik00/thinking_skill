# tests/unit/usecases/test_run_debate.py
import pytest
from app.usecases.run_debate import RunDebateUseCase
from tests.mocks.fake_adapters import FakeBrain, FakeMemory, FakeNerve

def test_run_debate_flow():
    # Given (Arrange)
    brain = FakeBrain(response="Mock Content")
    memory = FakeMemory()
    nerve = FakeNerve()
    use_case = RunDebateUseCase(brain=brain, memory=memory, nerve=nerve)

    # 1. Test with keyword (Should Save)
    topic_save = "TDD 저장 practice"
    result_save = use_case.execute(topic_save)
    
    assert result_save.topic == topic_save
    assert len(memory.saved_items) == 1
    assert result_save.metadata["saved_path"].startswith("/mock/path/")
    assert nerve.triggered_count == 1

    # 2. Test without keyword (Should NOT Save)
    topic_nosave = "Just Chatting"
    result_nosave = use_case.execute(topic_nosave)
    
    assert len(memory.saved_items) == 1  # Still 1 (no new save)
    assert nerve.triggered_count == 2    # Triggered twice (always triggers)
