# Walkthrough: Spec 013 (Selective Archiving)

## 📌 개요
기존의 무조건적인(또는 단순 키워드 기반) 자동 저장 로직을 제거하고, **에이전트(Brain)가 스스로 판단하거나 사용자가 요청했을 때만** 결과를 저장하도록 변경했습니다.
이를 위해 `LangGraphBrain`에 `save_debate` 도구를 바인딩하고, System Prompt를 통해 도구 사용을 유도했습니다.

## 🛠️ 변경 사항

### 1. Application Layer (`RunDebateUseCase`)
- **Legacy Logic Removed**: `execute` 및 `execute_stream` 메서드에 있던 하드코딩된 저장 로직(`# 3. Save to Memory`)을 제거했습니다.
- 이제 UseCase는 오직 토론 진행과 Nerve Trigger만 담당합니다.

### 2. Infrastructure Layer (`LangGraphBrain`)
- **Tool Integration**: `MemoryVault`를 주입받아 `save_debate` 도구를 생성하고, LLM에 바인딩했습니다.
- **Graph Update**: `ToolNode`를 그래프에 추가하고, Critical Agent가 도구를 호출할 수 있도록 조건부 엣지(`conditional_edges`)를 연결했습니다.
- **Prompt Update**: `CRITICAL_SYSTEM_PROMPT`에 "중요한 결론이거나 사용자가 요청하면 저장하라"는 지침을 추가했습니다.

### 3. Dependency Injection (`mcp_server.py`)
- `LangGraphBrain` 초기화 시 `LocalAdapter`(Vault)를 주입하도록 수정했습니다.

## ✅ 검증 결과

### Verification Script
`scripts/verify_tool_calling.py` 실행 결과:
```
--- Verifying Selective Archiving (Spec 013) with MOCKED LLM ---

[Test 1] Casual Conversation (Expect: NO Save)
Response: This is a casual response.
✅ Passed: No save triggered for casual topic.

[Test 2] Explicit Save Request (Expect: YES Save)
MockVault: Saving result about 'Quantum Computing'
Response: I have saved the debate as requested.
✅ Passed: Save triggered by user request.
   Saved Topic: Quantum Computing
```
- **Casual Chat**: 저장 도구가 호출되지 않음.
- **Explicit Request**: "save this debate" 요청 시 저장 도구가 호출되고 파일이 생성됨(Mock).

## 📝 사용 방법
- 더 이상 대화가 자동으로 저장되지 않습니다.
- 저장을 원하시면 대화 중 또는 끝에 **"이 내용은 저장해줘"**, **"Save this"** 등으로 명시적으로 요청하세요.
- 에이전트가 판단하기에 매우 유의미한 결론("Critical Conclusion")이 도출되면 스스로 저장할 수도 있습니다.
