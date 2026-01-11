# 작업 목록 - Spec 013: 선택적 아카이빙

- [ ] **사전 준비 (Prep)**
    - [x] Spec 작성
    - [x] Plan 작성
    - [ ] Plan 승인

- [x] **구현 (Execution)**
    - [x] **App Layer**: `RunDebateUseCase` 자동 저장 로직 제거.
    - [x] **Infra Layer (Prompt)**: `prompts.py`에 저장 도구 사용 지침 추가.
    - [x] **Infra Layer (Graph)**: `LangGraphBrain`에 `bind_tools` 및 `ToolNode` 아키텍처 적용.
        - Tool 정의 (또는 `mcp_server`에서 import).
        - Graph 구조 변경 (Conditional Edge 추가).

- [x] **검증 (Verification)**
    - [x] `run_debate_cli` 테스트: 일반 대화 (저장 X) vs 저장 요청 (저장 O).
