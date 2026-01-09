# app/usecases/run_debate.py
from app.domain.entities import DebateResult
from app.domain.interfaces import ThinkingBrain, MemoryVault, NerveSystem

class RunDebateUseCase:
    """
    Coordinator (Interactor) for the Debate process.
    Connects Domain Entities with Infrastructure implementations via Interfaces.
    """
    def __init__(
        self,
        brain: ThinkingBrain,
        memory: MemoryVault,
        nerve: NerveSystem
    ):
        self.brain = brain
        self.memory = memory
        self.nerve = nerve

    def execute(self, topic: str) -> DebateResult:
        print(f"\nThinking about '{topic}'...\n")
        
        # 1. Ask the Brain to think (Core Logic)
        content = self.brain.think(topic)
        
        # 2. Create Domain Entity
        result = DebateResult(topic=topic, content=content)
        
        # 3. Save to Memory (Persistence)
        saved_path = self.memory.save(result)
        result.metadata["saved_path"] = saved_path
        print(f"\n[System]: Archived discussion to {saved_path}")
        
        # 4. Trigger Nervous System (Automation)
        self.nerve.trigger(result)
        
        return result
