# PR: TDD Foundation (Phase 4.5)

## 📌 목적 (Goal)
- **FastAPI 서버 도입 전**, 비즈니스 로직(`RunDebateUseCase`)을 안전하게 검증할 수 있는 테스트 환경을 구축했습니다.
- 외부 의존성(LLM, DB, n8n) 없이도 로직을 테스트할 수 있는 **Mocking Strategy**를 적용했습니다.

## 🛠 변경 사항 (Changes)

### 1. Test Environment
- `pyproject.toml`: `pytest`, `pytest-cov`, `pytest-asyncio` 추가 및 설정.

### 2. Mocks (`tests/mocks/`)
- `FakeBrain`: LLM 호출 없이 고정된 응답 반환.
- `FakeMemory`: 파일 시스템 대신 메모리 리스트에 저장.
- `FakeNerve`: 실제 HTTP 요청 없이 호출 여부만 카운트.

### 3. Unit Tests (`tests/unit/`)
- `test_run_debate.py`: **GWT (Given-When-Then)** 패턴 적용.
    - Brain이 생각을 잘 하는지 검증.
    - Memory에 저장이 잘 되는지 검증.
    - Nerve가 트리거되는지 검증.

## ✅ 검증 (Verification)
`RunDebateUseCase`의 **Test Coverage 100%** 달성! 💯

```bash
uv run pytest --cov=app.usecases tests/unit
```
```text
Name                         Stmts   Miss  Cover
------------------------------------------------
app/usecases/run_debate.py      16      0   100%
```
