# Spec 017: Admin Dashboard (MVP)

## 1. 목표 (Goal)
운영자가 시스템 내부 상태(저장된 토론, 임베딩)를 쉽게 확인하고 모니터링할 수 있는 **Admin 대시보드**를 제공합니다.

## 2. 배경 (Context)
현재 시스템은 Agent의 활동 결과(Markdown)와 기억(ChromaDB)을 파일 시스템과 벡터 DB에 저장합니다. 하지만 이를 확인하려면 터미널에 접속하거나 파일을 직접 열어야 하는 불편함이 있습니다. MVP 단계에서 최소한의 가시성을 확보할 필요가 있습니다.

## 3. 범위 (Scope)
- **Tech Stack**: `Streamlit` (Python 기반의 빠른 UI 구축).
- **Core Features**:
    1.  **Debate Viewer**: `data/debates/*.md` 파일 목록 조회 및 내용 렌더링.
    2.  **Memory Inspector**: ChromaDB에 저장된 문서(Documents)와 메타데이터 조회.
    3.  **Search Playground**: 관리자가 쿼리를 입력하면 벡터 검색 결과를 바로 확인 (Relevance 테스트용).

## 4. 제외 대상 (Non-Goals)
- **Edit/Delete**: 데이터 수정 기능은 포함하지 않습니다 (Read-only).
- **Authentication**: 로컬 실행을 전제로 하므로 별도의 로그인은 구현하지 않습니다.
