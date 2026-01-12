# app/interfaces/cli/runner.py
import sys
import argparse
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.infrastructure.automation.n8n_adapter import N8nAdapter
from app.usecases.run_debate import RunDebateUseCase

def main():
    parser = argparse.ArgumentParser(description="MACS: Multi-Agent Creative Studio (Refactored)")
    parser.add_argument("topic", nargs="?", help="Topic for discussion")
    args = parser.parse_args()

    print("=== MACS: Multi-Agent Creative Studio (Clean Arch) ===")
    print("Type 'exit' or 'q' to quit.")

    topic = args.topic
    if not topic:
        topic = input("\nEnter a topic to discuss: ").strip()

    if topic.lower() in ["exit", "q"]:
        print("Goodbye!")
        return

    # --- Composition Root ---
    # 1. Instantiate Adapters (Infrastructure)
    # 1. Instantiate Adapters (Infrastructure)
    try:
        from app.infrastructure.storage.file_persona_repository import FilePersonaRepository
        persona_repo = FilePersonaRepository()
        
        memory = LocalAdapter(archive_dir="data/archives")
        nerve = N8nAdapter()
        brain = LangGraphBrain(memory=memory, nerve=nerve, persona_repo=persona_repo)  
        
        # 2. Inject Dependencies into Use Case
        use_case = RunDebateUseCase(brain=brain, memory=memory, nerve=nerve)
        
        # 3. Execute Control Flow
        use_case.execute(topic)
        
        print("\n=== Loop Finished ===\n")
        
    except Exception as e:
        print(f"\n[Error] Failed to execute debate: {e}")

if __name__ == "__main__":
    main()
