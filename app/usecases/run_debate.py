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

    async def execute_stream(self, topic: str):
        """
        Orchestrates the debate in streaming mode.
        Yields chunks as they are generated, then saves/triggers at the end.
        """
        print(f"\nThinking (Stream) about '{topic}'...\n")
        
        full_content = ""
        
        # 1. Stream from Brain
        async for chunk in self.brain.think_stream(topic):
            full_content += chunk
            yield chunk
            
        # 2. Post-processing (same as execute)
        result = DebateResult(topic=topic, content=full_content)
        
        # 3. Save to Memory
        # Note: These are blocking calls, running in the event loop. 
        # For a production system, these should be async or run_in_executor.
        saved_path = self.memory.save(result)
        result.metadata["saved_path"] = saved_path
        print(f"\n[System]: Archived discussion to {saved_path}")
        
        # 4. Trigger Nervous System
        self.nerve.trigger(result)

