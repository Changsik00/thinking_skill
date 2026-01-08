- [x] **Task 1: Project Scaffolding**
    - Create directories: `agents`, `mcp-servers`, `workflows`, `data`.
    - Create `.gitignore`.
    - Verification: `ls -R` shows structure. (Done)

- [x] **Task 2: Python Initialization (uv)**
    - Run `uv init`.
    - Run `uv add langchain langgraph langchain-google-genai chromadb python-dotenv`.
    - Update `docs/setup-guide.md`.
    - Verification: `uv sync` succeeds.

- [x] **Task 3: Docker Orchestration**
    - Create `docker-compose.yml`.
    - Start containers (`up -d`).
    - Verification: `docker ps` shows running services.

- [x] **Task 4: Documentation**
    - Create `docs/` directory.
    - Write `docs/setup-guide.md` (Setup, Run, Troubleshoot).
    - Link in `README.md`.
