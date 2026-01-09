# Task List: Spec 008 (MCP Server Integration)

## 1. 기획 단계 (Planning Phase)
- [x] Spec 008 초안 작성 (`spec.md`, `pr_description.md`)
- [x] 구현 계획 작성 (`plan.md`)
- [x] **Plan 승인 완료** <!-- id: 0 -->

## 2. 구현 단계 (Execution Phase)
- [x] **Task 1: 도메인 레이어 업데이트** <!-- id: 1 -->
    - `MemoryVault` 인터페이스에 `list_debates`, `get_debate` 메소드 추가.
- [x] **Task 2: 어댑터 구현** <!-- id: 2 -->
    - `LocalAdapter`에서 마크다운 파싱(`_parse_markdown_file`) 및 조회 목록(`list_debates`) 구현.
    - `get_debate` 구현.
- [x] **Task 3: 유스케이스 구현** <!-- id: 3 -->
    - `app/usecases/manage_debates.py` 생성 (`ListDebatesUseCase`, `GetDebateUseCase`).
- [x] **Task 4: MCP 서버 인터페이스** <!-- id: 4 -->
    - `app/interfaces/mcp_server.py` 생성.
    - Resources 등록 (`debate://list`, `debate://{topic}`).
    - Tool 등록 (`search_debates`).
    - `pyproject.toml`에 `mcp` 의존성 추가.
- [x] **Task 5: 문서화 (Documentation)** <!-- id: 5 -->
    - `docs/mcp-guide.md` 작성 (개념, 아키텍처 다이어그램, 사용법).
    - `README.md` 업데이트.

## 3. 검증 단계 (Verification Phase)
- [x] **Task 6: 단위 테스트** <!-- id: 6 -->
    - `tests/unit/usecases/test_manage_debates.py` 생성.
    - `uv run pytest`로 전체 테스트 수행.
- [x] **Task 7: 수동 검증** <!-- id: 7 -->
    - `mcp-inspector` 또는 `python app/interfaces/mcp_server.py`로 동작 검증. (PR Review 시 사용자 직접 수행)
