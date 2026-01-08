# Task List: Integration MVP

- [x] **Task 1: File Archiving**
    - Create `utils/storage.py` with `save_to_markdown`.
    - Integrate into `agents/runner.py`.
    - Verification: Run runner, check `data/archives`.

- [ ] **Task 2: ChromaDB Integration**
    - Update `utils/storage.py` with `save_to_chroma`.
    - Integrate into `agents/runner.py`.
    - Verification: Run runner, check ChromaDB data count.

- [ ] **Task 3: n8n Webhook**
    - Create `utils/automation.py` with `trigger_n8n_workflow`.
    - Integrate into `agents/runner.py`.
    - Verification: Run runner, check n8n Execution log.
