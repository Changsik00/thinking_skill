# Spec 012: 모델 업그레이드 및 동적 선택 (Model Upgrade)

## 🎯 요약 (Summary)
LLM 모델을 최신화(`gemini-2.0-flash-thinking` 등)하고, 상황에 따라 모델을 선택할 수 있는 **동적 모델 선택(Dynamic Model Selection)** 아키텍처를 구현했습니다.
또한 `app/domain/interfaces` 패키지 구조를 리팩토링하여 순환 참조 및 섀도잉 문제를 해결했습니다.

## 📝 변경 사항 (Changes)

### 1. Configuration (`.env`)
- `GEMINI_MODEL_NAME` 환경 변수 도입.
- **[High Performance]** vs **[Cost Effective]** 프로필 예시 제공.

### 2. Infrastructure Layer
- **`LangGraphBrain`**:
    - `think(model_name=...)` 파라미터를 통해 요청별 모델 전환 지원.
    - `configurable` 설정을 활용해 LangGraph Node 내부에서 동적으로 LLM 인스턴스 생성.

### 3. Application & API Layer
- **`RunDebateUseCase`**: `execute` 및 `execute_stream`에서 `model_name` 파라미터 수신 및 전파.
- **`OpenAI Router`**:
    - `list_models`: `gemini-3.0-flash`, `gemini-2.0-flash-thinking-exp` 등 최신 모델 리스트 반환.
    - `chat/completions`: 클라이언트(OpenWebUI)가 요청한 `model` 값을 UseCase로 전달.

### 4. Refactoring (Bug Fix)
- `app/domain/interfaces.py` 파일을 `app/domain/interfaces/core.py`로 이동하고 `__init__.py`에서 내보내도록 수정.
- 이유: Spec 011에서 생성된 `app/domain/interfaces/` 디렉토리가 기존 파일을 가리는(Shadowing) 문제 해결.

## ✅ 검증 (Verification)
`scripts/verify_model_upgrade.py` 스크립트를 통해 다음을 확인했습니다:
1. `.env` 설정에 따른 기본 모델 로딩.
2. `think(model_name='gemini-1.5-flash')` 호출 시 해당 모델로 전환.

## 📌 사용법 (Usage)
OpenWebUI 모델 선택창에서 원하는 모델을 선택하여 토론을 진행할 수 있습니다.
