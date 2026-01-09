# Task List: Web UI Integration

- [x] **Task 1: OpenAI Adapter**
    - Create `app/interfaces/api/openai_router.py`.
    - Implement `POST /openai/v1/chat/completions`.
    - Handle SSE formatting (`data: ...`).

- [x] **Task 2: Docker Setup**
    - Add `open-webui` to `docker-compose.yml`.

- [x] **Task 3: Documentation & Verify**
    - Create `docs/open-webui-guide.md` (Detailed Walkthrough).
    - Guide on: Initial Admin Creation, Connecting Custom OpenAI URL, Chatting.
    - Verify with Browser.
