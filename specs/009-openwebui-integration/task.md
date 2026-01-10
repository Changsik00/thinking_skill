# Task List: Spec 009 (OpenWebUI Integration)

## 0. 기획 단계 (Planning)
- [x] Spec 009 초안 작성 (`spec.md`)
- [x] 구현 계획 작성 (`plan.md`)
- [x] **Plan 승인 대기** <!-- id: 0 -->

## 1. 구현 단계 (Execution)
- [x] **Task 1: Save Tool 구현** <!-- id: 1 -->
    - `app/interfaces/mcp_server.py`에 `save_debate` 도구 추가.
    - `tests/unit/interfaces/test_mcp_server.py`에 테스트 추가.
- [x] **Task 2: SSE 모드 지원** <!-- id: 2 -->
    - `FastMCP`를 사용하여 SSE 서버 구동 방식 구현.
    - `uvicorn` 의존성 확인 및 추가.
- [x] **Task 3: 문서 업데이트** <!-- id: 3 -->
    - `docs/mcp-guide.md`에 OpenWebUI 연동 가이드 추가.

## 2. 검증 단계 (Verification)
- [x] **Task 4: 수동 검증 (OpenWebUI)** <!-- id: 4 -->
    - 서버 실행 및 OpenWebUI 연결 테스트.
    - 채팅을 통한 저장 기능 확인.
