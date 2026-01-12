# MACS (Multi-Agent Creative Studio)
![Build Status](https://github.com/Changsik00/thinking_skill/actions/workflows/test.yml/badge.svg)

아이디어 브레인스토밍부터 유튜브 콘텐츠 소스 생성까지, 로컬 기반의 멀티 에이전트 협업 자동화 시스템입니다.

---

## 1. Features (주요 기능)
- **🤖 삼각 토론 시스템 (Triangular Debate)**: 창의적 발산가(Creative)와 냉철한 비평가(Critical)의 자동 토론. (Gemini 2.0 Dynamic Selection)
- **🧠 선택적 아카이빙 (Smart Archiving)**: AI가 가치 있다고 판단하거나 사용자가 요청할 때만 결과 저장 (`data/archives` & ChromaDB).
- **🔧 MCP Support**: Claude Desktop, OpenWebUI 등에서 내 로컬 데이터와 도구를 직접 호출 (`search_debates`, `save_debate`).
- **🔗 Automation (Nerve)**: n8n Webhook을 통해 Slack, Notion 등 외부 도구로 워크플로우 확장.
- **📊 Admin Dashboard**: Streamlit 기반의 데이터 시각화 및 검색 테스트 도구.

## 2. Infrastructure & Stack
본 프로젝트는 **Local-First**를 지향하며 아래의 기술 스택과 포트를 사용합니다.

### 2.1. Tech Stack
| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Logic** | **LangChain / LangGraph** | 멀티 에이전트 상태 관리 및 오케스트레이션 |
| **LLM** | **Google Gemini** | 2.0 Flash (Creative) / 1.5 Pro (Critical) |
| **DB** | **ChromaDB** | 벡터 임베딩 저장 및 시맨틱 검색 |
| **Interface** | **FastAPI / OpenWebUI** | REST API 및 채팅 UI |
| **Admin** | **Streamlit** | 데이터 관리 대시보드 |
| **Auto** | **n8n** | 외부 서비스 연동 및 워크플로우 자동화 |

### 2.2. Port Map
로컬 포트 충돌 방지를 위해 아래 포트를 사용합니다.

| Port | Service | Description |
| :--- | :--- | :--- |
| **8000** | **FastAPI / MCP Server** | 메인 백엔드 서버 (SSE 포함) |
| **3000** | **OpenWebUI** | 채팅 클라이언트 웹 인터페이스 |
| **8501** | **Streamlit Admin** | 관리자 대시보드 |
| **5678** | **n8n** | 워크플로우 자동화 툴 |
| **8080** | **ChromaDB** | 벡터 데이터베이스 API |

## 3. Quick Start (Usage)

### 3.1. Prerequisites
- **Python 3.11+** & **[uv](https://docs.astral.sh/uv/)** (Package Manager)
- **Docker** & Docker Compose (for ChromaDB, n8n, OpenWebUI)
- **Generic API Key**: `.env` 설정 필요 (참고: `docs/setup-guide.md`)

```bash
# 설치 및 의존성 동기화
uv sync
```

### 2.2. Running the System
원하는 인터페이스에 따라 실행 명령어를 선택하세요.

| Mode | Command | Description |
| :--- | :--- | :--- |
| **All Infrastructure** | `docker compose up -d` | ChromaDB, n8n, OpenWebUI 실행. |
| **Admin Dashboard** | `uv run streamlit run app/admin/dashboard.py` | 저장된 데이터 조회 및 검색 테스트. |
| **MCP Server** | `uv run python -m app.interfaces.mcp_server` | Claude Desktop 연동용 (Stdio). |
| **MCP Server (SSE)** | `uv run python -m app.interfaces.mcp_server --sse` | OpenWebUI 연동용 (HTTP SSE). |
| **FastAPI Server** | `uv run uvicorn app.main:app --reload` | REST API 개발용. |
| **Unit Test** | `uv run pytest` | 로컬 테스트 실행. |

---

## 4. Project Structure (폴더 구조)
**Clean Architecture** 원칙에 따라 계층이 분리되어 있습니다.

```text
.
├── app/
│   ├── domain/             # [Core] 순수 비즈니스 로직 & 엔티티
│   ├── usecases/           # [App Logic] 애플리케이션 흐름 제어
│   ├── infrastructure/     # [Impl] LangGraph, Chroma, n8n 등의 구현체
│   └── interfaces/         # [Entry] API, CLI, MCP Server 진입점
├── docs/                   # 프로젝트 문서 (가이드, 아키텍처)
├── specs/                  # 개발 명세서 (Spect-Plan-Task logs)
├── tests/                  # 유닛 테스트 & Mocks
├── backlog/                # 프로젝트 백로그 (Queue)
└── data/                   # (GitIgnore) 로컬 데이터 저장소
```

## 5. Documentation (문서)
더 자세한 내용은 아래 문서를 참고하세요.

| 문서 | 설명 |
| :--- | :--- |
| **[Setup Guide](docs/setup-guide.md)** | 초기 설치 및 환경 변수 설정 가이드 |
| **[Architecture](docs/architecture.md)** | 클린 아키텍처 설계 원칙 및 다이어그램 |
| **[Core Loop](docs/core-loop-architecture.md)** | LangGraph 기반의 토론 엔진 동작 원리 |
| **[MCP Guide](docs/mcp-guide.md)** | Model Context Protocol 개념 및 연동 방법 |
| **[OpenWebUI Guide](docs/open-webui-guide.md)** | OpenWebUI와 MCP 도구 사용법 |
| **[Admin Guide](docs/admin-guide.md)** | 대시보드 사용법 및 ChromaDB 확인 |
| **[Data Storage Policy](docs/data-storage-policy.md)** | 선택적 아카이빙 및 파일 저장 정책 |
