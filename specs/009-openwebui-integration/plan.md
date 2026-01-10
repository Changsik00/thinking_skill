# Spec 009 구현 계획 (Implementation Plan)

## 사용자 검토 필요 (User Review Required)
- **포트 노출**: SSE 서버는 로컬 네트워크(기본 포트 8000)를 통해 접근 가능합니다. Docker에서 접근 시 방화벽 차단이 없는지 확인 필요.

## 변경 제안 (Proposed Changes)

### Interface Layer
#### [수정] [mcp_server.py](file:///Users/ck/Project/Thingking/app/interfaces/mcp_server.py)
- **의존성**: 필요 시 `starlette` 또는 `uvicorn` 추가 (FastMCP는 보통 자체적으로 또는 `mcp[sse]`로 처리).
- **실행 모드**: SSE 모드로 실행하기 위한 CLI 인자 또는 스크립트 추가.
- **새로운 도구**: `save_debate(content: str) -> str` 등록.
    - 구현:
        - 내용(content)으로 `DebateResult` 객체 생성.
        - `LocalAdapter.save()` 호출.
        - 저장된 경로 반환.

### Documentation
#### [수정] [mcp-guide.md](file:///Users/ck/Project/Thingking/docs/mcp-guide.md)
- "OpenWebUI 연동" 섹션 추가.
- `host.docker.internal` 설정 설명.

## 검증 계획 (Verification Plan)
### 자동화 테스트 (Automated Tests)
- `tests/unit/interfaces/test_mcp_server.py` 확장하여 새로운 `save_debate` 도구 테스트.
- (선택) `TestClient`를 통해 SSE 엔드포인트 존재 여부 테스트.

### 수동 검증 (Manual Verification)
1. SSE 모드로 서버 실행: `uv run python -m app.interfaces.mcp_server --sse` (또는 유사 명령).
2. 브라우저 접속: `http://localhost:8000/sse` (SSE 핸드셰이크 또는 엔드포인트 정보 확인).
3. OpenWebUI 연결:
    - 관리자 패널(Admin Panel) -> Connections -> Add Custom.
    - URL: `http://host.docker.internal:8000/sse`.
4. 채팅 테스트: "안녕, 이 대화 저장해줘." -> 파일 생성 확인.
