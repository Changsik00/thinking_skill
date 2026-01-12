# 데이터 저장 정책 (Data Storage Policy)

이 문서는 MACS(Multi-Agent Creative Studio) 시스템의 토론 결과물 저장 정책, 파일 구조 및 Obsidian 통합 방식을 설명합니다.

## 1. 저장 원칙 (Storage Principles)

### 1.1 선택적 아카이빙 (Selective Archiving)
시스템은 모든 대화를 자동으로 저장하지 않습니다. 오직 다음 두 가지 경우에만 저장이 수행됩니다:
1.  **AI 판단**: Debate Agent(Brain)가 대화 중 "중요한 결론"이 도출되었다고 판단하여 스스로 `save_debate` 도구를 호출하는 경우.
2.  **사용자 명시적 요청**: 사용자가 "이 내용 저장해줘", "결과를 파일로 남겨"라고 명령하는 경우.

> **Note**: 이는 단순 테스트나 잡담으로 인한 "데이터 오염(Garbage Data)"을 방지하기 위함입니다 (Spec 013 참조).

## 2. 저장 위치 (Storage Location)

시스템은 기본적으로 로컬 파일 시스템(`Markdown`)과 벡터 데이터베이스(`ChromaDB`)에 이중으로 저장합니다.

### 2.1 파일 시스템 (Markdown)
- **기본 경로**: `data/archives/`
- **Obsidian 통합**: 
    - `.env` 파일의 `OBSIDIAN_VAULT_PATH` 변수를 설정하여 저장 경로를 사용자의 Obsidian Vault로 변경할 수 있습니다.
    - 설정 예시: `OBSIDIAN_VAULT_PATH=/Users/me/Documents/ObsidianVault/MACS`
    - 설정이 없으면 프로젝트 내 `data/archives`에 저장됩니다.

### 2.2 벡터 데이터베이스 (ChromaDB)
- **경로**: `data/chroma/`
- **용도**: 시맨틱 검색(Semantic Search) 및 문맥 검색(RAG)을 위해 사용됩니다.
- **동기화**: 파일 시스템에 저장될 때 자동으로 ChromaDB에도 임베딩되어 저장됩니다.

## 3. 파일 구조 및 형식 (File Structure & Format)

저장되는 파일은 Obsidian과의 호환성을 위해 **YAML Frontmatter**를 포함한 표준 Markdown 형식을 따릅니다.

### 3.1 파일명 규칙 (Naming Convention)
```text
{YYYY-MM-DD}_{HH-MM-SS}_{Topic}.md
```
- 예: `2024-03-20_14-30-00_TDD_vs_BDD.md`
- 공백과 특수문자는 `_`로 치환되거나 제거됩니다.

### 3.2 파일 내용 예시 (Content Example)
```markdown
---
type: debate
topic: "TDD vs BDD"
model: "gemini-2.0-flash-001"
date: "2024-03-20 14:30:00"
tags: [macs, agent, debate]
---

# Topic: TDD vs BDD
Date: 2024-03-20 14:30:00

## Final Conclusion
(토론 내용 본문...)
```

## 4. 데이터 관리 (Data Management)

### 4.1 Sync (동기화)
- 수동으로 Markdown 파일을 삭제한 경우, ChromaDB에 "고아 데이터(Orphaned Embeddings)"가 남을 수 있습니다.
- 이를 해결하기 위해 `sync_debates` 도구가 제공됩니다.
- **Admin Dashboard** 또는 CLI를 통해 동기화 기능을 실행하면 파일이 없는 DB 레코드를 정리합니다.
