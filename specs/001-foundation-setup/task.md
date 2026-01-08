- [x] **Task 1: Project Scaffolding**
    - Create directories: `agents`, `mcp-servers`, `workflows`, `data`.
    - Create `.gitignore`.
    - Verification: `ls -R` shows structure. (Done)

- [x] **Task 2: Python Initialization**
    - Remove `pyproject.toml` (switching to pip).
    - Create `requirements.txt` with: `langchain`, `langgraph`, `langchain-google-genai`, `chromadb`, `python-dotenv`.
    - Create `.env.example`.
    - Verification: `pip install -r requirements.txt --dry-run` succeeds.

- [x] **Task 3: Docker Orchestration**
    - Create `docker-compose.yml`.
    - Start containers (`up -d`).
    - Verification: `docker ps` shows running services.

- [x] **Task 4: Documentation**
    - Create `docs/` directory.
    - Write `docs/setup-guide.md` (Setup, Run, Troubleshoot).
    - Link in `README.md`.
