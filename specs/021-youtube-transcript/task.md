# Task 021: YouTube Transcript Integration

- [x] **준비 (Preparation)**
    - [x] 브랜치 생성 (`feat/021-youtube-transcript`).
    - [x] 문서 작성 (`spec.md`, `plan.md`).
    - [ ] 승인 (Approval).

- [ ] **구현 (Execution)**
    - [ ] **Install**: `uv add youtube-transcript-api`.
    - [ ] **Adapter**: `YoutubeAdapter` 구현 (`infrastructure/external/`).
    - [ ] **Tool**: `mcp_server.py`에 도구 추가 및 `Brain` 바인딩.

- [ ] **검증 (Verification)**
    - [ ] **Unit Test**: `test_youtube_adapter.py` 작성 및 통과.
    - [ ] **Lint**: `ruff check` 통과.
    - [ ] **E2E**: 실제 영상 URL로 요약 요청 테스트.
