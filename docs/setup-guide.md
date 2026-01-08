# 설정 및 문제 해결 가이드 (Setup & Troubleshooting)

## 1. 사전 요구 사항 (Prerequisites)
- **OS**: macOS (권장), Linux, 또는 Windows (WSL2)
- **Python**: 3.11 버전 이상
- **Docker**: Docker Desktop이 설치되어 있고 실행 중이어야 합니다.

## 2. 설치 (Installation)

1.  **레포지토리 클론**: (이미 완료했다면 생략)
2.  **환경 변수 설정**:
    ```bash
    cp .env.example .env
    # .env 파일을 열어 GEMINI_API_KEY 값을 입력하세요.
    ```
3.  **Python 의존성 설치**:
    MACS는 **uv**를 패키지 매니저로 사용합니다.
    ```bash
    uv sync
    ```

## 3. 인프라 실행 (Running the Infrastructure)
MACS는 행동 및 메모리 계층(Action & Memory)을 위해 Docker를 사용합니다.

```bash
docker compose up -d
```

서비스 실행 확인:
```bash
docker ps
# 'chromadb/chroma' 와 'n8n' 컨테이너가 보여야 합니다.
```

## 4. 문제 해결 (Troubleshooting)

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
