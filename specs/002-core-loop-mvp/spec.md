# Spec 002: Core Loop MVP

## 1. 개요 (Intent)
LangGraph를 사용하여 **Host(사용자) - Creative(창의) - Critical(비판)** 에이전트 간의 기본적인 토론 루프를 구현하고 검증합니다.
UI 연동 없이 **Terminal(CLI)** 환경에서 로직이 정상 작동하는지 확인하는 것이 목표입니다.

## 2. 범위 (Scope)
- **Agent Roles**:
    - **Creative Agent**: 아이디어를 구체화하고 확장하는 페르소나 (System Prompt).
    - **Critical Agent**: 현실적인 제약과 논리적 허점을 지적하는 페르소나 (System Prompt).
- **LangGraph Logic**:
    - State 정의 (메시지 히스토리 관리).
    - Node 구성: User Input -> Creative -> Critical -> Loop or End.
    - Graph 실행 로직 구현.
- **Infrastructure**:
    - `langchain-google-genai`를 통한 Gemini 1.5 Flash 연동.
    - `.env`에서 `GEMINI_API_KEY` 로드.

## 3. 구현 상세 (Implementation Details)

### 3.1 파일 구조
```
/Users/ck/Project/Thingking/
├── agents/
│   ├── prompts.py       # [NEW] 시스템 프롬프트 정의
│   ├── graph.py         # [NEW] LangGraph 로직 (Nodes, Edges)
│   └── state.py         # [NEW] Graph State 정의 (`TypedDict`)
└── main.py              # [NEW] CLI 실행 엔트리포인트
```

### 3.2 시나리오 예시 (Flow)
**목표**: "뇌가 제대로 동작하는지 검증" (UI/DB 없이 로직만 확인)

1.  **Host (User)**: (터미널 입력) "유튜브 쇼츠 아이디어 좀 내봐. 주제는 '퇴근 후 부업'이야."
2.  **Creative Agent**: "1. 펫시터 브이로그 어때? 2. 편의점 신상 리뷰는?" (아이디어 발산)
3.  **Critical Agent**: "1번은 신뢰성 문제가 있어. 2번은 경쟁이 너무 치열해. 차라리 '펫시터 매칭 꿀팁'으로 좁히는 게 나아." (검증 및 비판)
4.  **Loop End**: (터미널 출력) 비판이 반영된 최종 의견을 보여주고 종료.

이 과정을 통해 **"내 아이디어가 핑퐁을 통해 고도화되는가?"** 를 가장 먼저 확인하려는 것입니다.

## 4. 제약 사항 (Constraints)
- 복잡한 도구(Tool) 사용은 배제합니다 (순수 대화 위주).
- **Clean Architecture**: `main.py`는 로직을 호출하기만 하고, 실제 흐름은 `agents/` 패키지 내부에 캡슐화합니다.
- 모든 코드는 **Type Hinting**을 포함해야 합니다.

## 5. 검증 계획 (Verification Plan)
- `python main.py` 실행 시:
    - Creative, Critical 에이전트가 각자의 역할에 맞는 답변을 출력하는지 육안 확인.
    - 에러 없이 그래프가 종료되는지 확인.
