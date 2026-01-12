# Task 019: Persona Management System

- [ ] **준비 (Preparation)**
    - [x] 브랜치 생성 (`feat/019-persona-management`).
    - [x] 문서 작성 (`spec.md`, `plan.md`).
    - [ ] 승인 (Approval).

- [ ] **구현 (Execution)**
    - [ ] **Config**
        - [ ] `configs/personas.yaml` 생성 및 기존 프롬프트 이관.
    - [ ] **Domain**
        - [ ] `app/domain/entities/persona.py` 생성.
        - [ ] `app/domain/repositories/persona_repository.py` (Interface) 생성.
    - [ ] **Infrastructure**
        - [ ] `app/infrastructure/storage/file_persona_repository.py` 구현.
    - [ ] **Refactoring**
        - [ ] `LangGraphBrain` 수정 (Repository 주입).
        - [ ] `mcp_server.py`, `cli.py` 등 DI 설정 업데이트.
        - [ ] `prompts.py` 삭제 (또는 Deprecated 처리).

- [ ] **검증 (Verification)**
    - [ ] `tests/unit/infrastructure/test_file_persona_repo.py` 추가.
    - [ ] 기존 `test_run_debate.py` 영향도 확인 및 수정.
    - [ ] 수동 테스트: YAML 변경 후 반영 확인.
