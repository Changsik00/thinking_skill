# Task List: TDD Foundation

- [x] **Task 1: Environment Setup**
    - `uv add --dev pytest pytest-cov pytest-asyncio`
    - Update `pyproject.toml` with pytest config.

- [x] **Task 2: Testing Infrastructure**
    - Create `tests/mocks/fake_adapters.py`.
    - Implement `FakeBrain`, `FakeMemory`, `FakeNerve`.

- [x] **Task 3: Unit Testing**
    - Create `tests/unit/usecases/test_run_debate.py`.
    - Implement `test_run_debate_flow`.

- [x] **Task 4: Verification**
    - Run `uv run pytest`.
    - Check code coverage.
