# Spec 008: MCP Server Integration

## 1. Goal
Thingking 애플리케이션을 **Model Context Protocol (MCP)** 서버로 확장하여, 외부 에이전트(Obsidian 플러그인, Cursor, Claude Desktop 등)가 Thingking의 데이터와 기능에 접근할 수 있도록 합니다.
기존의 단방향 "파일 저장" 방식에서 벗어나, 외부에서 Thingking의 지식 베이스를 **조회(Resource)** 하고 **요청(Tool)** 할 수 있는 양방향 연동을 목표로 합니다.

## 2. Background
- **As-Is**: `specs/007-obsidian`에서 구현한 방식은 토론 결과를 로컬 파일 시스템(`OBSIDIAN_VAULT_PATH`)에 단순 저장하는 단방향 흐름입니다. ("무지성 save")
- **To-Be**: Obsidian이나 다른 MCP Client가 "Thingking, 방금 토론한 내용 요약해줘" 또는 "지난달 토론 목록 보여줘"와 같이 맥락을 조회할 수 있어야 합니다.

## 3. Scope
이 Spec은 **Core MCP Server** 구축과 **기본 Resource/Tool** 구현을 범위로 합니다.

### 3.1. MCP Server Setup
- `mcp` 라이브러리를 사용해 Thingking 내에 MCP Server 인스턴스 구성.
- 기존 FastAPI 서버와 공존하거나, 별도 진입점(`python -m app.mcp`) 제공.
- **Transport**: Stdio (로컬 실행용) 및 SSE (원격/FastAPI 통합용) 고려.
    - 1차 목표는 **Stdio** (Claude Desktop/Cursor 연동 최적화).

### 3.2. Resources (데이터 조회)
- `debate://latest`: 가장 최근 토론 내용 조회.
- `debate://list`: 저장된 토론 목록 조회.
- `debate://{id}`: 특정 토론 전문 조회.

### 3.3. Tools (기능 실행)
- `search_debates(query: str)`: 키워드로 과거 토론 검색 (Vector DB 활용).
- `start_debate(topic: str)`: (Optional) 외부에서 새로운 토론 트리거.

## 4. Architecture
- **Layer**: `app/interfaces/mcp/` 패키지 신설.
- **Dependency**: `mcp` 패키지 추가.
- **Interaction**: MCP Layer -> UseCases -> Repositories.

## 5. Constraints
- Obsidian 자체가 MCP Client가 되려면 별도 플러그인이 필요할 수 있음. (이 Spec에서는 Server 구현에 집중)
- Clean Architecture 원칙 준수 (MCP는 Interface Layer에 속함).
