# Spec 005.1: Documentation & Housekeeping

## 1. Intent (의도)
**"지도를 현행화한다."**
빠른 개발로 인해 문서(README, Backlog)가 실제 코드(`Clean Arch`, `FastAPI Server`)와 달라졌습니다. 이를 동기화하여 프로젝트의 가독성과 유지보수성을 높입니다.

## 2. Scope (범위)

### 2.1. Backlog (`backlog/queue.md`)
- Phase 4 (Clean Refactoring) [x]
- Phase 4.5 (TDD) [x]
- Phase 5 (FastAPI MVP) [x]
- **NEW**: Phase 5.5 (Streaming Support) 추가.

### 2.2. README (`README.md`)
- **Folder Structure**: `agents/` 삭제 및 `app/domain`, `app/usecases` 등 반영.
- **Run Commands**: `uv run uvicorn app.main:app` 등 최신 명령어 가이드.

### 2.3. Architecture Doc (`docs/architecture.md`)
- **Diagram**: Domain / UseCase / Infrastructure / Interface 계층 구조 설명.
- **Rules**: "Domain은 의존성이 없어야 한다" 등 아키텍처 원칙 명시.

## 3. Verification Plan
- `README.md`를 보고 처음 온 개발자가 서버를 띄울 수 있어야 함.
- `backlog/queue.md`가 현재 진행 상황(Phase 5 완료, 5.5 예정)을 정확히 반영해야 함.
