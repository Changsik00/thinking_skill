# tests/unit/usecases/test_run_debate.py
from app.usecases.run_debate import RunDebateUseCase
from tests.mocks.fake_adapters import FakeBrain, FakeMemory, FakeNerve


def test_run_debate_flow():
    # Given (Arrange)
    brain = FakeBrain(response="Mock Content")
    memory = FakeMemory()
    nerve = FakeNerve()
    use_case = RunDebateUseCase(brain=brain, memory=memory, nerve=nerve)

    # 1. Test execution flow
    topic = "Any Topic"
    result = use_case.execute(topic)

    assert result.topic == topic
    assert result.content == "Mock Content"
    # Logic Update (Spec 013): UseCase no longer auto-saves.
    # FakeBrain does not invoke tools, so nothing should be saved.
    assert len(memory.saved_items) == 0
    # Nerve should still be triggered (if implemented in UseCase)
    # Checking implementation: UseCase calls nerve.trigger(result)
    assert nerve.triggered_count == 1
