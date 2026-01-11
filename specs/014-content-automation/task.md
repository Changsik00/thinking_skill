# Task 014: Content Automation (Infrastructure)

- [x] **준비 (Preparation)**
    - [x] `backlog/queue.md` 업데이트.
    - [x] `specs/014-content-automation/*` 문서 생성.

- [x] **구현 (Execution)**
    - [x] **Adapter 개선**: `N8nAdapter` 기능 확장 (Target 파라미터 지원).
    - [x] **Infra Layer (Brain)**: `LangGraphBrain`에 `trigger_automation` 도구 바인딩.
    - [x] **Configuration**: `mcp_server.py` 의존성 주입 연결.

- [x] **검증 (Verification)**
    - [x] `pytest` 작성: `test_n8n_trigger.py` (Mocking requests).
    - [x] 로컬 연결 테스트: n8n Webhook 수신 확인.
