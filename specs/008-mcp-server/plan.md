# Implementation Plan - Spec 008: MCP Server

Thingking을 MCP Server로 확장하여 Obsidian 등 외부 도구에서 저장된 토론 내역을 조회할 수 있도록 합니다.

## User Review Required
> [!IMPORTANT]
> **Interface Change**: `MemoryVault` 인터페이스에 `list_debates`와 `get_debate` 메소드가 추가됩니다.
> 이는 기존 `LocalAdapter` 구현에 영향을 미치며, 파일 시스템(Markdown)을 "Read"하는 로직이 추가됩니다.

## Proposed Changes

### Domain Layer
#### [MODIFY] [interfaces.py](file:///Users/ck/Project/Thingking/app/domain/interfaces.py)
- `MemoryVault` 클래스에 조회용 추상 메소드 추가:
    - `list_debates(self, limit: int = 10) -> List[DebateResult]`
    - `get_debate(self, topic: str) -> Optional[DebateResult]`

### Infrastructure Layer (Adapters)
#### [MODIFY] [local_adapter.py](file:///Users/ck/Project/Thingking/app/infrastructure/storage/local_adapter.py)
- `list_debates`: `OBSIDIAN_VAULT_PATH` 내의 Markdown 파일 목록을 스캔하여 반환. (Frontmatter 파싱)
- `get_debate`: 특정 파일(Topic 기준)을 읽어 `DebateResult`로 복원.

### UseCase Layer
#### [NEW] [manage_debates.py](file:///Users/ck/Project/Thingking/app/usecases/manage_debates.py)
- `GetDebateListUseCase`: `MemoryVault.list_debates` 호출.
- `GetDebateDetailUseCase`: `MemoryVault.get_debate` 호출.

### Interface Layer (MCP)
#### [NEW] [mcp_server.py](file:///Users/ck/Project/Thingking/app/interfaces/mcp_server.py)
- `mcp` 패키지(FastMCP)를 사용하여 서버 인스턴스 생성.
- **Resources**:
    - `debate://list`: 최근 토론 목록.
    - `debate://{topic_slug}`: 토론 상세 내용.
- **Entry Point**: `if __name__ == "__main__": mcp.run()`

### Dependencies
#### [MODIFY] [pyproject.toml](file:///Users/ck/Project/Thingking/pyproject.toml)
- `mcp` 패키지 추가.

## Documentation
#### [NEW] [docs/mcp-guide.md](file:///Users/ck/Project/Thingking/docs/mcp-guide.md)
- **Concept**: Model Context Protocol 및 FastMCP 라이브러리 설명.
- **Architecture**: 외부 Client(Claude/Obsidian)와 Thingking 간의 통신 메커니즘 (Mermaid Diagram 포함).
- **Capabilities**: 제공되는 Resource(`debate://`) 및 Tool(`search_debates`) 목록 및 사용법.

#### [MODIFY] [README.md](file:///Users/ck/Project/Thingking/README.md)
- MCP Server 기능 소개 및 `docs/mcp-guide.md` 링크 추가.

## Verification Plan

### Automated Tests
- **Unit Tests**:
    - `test_local_adapter.py`: 파일 생성 후 `list` 및 `get` 동작 검증.
    - `test_manage_debates.py`: UseCase 검증.
- **MCP Protocol Test**:
    - `mcp-inspector` (if available) 또는 간단한 script로 MCP Server 실행 및 Stdio 통신 테스트.

### Manual Verification
1. `uv run python app/interfaces/mcp_server.py` 실행.
2. Claude Desktop 설정(`claude_desktop_config.json`)에 Thingking MCP 등록.
3. Claude에서 "Thingking에 저장된 최근 토론 리스트 보여줘" 질의.
