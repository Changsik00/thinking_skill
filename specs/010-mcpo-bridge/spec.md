# Spec 010: OpenWebUI OpenAPI Bridge (mcpo) 통합

## 1. 배경 및 문제점 (Problem Statement)
이전 단계(Spec 009)에서 OpenWebUI의 **Native MCP 지원(SSE 직접 연결)**을 시도했으나, 사용자 환경(v0.6.43)에서 **MCP 연결 UI(Type 드롭다운)가 보이지 않는 현상**이 발생했습니다. 브라우저 캐시 초기화 및 최신 이미지 업데이트를 수행했음에도 UI가 활성화되지 않아, 대안적이고 확실한 연결 방식이 필요해졌습니다.

## 2. 결정 사항 (Decision)
**"OpenAPI Bridge (mcpo)" 방식을 공식 채택합니다.**
불안정한 Experimental UI를 억지로 활성화하기보다, OpenWebUI가 기본적으로 완벽하게 지원하는 **OpenAPI 표준**을 활용하여 MCP 서버를 연결합니다. 이를 위해 공식 프록시 도구인 `mcpo` 컨테이너를 도입합니다.

## 3. 기존 방식 vs 변경 방식 비교 (Comparison)

| 구분 | 기존 방식 (Spec 009: Native) | 변경 방식 (Spec 010: Bridge) |
| :--- | :--- | :--- |
| **연결 구조** | `OpenWebUI` --(SSE)--> `Thingking` | `OpenWebUI` --(OpenAPI)--> `mcpo` --(SSE)--> `Thingking` |
| **장점** | 구조가 단순함 (추가 컨테이너 불필요) | **호환성이 완벽함** (UI 제약 없음), 표준 OpenAPI 사용 |
| **단점** | UI 버그 발생 시 사용 불가 | 컨테이너 하나(`mcpo`)를 추가로 띄워야 함 |
| **사용자 설정** | 'Admin > External Tools > MCP' (현재 메뉴 없음) | 'Admin > External Tools > **OpenAPI**' (메뉴 존재함) |

## 4. 목표 (Goal)
`mcpo` 프록시 서버를 통해 Thingking MCP 서버를 OpenWebUI에 **OpenAPI 도구**로 등록합니다.
- **입력**: Thingking MCP 서버 (`http://host.docker.internal:8000/mcp/sse`)
- **중계**: `mcpo` 컨테이너 (Port 3001)
- **출력**: OpenAPI 사양서 (`http://host.docker.internal:3001/openapi.json`)

## 5. 범위 (Scope)
- **Docker Compose**: `docker-compose.yml`에 `mcpo` 서비스 추가.
- **설정 파일**: `config/mcpo.json` 생성 (MCP 서버 매핑).
- **검증**: OpenWebUI에서 OpenAPI 타입으로 연결 테스트.

## 6. 성공 기준 (Success Metrics)
1. `docker-compose up` 실행 시 `mcpo` 컨테이너가 정상 구동되어야 한다.
2. `http://localhost:3001/openapi.json`으로 접속 시 JSON 문서가 보여야 한다.
3. OpenWebUI에서 **OpenAPI** 타입으로 연결했을 때, `save_debate` 등의 도구가 채팅창에 나타나야 한다.
