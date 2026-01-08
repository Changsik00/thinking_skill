# Spec 001: Foundation Setup

## 1. Intent
Establish the core infrastructure for the MACS project to enable Phase 2 (Core Loop) development.
This includes setting up the directory structure, the Docker environment for local services, and the Python project configuration.

## 2. Scope
- **Directory Structure**: Create `agents/`, `mcp-servers/`, `workflows/`, `data/`.
- **Docker Environment**: Create `docker-compose.yml` defining services for:
    - `chroma`: ChromaDB vector store (Port 8000).
    - `n8n`: Workflow automation tool (Port 5678).
- **Python Setup**:
    - Initialize `pyproject.toml` using Poetry.
    - Add essential dependencies: `langgraph`, `langchain-google-genai`, `chromadb`.
    - Create a standard `.gitignore` for Python, Docker, and environment files.

## 3. Implementation Details

### 3.1 Directory Structure
```
/Users/ck/Project/Thingking/
├── agents/             # [NEW]
├── mcp-servers/        # [NEW]
├── workflows/          # [NEW]
├── data/               # [NEW]
├── specs/              # [Existing]
├── backlog/            # [Existing]
├── docker-compose.yml  # [NEW]
└── pyproject.toml      # [NEW]
```

### 3.2 Docker Configuration (`docker-compose.yml`)
Use the official images for ChromaDB and n8n.
- **ChromaDB**: `chromadb/chroma:latest`
    - Volume: `./data/chroma:/chroma/chroma`
- **n8n**: `docker.n8n.io/n8nio/n8n`
    - Volume: `./data/n8n:/home/node/.n8n`
    - Env: `N8N_SECURE_COOKIE=false` (for local dev)

### 3.3 Python Setup
Use `poetry init` manually or write `pyproject.toml` directly.
Dependencies:
- `langchain`
- `langgraph`
- `langchain-google-genai`
- `chromadb`
- `python-dotenv`

## 4. Verification Plan
1.  **Directory Check**: Run `ls -R` to verify structure.
2.  **Docker Health Check**: Run `docker-compose up -d` and check `docker ps` to ensure containers are running without restart loops.
3.  **Python Env Check**: Run `poetry install` and verify VirtualEnv is created.

## 5. Constraints
- Do not implement any Agent logic yet.
- Keep `docker-compose` simple (MVP).
