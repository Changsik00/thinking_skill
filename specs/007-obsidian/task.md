# Task List: Obsidian Integration

- [x] **Task 1: Environment Setup**
    - Update `.env.example` with `OBSIDIAN_VAULT_PATH`.
    - Create `tests/unit/infrastructure/test_local_adapter.py`.

- [x] **Task 2: Adapter Implementation**
    - Refactor `LocalAdapter.__init__`.
    - Enhance `_save_to_markdown` with Frontmatter.

- [/] **Task 3: Verification**
    - Manual Verify: Set path to a dummy folder.
    - Run debate via Web UI.
    - Check file creation.

- [x] **Task 4: Selective Archiving** (Refinement)
    - Update `RunDebateUseCase` to filter saves by keyword.
    - Update `tests/unit/usecases/test_run_debate.py`.
