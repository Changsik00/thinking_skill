# Spec 018: 문서 및 다이어그램 수정 (Documentation & Diagram Fixes)

## 1. 개요 (Overview)
현재 프로젝트 문서(`docs/*.md`)의 Mermaid 다이어그램에서 구문 오류(Syntax Error)와 가독성 이슈가 발견되었습니다. 또한 `README.md`의 실행 가이드와 구조 설명이 최신 상태를 반영하지 못하고 있습니다. 이를 해결하여 문서의 정확성과 접근성을 높입니다.

## 2. 문제 정의 (Problem Statement)
*   **Mermaid 오류**:
    *   `docs/mcp-guide.md`: 괄호 `(` 처리가 잘못되어 파싱 에러 발생.
    *   `docs/architecture.md`: 괄호 `(` 처리가 잘못되어 파싱 에러 발생.
*   **가독성 이슈**:
    *   `docs/core-loop-architecture.md`: Dark Mode에서 글씨가 잘 보이지 않음 (테마 호환성).
*   **README 부족**:
    *   **Usage**: 실행 방법이 여러 문서에 흩어져 있고, 한눈에 보기 어려움.
    *   **Structure**: 폴더 구조 설명이 부실함.
    *   **Docs Index**: 최근 추가된 문서(`data-storage-policy` 등)가 누락됨.

## 3. 작업 범위 (Scope)

### 3.1 다이어그램 수정 (Diagram Fixes)
*   `docs/mcp-guide.md`: `Adapter -->|의미 검색 (Future)| VectorDB` 라인의 괄호 이스케이프 또는 따옴표 처리.
*   `docs/architecture.md`: `Interface[Interfaces (Web/CLI)]`와 같은 노드 레이블의 괄호 처리.
*   `docs/core-loop-architecture.md`: 다이어그램 색상을 Light/Dark 모드 모두에서 잘 보이도록 스타일(classDef) 적용 또는 색상 조정.

### 3.2 README 개선 (README Enhancement)
*   **Unified Usage Section**: `CLI`, `Streamlit`, `MCP Server`, `Docker` 실행 방법을 하나의 섹션에서 탭(Tab) 또는 명확한 서브헤더로 정리.
*   **Project Structure**: `tree` 구조를 업데이트하고 각 디렉토리(`app`, `docs`, `specs`, `tests`, `scripts`)의 역할을 명시.
*   **Documentation Index**: 모든 `docs/*.md` 파일에 대한 링크와 간단한 요약 추가.

## 4. 성공 기준 (Success Criteria)
*   GitHub Preview에서 모든 Mermaid 다이어그램이 에러 없이 렌더링되어야 함.
*   Dark Mode에서도 다이어그램 텍스트가 명확히 보여야 함.
*   `README.md`만 보고도 프로젝트의 모든 기능(CLI, Web, Admin)을 실행할 수 있어야 함.
