# Plan 017: Admin Dashboard

## Goal Description
`Streamlit`을 활용하여 저장된 토론 내역과 ChromaDB 상태를 시각화하는 Admin Page를 구축합니다.

## Proposed Changes

### Application Layer (`app/admin`)
#### [NEW] [dashboard.py](file:///Users/ck/Project/Thingking/app/admin/dashboard.py)
- **탭 구조**:
    - **Tab 1: File Storage**: `data/debates/` 디렉토리의 Markdown 파일 리스팅 및 뷰어.
    - **Tab 2: Vector DB**: ChromaDB 컬렉션(`debates`)의 통계(Count) 및 최근 아이템 조회.
    - **Tab 3: Playground**: 검색어 입력 -> 유사도 기반 검색 결과 표시.

### Infrastructure Layer
- **Dependencies**: `pyproject.toml`에 `streamlit` 추가 (`uv add streamlit`).

### Documentation
#### [MODIFY] [README.md](file:///Users/ck/Project/Thingking/README.md)
- "Admin Dashboard 실행 방법" 추가.

## Verification Plan
### Manual Verification
- `uv run streamlit run app/admin/dashboard.py` 실행.
- 브라우저(`localhost:8501`)에서:
    - 저장된 토론 파일이 보이는지 확인.
    - 벡터 검색이 정상 작동하는지 확인.
