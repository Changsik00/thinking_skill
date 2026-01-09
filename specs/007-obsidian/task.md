# Task List: Obsidian Integration

- [ ] **Task 1: Environment Setup**
    - Update `.env.example` with `OBSIDIAN_VAULT_PATH`.
    - Create `tests/unit/infrastructure/test_local_adapter.py`.

- [ ] **Task 2: Adapter Implementation**
    - Refactor `LocalAdapter.__init__`.
    - Enhance `_save_to_markdown` with Frontmatter.

- [ ] **Task 3: Verification**
    - Manual Verify: Set path to a dummy folder.
    - Run debate via Web UI.
    - Check file creation.
