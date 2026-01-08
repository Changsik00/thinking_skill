# Pull Request: Foundation Setup (Spec 001)

## 요약 (Summary)
MACS 프로젝트의 Phase 2 개발을 가능하게 하는 기초 인프라를 구축했습니다.

## 변경 사항 (Changes)
- **디렉토리 구조**: `agents`, `mcp-servers`, `workflows`, `data` 생성.
- **Python 환경**:
    - `pyproject.toml` 대신 `requirements.txt` (pip 기반) 사용.
    - `.env.example` 추가.
- **Docker 오케스트레이션**:
    - ChromaDB 및 n8n 실행을 위한 `docker-compose.yml` 생성.
    - 컨테이너 정상 실행 확인.
- **문서화 (Documentation)**:
    - `specs/` 디렉토리 구조 재편.
    - `agent.md` 규칙 강화 (폴더 구조 등).
    - `docs/setup-guide.md` (한글) 추가 및 `README.md` 링크.

## 검증 (Verification)
- [x] **폴더 구조**: `ls -R`로 확인 완료.
- [x] **Python 환경**: `pip install --dry-run`으로 확인 완료.
- [x] **Docker**: `docker ps`로 실행 상태(ChromaDB, n8n) 확인 완료.
- [x] **문서화**: `README.md` 링크 및 가이드 내용 확인 완료.

## 연결된 Spec
- [Spec 001](specs/001-foundation-setup/spec.md)
