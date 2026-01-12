# Spec 017: Admin Dashboard (MVP)

## 🎯 목적 (Goal)
운영 편의성을 위해 터미널 명령어 없이도 저장된 토론 내역과 Vector DB 상태를 시각적으로 확인할 수 있는 **Admin Dashboard**를 구축합니다.

## 🛠 변경 사항 (Changes)
### 1. Infrastructure (`pyproject.toml`)
- **Streamlit** 의존성 추가: Python 기반의 대시보드 프레임워크.

### 2. Application Layer (`app/admin/dashboard.py`)
- **Tab 1 (File Storage)**: `data/debates/` 경로의 Markdown 파일 뷰어.
- **Tab 2 (Vector DB)**: ChromaDB 컬렉션(`debates`) 상태 조회 및 아이템 미리보기.
- **Tab 3 (Search Playground)**: 의미 기반 검색(Semantic Search) 테스트 UI.

### 3. Documentation (`docs/admin-guide.md`)
- 대시보드 실행 명령어(`uv run streamlit ...`) 및 기능 설명 추가.
- `README.md`에 실행 가이드 업데이트.

## ✅ 검증 (Verification)
- [x] **Installation**: `uv sync` 후 `streamlit --version` 정상 확인.
- [x] **Syntax Check**: `dashboard.py` 컴파일 오류 없음.

## 📝 리뷰 포인트
- 대시보드의 기능이 운영에 유용한지, 추가로 필요한 뷰(View)가 있는지 제안 바랍니다.
