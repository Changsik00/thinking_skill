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

    def execute(self, topic: str, model_name: str = None) -> DebateResult:
        print(f"\nThinking about '{topic}' (Model: {model_name or 'Default'})...\n")
        
        # 1. Ask the Brain to think (Core Logic)
        content = self.brain.think(topic, model_name=model_name)
        
        # 2. Create Domain Entity
        result = DebateResult(topic=topic, content=content, model=model_name or "Default")
        
        # 3. Save to Memory (Conditional)
        # 3. Save to Memory (Conditional)
        # LEGACY: Auto-save logic removed in Spec 013.
        # Saving is now handled by the Brain via 'save_debate' tool call.
        
        # 4. Trigger Nervous System (Automation)
        self.nerve.trigger(result)
        
        return result

    async def execute_stream(self, topic: str, model_name: str = None):
        """
        Orchestrates the debate in streaming mode.
        Yields chunks as they are generated, then saves/triggers at the end.
        """
        print(f"\nThinking (Stream) about '{topic}' (Model: {model_name or 'Default'})...\n")
        
        full_content = ""
        
        # 1. Stream from Brain
        async for chunk in self.brain.think_stream(topic, model_name=model_name):
            full_content += chunk
            yield chunk
            
        # 2. Post-processing (same as execute)
        result = DebateResult(topic=topic, content=full_content, model=model_name or "Default")
        
        # 3. Save to Memory (Conditional)
        # Only save if topic explicitly requests it (Selective Archiving)
        # 3. Save to Memory (Conditional)
        # LEGACY: Auto-save logic removed in Spec 013.
        # Saving is now handled by the Brain via 'save_debate' tool call.
        
        # 4. Trigger Nervous System
        self.nerve.trigger(result)

