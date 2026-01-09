# Phase 6: Web UI (OpenWebUI Integration)

## 📌 Summary
터미널을 넘어 **웹 기반의 채팅 인터페이스(OpenWebUI)**를 도입했습니다.
이제 브라우저에서 ChatGPT와 대화하듯이 에이전트와 토론할 수 있습니다.

## 🛠 Key Changes

### 1. OpenAI Compatibility Layer (`Adapter`)
- **OpenAI Adapter**: `app/interfaces/api/openai_router.py`
    - `POST /openai/v1/chat/completions`: OpenWebUI의 요청을 받아 `RunDebateUseCase`를 실행하고, 결과를 OpenAI 포맷(SSE)으로 변환하여 스트리밍합니다.
    - `GET /openai/v1/models`: UI 드롭다운에 모델 목록(`macs-agent`)을 표시합니다.
- **TDD Verification**: `tests/unit/interfaces/test_openai_router.py`를 통해 엔드포인트 동작을 검증했습니다.

### 2. Infrastructure (`Docker`)
- **Port Adjustment**: ChromaDB 포트를 `8001`로 변경하여 FastAPI(`8000`)와의 충돌을 해결했습니다.
- **OpenWebUI Service**: `docker-compose.yml`에 추가 (`http://localhost:3000`).

### 3. Documentation (`Docs`)
- `docs/setup-guide.md`: 포트 변경 사항 및 Docker 실행 가이드 업데이트.
- **`docs/open-webui-guide.md` (New)**: 관리자 계정 생성부터 모델 연결까지 그림 없이도 따라할 수 있는 상세 가이드.

## ✅ Verification Steps (Manual)
1. `docker compose up -d` (Re-create containers).
2. `uv run uvicorn app.main:app --port 8000 --reload`.
3. 접속: [http://localhost:3000](http://localhost:3000).
4. 가이드(`docs/open-webui-guide.md`)에 따라 설정 후 채팅 테스트.
