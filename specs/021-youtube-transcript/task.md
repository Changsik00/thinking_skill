# Task 021: YouTube Transcript Integration

- [x] **준비 (Preparation)**
    - [x] 브랜치 생성 (`feat/021-youtube-transcript`).
    - [x] 문서 작성 (`spec.md`, `plan.md`).
    - [x] 승인 (Approval).

- [x] **구현 (Execution)**
    - [x] **Install**: `uv add youtube-transcript-api`.
    - [x] **Adapter**: `YoutubeAdapter` 구현 (`infrastructure/external/`).
    - [x] **Tool**: `mcp_server.py`에 도구 추가 및 `Brain` 바인딩.

- [x] **검증 (Verification)**
    - [x] **Unit Test**: `test_youtube_adapter.py` 작성 및 통과.
    - [x] **Lint**: `ruff check` 통과.
    - [x] **E2E**: 실제 영상 URL로 요약 요청 테스트 (Manual).
