# Plan: Foundation Setup

## Goal
Execute Spec 001 to establish the project's foundational infrastructure.

## User Review Required
> [!NOTE]
> Ensure Docker Desktop is running on your Mac before we start the execution phase.

## Proposed Changes

### Configuration
#### [NEW] [pyproject.toml](file:///Users/ck/Project/Thingking/pyproject.toml)
- Define python version and dependencies (`langchain`, `langgraph`, `chromadb`).

#### [NEW] [docker-compose.yml](file:///Users/ck/Project/Thingking/docker-compose.yml)
- Define `chroma` and `n8n` services.

#### [NEW] [.gitignore](file:///Users/ck/Project/Thingking/.gitignore)
- Standard python and docker ignore rules.

### Structure
- Create directories: `agents/`, `mcp-servers/`, `workflows/`, `data/`.

## Verification Plan

### Automated Tests
- `poetry install`: Verify dependencies resolve without conflict.
- `docker-compose config`: Verify syntax of compose file.

### Manual Verification
- `docker-compose up -d`: Check if services start.
- `curl localhost:8000/api/v1/heartbeat`: Check ChromaDB health (if applicable API exists) or just container status.

## Tasks
- [ ] **Task 1: Project Scaffolding**
    - Create folder structure.
    - Create `.gitignore`.
- [ ] **Task 2: Python Initialization**
    - Create `pyproject.toml`.
    - Run `poetry install` (or generate lock file).
- [ ] **Task 3: Docker Orchestration**
    - Create `docker-compose.yml`.
    - Run `docker-compose up -d` to verify.
    - Update `backlog/queue.md` (mark Phase 1 done).
