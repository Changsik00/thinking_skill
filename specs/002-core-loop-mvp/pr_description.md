# Pull Request: Core Loop MVP (Spec 002)

## 요약 (Summary)
Spec 002에 정의된 **Host -> Creative -> Critical** 에이전트 토론 루프를 구현했습니다.
터미널환경(CLI)에서 사용자가 주제를 입력하면, 두 페르소나가 아이디어 발산과 비판을 수행합니다.

## 변경 사항 (Changes)
- **Agents Logic (`agents/`)**:
    - `prompts.py`: 창의적 발산가(Creative)와 냉철한 비평가(Critical) 페르소나 정의.
    - `state.py`: LangGraph 상태 정의 (`messages`).
    - `graph.py`: Gemini 2.0 Flash 모델 연동 및 Node/Edge 연결.
- **Entry Point**:
    - `agents/runner.py`: CLI 실행기 (기존 `main.py`에서 이동).
    - 실행 명령: `uv run python -m agents.runner "주제"`
- **Configuration**:
    - `pyproject.toml`: `onnxruntime` 호환을 위해 Python 버전을 `3.11` 이상으로 상향.
    - Model Update: `gemini-1.5-flash`가 API에서 잡히지 않아 `gemini-2.0-flash-001`로 변경.
- **Documentation**:
    - `docs/core-loop-architecture.md`: LangGraph 동작 원리 및 아키텍처 설명 추가.

## 검증 (Verification)
- [x] **CLI 실행**: `uv run python -m agents.runner "주제"` 명령으로 정상 작동 확인.
- [x] **페르소나 확인**: Creative가 아이디어를 내고, Critical이 이를 비판하는 흐름 확인.

## 연결된 Spec
- [Spec 002](specs/002-core-loop-mvp/spec.md)
