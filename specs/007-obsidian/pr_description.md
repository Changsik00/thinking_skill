# Phase 7: Obsidian Integration & Selective Archiving

## 📌 Summary
이제 에이전트의 토론 결과가 사용자의 **Obsidian Vault**로 직접 저장됩니다.
단, 모든 대화가 저장되는 것이 아니라, 사용자가 **"저장"**을 원할 때만 저장되는 똑똑한 기록 시스템입니다.

## 🛠 Key Changes

### 1. Obsidian Direct Save (`Adapter`)
- **Path Configuration**: `.env`의 `OBSIDIAN_VAULT_PATH`로 저장 경로를 설정합니다.
- **Auto-Formatting**: 마크다운 파일 상단에 **YAML Frontmatter**를 자동으로 붙여줍니다.
    ```yaml
    ---
    type: debate
    topic: "Quantum Computing"
    model: "macs-agent"
    tags: [macs, agent, debate]
    ---
    ```

### 2. Selective Archiving (`UseCase`)
- **Intent Filter**: 주제(Topic)에 `["저장", "save", "archive", "기록"]` 키워드가 포함될 때만 저장합니다.
- 잡담은 흘려보내고, 중요한 토론만 기록할 수 있습니다.

### 3. TDD Verification
- `tests/unit/infrastructure/test_local_adapter.py`: 경로 및 Frontmatter 생성 검증.
- `tests/unit/usecases/test_run_debate.py`: 키워드 유무에 따른 저장/미저장 로직 검증.

## ✅ Verification Steps (Manual)
1. `.env` 설정: `OBSIDIAN_VAULT_PATH=/Users/ck/Documents/Obsidian` (예시)
2. 서버 재시작: `uv run uvicorn ...`
3. 저장 테스트:
    - "안녕하세요" (저장 안 됨 ❌)
    - "AI의 미래에 대해 토론하고 **저장**해줘" (저장 됨 ✅ -> Obsidian 확인)
