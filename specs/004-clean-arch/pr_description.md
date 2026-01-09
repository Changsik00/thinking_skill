# PR: Core Refactoring (Clean Architecture)

## 📌 목적 (Goal)
- 기존의 스크립트 기반 코드를 **Clean Architecture** (Layered Architecture)로 리팩토링합니다.
- 비즈니스 로직(`UseCase`)과 인프라(`Tech Stack`)를 완전히 분리하여, 향후 **FastAPI** 도입 및 확장에 대비합니다.

## 🛠 변경 사항 (Changes)

### 1. New Architecture (`app/`)
- **Domain Layer (`app/domain`)**: 외부 의존성이 전혀 없는 순수 파이썬 영역.
    - `DebateResult` (Entity)
    - `ThinkingBrain`, `MemoryVault`, `NerveSystem` (Interfaces/Ports)
- **Use Case Layer (`app/usecases`)**: 비즈니스 흐름 제어.
    - `RunDebateUseCase`: 인프라 구현체를 주입받아 실행.
- **Infrastructure Layer (`app/infrastructure`)**: 실제 구현체 (Adapters).
    - `LangGraphBrain`: `agents/graph.py` 로직 이식.
    - `LocalAdapter`: 파일/ChromaDB 저장 로직 이식.
    - `N8nAdapter`: Webhook 호출 로직 이식.
- **Interface Layer (`app/interfaces`)**:
    - `cli/runner.py`: 의존성 주입(DI) 및 실행 담당.

### 2. Cleanup
- `agents/`, `utils/`, `main.py`, `debug_models.py` 삭제 (더 이상 사용하지 않음).

## ✅ 검증 (Verification)
기존 CLI 명령어와 **100% 동일하게 동작**해야 합니다.

```bash
uv run python -m app.interfaces.cli.runner "Refactor Test"
```
**확인 포인트:**
1. 터미널에 토론 내용 출력.
2. `[System]: Saved to ChromaDB` 로그 확인.
3. `[System]: Archived discussion to ...` 로그 확인.
4. `[System]: n8n Webhook triggered successfully` 로그 확인.
