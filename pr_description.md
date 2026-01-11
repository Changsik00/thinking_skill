# PR: Spec 013 - 선택적 아카이빙 (Selective Archiving)

## 📌 개요
기존의 자동 저장 방식을 제거하고, **"저장해줘"**와 같은 명시적 요청이 있을 때만 에이전트가 도구를 사용하여 저장하도록 변경했습니다.
이를 통해 불필요한 데이터 저장을 막고, 에이전트의 주권(Agency)을 강화했습니다.

## 🛠️ 변경 사항

### 1. Application Layer (`RunDebateUseCase`)
- **[MODIFY]** `execute`, `execute_stream`: 자동 저장 로직 삭제.
- UseCase는 더 이상 `memory.save()`를 직접 호출하지 않습니다.

### 2. Infrastructure Layer (`LangGraphBrain`)
- **[MODIFY]** `LangGraphBrain`: `MemoryVault`를 주입받아 `save_debate` 도구를 생성 및 바인딩.
- **[NEW]** `ToolNode`: 그래프에 도구 실행 노드 추가.
- **[MODIFY]** `prompts.py`: Critical Agent에게 "중요하면 저장하라"는 지침 추가.

### 3. Verification
- `scripts/verify_tool_calling.py` (Mock Test) 통과.
- 일반 대화: 저장 안 됨.
- 저장 요청: `save_debate` 도구 호출됨.

## 📝 리뷰 포인트
- `LangGraphBrain` 내부의 `_create_save_tool` 및 `_build_graph` 로직.
- `RunDebateUseCase`의 단순화된 흐름.
