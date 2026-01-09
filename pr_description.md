## 목적 (Goal)
**Spec 008: MCP (Model Context Protocol) 서버 통합**을 구현했습니다.
이를 통해 AI 에이전트(Claude Desktop 등)가 "Thingking"의 토론 데이터를 컨텍스트로 직접 조회할 수 있게 됩니다.

## 변경 사항 (Changes)
- **Domain Layer**: `MemoryVault` 인터페이스에 `list_debates`, `get_debate` 추가.
- **Infrastructure**: `LocalAdapter`에 마크다운 파싱 및 조회 로직 구현.
- **Use Case**: `ManageDebatesUseCase` (`ListDebates`, `GetDebate`) 추가.
- **Interface**: `app/interfaces/mcp_server.py` 생성 (`FastMCP` 사용).
    - **Resources**: `debate://list`, `debate://{topic}`
    - **Tools**: `search_debates(query)`
- **Documentation**: `docs/mcp-guide.md` 추가 및 `README.md` 업데이트.
- **Backlog**: `backlog/queue.md` 정리 (Sync Tool 관련 후속 태스크 추가).

## 검증 (Verification)
- **Unit Tests**: `tests/unit/usecases/test_manage_debates.py` 및 `tests/unit/interfaces/test_mcp_server.py` 추가. 총 13개 테스트 통과.
- **Manual Verification**: PR 리뷰 시 수행 위임.
    - 서버 실행: `uv run python -m app.interfaces.mcp_server`
    - `mcp-inspector` 또는 Claude Desktop에서 확인.
