# OpenWebUI 사용 가이드 (User Manual)

이 문서는 **OpenWebUI**를 사용하여 에이전트(MACS)와 대화하는 방법을 단계별로 설명합니다.

## 1. 초기 접속 (Initial Access)

1.  터미널에서 인프라를 실행합니다:
    ```bash
    docker compose up -d
    ```
    *(이미 실행 중이라면 생략 가능)*

2.  브라우저를 열고 다음 주소로 접속합니다:
    - **URL**: [http://localhost:3000](http://localhost:3000)

3.  **관리자 계정 생성 (First Admin)**:
    - 첫 접속 시 로그인 화면이 나옵니다.
    - 하단의 **"Sign up"** 버튼을 클릭합니다.
    - 이름, 이메일, 비밀번호를 입력하고 가입합니다.
    - *Note*: 이 데이터는 로컬(`docker volume`)에만 저장되므로, 이메일은 실제가 아니어도 됩니다 (예: `admin@macs.com`).

## 2. 모델 연결 설정 (Connection Setup)

OpenWebUI가 우리 FastAPI 서버(`app`)를 "OpenAI"라고 착각하게 만들어야 합니다.

1.  로그인 후, 왼쪽 하단 프로필 아이콘 클릭 -> **Settings** (설정) 선택.
2.  **Connections** 탭(또는 **Admin Settings** -> **Connections**)으로 이동합니다.
3.  **OpenAI API** 섹션을 찾습니다.
4.  다음과 같이 입력합니다:
    - **API Base URL**: `http://host.docker.internal:8000/openai/v1`
        - *주의*: `localhost`가 아니라 `host.docker.internal`을 써야 Docker 컨테이너가 내 컴퓨터(Host)의 8000번 포트를 찾을 수 있습니다.
    - **API Key**: `sk-any` (아무 값이나 입력)
5.  오른쪽의 **Save** (저장) 또는 **Verify Connection** 버튼을 누릅니다.
    - 초록색으로 "Verified"가 뜨면 성공입니다! 🟢

## 3. 대화하기 (Chatting)

1.  메인 화면으로 돌아옵니다.
2.  상단 모델 선택창(Select Model)을 클릭합니다.
    - `gemini-2.0-flash-001` 또는 `macs-agent`가 목록에 보여야 합니다.
3.  모델을 선택하고 채팅창에 주제를 입력합니다.
    - 예: "AI와 인간의 창의성 대결"
4.  에이전트가 생각하는 과정(Thinking Process)을 거쳐 답변하는 것을 실시간으로 지켜봅니다. 🌊

## 4. 문제 해결 (Troubleshooting)

### Q. 모델 목록이 안 보여요!
- **FastAPI 서버가 켜져 있는지 확인하세요**: `uv run uvicorn ... --port 8000`이 실행 중이어야 합니다.
- **주소 확인**: 설정에서 URL 뒤에 `/openai/v1`을 정확히 붙였는지 확인하세요.
- **Docker Network**: 만약 `host.docker.internal`이 동작하지 않는다면(Linux 등), `http://172.17.0.1:8000/openai/v1`을 시도해보세요.
