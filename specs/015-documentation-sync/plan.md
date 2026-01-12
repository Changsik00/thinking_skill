# Plan 015: Documentation Sync

## Goal Description
현재 문서(`README.md`, `docs/architecture.md`)는 최신 개발 사항(Spec 010~014)을 반영하고 있지 않습니다.
특히 **OpenWebUI 연동**, **Selective Archiving (자동 저장 해제)**, **n8n Automation** 등 주요 기능 변경 사항을 문서화하여 시스템의 실제 상태와 문서의 일치성을 확보합니다.

## User Review Required
> [!IMPORTANT]
> **Selective Archiving 반영**: 기존 `README.md`의 "자동 아카이빙" 문구를 "선택적 아카이빙"으로 수정하며, 시스템 기본 동작에 대한 설명을 변경합니다. 오해의 소지가 없도록 명확히 기술할 예정입니다.

## Proposed Changes

### Documentation
#### [MODIFY] [README.md](file:///Users/ck/Project/Thingking/README.md)
- **Features 섹션 업데이트**: 
    - "자동 아카이빙" -> "선택적 아카이빙 (Selective Archiving)"으로 변경.
    - "OpenWebUI 지원" 및 "MCPO Bridge" 내용 추가.
- **Usage 섹션 업데이트**: 
    - OpenWebUI 접속 방법 안내 (`http://localhost:3000`).
    - `save_debate` 도구 사용법 간략 언급 (Agent가 판단하여 저장).

#### [MODIFY] [architecture.md](file:///Users/ck/Project/Thingking/docs/architecture.md)
- **Architecture 섹션 업데이트**: 
    - **MCPO Bridge**: Interface Layer 또는 Infrastructure Layer에 MCPO 컨테이너 역할 기술.
    - **Brain Upgrade**: `LangGraphBrain`이 `Dynamic Model Selection`을 지원함을 명시.
    - **Selective Archiving**: UseCase 흐름도에서 "무조건 저장" 로직을 "Agent 도구 호출 시 저장"으로 변경 설명.

## Verification Plan

### Manual Verification
1. **Rendering Check**: GitHub 스타일 Markdown 뷰어로 `README.md` 및 `architecture.md` 렌더링 확인 (깨진 링크나 포맷 확인).
2. **Content Audit**: 
    - `README.md`의 "Architecture" 섹션이 `docs/architecture.md`와 일관성이 있는지 대조.
    - Usage 가이드대로 OpenWebUI 접속이 가능한지(현재 실행 중이라면) 확인. (이번 작업은 문서 수정이므로 내용의 정확성 위주 검증)
