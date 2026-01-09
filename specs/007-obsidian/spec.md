# Spec 007: Obsidian Integration

## 1. Intent (의도)
**"생각의 확장."**
생성된 토론 결과(`DebateResult`)가 단순히 `data/archives`에 갇혀있는 것이 아니라, 사용자의 **Second Brain (Obsidian)**으로 즉시 흘러들어가야 합니다.
이를 통해 에이전트의 출력이 사용자의 지식 베이스와 **Seamless**하게 연결되도록 합니다.

## 2. Approach (접근 방식)

### 2.1. File System Integration (Direct Save) - **Priority**
Obsidian은 본질적으로 "마크다운 파일 뷰어"입니다.
따라서 별도의 복잡한 API 연동 없이, **파일 저장 경로를 Obsidian Vault 내부로 지정**하는 것만으로도 완벽한 연동이 가능합니다.

- **Current**: `data/archives` (Hardcoded/Default)
- **New**: `OBSIDIAN_VAULT_PATH` (Environment Variable)
    - 예: `/Users/ck/Documents/Obsidian/MyVault/Inbox`

### 2.2. Metadata Enhancement
Obsidian 사용성을 높이기 위해, 마크다운 파일에 **Frontmatter (Properties)**를 추가합니다.
```yaml
---
type: debate
topic: "AI Ethics"
model: "gemini-2.0-flash"
date: 2024-01-09
tags: [macs, agent, debate]
---
```

## 3. Future Scope (MCP)
추후 옵시디언에서 에이전트에게 "이 문서와 관련된 토론을 해줘"라고 요청하는 역방향 연동(MCP Server)은 다음 단계로 미룹니다. 이번 단계는 **단방향 저장(Save)**에 집중합니다.

## 4. Verification Plan
1. `.env`에 `OBSIDIAN_VAULT_PATH=/tmp/test-vault` 설정.
2. Web UI에서 토론 진행.
3. `/tmp/test-vault` 내부에 마크다운 파일 생성 확인.
4. 파일 내용에 Frontmatter 포함 여부 확인.
