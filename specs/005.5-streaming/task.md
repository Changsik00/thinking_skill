# Task List: Streaming Support

- [/] **Task 1: Domain & Infra**
    - Update `ThinkingBrain` interface.
    - Implement `think_stream` in `LangGraphBrain` (`astream_events`).

- [ ] **Task 2: Use Case**
    - Update `RunDebateUseCase` to support streaming.
    - Implement aggregation logic for final save.

- [ ] **Task 3: API Layer**
    - Update `router.py` with `StreamingResponse`.

- [ ] **Task 4: Verification**
    - Run `curl -N` test.
