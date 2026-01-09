# 설정 및 문제 해결 가이드 (Setup & Troubleshooting)

## 1. 사전 요구 사항 (Prerequisites)
- **OS**: macOS (권장), Linux, 또는 Windows (WSL2)
- **Python**: 3.11 버전 이상
- **Docker**: Docker Desktop이 설치되어 있고 실행 중이어야 합니다.

## 2. 설치 (Installation)

1.  **레포지토리 클론**: (이미 완료했다면 생략)
2.  **환경 변수 설정**:
    ```bash
    cp .env### 2. 환경 설정 (.env)
`.env.example` 파일을 복사하여 `.env`를 생성하고 키를 입력하세요.

```bash
cp .env.example .env
```

- `GEMINI_API_KEY`: Google AI Studio에서 발급받은 키.
- `CHROMA_PORT`: **8001** (Docker 포트 충돌 방지용)
- `N8N_WEBHOOK_URL`: n8n 웹훅 주소 (선택 사항)

### 3. Running the Agent (실행 방법)

**Step 1: Start Infrastructure (Docker)**
DB(Chroma)와 UI(OpenWebUI), 자동화(n8n) 도구를 실행합니다.
```bash
docker compose up -d
```
- **OpenWebUI**: `http://localhost:3000` (채팅 인터페이스)
- **n8n**: `http://localhost:5678` (워크플로우)
- **ChromaDB**: `localhost:8001` (벡터 DB)

**Step 2: Start API Server (FastAPI)**
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
서버가 `http://localhost:8000` 에서 시작됩니다.


## 4. n8n 설정 (n8n Setup)

n8n을 처음 실행하면 초기 설정이 필요합니다.

1.  **접속**: 브라우저에서 [http://localhost:5678](http://localhost:5678) 접속.
2.  **계정 생성**: 'Set up admin account' 화면에서 이메일/비밀번호 입력 (로컬 전용이므로 자유롭게 입력).
3.  **Webhook 생성**:
    - 우측 상단 `+ Add first step` 클릭.
    - 검색창에 `Webhook` 입력 후 선택.
    - **Authentication**: `None` 선택.
    - **HTTP Method**: `POST` 선택.
    - **Path**: `macs-endpoint` 입력.
    - 상단 `Webhook` 노드 창 닫기 (X 버튼).
4.  **활성화**:
    - 우측 상단 `Activate` 스위치를 켭니다. (Activate Workflow)

> **Note**: 이 설정을 마치면 에이전트 실행 시 "n8n Webhook triggered successfully" 메시지가 뜹니다.

## 5. 문제 해결 (Troubleshooting)

### 문제: Docker 연결 실패
**에러**: `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
**해결**:
- **Docker Desktop** 앱이 실행 중인지 확인하세요.
- macOS의 경우, 상단 메뉴바에 고래 아이콘이 있는지 확인하세요.

### 문제: 컨테이너 이름 충돌
**에러**: `Conflict. The container name "/thingking-n8n-1" is already in use...`
**해결**:
이전 컨테이너가 남아있는 경우입니다. 삭제 후 다시 실행하세요:
```bash
docker rm -f thingking-n8n-1 thingking-chroma-1
docker compose up -d
```
