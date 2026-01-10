# 작업 목록 - Spec 010: OpenAPI Bridge 통합

- [x] **기획 (Planning)**
    - [x] 스펙 문서 작성 (`spec.md`) - 한글화 및 결정 배경 포함
    - [x] 구현 계획 작성 (`plan.md`)
    - [x] 계획 승인

- [x] **구현 (Execution)**
    - [x] `config/mcpo.json` 파일 생성 (MCP 정보 등록)
    - [x] `docker-compose.yml` 수정 (`mcpo` 서비스 추가)
    - [x] Docker 환경 재시작 (`up -d`)

- [x] **검증 (Verification)**
    - [x] `mcpo` 컨테이너 실행 확인
    - [x] OpenAPI JSON 생성 확인 (`curl`)
    - [x] OpenWebUI에서 OpenAPI 연동 성공 확인 (수동 파이썬 스크립트 등록)
    - [x] 실제 도구(`save_debate`) 동작 확인 (완료)
