# Project Backlog: MACS (Multi-Agent Creative Studio)

This document tracks all planned work, organized by MVP phases to ensure a Lean Startup approach.

## 0. Now (Current Priority)
_Items promoted to Spec or currently under discussion._

- [x] **[Phase 1] Foundation Setup**
    - Create directory structure (`agents`, `mcp-servers`, `workflows`, `data`).
    - Initialize Python environment (`poetry` or `pip`, `.gitignore`).
    - Create `docker-compose.yml` for ChromaDB & n8n.
    - **Goal**: Verify containers run and python env is ready.

## 1. Next (Phase 2: Core Loop MVP)
_Focus: Verify the debate logic in isolation (Terminal-based)._

- [x] **LangGraph Base Setup**: Define State and Nodes.
- [x] **Agent Personas**: Implement "Creative" and "Critical" system prompts.
- [x] **Debate Logic**: Implement the loop (Host -> A -> B -> Host).
- [x] **Terminal Demo**: Run the debate in the console to verify logic.

## 2. Later (Phase 3: Integration MVP)
_Focus: Connect the brain to the body (Automation & Memory)._

- [ ] **n8n Webhook**: Create n8n workflow to receive data.
- [ ] **ChromaDB Connection**: Implement Python client to save vectors.
- [ ] **Archiving**: Logic to save discussion summary to Markdown/Obsidian.

## 3. Future (Phase 4: Interface MVP)
_Focus: User Experience._

- [ ] **OpenWebUI Setup**: Configure OpenWebUI.
- [ ] **API Exposure**: Expose LangGraph as an API (FastAPI) for OpenWebUI to consume.
- [ ] **Full Test**: End-to-end test from Chat UI.

## 4. Icebox (Ideas & Enhancements)
- [ ] Voice Interface (TTS/STT).
- [ ] YouTube API Integration (Auto-upload).
- [ ] Dashboard for vector DB visualization.
- [ ] **Gemini 3 Migration**: Upgrade to `gemini-3-flash` and use `thinking_level`.
- [ ] **Selective Archiving**: Allow user to say "Save this" during chat to trigger storage (requires Interface MVP).
