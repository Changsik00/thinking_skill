# 작업 목록 - Spec 012: 모델 업그레이드

- [ ] **사전 준비 (Prep)**
    - [x] Spec 작성 (`spec.md`)
    - [x] Plan 작성 (`plan.md`)
    - [ ] Plan 승인

- [ ] **구현 (Execution)**
    - [ ] **Config**: `.env.example` 및 `.env` 업데이트.
    - [ ] **Core Interface**: `ThinkingBrain` 인터페이스 수정 (`model_name` param).
    - [ ] **Infrastructure**: `LangGraphBrain` 동적 모델 로딩 구현 (`configurable` 활용).
    - [ ] **Application**: `RunDebateUseCase`에 `model_name` 파라미터 전달 로직 추가.
    - [ ] **API**: `openai_router` (요청 모델명 추출/전달 및 `list_models` 최신화).

- [ ] **검증 (Verification)**
    - [ ] `run_debate_cli.py` 실행 테스트 (모델 로드 확인)
