# agents/runner.py
import sys
# If running as a script inside agents, we might need sys.path hack or run as module
# Standardizing to run via `uv run python -m agents.runner`

from langchain_core.messages import HumanMessage
from agents.graph import graph
from utils.storage import save_to_markdown, save_to_chroma

def run_loop():
    print("=== MACS: Multi-Agent Creative Studio (MVP) ===")
    print("Type 'exit' or 'q' to quit.")
    
    try:
        if len(sys.argv) > 1:
            user_input = " ".join(sys.argv[1:])
            print(f"Topic inputs from args: {user_input}")
        else:
            user_input = input("\n[Host]: Enter a topic > ")

        if user_input.lower() in ["exit", "q", ""]:
            print("Exiting...")
            return

        print(f"\nThinking about '{user_input}'...\n")

        # Initial State
        initial_state = {"messages": [HumanMessage(content=user_input)]}

        # Stream Execution
        final_content = ""
        for event in graph.stream(initial_state):
            for node, data in event.items():
                if "messages" in data and data["messages"]:
                    latest_msg = data["messages"][-1]
                    sender = node.capitalize()
                    content = latest_msg.content
                    print(f"--- [{sender}] ---")
                    print(f"{content}\n")
                    
                    # Store Critical's response as potential final conclusion
                    # Assuming Critical is the last node in MVP loop
                    if node == "critical":
                        final_content = content

        print("=== Loop Finished ===")
        
        # Archiving
        if final_content:
            saved_path = save_to_markdown(user_input, final_content)
            print(f"\n[System]: Archived discussion to {saved_path}")
            
            # ChromaDB
            try:
                save_to_chroma(user_input, final_content)
            except Exception as e:
                print(f"\n[System] ChromaDB Error: {e}")
        else:
            print("\n[System]: No content to archive.")

    except KeyboardInterrupt:
        print("\n\nAborted.")
    except Exception as e:
        print(f"\n[Error]: {e}")

if __name__ == "__main__":
    run_loop()
