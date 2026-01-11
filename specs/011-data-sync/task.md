# 작업 목록 - Spec 011: 데이터 동기화 도구

- [ ] **사전 준비 (Prep)**
    - [x] Spec 작성 (`spec.md`)
    - [x] Plan 작성 (`plan.md`)
    - [ ] Plan 승인

- [ ] **구현 (Execution)**
    - [ ] **Core Logic**: `SyncDebatesUseCase` 및 Unit Test 작성 (@ `app/usecases/sync_debates.py`, `tests/usecases/test_sync_debates.py`)
    - [ ] **Infra**: ChromaDB Repository에 `list_all_ids` 메서드 추가 (@ `app/infrastructure/chroma_debate_repository.py`)
    - [ ] **Interface**: MCP Server에 `sync_debates` 도구 등록 (@ `app/interfaces/mcp_server.py`)

- [ ] **검증 (Verification)**
    - [ ] Unit Test 통과 (`pytest`)
    - [ ] Manual Test: 파일 삭제 후 Sync 동작 확인
