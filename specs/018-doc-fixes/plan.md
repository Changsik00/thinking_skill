# Plan 018: 문서 수정 계획 (Documentation Plan)

## 1. 다이어그램 수정 (Diagram Fixes)

### `docs/mcp-guide.md`
*   **Issue**: `Parse error` (괄호 처리).
*   **Fix**: Mermaid 노드 레이블 내 괄호 `()`를 따옴표 `""`로 감싸거나 이스케이프 처리.
    *   `VectorDB[("VectorDB")]` 등.

### `docs/architecture.md`
*   **Issue**: `Parse error` (괄호 처리).
*   **Fix**: 레이블 내 괄호 처리 수정.
    *   `Interface["Interfaces (Web/CLI)"]` 형태로 변경.

### `docs/core-loop-architecture.md`
*   **Issue**: Visibility in Dark Mode.
*   **Fix**: 명시적인 `style` 지정보다는 Mermaid의 기본 테마를 따르되, 필요시 `classDef`로 고대비 색상(예: 밝은 회색 배경에 검은 글씨, 또는 테마 중립적인 색상) 적용.

## 2. README.md 전면 개편

### 섹션 재구성
1.  **Project Title & Badges** (유지)
2.  **Introduction** (유지)
3.  **Features** (유지)
4.  **Quick Start (Usage)** - **[Major Update]**
    *   `Prerequisites` (Python, uv, Docker)
    *   `Installation`
    *   `Running the App` (CLI, Streamlit, MCP Server)
5.  **Project Structure** - **[Major Update]**
    *   `tree` 명령어로 최신 구조 반영.
    *   주요 디렉토리 설명 추가.
6.  **Documentation** - **[Update]**
    *   문서 목록 테이블화 또는 리스트 업데이트.

## 3. 검증 계획 (Verification Plan)
*   **Local Preview**: VS Code Markdown Preview로 렌더링 확인.
*   **GitHub Preview**: PR 생성 후 GitHub 웹 인터페이스에서 다이어그램 렌더링 및 다크 모드 가독성 확인.
