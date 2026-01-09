# Implementation Plan: Streaming Support

## 1. Goal
Blocking API를 Streaming API로 전환하여 사용자 경험 개선.

## 2. Proposed Changes

### Domain Layer (`app/domain/interfaces.py`)
- `ThinkingBrain` 인터페이스에 `think_stream(topic: str) -> AsyncIterator[str]` 추가.

### Infrastructure Layer (`app/infrastructure/llm/langgraph_adapter.py`)
- `LangGraphBrain`에 `think_stream` 구현.
- `graph.astream_events`를 사용하여 토큰/노드 업데이트 이벤트를 캡처하여 yield.

### Use Case Layer (`app/usecases/run_debate.py`)
- `RunDebateUseCase` 수정:
    - `execute`는 유지 (하위 호환).
    - `execute_stream` 추가.
    - **중요**: 스트리밍 데이터를 `full_content` 변수에 계속 모아야 함. 스트림 종료 후 `MemoryVault.save` 및 `NerveSystem.trigger` 호출.

### Interface Layer (`app/interfaces/api/router.py`)
- `POST /api/v1/debates/stream` 엔드포인트 추가 (또는 기존 엔드포인트 변경).
- `StreamingResponse` 사용.

## 3. Verification Plan
- `tests/manual_stream_test.py`: 간단한 클라이언트 스크립트로 청크 수신 확인.
- `curl` 테스트.
