# Project Backlog: MACS (Multi-Agent Creative Studio)

This document tracks all planned work, organized by MVP phases to ensure a Lean Startup approach.

## 0. Now (Current Priority)
_Items promoted to Spec or currently under discussion._

- [x] **[Phases 1-7] Foundation & Core Interface**
    - Docker, LangGraph, FastAPI Server, OpenWebUI complete.
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
- [ ] **Spec 017: Admin Dashboard (MVP)**
    - **Goal**: Web-based viewer for Debates & Vector DB.
    - **Tech**: Streamlit.

## 1. Next (Phase 9: Reliability & Expansion)
_Focus: DevOps & Quality Assurance & New Features._

- [ ] **Voice Interface**: TTS/STT integration (Creative Studio concept).
- [ ] **YouTube Sync**: Auto-upload debate content.
- [ ] Dashboard for vector DB visualization.
- [ ] **Multi-Provider Support**: Add adapters for OpenAI (GPT-4o) and Anthropic (Claude 3.5).
- [ ] **ChromaDB Admin UI**: Add `chromadb-admin` container.
