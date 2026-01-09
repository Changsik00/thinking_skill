# Implementation Plan: Interface MVP (FastAPI)

## 1. Goal
CLI에 이어 HTTP API 인터페이스를 구현하여 외부 시스템과 통신할 수 있게 만든다.

## 2. dependencies
- `fastapi`
- `uvicorn`

## 3. Proposed Changes

### Interface Layer (API)
#### [NEW] app/interfaces/api/schemas.py
- `DebateRequest`: `topic` (str)
- `DebateResponse`: `topic`, `content`, `created_at`

#### [NEW] app/interfaces/api/router.py
- `APIRouter` 정의.
- `POST /debates`: `RunDebateUseCase` 실행.
- **Dependency Injection**: `Depends`를 사용하여 UseCase를 주입받음.

### Main Application
#### [NEW] app/main.py
- `FastAPI` 앱 인스턴스 생성.
- `lifespan` 이벤트에서 인프라(Adapters) 초기화 및 DI 컨테이너 설정.
- `api_router` 등록.

## 4. Verification Plan
1. `uv run uvicorn app.main:app --reload`
2. `curl -X POST "http://localhost:8000/api/v1/debates" -H "Content-Type: application/json" -d '{"topic": "API Test"}'`
3. 응답 JSON 확인 및 서버 로그 확인.
