# Plan 021: YouTube Transcript Implementation

## 1. Setup
*   **Dependency**: `uv add youtube-transcript-api`.

## 2. Architecture Design
*   **Adapter Pattern**: `app/infrastructure/external/youtube_adapter.py`
    *   `class YoutubeAdapter`:
        *   `get_transcript(url: str) -> str`: URL 파싱 -> Video ID 추출 -> `YouTubeTranscriptApi.get_transcript` 호출 -> 텍스트로 병합 반환.
*   **Domain**: 별도 엔티티 불필요 (String으로 처리).
*   **Interface (MCP)**:
    *   `app/interfaces/mcp_server.py`에 `fetch_youtube_script` 도구 등록.
    *   `LangGraphBrain`이 이 도구를 사용할 수 있도록 `bind_tools`에 포함.

## 3. Implementation Steps
1.  **Install**: 패키지 설치.
2.  **Adapter**: `YoutubeAdapter` 구현 (Video ID 정규식 추출 포함).
3.  **Tool Binding**: `mcp_server.py`에서 `YoutubeAdapter` 인스턴스화 및 툴 등록.
4.  **Integration**: `create_combined_app`에서 의존성 주입.

## 4. Verification Plan
*   **Unit Test**: `tests/unit/infrastructure/test_youtube_adapter.py`
    *   `YouTubeTranscriptApi.get_transcript`를 Mocking하여 테스트.
    *   잘못된 URL 처리 테스트.
*   **Manual Test**: 실제 YouTube 영상(예: TED Talk, 뉴스 등 자막 있는 영상) URL로 OpenWebUI에서 테스트.
