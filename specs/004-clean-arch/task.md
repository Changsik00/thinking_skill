# Task List: Core Refactoring (Clean Arch)

- [x] **Task 1: Domain Layer**
    - Create `app/domain/entities.py`.
    - Create `app/domain/interfaces.py`.
- [x] **Task 2: Infrastructure Layer**
    - Implement `app/infrastructure/llm/langgraph_adapter.py`.
    - Implement `app/infrastructure/storage/local_adapter.py`.
    - Implement `app/infrastructure/automation/n8n_adapter.py`.
    - Refactor `agents/*` and `utils/*` code into new locations.
- [x] **Task 3: Use Case Layer**
    - Implement `app/usecases/run_debate.py`.
- [x] **Task 4: Interface Layer**
    - Create `app/interfaces/cli/runner.py` (New Entry Point).
- [x] **Task 5: Verification**
    - Run `uv run python -m app.interfaces.cli.runner` to confirm regression.
    - Cleanup old files (`agents/`, `utils/`).
