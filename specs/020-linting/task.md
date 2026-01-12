# Task 020: Linting & Formatting Automation

- [ ] **준비 (Preparation)**
    - [x] 브랜치 생성 (`feat/020-linting`).
    - [x] 문서 작성 (`spec.md`, `plan.md`).
    - [ ] 승인 (Approval).

- [ ] **구현 (Execution)**
    - [ ] **Installation**: `uv add --dev ruff`.
    - [ ] **Config**: `pyproject.toml`에 `[tool.ruff]` 설정 추가.
    - [ ] **Fix**: 기존 코드베이스에 `ruff format` 및 `ruff check --fix` 적용.
    - [ ] **CI**: `.github/workflows/test.yml` 업데이트.

- [ ] **검증 (Verification)**
    - [ ] 로컬 실행: `uv run ruff check .` 성공 확인.
    - [ ] CI 실행: GitHub Actions 로그 확인.
