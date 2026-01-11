# Plan: Spec 011 - 데이터 동기화 도구

## 1. 개요
Obsidian 파일 시스템과 ChromaDB 간의 데이터 정합성을 맞추기 위한 `sync_debates` 도구를 구현합니다. 특히 "삭제된 파일"이 DB에 남는 문제를 해결하는 데 집중합니다.

## User Review Required
> [!NOTE]
> 이번 구현은 '삭제된 파일 정리(Garbage Collection)'에 초점을 맞춥니다.
> '수정된 파일 업데이트'나 '새 파일 추가'는 이번 스펙 범위에 포함되지 않으며, 추후 `Scan` 기능으로 별도 구현될 수 있습니다.

## 2. 변경 사항 (Proposed Changes)

### Domain Layer
#### [NEW] `app/usecases/sync_debates.py`
- `SyncDebatesUseCase` 클래스 구현.
- 로직:
  1. `DebateRepository.list_all_ids()` 호출 -> DB ID 목록 획득.
  2. `os.listdir` 등을 통해 실제 파일 ID 목록 획득.
  3. 차집합(Diff) 계산.
  4. `DebateRepository.delete(id)` 호출.

### Interface Layer (Clean Architecture)
#### [MODIFY] `app/interfaces/mcp_server.py`
- `sync_debates` 도구 등록.
- Dependency Injection: `SyncDebatesUseCase` 주입.

### Infrastructure Layer
#### [MODIFY] `app/infrastructure/chroma_debate_repository.py`
- `list_all_ids()` 메서드 추가 구현.
- (기존 `delete` 메서드 재사용)

## 3. 검증 계획 (Verification Plan)

### Automated Tests
- `pytest tests/usecases/test_sync_debates.py`
  - Mock Repository를 사용하여 파일이 없을 때 delete가 호출되는지 검증.

### Manual Verification
1. `data/archives`에 임시 파일 생성 및 `save_debate`로 DB 저장.
2. 임시 파일 수동 삭제.
3. `sync_debates` 도구 실행.
4. `search_debates`로 해당 임시 파일 내용 검색 -> 검색되지 않아야 함.
