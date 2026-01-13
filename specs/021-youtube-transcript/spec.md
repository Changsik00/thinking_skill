# Spec 021: YouTube Transcript Integration

## 1. 개요 (Overview)
YouTube 영상의 자막(Transcript)을 추출하여 AI가 영상 내용을 "읽고" 토론할 수 있게 합니다. 이는 "Creative Studio"로서 외부 콘텐츠를 소화하고 재가공하는 첫 번째 단계입니다.

## 2. 문제 정의 (Problem Statement)
*   **Current State**: 사용자는 AI와 토론할 때 텍스트를 직접 입력해야 합니다. 영상의 경우 내용을 일일이 요약하거나 복사해넣어야 합니다.
*   **Need**: YouTube 링크만 주면 AI가 알아서 내용을 파악하고 대화를 시작할 수 있어야 합니다.

## 3. 목표 (Goals)
*   **Tool**: `fetch_transcript(video_url)` 도구 구현.
*   **Context**: 가져온 자막을 `LangGraph`의 상태(State)나 프롬프트 컨텍스트에 포함.
*   **UX**: OpenWebUI에서 "이 영상 요약해줘 [URL]"라고 말하면 즉시 동작.

## 4. 기술 스택 (Tech Stack)
*   **Library**: `youtube-transcript-api` (비공식 API지만 가장 널리 쓰이고 안정적임).
*   **Architecture**:
    *   `Infrastructure`: `YoutubeAdapter` (API 래핑).
    *   `Interface`: MCP Tool로 노출.

## 5. 논-골 (Non-Goals)
*   **Audio Processing**: 오디오 파일을 직접 다운로드해서 Whisper를 돌리는 것은 이번 스펙 아님 (비용/시간 문제). 자막이 있는 영상만 타겟팅.
*   **Video Analysis**: 화면(비전) 분석은 포함하지 않음.

## 6. 주요 질문 및 설계 결정 (Design Decisions & FAQ)
### Q1. API 키가 필요한가요?
*   **No**: `youtube-transcript-api` 라이브러리는 사용자 브라우저처럼 동작하여 비공식적으로 자막을 가져오므로 별도의 Google Cloud API Key 발급이 필요 없습니다. (설치가 간편함)

### Q2. DB 저장 전략 (Vector DB Strategy)
*   **Raw Data**: 스크립트 원본을 무조건 DB에 넣지 않습니다 (Garbage 방지).
*   **Context First**: `fetch_transcript`는 자막 텍스트를 **현재 대화 컨텍스트(Active Memory)**로 가져옵니다.
*   **Save via Debate**: 사용자가 AI와 영상을 분석한 뒤, "이 내용 저장해줘"라고 할 때 `save_debate` 도구를 통해 **요약/분석된 결과**와 함께 저장합니다. 이렇게 해야 나중에 검색할 때 "영상 전체 스크립트"가 아니라 "의미 있는 지식" 단위로 검색됩니다.

### Q3. 실행 시점 (Trigger Flow)
*   **Implicit Trigger**: 사용자가 채팅창에 URL을 입력하면 (`https://youtu.be/...`), LLM이 이를 인식하고 스스로 `fetch_transcript(url)` 도구를 호출합니다.
*   **Flow**: User Input -> Brain (Decide Tool) -> `fetch_transcript` -> Context Update -> Brain (Summary/Answer).
