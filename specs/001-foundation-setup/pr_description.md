# Pull Request: Foundation Setup (Spec 001)

## Summary
Implements the foundational infrastructure for the MACS project, enabling Phase 2 development.

## Changes
- **Directory Structure**: Created `agents`, `mcp-servers`, `workflows`, `data`.
- **Python Environment**:
    - Replaced `pyproject.toml` with `requirements.txt` (pip-based).
    - Added `.env.example`.
- **Docker Orchestration**:
    - Created `docker-compose.yml` for ChromaDB and n8n.
    - Verified containers are running.
- **Documentation**:
    - Reorganized `specs/` directory.
    - Updated `agent.md` with stricter folder rules.

## Verification
- [x] **Folder Structure**: Verified via `ls -R`.
- [x] **Python Env**: Verified via `pip install --dry-run`.
- [x] **Docker**: Verified via `docker ps` (ChromaDB & n8n running).

## Linked Spec
- [Spec 001](specs/001-foundation-setup/spec.md)
