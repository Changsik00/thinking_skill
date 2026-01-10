# Spec 009: OpenWebUI Integration & Selective Save Tool

## 개요
이 PR은 Docker 환경의 **OpenWebUI**와 로컬 MCP 서버 간의 연동을 위한 **SSE 모드**를 구현하고, 대화 내용을 저장할 수 있는 **선택적 저장 도구(`save_debate`)**를 추가합니다.

## 변경 사항
### 1. Save Tool 추가 (`app/interfaces/mcp_server.py`)
- `save_debate(topic, content)` 도구를 추가하여 에이전트가 대화 내용을 파일/DB에 저장할 수 있도록 함.
- **예외 처리**: 저장 실패 시 JSON-RPC 에러 대신 LLM이 이해할 수 있는 에러 메시지 반환 (`try-except` 적용).
- 기존 `LocalAdapter.save` 로직 재사용.
- **테스트**: `test_save_debate_tool`, `test_save_debate_tool_failure` 추가.

### 2. SSE 모드 지원 (`app/interfaces/mcp_server.py`)
- `--sse` 플래그를 통해 `uvicorn` 기반의 SSE 서버 실행 모드 추가.
- `uv run python -m app.interfaces.mcp_server --sse` 명령으로 실행.
- 호스트 바인딩: `0.0.0.0` (Docker 접근 허용).

### 3. 문서화 (`docs/mcp-guide.md`)
- OpenWebUI 연동 가이드 추가.
- Docker Host 연결 설정 방법 기술.

## 검증 (Verification)
- **Unit Test**: `uv run pytest` (Save Tool 동작 확인 완료).
- **Manual Verification**: `scripts/verify_sse.py`를 통해 SSE 엔드포인트(`http://localhost:8000/sse`) 응답 확인 완료 (Status 200).
