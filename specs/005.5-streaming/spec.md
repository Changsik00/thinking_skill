# Spec 005.5: Streaming Support (SSE)

## 1. Intent (의도)
**"기다림을 경험으로 바꾼다."**
현재의 Blocking 방식은 LLM이 긴 토론을 마칠 때까지 사용자를 기다리게 합니다 (10~30초).
이를 **Streaming (Server-Sent Events)** 방식으로 변경하여, 에이전트가 생각하는 과정을 실시간으로 보여주어 체감 지연 시간을 "0"에 가깝게 만듭니다.

## 2. Scope (범위)

### 2.1. Infrastructure Layer (`app/infrastructure`)
- **`LangGraphBrain`**: 기존의 `invoke` 대신 `stream` 또는 `astream` 메서드를 사용하여 토큰 단위(또는 노드 단위)로 출력을 스트리밍합니다.
- **`Async Generator`**: 비동기 제너레이터 패턴 적용.

### 2.2. Domain Layer (`app/domain`)
- **`ThinkingBrain` Interface**: 반환 타입을 `DebateResult`에서 `AsyncIterator[str | DebateResult]` 형태로 변경하거나, 별도의 스트리밍 메서드 추가.
    - *Note*: 기존 `think` 메서드와 별도로 `think_stream`을 추가하는 것이 안전할 수 있음.

### 2.3. Use Case Layer (`app/usecases`)
- **`RunDebateUseCase`**: 스트리밍된 청크를 받아서 그대로 상위 레이어로 전달(`yield`).
- **Side Effects**: 스트리밍이 **완료된 후**에 Memory 저장 및 Nerve 트리거 수행.

### 2.4. Interface Layer (`app/interfaces`)
- **`api/router.py`**: `StreamingResponse` (media_type="text/event-stream") 적용.

## 3. Architecture Design
- **Flow**: API -> UseCase (Yield) -> Brain (Yield)
- **Side Effect Handling**: 스트리밍 중에는 DB 저장 등을 하지 않고, 스트림이 끝나는 시점에 모아서 처리 (Aggregate & Save).

## 4. Verification Plan (검증 계획)
- `curl -N -X POST ...` 명령어로 버퍼링 없이 데이터가 들어오는지 확인.
- 브라우저에서도 EventSource 연결 테스트.
