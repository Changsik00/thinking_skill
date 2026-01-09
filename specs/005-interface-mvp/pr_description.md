# PR: Interface MVP (FastAPI)

## 📌 목적 (Goal)
- **FastAPI**를 도입하여 Clean Architecture의 Core Logic(`RunDebateUseCase`)을 **HTTP API**로 서빙합니다.
- 프론트엔드 연동을 위한 **`POST /api/v1/debates`** 엔드포인트를 제공합니다.

## 🛠 변경 사항 (Changes)

### 1. Requirements
- `fastapi`, `uvicorn` 추가.

### 2. Interface Layer (`app/interfaces/api`)
- **`schemas.py`**: Request/Response DTO (Pydantic).
- **`router.py`**: API 핸들러. `Depends`를 통해 UseCase 주입.

### 3. Main Application (`app/main.py`)
- **Composition Root**: 앱 시작 시(`lifespan`) 인프라 어댑터 초기화 및 DI 연결.
- **Dependency Override**: `get_run_debate_use_case` 스텁을 실제 구현체로 주입.

## ✅ 검증 (Verification)
`curl` 요청을 통해 종단간(End-to-End) 테스트 성공.

```bash
curl -X POST "http://localhost:8000/api/v1/debates" \
     -H "Content-Type: application/json" \
     -d '{"topic": "FastAPI Works!"}'
```
**결과:**
- Server Log: `Thinking about 'FastAPI Works!'...`
- Response: `{"topic": "FastAPI Works!", "content": "...", ...}`
