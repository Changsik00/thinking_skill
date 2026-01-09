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

- [x] **n8n Webhook**: Create n8n workflow to receive data.
- [x] **ChromaDB Connection**: Implement Python client to save vectors.
- [x] **Archiving**: Logic to save discussion summary to Markdown/Obsidian.

## 3. Future (Phase 4: Core Refactoring)
_Focus: Clean Architecture & Foundation Strengthening._

- [ ] **Domain Layer**: Define entities (Topic, DebateResult).
- [ ] **Use Case Layer**: Encapsulate logic (RunDebateUseCase).
- [ ] **Infra Layer**: Decouple LangGraph, Chroma, n8n.

## 4. Phase 4.5: TDD Foundation
_Focus: Reliability & Testability._

- [x] **Test Setup**: Configure `pytest`.
- [x] **Unit Tests**: Test `RunDebateUseCase` with Mock Adapters.
- [x] **Coverage**: Ensure core logic is covered.

## 5. Future (Phase 5: Interface MVP)
_Focus: User Experience (FastAPI + OpenWebUI)._

- [ ] **FastAPI Server**: Implement modern generic API server.
- [ ] **OpenWebUI Setup**: Configure OpenWebUI connection.
- [ ] **Full Test**: End-to-end test from Chat UI.

## 5. Icebox (Ideas & Enhancements)
- [ ] Voice Interface (TTS/STT).
- [ ] YouTube API Integration (Auto-upload).
- [ ] Dashboard for vector DB visualization.
- [ ] **Gemini 3 Migration**: Upgrade to `gemini-3-flash` and use `thinking_level`.
- [ ] **Selective Archiving**: Allow user to say "Save this" during chat to trigger storage (requires Interface MVP).
- [ ] **ChromaDB Admin UI**: Add `chromadb-admin` container to `docker-compose.yml` for visual data inspection.
