# PR: Streaming Support (Phase 5.5)

## 📌 목적 (Goal)
- **Blocking API의 한계 극복**: 긴 응답 시간을 기다리는 대신, **실시간 스트리밍(SSE)**으로 토큰을 즉시 보여주어 사용자 경험을 획기적으로 개선합니다.

## 🛠 변경 사항 (Changes)

### 1. Infrastructure Layer (`app/infrastructure/llm`)
- **`LangGraphBrain`**: `astream_events(version="v1")`를 사용하여 LLM의 생성 토큰을 실시간으로 `yield` 합니다.

### 2. Domain Layer (`app/domain`)
- **`ThinkingBrain`**: `think_stream` 비동기 인터페이스 추가.

### 3. Use Case Layer (`app/usecases`)
- **`RunDebateUseCase`**: `execute_stream` 메서드 추가.
    - 스트리밍 중에는 chunk를 단순히 전달(`yield`)만 하고,
    - 내부적으로 `full_content`에 모았다가 스트림 종료 시 **DB 저장 및 n8n 트리거**를 수행합니다.

### 4. Interface Layer (`app/interfaces/api`)
- **`router.py`**: `POST /debates/stream` 엔드포인트 추가.
- `StreamingResponse` (media_type="text/plain") 사용.

## ✅ 검증 (Verification)
`curl -N` (No Buffer) 옵션으로 토큰이 실시간으로 찍히는 것을 확인했습니다.

```bash
curl -N -X POST "http://localhost:8000/api/v1/debates/stream" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Streaming Test"}'
```
**결과**: 타다닥... (실시간 출력 성공)
