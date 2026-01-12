# Task 016: DevOps Automation (Infrastructure)

- [x] **준비 (Preparation)**
    - [x] `specs/016-devops-automation/*` 문서 작성 (Spec, Plan).
    - [x] 브랜치 생성 (`feat/016-devops-automation`).
    - [x] Plan 승인 (Blocking).

- [/] **구현 (Execution)**
    - [/] **Infrastructure Layer**: GitHub Actions Workflow 생성 및 설정.
        - [x] `.github/workflows/test.yml` 생성 (uv, pytest).
        - [x] Feature Branch Trigger 설정 (`main`, `feat/**`).
        - [x] Env Var 설정 (`GEMINI_API_KEY` fix).
    - [/] **Test Fixes (Regressions detected by CI)**:
        - [ ] Fix `test_openai_router.py`: `mock_generator` signature.
        - [ ] Fix `test_run_debate.py`: `FakeBrain.think` signature.
    - [ ] **Data/Docs Layer**: README 업데이트.
        - [ ] Build Status Badge 추가.

- [ ] **검증 (Verification)**
    - [ ] **CI Test**: GitHub Actions 실행 확인 (`gh run watch`).
    - [ ] **Pipeline Success**: `pytest` 통과 여부 확인 (Green).
