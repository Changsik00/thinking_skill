# Spec 018: Documentation & Diagram Fixes

## 📝 Description
프로젝트 문서의 **Mermaid 다이어그램 구문 오류**를 수정하고, **README.md**를 전면 개편하여 사용성과 가독성을 개선했습니다.

## 🛠 Changes

### 1. Diagram Syntax Fixes
- `docs/mcp-guide.md`: Mermaid 레이블 내의 괄호 `()`가 파싱 에러를 유발하는 문제 해결 (따옴표 처리).
- `docs/architecture.md`: 동일한 괄호 파싱 에러 수정.

### 2. Diagram Visibility Improvements
- `docs/core-loop-architecture.md`: 다크 모드에서 다이어그램 글씨가 보이지 않던 문제 해결.
    - `classDef`를 사용하여 테마에 상관없이 잘 보이는 색상(파스텔톤 배경 + 검은 글씨)으로 스타일링 적용.

### 3. README Overhaul
- **Unified Usage Section**: 흩어져 있던 실행 가이드(Docker, Server, MCP, Dashboard)를 `Quick Start` 섹션으로 통합.
- **Project Structure**: `tree` 기반의 최신 프로젝트 구조 반영 및 디렉토리 설명 추가.
- **Doc Index**: `Setup Guide`, `Admin Guide`, `Data Storage Policy` 등 누락된 문서 링크 추가.

## ✅ Verification
- 로컬 마크다운 프리뷰를 통해 다이어그램 렌더링 확인 완료.
- GitHub PR 생성 후 웹 렌더링 추가 확인 예정.
