# Plan: Spec 013 - 선택적 아카이빙

## 1. 개요
자동 저장(Auto-save) 로직을 제거하고, 에이전트(`Brain`)가 `save_debate` 도구를 스스로 호출하여 저장하도록 변경합니다.

## User Review Required
> [!NOTE]
> 이제 토론이 끝나도 자동으로 저장되지 않습니다. 
> "저장해줘"라고 요청하거나 에이전트가 가치 있다고 판단할 때만 저장됩니다.

## 2. 변경 사항 (Proposed Changes)

### Application Layer
#### [MODIFY] `app/usecases/run_debate.py`
- 자동 저장 감지 로직(키워드 매칭) 및 `memory.save` 직접 호출 코드 제거.
- **Trigger**: `tool_calls`가 발생하면 실행되도록 수정 (또는 LangGraph 내부에서 실행되도록 위임).
- **Note**: LangGraph 내부에서 ToolCall이 발생하면, 이를 실행하는 Node가 필요합니다. 하지만 현재 구조(`think` -> return str)에서는 ToolCall이 반환값에 포함될 수 있습니다. 
    - **전략**: `LangGraphBrain`이 ToolCall을 내부적으로 처리하거나, `think`의 반환값이 단순 `str`이 아니라 Tool Call 정보를 포함해야 함.
    - **Simple Strategy**: 이번 단계에서는 Brain이 Tool Call을 "생성"하면, `RunDebateUseCase`나 Adapter가 이를 감지해야 함. 그러나 LangGraph의 `prebuilt` ToolNode를 사용하는 것이 정석.
    - **Revised Strategy**: 
        1. `LangGraphBrain`에 `tools` 바인딩.
        2. `critical_node` 뒤에 `tools_node` 추가 (Conditional Edge).
        3. 도구 실행 결과가 메시지에 포함되어 최종 응답으로 나옴.

### Infrastructure Layer
#### [MODIFY] `app/infrastructure/llm/langgraph_adapter.py`
- `mcp_server.py`의 `save_debate` 도구(또는 해당 로직을 가진 함수)를 가져옴.
- `_get_llm`에서 `.bind_tools([save_debate])` 적용.
- `_build_graph`에 `ToolNode` 추가 및 `should_continue` 조건부 엣지 구현.

#### [MODIFY] `app/infrastructure/llm/prompts.py`
- `CRITICAL_SYSTEM_PROMPT` 업데이트:
    - "논의가 충분히 가치 있거나 사용자가 요청하면 `save_debate` 도구를 사용하여 기록을 남기세요."

## 3. 검증 계획 (Verification Plan)

### Manual Verification
1. `python scripts/run_debate_cli.py "AI Ethics"` 실행 -> 저장 안 됨 (확인).
2. `python scripts/run_debate_cli.py "AI Ethics, 그리고 이건 저장해줘"` 실행 -> `save_debate` 도구 호출 -> 저장됨 (확인).
