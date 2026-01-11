# Walkthrough: Spec 011 (Data Sync)

## 📌 개요
Obsidian에서 토론 파일을 삭제했을 때, ChromaDB에 남아있는 '고아 임베딩 데이터'를 정리하는 `sync_debates` 도구를 구현했습니다.

## 🛠️ 변경 사항

### 1. Domain Layer: `SyncRepository` & `SyncDebatesUseCase`
- **`app/domain/interfaces/sync_repository.py`**: 동기화에 필요한 저장소 인터페이스 정의 (`list_all_chroma_ids`, `list_all_file_ids`, `delete_chroma_documents`).
- **`app/usecases/sync_debates.py`**: 집합 연산(Diff)을 통해 삭제 대상을 추출하고 제거하는 순수 로직 구현.

### 2. Infrastructure Layer: `LocalAdapter` 업데이트
- **`app/infrastructure/storage/local_adapter.py`**:
    - `list_all_file_ids`: 파일명(`YYYY-mm-dd_HH-MM-SS_Topic.md`)을 파싱하여 ChromaDB ID(`Topic_YYYYmmddHHMMSS`) 형식으로 변환/복원.
    - `list_all_chroma_ids`: ChromaDB 컬렉션 전체 조회.
    - `delete_chroma_documents`: 실제 삭제 수행.

### 3. Interface Layer: MCP Tool 등록
- **`app/interfaces/mcp_server.py`**: `sync_debates(dry_run: bool)` 도구 등록.

## ✅ 검증 결과

### Unit Test
`tests/usecases/test_sync_debates.py`를 통해 다음 시나리오 검증 완료:
- **Clean State**: 파일과 DB가 일치할 때 아무것도 삭제하지 않음.
- **Garbage Found**: DB에만 있는 ID를 정확히 식별하여 삭제.
- **Dry Run**: 삭제 로직을 타지 않고 리포트만 반환.

```bash
$ pytest tests/usecases/test_sync_debates.py
...
tests/usecases/test_sync_debates.py ... [100%]
3 passed in 0.02s
```

## 📝 사용 방법
OpenWebUI 채팅창에서:
1. "이전 토론 파일들을 정리했는데 DB랑 동기화해줘"
2. Agent 호출: `sync_debates(dry_run=True)` (먼저 확인 권장)
3. Agent 호출: `sync_debates(dry_run=False)` (실제 삭제)
