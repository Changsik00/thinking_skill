# Project Backlog: MACS (Multi-Agent Creative Studio)

This document tracks all planned work, organized by MVP phases to ensure a Lean Startup approach.

## 0. Now (Phase 9: Reliability & Expansion)
_Items promoted to Spec or currently under discussion._

### Recent Completions (Specs 010-021)
- [x] **Spec 010: OpenWebUI MCP Bridge**
    - `mcpo` container added and configured.
    - Tools exposed to OpenWebUI via OpenAPI.
- [x] **Spec 011: Data Synchronization**
    - `sync_debates` tool implemented.
- [x] **Spec 012: Model Upgrade**
    - Gemini 3 / Dynamic Model Selection implemented.
- [x] **Spec 013: Selective Archiving (Smart Save)**
    - **Goal**: Disable auto-save; allow Agent to save only when requested or valuable.
    - **Method**: Modify `RunDebateUseCase` and ensure `save_debate` tool is effectively used by the Brain.
- [x] **Spec 014: Content Automation (n8n)**
    - **Goal**: Trigger external workflows (e.g., Slack, Blog) via n8n.
    - **Scope**: `N8nAdapter` update, `trigger_automation` tool, Local Verification.
- [x] **Spec 016: DevOps Automation (CI)**
    - **Goal**: GitHub Actions for automated testing.
    - **Scope**: `.github/workflows/test.yml`, `uv` integration, `pytest`.
- [x] **Spec 017: Admin Dashboard (MVP)**
    - **Goal**: Web-based viewer for Debates & Vector DB.
    - **Tech**: Streamlit.
- [x] **Spec 019: Persona Management System**
    - **Goal**: Allow users to configure Agent Personas (e.g., Angry Critic, Friendly Mentor) without code changes.
    - **Scope**: YAML/JSON configuration, API for switching personas, Dashboard integration.
- [x] **Spec 020: Linting & Formatting Automation**
    - **Goal**: Auto-format code and catch errors (like IndentationError) early.
    - **Tech**: `ruff` (linter + formatter), `pre-commit` (optional), CI integration.
- [x] **Spec 021: YouTube Transcript Integration**
    - **Goal**: Fetch transcripts from YouTube videos to enable discussion ("Talk with Video").
    - **Tech**: `youtube-transcript-api`, New Tool `fetch_transcript`.

## 1. Next (Future Work)
- [ ] **Spec 022: Voice Interface**: TTS/STT integration (Creative Studio concept).
- [ ] **Targeted Archiving (YouTube)**: Extract and save only key insights from video transcripts to Vector DB (Refinement of Spec 021).
- [ ] Dashboard for vector DB visualization.
- [ ] **Multi-Provider Support**: Add adapters for OpenAI (GPT-4o) and Anthropic (Claude 3.5).
- [ ] **ChromaDB Admin UI**: Add `chromadb-admin` container (Dedicated Tool).
- [ ] **Dedicated Chroma Admin Tool**: Evaluate `chroma-admin` or `BootstrapDash` templates for advanced DB management (Icebox).

## 2. History (Completed Phases 1-7)
_Foundation & Core Interface_

### Phase 1: Foundation Setup
- [x] **Foundation Setup**
    - Create directory structure (`agents`, `mcp-servers`, `workflows`, `data`).
    - Initialize Python environment (`poetry` or `pip`, `.gitignore`).
    - Create `docker-compose.yml` for ChromaDB & n8n.

### Phase 2: Core Loop MVP
- [x] **LangGraph Base Setup**: Define State and Nodes.
- [x] **Agent Personas**: Implement "Creative" and "Critical" system prompts.
- [x] **Debate Logic**: Implement the loop (Host -> A -> B -> Host).
- [x] **Terminal Demo**: Run the debate in the console to verify logic.

### Phase 3: Integration MVP
- [x] **n8n Webhook**: Create n8n workflow to receive data.
- [x] **ChromaDB Connection**: Implement Python client to save vectors.
- [x] **Archiving**: Logic to save discussion summary to Markdown/Obsidian.

### Phase 4: Interface MVP (Web UI)
- [x] **OpenWebUI Setup**: Configure OpenWebUI.
- [x] **API Exposure**: Expose LangGraph as an API (FastAPI) for OpenWebUI to consume.
- [x] **Full Test**: End-to-end test from Chat UI.

### Phase 5: Latency Optimization (SSE)
- [x] **LangGraph Stream**: Token-by-token generation.
- [x] **UseCase Generator**: Yield results.
- [x] **FastAPI SSE**: `StreamingResponse` endpoint.

### Phase 6: Advanced Interface (Web UI)
- [x] **OpenWebUI Setup**: Configure OpenWebUI connection.
- [x] **Full Test**: End-to-end test from Chat UI.

### Phase 7: MCP Integration (Spec 008)
- [x] **Obsidian Connection**:
    - [x] Option A: Direct Save (Configured `OBSIDIAN_VAULT_PATH`).
    - [x] Option B: MCP Server (Allow Obsidian to query Thingking).
