# 구현 계획 - Spec 010: OpenWebUI OpenAPI Bridge 연결

## 사용자 검토 필요 (User Review Required)
> [!NOTE]
> 이 계획은 Docker 환경에 새로운 컨테이너(`mcpo`)를 하나 추가합니다. 호스트의 **3001번 포트**를 사용하므로, 해당 포트가 비어있어야 합니다.

## 변경 제안 (Proposed Changes)

### 1. Docker 구성 변경
#### [MODIFY] [docker-compose.yml](file:///Users/ck/Project/Thingking/docker-compose.yml)
- `mcpo` 서비스를 추가합니다. (이미지: `ghcr.io/open-webui/mcpo:main`)
- 컨테이너 포트 80을 호스트 포트 **3001**에 매핑합니다.
- 설정 파일 매핑: `./config/mcpo.json` -> `/app/config.json`
- 환경 변수 설정: `MACS_MCP_URL` 등으로 내부 통신 경로 지정.

### 2. 설정 파일 생성
#### [NEW] [config/mcpo.json](file:///Users/ck/Project/Thingking/config/mcpo.json)
- MCP 서버 정보를 정의하는 JSON 파일입니다.
- Thingking 서버의 SSE 주소(`http://host.docker.internal:8000/mcp/sse`)를 등록합니다.

## 검증 계획 (Verification Plan)
### 자동화 테스트
- `curl http://localhost:3001/openapi.json` 명령어로 프록시가 정상적으로 OpenAPI 문서를 생성하는지 확인합니다.

### 수동 검증
1. OpenWebUI > 관리자 설정 > 외부 도구 (External Tools) 접속.
2. 연결 추가 (+) 버튼 클릭.
3. **Type**: `OpenAPI` 선택 (기본값).
4. **URL**: `http://host.docker.internal:3001/openapi.json` 입력.
5. 저장 후 채팅창에서 `+` 버튼을 눌러 `save_debate` 도구가 뜨는지 확인.
