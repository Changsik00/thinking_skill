# Spec 004.5: TDD Foundation

## 1. Intent (의도)
**"튼튼한 기초 위에 서버를 올린다."**
FastAPI 서버(Phase 5)를 구현하기 전에, 테스트 환경을 구축하고 핵심 비즈니스 로직(`UseCase`)을 검증합니다. 외부 의존성(LLM, DB) 없이도 로직을 테스트할 수 있음을 증명합니다.

## 2. Scope (범위)

### 2.1. In-Scope
- **Dependencies**: `pytest`, `pytest-cov`, `pytest-asyncio` 추가.
- **Unit Tests**: `tests/unit/usecases/`
    - `test_run_debate.py`: Brain/Memory/Nerve Mock 객체를 이용한 흐름 검증.
- **Mocks**: `tests/mocks/`
    - `FakeBrain`: 항상 고정된 문자열 반환.
    - `FakeMemory`: 메모리 리스트에 저장.
    - `FakeNerve`: 호출 횟수 카운트.

### 2.2. Out-of-Scope
- **Integration Tests**: 실제 ChromaDB나 n8n을 호출하는 테스트는 제외 (이는 느리고 비용이 듦).
- **Other Layers**: Infra Layer 자체에 대한 테스트는 제외 (어댑터는 단순 위임이므로).

## 3. Verification Plan (검증 계획)
- `uv run pytest` 실행 시 **All Passed**.
- `RunDebateUseCase`에 대한 Test Coverage **100%** 달성.
