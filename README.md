# MACS (Multi-Agent Creative Studio)
![Build Status](https://github.com/Changsik00/thinking_skill/actions/workflows/test.yml/badge.svg)

아이디어 브레인스토밍부터 유튜브 콘텐츠 소스 생성까지, 로컬 기반의 멀티 에이전트 협업 자동화 시스템입니다.

---

## 1. Architecture (Clean Architecture)

본 프로젝트는 **Clean Architecture** 원칙에 따라 철저하게 계층을 분리했습니다.

- **Domain (`app/domain`)**: 순수 비즈니스 로직 (외부 의존성 0%).
- **Use Cases (`app/usecases`)**: 애플리케이션 흐름 제어 및 오케스트레이션.
- **Infrastructure (`app/infrastructure`)**: LangGraph, ChromaDB, n8n 등 기술적 구현체.
- **Interfaces (`app/interfaces`)**: CLI, FastAPI 등 외부 통신 관문.

## 2. 주요 기능 (Features)

- **삼각 토론 시스템**: 창의적 발산가(Creative)와 냉철한 비평가(Critical)의 자동 토론. (Gemini 2.0/Gemini 1.5 Dynamic Selection)
- **선택적 아카이빙**: Agent가 토론 가치를 판단하여 Markdown 파일 및 ChromaDB(임베딩)에 선택적으로 영구 저장 (`save_debate`).
- **OpenWebUI 지원**: 직관적인 채팅 인터페이스 제공 (MCP Tool 호출 지원).
- **자동화 연동**: n8n Webhook을 통해 외부 워크플로우(Notion, Slack 등) 트리거.
- **REST API**: FastAPI 기반의 HTTP 인터페이스 제공.

## 3. 실행 방법 (Usage)

### 3.1. 사전 요구사항 (Prerequisites)
- Docker & Docker Compose
- `uv` (Python Package Manager)

### 3.2. 인프라 실행 (Docker)
```bash
docker compose up -d
```
ChromaDB, n8n, OpenWebUI (`http://localhost:3000`), MCPO Bridge 컨테이너가 실행됩니다.
**OpenWebUI**에 접속하여 MCP 도구들을 활용할 수 있습니다.

### 3.3. 서버 실행 (FastAPI)
```bash
uv run uvicorn app.main:app --reload
```
서버가 `http://localhost:8000` 에서 시작됩니다.

### 3.4. API 테스트 (Curl)
```bash
curl -X POST "http://localhost:8000/api/v1/debates" \
     -H "Content-Type: application/json" \
     -d '{"topic": "인공지능의 미래"}'
```

### 3.5. 테스트 실행 (Unit Test)
```bash
uv run pytest
```
Mock 기반의 유닛 테스트를 수행합니다.

### 3.6. MCP Server 실행
```bash
uv run python -m app.interfaces.mcp_server
```
Obsidian/Claude Desktop 연동을 위한 MCP 서버를 실행합니다.

## 4. 폴더 구조 (Structure)
```
app/
├── domain/             # Entities, Interfaces
├── usecases/           # Business Logic
├── infrastructure/     # Adapters (LLM, Storage, Automation)
└── interfaces/         # Adapters (API, CLI)
tests/                  # Unit Tests & Mocks
specs/                  # Development Specifications
```

## 5. Documentation
- [Setup Guide](docs/setup-guide.md)
- [Architecture Details](docs/architecture.md)
- [MCP Guide](docs/mcp-guide.md)
