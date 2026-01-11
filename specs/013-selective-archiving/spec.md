# Spec 013: 선택적 아카이빙 (Selective Archiving)

## 1. 개요 (Overview)
현재 시스템은 토론이 끝나면 사용자의 명시적 의도나 데이터 가치와 상관없이(또는 단순 키워드 매칭으로) 자동 저장하려 합니다.
이를 개선하여 **LLM이 판단하거나 사용자가 요청했을 때만** 결과를 저장하도록 변경합니다.

## 2. 문제 정의 (Problem Statement)
- **쓰레기 데이터**: 단순 테스트나 잡담도 모두 저장될 위험이 있음.
- **불명확한 로직**: `RunDebateUseCase`에 하드코딩된 "저장", "save" 키워드 매칭 로직은 유연하지 않음.
- **에이전트 주권 부족**: 에이전트가 대화의 가치를 판단하여 "이건 저장해둘만해"라고 결정하지 못함.

## 3. 제안 솔루션 (Proposed Solution)

### 3.1 UseCase 로직 단순화
- `RunDebateUseCase`에서 "저장(Save)" 관련 로직을 **완전히 제거**합니다.
- UseCase는 오직 "Think"와 "Trigger Nerve"에만 집중합니다.

### 3.2 도구 기반 저장 (Tool-based Saving)
- `ThinkingBrain` (Gemini)이 `save_debate` 도구를 **필요할 때 스스로 호출**하도록 유도합니다.
- **System Prompt 개선**:
    - "중요한 결론이 도출되었거나 사용자가 저장을 요청하면 `save_debate` 도구를 사용해라"라는 지침 추가.
- (이미 구현됨) `mcp_server.py`에 `save_debate` 도구가 등록되어 있으므로, Brain이 이를 인지할 수 있어야 함.

## 4. 범위 (Scope)

### 포함 (In Scope)
- `App Layer`: `RunDebateUseCase` 내 레거시 저장 로직 삭제.
- `Infra Layer (Prompt)`: `CREATIVE_SYSTEM_PROMPT` (또는 `CRITICAL`)에 도구 사용 지침 강화.
- `검증`: "저장해줘"라고 말햇을 때만 저장이 일어나는지 테스트.

### 제외 (Out of Scope)
- 새로운 저장 방식 구현 (기존 `MemoryVault.save` 활용).

## 5. 성공 기준 (Success Criteria)
- 일반 대화 시: 자동 저장되지 않음.
- "이 내용 저장해" 요청 시: `save_debate` 도구가 호출되어 Obsidian/Chroma에 저장됨.
