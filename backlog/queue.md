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

- [x] **Domain Layer**: Define entities (Topic, DebateResult).
- [x] **Use Case Layer**: Encapsulate logic (RunDebateUseCase).
- [x] **Infra Layer**: Decouple LangGraph, Chroma, n8n.

## 4. Phase 4.5: TDD Foundation
_Focus: Reliability & Testability._

- [x] **Test Setup**: Configure `pytest`.
- [x] **Unit Tests**: Test `RunDebateUseCase` with Mock Adapters.
- [x] **Coverage**: Ensure core logic is covered.

## 5. Phase 5: Interface MVP (FastAPI)
_Focus: User Experience (FastAPI + OpenWebUI)._

- [x] **FastAPI Server**: Implement modern generic API server.

## 6. Phase 5.5: Streaming Support (Completed)
_Focus: Latency Optimization (SSE)._

- [x] **LangGraph Stream**: Token-by-token generation.
- [x] **UseCase Generator**: Yield results.
- [x] **FastAPI SSE**: `StreamingResponse` endpoint.

## 7. Phase 6: Advanced Interface (Web UI) (Completed)
_Focus: Frontend Integration (OpenWebUI)._

- [x] **OpenWebUI Setup**: Configure OpenWebUI connection.
- [x] **Full Test**: End-to-end test from Chat UI.

## 8. Phase 7: MCP Integration (Spec 008)
_Focus: Context Connectivity (Obsidian & Tools)._

- [x] **Obsidian Connection**:
    - [x] Option A: Direct Save (Configured `OBSIDIAN_VAULT_PATH`).
    - [x] Option B: MCP Server (Allow Obsidian to query Thingking).
- [ ] **OpenWebUI Connection (OpenAPI Bridge Mode)** (Spec 010):
    - **Goal**: Integrate Dockerized OpenWebUI with Local MCP Server via `mcpo` proxy.
    - **Reason**: Native MCP UI is missing/unstable; `mcpo` provides robust OpenAPI-based connection.
    - **Method**: Add `mcpo` service to `docker-compose.yml`.
    - **Config**: Register `http://host.docker.internal:8000/sse` in `config.json` via volume.
- [x] **Data Synchronization Tools** (Spec 011):
    - **Issue**: File deletion in Obsidian is not reflected in ChromaDB.
    - **Solution**: Implemented `sync_debates` MCP tool to clean up orphaned embeddings.

## 9. Phase 8: Content Automation
_Focus: Practical Application via n8n._

- [ ] **Content Generator Mode**:
    - **PPT Generator**: JSON output -> n8n -> Google Slides.
    - **Reporting**: Weekly Summary -> n8n -> Email/Slack.
    - **SNS Publishing**: Blog Post -> n8n -> WordPress/Twitter.
    - Update `RunDebateUseCase` to output structured JSON for n8n.

## 10. Phase 9: CI/CD & Reliability (Deferred)
_Focus: DevOps & Quality Assurance._

- [ ] **GitHub Actions**: Setup `.github/workflows/test.yml`.
- [ ] **Unit Tests**: Trigger `pytest` on push (Free Tier).

## 11. Phase 10: Automated E2E Testing (Optional)
_Focus: Reliability (Browser Automation)._
*Context: High setup cost/complexity vs value. Recommended for stable phase.*

- [ ] **Playwright Setup**: Browser automation test.
- [ ] **Login & Chat Test**: Automate user flow (Login -> Chat -> Check Response).

## 12. Icebox (Ideas & Enhancements)
- [ ] Voice Interface (TTS/STT).
- [ ] YouTube API Integration (Auto-upload).
- [ ] Dashboard for vector DB visualization.
- [ ] **Gemini 3 Migration**: Upgrade to `gemini-3-flash` and use `thinking_level`.
- [ ] **Selective Archiving**: Allow user to say "Save this" during chat to trigger storage (requires Interface MVP).
- [ ] **ChromaDB Admin UI**: Add `chromadb-admin` container to `docker-compose.yml` for visual data inspection.
