# Feature: Spec 021 유튜브 자막 연동 (YouTube Transcript Integration)

## 🎯 목표 (Goal)
AI가 YouTube 영상의 자막(Transcript)을 가져와 내용을 "읽을" 수 있게 합니다. 이를 통해 사용자가 "이 영상 요약해줘: [URL]"과 같이 질문하면 실제 영상 내용을 바탕으로 답변할 수 있습니다.

## 🛠️ 변경 사항 (Changes)
### 인프라 (Infrastructure)
*   **[NEW]** `app/infrastructure/external/youtube_adapter.py`: `youtube-transcript-api`를 사용하여 `YoutubeAdapter`를 구현했습니다. URL 파싱(정규식) 및 자막 추출/포맷팅을 담당합니다.
*   **[UPDATE]** `pyproject.toml`: `youtube-transcript-api` 의존성을 추가했습니다.

### 인터페이스 (Interface)
*   **[UPDATE]** `app/interfaces/mcp_server.py`:
    *   `YoutubeAdapter`를 초기화합니다.
    *   `fetch_transcript(url)` 함수를 MCP 도구(Tool)로 등록하여 Agent가 사용할 수 있게 합니다.
    *   `LangGraphBrain`에 이 도구를 주입합니다.

### 핵심 로직 (Brain)
*   **[REFACTOR]** `app/infrastructure/llm/langgraph_adapter.py`:
    *   `LangGraphBrain`이 생성자(`__init__`)에서 외부 도구 목록(`tools`)을 받을 수 있도록 수정했습니다.
    *   `_build_graph` 메서드에서 주입받은 도구들을 `ToolNode`에 포함시켜, Agent가 확장 가능하도록 개선했습니다.

## ✅ 검증 (Verification)
*   **단위 테스트 (Unit Tests)**: `tests/unit/infrastructure/test_youtube_adapter.py` 통과.
    *   표준 URL, 단축 URL, 임베드 URL 등 다양한 형식을 올바르게 파싱하는지 확인했습니다.
    *   API 응답을 Mocking하여 텍스트가 올바르게 포맷팅되는지 검증했습니다.
*   **통합 체크 (Integration Checks)**: `test_selective_archiving.py` 통과 (Brain 로직 회귀 테스트).
*   **린트 (Linting)**: `ruff check` 및 포맷팅 검사 통과.
