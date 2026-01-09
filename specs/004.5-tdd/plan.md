# Implementation Plan: TDD Foundation

## 1. Goal
비즈니스 로직(`RunDebateUseCase`)이 인프라 없이도 검증 가능함을 증명하고, 안전한 테스트 환경을 구축한다.

## 2. dependencies
- `pytest`
- `pytest-cov`
- `pytest-asyncio` (비동기 테스트 대비)

## 3. Proposed Changes

### Test Configuration
#### [MODIFY] pyproject.toml
- `[tool.pytest.ini_options]` 섹션 추가.
- `pythonpath = ["."]` 설정 (import path 문제 해결).

### Mocks
#### [NEW] tests/mocks/fake_adapters.py
- `FakeBrain(ThinkingBrain)`: "Fake Idea" 반환.
- `FakeMemory(MemoryVault)`: `self.saved_items` 리스트에 저장.
- `FakeNerve(NerveSystem)`: `self.triggered_count` 증가.

### Unit Tests
#### [NEW] tests/unit/usecases/test_run_debate.py
- `test_run_debate_flow`:
    1. Fake Adapter들로 `RunDebateUseCase` 초기화.
    2. `execute("Test Topic")` 호출.
    3. Assertions:
        - Result Content가 "Fake Idea"인가?
        - Memory에 1개 저장되었는가?
        - Nerve가 1번 트리거되었는가?

## 4. Verification Plan
- `uv run pytest tests/unit` 결과가 **Pass**여야 함.
