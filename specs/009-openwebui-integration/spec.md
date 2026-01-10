# Spec 009: OpenWebUI 연동 (SSE 및 선택적 저장)

## 1. 배경 (Background)
현재 MCP 서버(Spec 008)는 **Stdio 모드**로 동작하며, Claude Desktop 같은 로컬 앱에서는 잘 작동합니다. 하지만 사용자는 **Docker에서 실행되는 OpenWebUI**도 사용하고 있습니다.
Docker 컨테이너는 호스트의 Stdio와 직접 통신하기 어렵습니다. 이를 해결하기 위해 MCP 서버를 HTTP 상의 **SSE (Server-Sent Events)** 방식으로 노출해야 합니다.
또한, 대화 도중 LLM이 판단하여 저장할 수 있는 "선택적 저장(Save this)" 기능도 요청되었습니다.

## 2. 목표 (Goal)
1.  **SSE 지원**: MCP 서버를 SSE 모드로 실행하여 HTTP로 접근 가능하게 함 (예: `http://localhost:8000/sse`).
2.  **선택적 아카이빙**: 에이전트가 호출하여 대화 맥락을 저장할 수 있는 `save_debate` 도구 구현.
3.  **OpenWebUI 연결**: Dockerized OpenWebUI와 로컬 MCP 서버 간의 연결 검증.

## 3. 범위 (Scope)
### 3.1. 인터페이스 레이어 (`app/interfaces/mcp_server.py`)
- **수정**: `main` 실행 블록을 수정하거나 별도 진입점을 추가하여 `uvicorn` 또는 `FastMCP` SSE 모드로 실행.
    - *결정*: `FastMCP`는 FastAPI 앱처럼 동작할 수 있으므로 이를 적절히 노출합니다.
- **새로운 도구**: `save_debate(content: str)`
    - 이 도구는 `LocalAdapter.save()`를 호출합니다.

### 3.2. 인프라 (Infrastructure)
- **네트워크**: 서버가 Docker에서 접근 가능한 호스트/포트(예: `0.0.0.0`)에 바인딩되도록 함.

### 3.3. 문서화 (Documentation)
- `docs/mcp-guide.md`에 OpenWebUI 설정 방법 추가.

## 4. 제약 사항 (Constraints)
- **Local First**: 서버는 Docker 내부가 아닌 호스트 머신(Mac)에서 실행됩니다.
- **보안**: 네트워크 포트에 바인딩되므로 로컬 사용만 전제로 합니다 (인증 없음, 로컬 네트워크 신뢰).

## 5. 성공 지표 (Success Metrics)
- OpenWebUI가 `search_debates`와 `save_debate` 도구를 인식함.
- OpenWebUI에서 "이 대화 저장해줘"라고 말하면 호스트에 파일/DB 기록이 생성됨.
