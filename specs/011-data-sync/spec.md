# Spec 011: 데이터 동기화 도구 (Data Synchronization Tools)

## 1. 개요 (Overview)
현재 Thingking 시스템은 Obsidian에 저장된 Markdown 파일과 ChromaDB에 저장된 벡터 데이터 간의 동기화가 **단방향(Save 시점)**으로만 이루어집니다.
이로 인해 Obsidian에서 파일을 삭제하거나 이름을 변경했을 때, ChromaDB에는 "고아 데이터(Orphaned Data)"가 남아 검색 결과에 잘못된 정보가 노출될 위험이 있습니다.

본 스펙은 이 문제를 해결하기 위해 **명시적인 동기화(Sync) 도구**를 구현하여 정합성을 보장하는 것을 목표로 합니다.

## 2. 문제 정의 (Problem Statement)
- **증상**: 사용자가 Obsidian에서 `debate_20240101.md` 파일을 삭제해도, ChromaDB에는 해당 문서의 임베딩이 영구적으로 남음.
- **영향**: MCP `search_debates` 도구 사용 시, 삭제된 토론 내용이 검색 결과로 반환됨 (Dead Link).
- **원인**: 파일 시스템 이벤트(삭제)가 DB에 전파되지 않음.

## 3. 제안 솔루션 (Proposed Solution)
**`sync_debates` MCP 도구 추가**

자동화된 백그라운드 프로세스(Watcher)보다는, 명시적으로 실행할 수 있는 **도구(Tool)** 형태로 구현하여 복잡도를 낮추고 안정성을 확보합니다.

### 3.1 핵심 로직 (`SyncDebatesUseCase`)
1. **Fetch File List**: `OBSIDIAN_VAULT_PATH` 내의 모든 유효한 Markdwon 파일 목록(`Set A`)을 조회.
2. **Fetch DB List**: ChromaDB의 모든 Document ID 목록(`Set B`)을 조회.
3. **Calc Diff**:
    - **To Delete** = `Set B` - `Set A` (DB에는 있는데 파일은 없음)
    - **To Add/Update** = `Set A` - `Set B` (파일은 있는데 DB에는 없음 - *선택적 구현*)
4. **Execute**:
    - `Delete` 대상 ID들을 ChromaDB에서 일괄 삭제.
    - 결과 리포트 반환 (예: "Deleted 3 orphaned items").

### 3.2 MCP 인터페이스
- **Tool Name**: `sync_debates`
- **Description**: Obsidian 파일 시스템과 ChromaDB 간의 데이터를 동기화합니다. 삭제된 파일의 벡터 데이터를 정리합니다.
- **Input**: 없음 (또는 `dry_run: bool`)

## 4. 범위 (Scope)

### 포함 (In Scope)
- UseCase: `SyncDebatesUseCase` 구현 (삭제 로직 중심).
- MCP Tool: `sync_debates` 도구 등록.
- Repository: ChromaDB 모든 ID 조회 기능 추가 (`list_all_ids`).
- Test: Mock을 활용한 동기화 로직 유닛 테스트.

### 제외 (Out of Scope)
- 실시간 파일 감시 (File Watcher).
- 파일 내용 변경에 대한 정밀 비교 (해시 비교 등은 추후 과제).
- Obsidian 플러그인 개발.

## 5. 성공 기준 (Success Criteria)
- Obsidian에서 파일을 수동 삭제한 후 `sync_debates` 도구를 실행하면, ChromaDB에서도 해당 데이터가 검색되지 않아야 함.
- 삭제된 항목의 개수가 정확히 반환되어야 함.
