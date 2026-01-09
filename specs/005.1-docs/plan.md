# Implementation Plan: Documentation & Housekeeping

## 1. Goal
프로젝트 문서와 실제 구현 상태의 불일치를 해소한다.

## 2. Proposed Changes

### Project Management
#### [MODIFY] backlog/queue.md
- Phase 4, 4.5, 5 완료 처리.
- **Phase 5.5: Streaming Support** 섹션 신설.

### Documentation
#### [MODIFY] README.md
- **시스템 아키텍처**: 기존 Agent 중심 설명 -> Layered Architecture 설명으로 변경.
- **실행 방법**: Docker 실행 -> FastAPI 서버 실행 가이드 추가.

#### [NEW] docs/architecture.md
- Clean Architecture의 4계층(Domain, UseCase, Infra, Interface) 상세 설명.
- 개발 가이드 (새로운 기능 추가 시 어느 레이어부터 시작해야 하는지).

## 3. Verification Plan
- GitHub 프리뷰에서 마크다운 링크와 이미지가 잘 렌더링되는지 확인.
