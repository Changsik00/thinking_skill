# Spec 015: Documentation Sync

## 🎯 목적 및 배경
현재 프로젝트의 문서(`README.md`, `docs/architecture.md`)가 최신 개발 변경 사항(Spec 010~014)을 반영하고 있지 않습니다. 본 PR은 시스템의 실제 구현 상태와 문서 간의 정합성을 맞추기 위해 작성되었습니다.

## 🛠 구현 내용
### 1. README.md 업데이트
- **Features**: '자동 아카이빙'을 **'선택적 아카이빙 (Selective Archiving)'**으로 명칭 변경 및 개념 재정의.
- **Integration**: `OpenWebUI`, `n8n Automation` 지원 내용 추가.
- **Usage**: OpenWebUI 접속 정보 및 MCPO Bridge 실행 안내 추가.

### 2. Architecture 문서 업데이트 (`docs/architecture.md`)
- **Infrastructure**: `MCPO Bridge` 컨테이너 및 역할 추가.
- **Brain**: Gemini 2.0/1.5 **Dynamic Model Selection** 기능 명시.
- **Use Case**: 아카이빙 및 자동화 트리거의 선택적(Optional) 실행 로직 반영.

## ✅ 검증 (Verification)
- [x] **Markdown Rendering**: 로컬 뷰어를 통해 `README.md` 및 `architecture.md`의 포맷팅 깨짐 여부 확인 완료.
- [x] **Content Accuracy**: 업데이트된 내용이 현재 코드베이스(Spec 014 시점)와 일치함을 확인.

## 📝 리뷰 포인트
- 문서의 설명이 실제 시스템 동작(특히 Selective Archiving)을 오해 없이 전달하고 있는지 확인 부탁드립니다.
