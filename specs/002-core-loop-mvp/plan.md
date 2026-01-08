# Plan: Core Loop MVP (Spec 002)

## Goal
Implement the core debate logic using LangGraph as defined in Spec 002.
The system will run in the terminal, demonstrating a single loop of ideation and critique.

## User Review Required
> [!NOTE]
> This MVP uses `langchain-google-genai`. Ensure `GEMINI_API_KEY` is set in `.env`.

## Proposed Changes

### Logic (`agents/`)
#### [NEW] [prompts.py](file:///Users/ck/Project/Thingking/agents/prompts.py)
- Define `CREATIVE_SYSTEM_PROMPT`: Persona for generating divergent ideas.
- Define `CRITICAL_SYSTEM_PROMPT`: Persona for convergent criticism.

#### [NEW] [state.py](file:///Users/ck/Project/Thingking/agents/state.py)
- Define `AgentState(TypedDict)`:
    - `messages`: List[BaseMessage]
    - `current_speaker`: str (optional tracking)

#### [NEW] [graph.py](file:///Users/ck/Project/Thingking/agents/graph.py)
- Initialize model (`ChatGoogleGenerativeAI`).
- Define nodes: `creative_node`, `critical_node`.
- Define edges: User -> Creative -> Critical -> End.
- Compile and export `graph`.

### Entry Point
#### [NEW] [main.py](file:///Users/ck/Project/Thingking/main.py)
- Parse user input from CLI.
- Invoke `graph`.
- Print the conversation history nicely.

## Verification Plan

### Manual Verification
1.  Run `uv run main.py`.
2.  Input: "유튜브 쇼츠 아이디어 추천해줘".
3.  Expected Output:
    - `[Creative]`: Ideas...
    - `[Critical]`: Critique...
    - Process exits successfully.

## Tasks
- [ ] **Task 1: Agent Personas**: Create `agents/prompts.py`.
- [ ] **Task 2: State Definition**: Create `agents/state.py`.
- [ ] **Task 3: Graph Implementation**: Create `agents/graph.py` with nodes/edges.
- [ ] **Task 4: CLI Runner**: Create `main.py` and verify execution.
