# Spec 005: Interface MVP (FastAPI)

## 1. Intent (의도)
**"세상과 소통하는 문을 연다."**
지금까지 CLI에서만 돌던 토론 엔진(`RunDebateUseCase`)을 **HTTP API**로 노출하여, 웹 프론트엔드나 다른 서비스가 접근할 수 있게 만듭니다.

## 2. Scope (범위)

### 2.1. In-Scope
- **Dependencies**: `fastapi`, `uvicorn` 추가.
- **Entry Point**: `app/main.py` (FastAPI App & Composition Root).
- **API Router**: `app/interfaces/api/router.py`.
    - `POST /api/v1/debates`: 토론 시작 요청.
- **DTO**: `app/interfaces/api/schemas.py` (Pydantic Models).
    - Request: `{"topic": "..."}`
    - Response: `{"topic": "...", "content": "..."}`

### 2.2. Out-of-Scope
- **Web UI**: 프론트엔드 화면 구현은 제외 (Spec 006 예정).
- **DB 연동**: 여전히 `LocalAdapter` (파일/Chroma) 사용.

## 3. Architecture Design
- **Layer**: `Interface Layer`에 `api` 패키지 추가.
- **Dependency Injection**: `app/main.py`가 앱 시작 시 `UseCase`와 `Adapter`를 조립하여 `dependency_overrides` 또는 전역 상태로 주입.

## 4. Verification Plan (검증 계획)
- `uv run uvicorn app.main:app --reload` 실행.
- `curl` 또는 Swagger UI (`/docs`)를 통해 API 호출 성공 확인.
