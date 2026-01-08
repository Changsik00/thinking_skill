# MACS (Multi-Agent Creative Studio)

아이디어 브레인스토밍부터 유튜브 콘텐츠 소스 생성까지, 로컬 기반의 멀티 에이전트 협업 자동화 시스템입니다.

---

## 1. 의도 (Intent)
- **아이디어의 고도화**: 단일 AI와의 대화가 아닌, 서로 다른 성향(창의/비판)을 가진 에이전트 간의 토론을 통해 아이디어를 다각도에서 검증합니다.
- **지식의 자산화**: 휘발되는 대화가 아니라, 모든 과정과 결과물을 로컬(Obsidian)에 기록하여 개인 지식 베이스를 구축합니다.
- **콘텐츠 생산 자동화**: 기획 단계에서 멈추지 않고, 영상 제작에 필요한 스크립트와 이미지 소스(프롬프트)까지 한 번에 생성합니다.

## 2. 목표 (Goal)
- **삼각 토론 시스템**: 나(Host)와 2명의 AI 에이전트가 참여하는 효율적인 토론 루프 구현.
- **자동 아카이빙**: n8n을 활용해 토론 종료 즉시 마크다운(.md) 파일로 요약 및 옵시디언 저장.
- **멀티미디어 준비**: 유튜브 제작을 위한 씬(Scene)별 스크립트 및 나노바나나(Gemini)용 이미지 프롬프트 추출.
- **비용 최적화**: Gemini 1.5 Flash API와 로컬 인프라(Docker)를 결합한 최저 비용 운영.
- **개인정보 보호**: 프로젝트 단위로 생성되고 삭제되는 휘발성 벡터 DB(ChromaDB) 운용.

## 3. 환경 (Environment)

### Core Stack
- **Interface**: OpenWebUI (사용자 채팅창 및 에이전트 관리)
- **Orchestration**: Python (LangGraph) - 멀티 에이전트 논리 제어
- **Automation**: n8n - 데이터 처리 및 앱 간 연동
- **Database**: ChromaDB (로컬 기반 임시 벡터 저장소)
- **Protocol**: MCP (Model Context Protocol) - 로컬 파일 및 도구 접근

### AI Engine
- **LLM**: Google Gemini 1.5 Flash (메인 추론 및 토론)
- **Image Gen**: 나노바나나 (Gemini 기반 이미지 생성 프롬프트)

## 4. 폴더 구조 (Planned)
- `/agents`: LangGraph 기반 에이전트 협업 로직
- `/mcp-servers`: 로컬 자원 접근용 MCP 서버 코드
- `/workflows`: n8n 자동화 워크플로우 정의 파일
- `/data`: 임시 벡터 DB 저장 경로
- `docker-compose.yml`: 전체 시스템 통합 실행 설정

## 5. Documentation
- [Setup & Troubleshooting Guide](docs/setup-guide.md): 설치, 실행, 문제 해결 가이드.
